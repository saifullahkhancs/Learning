# import requests 
import asyncio
import json
import os
import asyncio
from logger import get_logger
from _kafka import Consumer
from aiokafka import ConsumerRecord
import config
from elasticsearch import Elasticsearch,helpers

ES_HOST = os.environ.get("ES_HOST", "localhost")
ES_PORT = int(os.environ.get("ES_PORT", "9200"))
ES_USER = os.environ.get("ES_USER", "elastic")
ES_PASSWORD = os.environ.get("ES_PASSWORD", "")

logger = get_logger(__name__ , config.DEBUG)
loop = asyncio.get_event_loop()
es = Elasticsearch([{'host': ES_HOST, 'port': ES_PORT, 'scheme': 'http'}],
                   basic_auth=(ES_USER, ES_PASSWORD))
try:
    if es.ping():
        print("Connected to Elasticsearch!")
    else:
        print("Failed to connect to Elasticsearch.")
except Exception as e:
    print(f"Error connecting to Elasticsearch: {e}")
consumer = Consumer(config.KAFKA_BOOTSTRAP_SERVERS , loop=loop)
@consumer.consume([config.TOPIC] , group_id=config.KAFKA_INTERNAL_GROUP)
async def process_logs(message: ConsumerRecord):
    try:
        data = message.value
        print(data)
        index = "url_data"
        res = es.index(index = index , body = data) 
        logger.info(f' the responce after saving the data is : - {res} ')
    except Exception as e:
       logger.exception(e)
if __name__ == '__main__':
    loop.run_forever()