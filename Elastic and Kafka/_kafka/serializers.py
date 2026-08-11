import json
import config
from logger import get_logger

logger = get_logger(__name__, config.DEBUG)


def json_serializer(data: dict):
    try:
        return json.dumps(data).encode('utf-8')
    except (TypeError, ValueError) as e:
        logger.exception(f'Failed to serialize data to JSON: {e}')
        raise
    except Exception as e:
        logger.exception(f'Unexpected serialization error: {e}')
        raise
