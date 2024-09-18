from constants.constants import ConfigParameters, LogType, NotificationType


class ConfigHandler:
    def __init__(self):
        self.config = {
            LogType.INFO: {
                ConfigParameters.THRESHOLD: 3,
                ConfigParameters.DURATION: 10,
                ConfigParameters.WAIT: 10,
                ConfigParameters.SUBSCRIBERS: [NotificationType.SMS]
            },
            LogType.WARNING: {
                ConfigParameters.THRESHOLD: 3,
                ConfigParameters.DURATION: 10,
                ConfigParameters.WAIT: 10,
                ConfigParameters.SUBSCRIBERS: [NotificationType.SMS, NotificationType.EMAIL]
            },
            LogType.CRITICAL: {
                ConfigParameters.THRESHOLD: 3,
                ConfigParameters.DURATION: 10,
                ConfigParameters.WAIT: 10,
                ConfigParameters.SUBSCRIBERS: [NotificationType.SMS, NotificationType.EMAIL, NotificationType.PHONE]
            },
            LogType.BLOCKER: {
                ConfigParameters.THRESHOLD: 3,
                ConfigParameters.DURATION: 10,
                ConfigParameters.WAIT: 10,
                ConfigParameters.SUBSCRIBERS: [NotificationType.SMS, NotificationType.EMAIL, NotificationType.PHONE]
            },
        }

    def load_config(self, config: dict):
        pass

    def get_config(self, log_type: LogType):
        if log_type not in self.config:
            return None

        return self.config[log_type]

    def get_config_value(self, log_type: LogType, config_param: ConfigParameters):
        config = self.get_config(log_type)

        if config_param not in config:
            return None

        return config[config_param]
