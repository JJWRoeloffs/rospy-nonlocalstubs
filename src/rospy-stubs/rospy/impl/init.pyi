import rosgraph.xmlrpc
from ..core import is_shutdown as is_shutdown, rospyerr as rospyerr, signal_shutdown as signal_shutdown
from .masterslave import ROSHandler as ROSHandler
from .tcpros import init_tcpros as init_tcpros
from _typeshed import Incomplete
from rosgraph.rosenv import DEFAULT_MASTER_PORT as DEFAULT_MASTER_PORT

DEFAULT_NODE_PORT: int

def start_node(environ, resolved_name, master_uri: Incomplete | None = ..., port: int = ..., tcpros_port: int = ...): ...

class RosStreamHandler(rosgraph.roslogging.RosStreamHandler):
    def __init__(self, colorize: bool = ..., stdout: Incomplete | None = ..., stderr: Incomplete | None = ...) -> None: ...
