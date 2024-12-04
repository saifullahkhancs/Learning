import logging
import sys

def get_logger(name, debug=False):
    fmt = logging.Formatter("{asctime} {msecs:03.0f} | "
                            "{levelname} | "
                            "{module}:"
                            "{funcName}:"
                            "{lineno} - {message}",
                            style='{',
                            datefmt='%Y-%m-%d %I:%M:%S %p %z'
                            )

    logger = logging.getLogger(name)
    log_level = logging.DEBUG if debug else logging.INFO
    logger.setLevel(log_level)

    stdout_handler = logging.StreamHandler(sys.stdout)
    stdout_handler.setFormatter(fmt)
    stdout_handler.setLevel(log_level)
    stdout_handler.addFilter(lambda record: record.levelno < logging.ERROR)

    stderr_handler = logging.StreamHandler(sys.stderr)
    stderr_handler.setFormatter(fmt)
    stderr_handler.setLevel(logging.ERROR)

    logger.addHandler(stdout_handler)
    logger.addHandler(stderr_handler)
    return logger
