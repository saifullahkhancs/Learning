import json
import config
from logger import get_logger

logger = get_logger(__name__, config.DEBUG)


def json_deserializer(data: bytes):
    try:
        logger.debug(f'\nDeserializing: {data}')
        return json.loads(data.decode('utf-8'))
    except json.JSONDecodeError as e:
        logger.exception(f'{e}')
        return {}
    except Exception as e:
        logger.exception(f'{e}')
        return {}
