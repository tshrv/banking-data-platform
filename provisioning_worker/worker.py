import asyncio

from loguru import logger


async def main():
    logger.info("Provisioning worker started")


if __name__ == "__main__":
    asyncio.run(main())
