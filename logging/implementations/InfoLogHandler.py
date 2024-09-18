#Singleton Class
from datetime import datetime, timedelta

from config.ConfigHandler import ConfigHandler
from constants.constants import LogType, ConfigParameters
from logging.LogHandler import LogHandler


class InfoLogHandler(LogHandler):
    __instance = None

    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = super().__new__(InfoLogHandler)
        return cls.__instance

    def __init__(self):
        # Only to initiate once
        if not hasattr(self, 'init'):
            self.log_type = LogType.INFO

            # Configuration Initilization
            configHandler = ConfigHandler()
            self.config = configHandler.get_config(self.log_type)
            threshold = configHandler.get_config_value(self.log_type, ConfigParameters.THRESHOLD)
            duration = configHandler.get_config_value(self.log_type, ConfigParameters.DURATION)
            wait = configHandler.get_config_value(self.log_type, ConfigParameters.WAIT)

            super().__init__(threshold=threshold, duration=duration, wait_time=wait)

            subscribers = configHandler.get_config_value(self.log_type, ConfigParameters.SUBSCRIBERS)
            for subscriber in subscribers:
                self.set_subscriber(subscriber)

            self.init = True

    def handle(self, timestamp: datetime, message: str):
        with self.lock:
            self.logs.append((timestamp, message))
            self.alert_window.append(timestamp)

    def is_threshold_breached(self) -> bool:
        time_now = datetime.now()
        time_duration_start: datetime = time_now - timedelta(seconds=self.duration)
        self.trim_logs_till_time(time_duration_start)

        if self.get_alert_count() < self.threshold:
            return False

        return True

    def trim_logs_till_time(self, start_time):
        with self.lock:
            while len(self.alert_window) > 0 and self.alert_window[0] <= start_time:
                self.alert_window.popleft()
