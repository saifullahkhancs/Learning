import asyncio

from aiokafka import AIOKafkaConsumer
import config
from utils import run_in_threadpool
from .deserializers import json_deserializer
from logger import get_logger

logger = get_logger(__name__, config.DEBUG)


class Consumer:
    def __init__(self,
                 bootstrap_servers,
                 value_deserializer=lambda x: json_deserializer(x),
                 enable_auto_commit=False,
                 loop=None,
                 **kwargs):
        self.bootstrap_servers = bootstrap_servers
        self.enable_auto_commit = enable_auto_commit
        self.value_deserializer = value_deserializer
        self.kwargs = kwargs
        self.loop = loop or asyncio.get_event_loop()

    async def __async_consumer(self,
                               bootstrap_servers,
                               group_id,
                               value_deserializer,
                               enable_auto_commit,
                               loop,
                               topics,
                               callback,
                               **kwargs):
        is_coroutine = asyncio.iscoroutinefunction(callback)
        logger.info('Creating Kafka consumer')
        consumer = AIOKafkaConsumer(bootstrap_servers=bootstrap_servers,
                                    group_id=group_id,
                                    value_deserializer=value_deserializer,
                                    enable_auto_commit=enable_auto_commit,
                                    max_poll_records=100,
                                    loop=loop,
                                    **kwargs)
        logger.info('Subscribing Kafka topics')
        consumer.subscribe(topics)
        logger.info(f'Starting Kafka consumer on topics {topics} and group {group_id}')
        await consumer.start()
        try:
            logger.info('Consuming messages')
            async for message in consumer:
                logger.info('Received message')
                if is_coroutine:
                    await callback(message)
                else:
                    await run_in_threadpool(callback, message)
                logger.info('Processed message')
                await consumer.commit()
                logger.info('Committed message')
        except Exception as e:
            logger.error(f'{e}', exc_info=True)
        finally:
            logger.info('Stopping Kafka consumer')
            await consumer.stop()
            self.loop.stop()

    def _add_handler(self, topics: list, group_id: str, f):
        self.loop.create_task(
            self.__async_consumer(self.bootstrap_servers, group_id,
                                  self.value_deserializer,
                                  self.enable_auto_commit,
                                  self.loop, topics, f, **self.kwargs))

    def consume(self, topics: list, group_id: str):
        def decorator(f):
            self._add_handler(topics, group_id, f)
            return f

        return decorator

    def run(self):
        self.loop.run_forever()
