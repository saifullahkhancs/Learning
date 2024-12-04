# import requests 
import asyncio
import json
import asyncio
import uuid
from logger import get_logger
from _kafka import Consumer
from aiokafka import ConsumerRecord
import config
from elasticsearch import Elasticsearch,helpers
from elasticsearch_dsl import connections
import traceback
import time
from datetime import datetime
import jmespath

from utils import process_data , index_mapper , model_mapper


logger = get_logger(__name__ , config.DEBUG)
loop = asyncio.get_event_loop()
# es = Elasticsearch([{'host': 'localhost', 'port': 9200 ,  'scheme': 'http'}],
#                    basic_auth=("elastic", "Sw9FS-lCn=lcRFe2vho4"))
if not config.ELASTICSEARCH_AUTH_ENABLED:
    connections.create_connection(
        hosts=f'http://{config.ELASTICSEARCH_HOST}',
        verify_certs=False, timeout=40, max_retries=5,
        retry_on_timeout=True,
        ssl_show_warn=False)
else:
    connections.create_connection(
        hosts=f'https://'
              f'{config.ELASTICSEARCH_USER}:'
              f'{config.ELASTICSEARCH_PASSWORD}@'
              f'{config.ELASTICSEARCH_HOST}',
        verify_certs=False, timeout=40, max_retries=5,
        retry_on_timeout=True,
        ssl_show_warn=False)

es = connections.get_connection()

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
        artifact_type = data.get("type")
        pro_data = await process_data(data , artifact_type)
        index = index_mapper.get(artifact_type)
        model = model_mapper.get(artifact_type)
        body = model(**pro_data) 
        if es.indices.exists(index = index):
            if isinstance(body.name, list):  # If name is a list
                resp = es.search(
                    index=index,
                    query={
                        "terms": {
                            "name": body.name  # Pass the list of names to search for
                        }
                    }
                )
            else:  # If name is a string
                resp = es.search(
                    index=index,
                    query={
                        "match": {
                            "name": body.name  # Use match query for a single string value
                        }
                    }
            )            
            if resp['hits']['hits']:

                doc_id = resp['hits']['hits'][0]["_id"]
                update_body = body.dict(exclude_none=True)
                res = es.update(index=index, id=doc_id, body={"doc": update_body})      
        else:
            res = es.index(index=index, id=data.get("_id"),  body=body.dict(exclude_none=True)) 
        
        # logger.info(f' the responce after saving the data is : - {res} ')
    except Exception as e:
       logger.error(e)
       logger.error(f"Traceback: {traceback.format_exc()}")
if __name__ == '__main__':
    loop.run_forever()