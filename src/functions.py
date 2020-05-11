import logging

from src.classes import FooClass

logger = logging.getLogger(__name__)


def run(val1, val2):
    logger.info("run")

    foo = FooClass(value=val2)

    return val1 + foo.run()
