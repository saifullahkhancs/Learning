import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

import asyncio
import json
from logger import get_logger
from _kafka import Consumer
from aiokafka import ConsumerRecord
import config
from shared.elasticsearch_utils import create_es_client

logger = get_logger(__name__ , config.DEBUG)
loop = asyncio.get_event_loop()
es = create_es_client(password="Sw9FS-lCn=lcRFe2vho4")
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