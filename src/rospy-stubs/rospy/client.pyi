from _typeshed import Incomplete
from rospy.core import logdebug as logdebug, logerr as logerr, loginfo as loginfo, logwarn as logwarn
from rospy.impl.tcpros_service import Service as Service

TIMEOUT_READY: float
DEBUG: Incomplete
INFO: Incomplete
WARN: Incomplete
ERROR: Incomplete
FATAL: Incomplete

def myargv(argv: Incomplete | None = ...): ...
def load_command_line_node_params(argv): ...
def on_shutdown(h) -> None: ...
def spin() -> None: ...
def init_node(name, argv: Incomplete | None = ..., anonymous: bool = ..., log_level: Incomplete | None = ..., disable_rostime: bool = ..., disable_rosout: bool = ..., disable_signals: bool = ..., xmlrpc_port: int = ..., tcpros_port: int = ...) -> None: ...
def get_master(env=...): ...
def get_published_topics(namespace: str = ...): ...

class _WFM:
    msg: Incomplete
    def __init__(self) -> None: ...
    def cb(self, msg) -> None: ...

def wait_for_message(topic, topic_type, timeout: Incomplete | None = ...): ...

class _Unspecified: ...

def get_param(param_name, default=...): ...
def get_param_cached(param_name, default=...): ...
def get_param_names(): ...
def set_param(param_name, param_value) -> None: ...
def search_param(param_name): ...
def delete_param(param_name) -> None: ...
def has_param(param_name): ...