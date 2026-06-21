import json
import config
from logger import get_logger

logger = get_logger(__name__, config.DEBUG)


def json_deserializer(data: bytes):
    try:
        logger.debug(f'\nDeserializing: {data}')
        return json.loads(data.decode('utf-8'))
    except json.JSONDecodeError as e:
        logger.exception(f'Failed to deserialize JSON: {e}')
        raise ValueError(f'Invalid JSON data: {e}') from e
    except Exception as e:
        logger.exception(f'Unexpected deserialization error: {e}')
        raise
