import json
import logging
import time

from kafka import KafkaProducer


def json_serializer(data):
    return json.dumps(data).encode("utf-8")


def setup_kafka_logging(logger_name='kafka', log_level=logging.INFO):
    logger = logging.getLogger(logger_name)
    logger.setLevel(log_level)

    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.DEBUG)

    formatter = logging.Formatter(
        '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    )
    console_handler.setFormatter(formatter)
    logger.addHandler(console_handler)

    return logger


def create_producer(bootstrap_servers='localhost:29092', serializer=None):
    if serializer is None:
        serializer = json_serializer

    setup_kafka_logging()

    return KafkaProducer(
        bootstrap_servers=bootstrap_servers,
        value_serializer=serializer,
    )


def send_event(producer, topic, event, sleep_after=5):
    response = producer.send(topic, event)
    print(response.get())
    time.sleep(sleep_after)
