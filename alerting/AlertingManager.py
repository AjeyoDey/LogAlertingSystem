import threading
import time

from constants.constants import LogType
from logging.Logger import Logger


class AlertManager:
    # To make the AlertManager singleton, it should not have a specific logger as a state (class variable)
    # Concrete loggers will be pulled in from
    def __init__(self):
        self.alert_check_window = 10
        self.threads = {}
        self.stop_event = threading.Event()

    def raise_alert(self, log_type: LogType):
        if self.check_log(log_type):
            logger = Logger().get_logger(log_level=log_type)
            logger.notify_subscribers()

    def check_log(self, log_type: LogType):
        logger = Logger().get_logger(log_level=log_type)
        return logger.is_threshold_breached()

    def analyse_logs(self, log_type: LogType):
        logger = Logger().get_logger(log_level=log_type)
        time_duration = logger.duration

        while not self.stop_event.is_set():
            if self.check_log(log_type):
                self.raise_alert(log_type)
            # Sleep for the Time Duration of a AlertWindow before polling again
            time.sleep(time_duration)

    def start_analysing(self):
        # Create and start threads for each log type
        for log_type in LogType:
            self.threads[log_type] = threading.Thread(target=self.analyse_logs, args=(log_type,))
            self.threads[log_type].start()

    def stop_analysing(self):
        self.stop_event.set()
        for thread in self.threads.values():
            thread.join()
