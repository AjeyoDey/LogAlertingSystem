import threading
from abc import abstractmethod, ABC
from collections import deque
from datetime import datetime

from constants.constants import NotificationType


class LogHandler(ABC):
    def __init__(self, threshold: int, duration: int, wait_time: int):
        self.__subscribers = []
        self.logs = []
        self.alert_window = deque()
        self.threshold = threshold
        self.duration = duration
        self.wait_time = wait_time
        self.lock = threading.Lock()

    @abstractmethod
    def handle(self, timestamp: datetime, message: str):
        pass

    @abstractmethod
    def is_threshold_breached(self) -> bool:
        pass

    @abstractmethod
    def trim_logs_till_time(self, start_time):
        pass

    def get_alert_count(self) -> int:
        return len(self.alert_window)

    def set_subscriber(self, notification_type: NotificationType):
        self.__subscribers.append(notification_type)

    def remove_subscriber(self, notification_type: NotificationType):
        self.__subscribers.remove(notification_type)

    def notify_subscribers(self):
        for subscriber in self.__subscribers:
            subscriber.notify()