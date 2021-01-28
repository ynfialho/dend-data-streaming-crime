import asyncio
from confluent_kafka import Consumer
import logging

logger = logging.getLogger(__name__)

BROKER_URL = "PLAINTEXT://localhost:9092"
TOPIC = "com.udacity.crime"

async def consume(topic_name):
    c = Consumer({"bootstrap.servers": BROKER_URL, "group.id": "31", 'auto.offset.reset': 'earliest'})
    c.subscribe([topic_name])

    while True:
        messages = c.consume(5, timeout=1.0)
        for message in messages:
            print(f"consume message {message.key()}: {message.value()}")
        await asyncio.sleep(1.0)


async def create_task(topic_name):
    """Runs the Producer and Consumer tasks"""
    task = asyncio.create_task(consume(topic_name))
    await task


def main():
    """Checks for topic and creates the topic if it does not exist"""
    try:
        asyncio.run(create_task(TOPIC))
    except KeyboardInterrupt as e:
        logger.info("shutting down")


if __name__ == "__main__":
    main()
