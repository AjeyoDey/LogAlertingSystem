from datetime import datetime

from constants.constants import LogType
from logging.implementations.BlockerLogHandler import BlockerLogHandler
from logging.implementations.CriticalLogHandler import CriticalLogHandler
from logging.implementations.InfoLogHandler import InfoLogHandler
from logging.implementations.WarningLogHandler import WarningLogHandler


class Logger:
    __instance = None

    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = super().__new__(Logger)
        return cls.__instance

    def __init__(self):
        self.info_logger = InfoLogHandler()
        self.warning_logger = WarningLogHandler()
        self.critical_logger = CriticalLogHandler()
        self.blocker_logger = BlockerLogHandler()

    def get_logger(self, log_level: LogType):
        if log_level == LogType.INFO:
            return self.info_logger
        elif log_level == LogType.WARNING:
            return self.warning_logger
        elif log_level == LogType.CRITICAL:
            return self.critical_logger
        elif log_level == LogType.BLOCKER:
            return self.blocker_logger

    def log_message(
        self, log_level: LogType, message: str,
        timeStamp: datetime = datetime.now()
    ):
        logger = self.get_logger(log_level=log_level)
        logger.handle(timestamp=timeStamp, message=message)