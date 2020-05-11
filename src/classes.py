import logging

logger = logging.getLogger(__name__)


class FooClass:
    def __init__(self, value):
        self.value = value

    def run(self):
        logger.info(f"FooClass.run<value={self.value}>")
        return self.value + 1
