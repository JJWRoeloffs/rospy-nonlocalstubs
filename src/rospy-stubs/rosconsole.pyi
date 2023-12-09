from .logger_level_service_caller import LoggerLevelServiceCaller as LoggerLevelServiceCaller, ROSConsoleException as ROSConsoleException
from _typeshed import Incomplete

NAME: str

def error(status, msg) -> None: ...

class RosConsoleEcho:
    LEVEL_COLOR: Incomplete
    LEVEL_MAX_LENGTH: Incomplete
    def __init__(self, options) -> None: ...
    @staticmethod
    def get_levels(): ...

def main(argv: Incomplete | None = ...) -> None: ...
