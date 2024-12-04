import json
import  config
from logger import get_logger

logger = get_logger(__name__, config.DEBUG)


def json_serializer(data: dict):
    try:
        return json.dumps(data).encode('utf-8')
    except Exception as e:
        logger.exception(f'{e}')
        return b''
