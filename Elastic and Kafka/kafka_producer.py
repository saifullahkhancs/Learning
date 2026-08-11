from confluent_kafka import Producer, Consumer, KafkaException
from elasticsearch import Elasticsearch,helpers
from elasticsearch.exceptions import TransportError, ConnectionError, NotFoundError
import json
import random
from datetime import datetime
producer_conf = {
    'bootstrap.servers': 'localhost:29092'
}

try:
    producer = Producer(producer_conf)
except Exception as e:
    print(f"Error connecting to kafka: {e}")
    raise SystemExit(f"Cannot start without Kafka: {e}") from e

def acked(err, msg):
    if err is not None:
        print("Failed to deliver message: %s: %s" % (str(msg), str(err)))
    else:
        print("Message produced:", msg.value().decode())
        print(f"Message delivered to {msg.topic()}  [{msg.partition()}]")

topic  = "logs"
log_levels = ['DEBUG', 'INFO', 'WARN', 'ERROR']
sources = ['application', 'system']
messages = [
    'User login successful', 'User login failed', 'Database connection established',
    'Error reading from file', 'Service started', 'Service stopped',
    'Unexpected error occurred', 'Configuration updated', 'Resource not found',
    'File uploaded', 'Timeout while connecting', 'Permission denied',
    'Server overload', 'Session expired', 'Cache cleared', 'Data synchronized'
]

# Function to generate log messages
def generate_log():
    return {
        "timestamp":  int(datetime.now().timestamp ()*1000) ,
        "log_level": random.choice(log_levels),
        "message": random.choice(messages),
        "source": random.choice(sources)
    }

log_messages = [generate_log() for _ in range(random.randint(15, 20))]
message = log_messages[0]
data = json.dumps(message)

print(data)

producer.produce(topic , key = "key",  value= data , callback = acked )
producer.poll(1)
