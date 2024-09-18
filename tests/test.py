import unittest
from datetime import datetime, timedelta
from unittest.mock import patch, MagicMock

from alerting.AlertingManager import AlertManager
from config.ConfigHandler import ConfigHandler
from constants.constants import LogType
from logging.Logger import Logger
from logging.implementations.BlockerLogHandler import BlockerLogHandler
from logging.implementations.CriticalLogHandler import CriticalLogHandler
from logging.implementations.InfoLogHandler import InfoLogHandler
from logging.implementations.WarningLogHandler import WarningLogHandler


class TestLogHandler(unittest.TestCase):
    def setUp(self):
        self.config_handler = ConfigHandler()
        self.now = datetime.now()

    def test_info_log_handler(self):
        handler = InfoLogHandler()
        handler.handle(self.now, "Info message")
        handler.handle(self.now + timedelta(seconds=1), "Another Info message")
        self.assertEqual(len(handler.logs), 2)
        self.assertFalse(handler.is_threshold_breached())

        # Simulate more messages to breach threshold
        for _ in range(3):
            handler.handle(self.now + timedelta(seconds=2), "Breaching Info message")
        self.assertTrue(handler.is_threshold_breached())

    def test_warning_log_handler(self):
        handler = WarningLogHandler()
        handler.handle(self.now, "Warning message")
        handler.handle(self.now + timedelta(seconds=1), "Another Warning message")
        self.assertEqual(len(handler.logs), 2)
        self.assertFalse(handler.is_threshold_breached())

        # Simulate more messages to breach threshold
        for _ in range(3):
            handler.handle(self.now + timedelta(seconds=2), "Breaching Warning message")
        self.assertTrue(handler.is_threshold_breached())

    def test_critical_log_handler(self):
        handler = CriticalLogHandler()
        handler.handle(self.now, "Critical message")
        handler.handle(self.now + timedelta(seconds=1), "Another Critical message")
        self.assertEqual(len(handler.logs), 2)
        self.assertFalse(handler.is_threshold_breached())

        # Simulate more messages to breach threshold
        for _ in range(3):
            handler.handle(self.now + timedelta(seconds=2), "Breaching Critical message")
        self.assertTrue(handler.is_threshold_breached())

    def test_blocker_log_handler(self):
        handler = BlockerLogHandler()
        handler.handle(self.now, "Blocker message")
        handler.handle(self.now + timedelta(seconds=1), "Another Blocker message")
        self.assertEqual(len(handler.logs), 2)
        self.assertFalse(handler.is_threshold_breached())

        # Simulate more messages to breach threshold
        for _ in range(3):
            handler.handle(self.now + timedelta(seconds=2), "Breaching Blocker message")
        self.assertTrue(handler.is_threshold_breached())


class TestAlertManager(unittest.TestCase):
    def setUp(self):
        self.alert_manager = AlertManager()
        self.logger = Logger()

    @patch.object(Logger, 'get_logger')
    @patch.object(Logger, 'log_message')
    def test_alert_triggering(self, mock_log_message, mock_get_logger):
        # Mock LogHandler's is_threshold_breached method
        mock_handler = MagicMock()
        mock_handler.is_threshold_breached.return_value = True
        mock_get_logger.return_value = mock_handler

        # Start the AlertManager to simulate alert checking
        with patch.object(AlertManager, 'check_log', return_value=True):
            self.alert_manager.raise_alert(LogType.INFO)

        # Verify that notify_subscribers is called
        mock_handler.notify_subscribers.assert_called_once()

    @patch.object(AlertManager, 'analyse_logs')
    def test_start_stop_analyse_logs(self, mock_analyse_logs):
        # Start analysing logs
        self.alert_manager.start_analysing()
        self.assertEqual(len(self.alert_manager.threads), len(LogType))

        # Stop analysing logs
        self.alert_manager.stop_analysing()
        self.alert_manager.stop_event.set()
        self.assertTrue(self.alert_manager.stop_event.is_set())
