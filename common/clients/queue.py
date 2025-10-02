import asyncio
import json
from typing import Awaitable, Callable

import aio_pika
from loguru import logger

from common.config import settings


class QueueClient:
    async def _get_connection(self) -> aio_pika.Connection:
        return await aio_pika.connect_robust(settings.RABBITMQ_URL)

    async def send(self, queue: str, message: dict):
        try:
            connection = await self._get_connection()
            async with connection:
                channel = await connection.channel()
                # creates queue if it does not exist
                queue = await channel.declare_queue(queue, durable=True)

                # Create a message object
                message = aio_pika.Message(
                    body=json.dumps(message).encode(),
                    delivery_mode=aio_pika.DeliveryMode.PERSISTENT,
                )

                # Publish the message to the default exchange, routing to the queue name
                await channel.default_exchange.publish(
                    message,
                    routing_key=queue.name,
                )

                logger.info(f'Sent message to queue "{queue}"')
        except Exception as e:
            logger.error(f'Failed to send message to queue "{queue}" - {e}')
            raise e

    async def consume(
        self,
        queue_name: str,
        callback: Callable[[aio_pika.IncomingMessage], Awaitable[None]],
        keep_running: bool = True,
    ):
        # Establish a robust connection (it will try to reconnect if connection is lost)
        connection = await self._get_connection()

        async with connection:
            # Creating a channel
            channel = await connection.channel()

            # Set up a Quality of Service (QoS) to limit prefetch count
            # This prevents a consumer from getting overwhelmed and ensures fair dispatch
            await channel.set_qos(prefetch_count=1)

            # Declaring the queue
            queue = await channel.declare_queue(queue_name, durable=True)

            # Start consuming messages. The 'no_ack=False' is default and means
            # we must manually acknowledge messages.
            await queue.consume(callback, no_ack=True)

            if keep_running:
                logger.info(f"[*] Waiting for messages from queue {queue_name}")
                await asyncio.Future()  # Keep the consumer running

            logger.info(f"Stopping consumer for queue {queue_name}")
