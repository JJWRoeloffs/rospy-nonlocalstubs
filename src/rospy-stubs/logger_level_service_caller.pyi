class ROSConsoleException(Exception): ...

class LoggerLevelServiceCaller:
    def __init__(self) -> None: ...
    def get_levels(self): ...
    def get_loggers(self, node): ...
    def get_node_names(self): ...
    def send_logger_change_message(self, node, logger, level): ...
