import unittest
import time

import logging

from src.logging_telegram_handler import TelegramHandler


class MyTestCase(unittest.TestCase):
    def test_something(self):

        chat_id = "211945135"
        alias = "[TEST logging_telegram_handler]"

        logging.basicConfig(level=logging.WARNING)

        logger = logging.getLogger(__name__)

        telegram_handler = TelegramHandler(chat_id, alias)
        telegram_handler.setLevel(logging.WARNING)
        logger.addHandler(telegram_handler)

        logger.critical("critical")
        logger.error("error")
        logger.warning("warning")
        logger.info("info")
        logger.debug("debug")

        time.sleep(2)

        self.assertEqual(True, True)  # add assertion here


if __name__ == '__main__':
    unittest.main()
