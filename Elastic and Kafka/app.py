# import requests 
import asyncio
import json
import asyncio
from logger import get_logger
from _kafka import Consumer
from aiokafka import ConsumerRecord
import config
from elasticsearch import Elasticsearch,helpers

logger = get_logger(__name__ , config.DEBUG)
loop = asyncio.get_event_loop()
es = Elasticsearch([{'host': 'localhost', 'port': 9200 ,  'scheme': 'http'}],
                   basic_auth=("elastic", "Sw9FS-lCn=lcRFe2vho4"))
try:
    if es.ping():
        logger.info("Connected to Elasticsearch!")
    else:
        raise ConnectionError("Elasticsearch ping returned False")
except Exception as e:
    logger.error(f"Error connecting to Elasticsearch: {e}")
    raise SystemExit(f"Cannot start without Elasticsearch: {e}") from e
consumer = Consumer(config.KAFKA_BOOTSTRAP_SERVERS , loop=loop)
@consumer.consume([config.TOPIC] , group_id=config.KAFKA_INTERNAL_GROUP)
async def process_logs(message: ConsumerRecord):
    try:
        data = message.value
        if not data:
            logger.warning("Received empty message, skipping")
            return
        index = "url_data"
        res = es.index(index = index , body = data) 
        logger.info(f' the responce after saving the data is : - {res} ')
    except Exception as e:
        logger.exception(f"Failed to index message to Elasticsearch: {e}")
        raise
if __name__ == '__main__':
    loop.run_forever()