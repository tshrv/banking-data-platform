import json
import time

import aio_pika
import pytest
from loguru import logger

from common.clients.queue import QueueClient


@pytest.mark.asyncio(loop_scope="session")
async def test_queue_send_and_consume_success():
    """Ensure messages are being sent to queue"""
    queue_name = "test-queue"
    message = {"request_id": str(time.time())}
    qc = QueueClient()
    await qc.send(queue_name, message)

    async def message_processor(incoming_message: aio_pika.IncomingMessage):
        logger.info(f"Received message {incoming_message}")
        msg_body = json.loads(incoming_message.body.decode())
        logger.info(f"Processing message {msg_body}")

    # prevent consumer from running forever
    await qc.consume(queue_name, message_processor, keep_running=False)
