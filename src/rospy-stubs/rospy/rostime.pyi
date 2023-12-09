import genpy

class Duration(genpy.Duration):
    def __init__(self, secs: int = ..., nsecs: int = ...) -> None: ...

class Time(genpy.Time):
    def __init__(self, secs: int = ..., nsecs: int = ...) -> None: ...
    @staticmethod
    def now(): ...
    @classmethod
    def from_seconds(cls, float_secs): ...

def get_rostime(): ...
def get_time(): ...
def set_rostime_initialized(val) -> None: ...
def is_rostime_initialized(): ...
def get_rostime_cond(): ...
def is_wallclock(): ...
def switch_to_wallclock() -> None: ...
def wallsleep(duration) -> None: ...
