import logging
from logging import StreamHandler
from telegram_send import TelegramJustSend

logger = logging.getLogger(__name__)


class TelegramHandler(StreamHandler):
    def __init__(self, chat_id, alias, token=None):
        StreamHandler.__init__(self)
        self.t = TelegramJustSend(chat_id, alias, api_key=token)
        self.t.start()

    def emit(self, msg):
        self.t.send(self.format(msg))
