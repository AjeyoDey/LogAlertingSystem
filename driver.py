import time
import unittest
from datetime import datetime

# Function to process file and log messages
from alerting.AlertingManager import AlertManager
from constants.constants import LogType
from logging.Logger import Logger


def process_log_file(file_path: str):
    logger = Logger()
    with open(file_path, 'r') as file:
        for line in file:
            line = line.strip()  # Remove any extra whitespace
            if not line:
                continue

            # Split the line into parts
            parts = line.split(' ', 2)
            if len(parts) < 3:
                print(f"Skipping invalid line: {line}")
                continue

            timestamp_str, log_level_str, message = parts

            # Parse timestamp
            try:
                timestamp = datetime.strptime(timestamp_str, '%Y-%m-%d %H:%M:%S')
            except ValueError:
                print(f"Skipping invalid timestamp: {timestamp_str}")
                continue

            # Map log level string to LogType
            log_level = LogType.from_string(log_level_str.upper())
            if not log_level:
                print(f"Skipping invalid log level: {log_level_str}")
                continue

            # Log the message
            logger.log_message(log_level, message=message, timeStamp=timestamp)


def driver():
    logger = Logger()
    alertManager = AlertManager()
    alertManager.stop_analysing()

    logger.log_message(LogType.INFO, message="Info 1")
    time.sleep(0.001)
    logger.log_message(LogType.INFO, message="Info 2")
    time.sleep(0.002)
    logger.log_message(LogType.INFO, message="Info 3")
    time.sleep(0.003)
    logger.log_message(LogType.INFO, message="Info 4")
    time.sleep(0.004)
    logger.log_message(LogType.INFO, message="Info 5")
    time.sleep(0.005)
    logger.log_message(LogType.INFO, message="Info 1")
    time.sleep(0.001)
    logger.log_message(LogType.INFO, message="Info 2")
    time.sleep(0.002)
    logger.log_message(LogType.INFO, message="Info 3")
    time.sleep(0.003)
    logger.log_message(LogType.INFO, message="Info 4")
    time.sleep(0.004)
    logger.log_message(LogType.INFO, message="Info 5")
    time.sleep(0.005)

    logger.log_message(LogType.WARNING, message="Info 1")
    time.sleep(0.001)
    logger.log_message(LogType.WARNING, message="Info 2")
    time.sleep(0.002)
    logger.log_message(LogType.WARNING, message="Info 3")
    time.sleep(0.003)
    logger.log_message(LogType.WARNING, message="Info 4")
    time.sleep(0.004)
    logger.log_message(LogType.WARNING, message="Info 5")
    time.sleep(0.005)

    # Stop the AlertManager
    alertManager.stop_analysing()

    # Testing the Unit Test Cases
    unittest.main()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    driver()
