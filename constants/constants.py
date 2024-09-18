import enum


class LogType(enum.Enum):
    INFO = "INFO"
    WARNING = "WARNING"
    CRITICAL = "CRITICAL"

    BLOCKER = "BLOCKER"

    @classmethod
    def from_string(cls, value: str):
        value = value.upper()  # Make the string case-insensitive
        for log_type in cls:
            if log_type.value == value:
                return log_type


class NotificationType(enum.Enum):
    SMS = "SMS"
    PHONE = "PHONE"
    EMAIL = "EMAIL"


class ConfigParameters(enum.Enum):
    THRESHOLD = "THRESHOLD"
    DURATION = "DURATION"
    WAIT = "WAIT"
    SUBSCRIBERS = "SUBSCRIBERS"