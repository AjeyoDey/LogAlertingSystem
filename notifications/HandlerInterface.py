from abc import ABC, abstractmethod


class NotificationFactory:
    def get_notification_handler(self, notification_type: NotificationType):
        if notification_type == NotificationType.PHONE:
            return PhoneNotificationHandler()
        if notification_type == NotificationType.EMAIL:
            return EmailNotificationHandler()
        if notification_type == NotificationType.SMS:
            return SMSNotificationHandler()

class NotificationHandler(ABC):
    def __init__(self):
        self.subscribers = []

    @abstractmethod
    def notify(self):
        pass

    def set_subscriber(self, user_name: str):
        self.subscribers.append(user_name)

    def remove_subscriber(self, user_name: str):
        self.subscribers.remove(user_name)


class SMSNotificationHandler(NotificationHandler):
    __instance = None

    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = super().__new__(SMSNotificationHandler)
        return cls.__instance

    def __init__(self):
        if not hasattr(self, 'init'):
            super().__init__()
            self.init = True

    def notify(self):
        for user_name in self.subscribers:
            print(f"Notified {user_name} via SMS.")


class EmailNotificationHandler(NotificationHandler):
    __instance = None

    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = super().__new__(EmailNotificationHandler)
        return cls.__instance

    def __init__(self):
        if not hasattr(self, 'init'):
            super().__init__()
            self.init = True

    def notify(self):
        for user_name in self.subscribers:
            print(f"Notified {user_name} via Email.")


class PhoneNotificationHandler(NotificationHandler):
    __instance = None

    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = super().__new__(EmailNotificationHandler)
        return cls.__instance

    def __init__(self):
        if not hasattr(self, 'init'):
            super().__init__()
            self.init = True

    def notify(self):
        for user_name in self.subscribers:
            print(f"Notified {user_name} via Phone.")