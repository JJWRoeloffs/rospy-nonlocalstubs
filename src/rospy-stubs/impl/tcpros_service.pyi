from _typeshed import Incomplete
from rospy.core import logdebug as logdebug, logerr as logerr, loginfo as loginfo, logwarn as logwarn
from rospy.exceptions import ROSException as ROSException, ROSInterruptException as ROSInterruptException, TransportInitError as TransportInitError, TransportTerminated as TransportTerminated
from rospy.impl.registration import get_service_manager as get_service_manager
from rospy.impl.tcpros_base import DEFAULT_BUFF_SIZE as DEFAULT_BUFF_SIZE, TCPROSTransport as TCPROSTransport, TCPROSTransportProtocol as TCPROSTransportProtocol, get_tcpros_server_address as get_tcpros_server_address, recv_buff as recv_buff, start_tcpros_server as start_tcpros_server
from rospy.service import ServiceException as ServiceException, _Service

def isstring(s): ...

logger: Incomplete

def wait_for_service(service, timeout: Incomplete | None = ...): ...
def convert_return_to_response(response, response_class): ...
def service_connection_handler(sock, client_addr, header): ...

class TCPService(TCPROSTransportProtocol):
    service_class: Incomplete
    def __init__(self, resolved_name, service_class, buff_size=...) -> None: ...
    def get_header_fields(self): ...

class TCPROSServiceClient(TCPROSTransportProtocol):
    service_class: Incomplete
    headers: Incomplete
    buff_size: Incomplete
    def __init__(self, resolved_name, service_class, headers: Incomplete | None = ..., buff_size=...) -> None: ...
    def get_header_fields(self): ...
    def read_messages(self, b, msg_queue, sock) -> None: ...

class ServiceProxy(_Service):
    uri: Incomplete
    seq: int
    buff_size: Incomplete
    persistent: Incomplete
    protocol: Incomplete
    transport: Incomplete
    def __init__(self, name, service_class, persistent: bool = ..., headers: Incomplete | None = ...) -> None: ...
    def wait_for_service(self, timeout: Incomplete | None = ...) -> None: ...
    def __call__(self, *args, **kwds): ...
    def call(self, *args, **kwds): ...
    def close(self) -> None: ...

class ServiceImpl(_Service):
    handler: Incomplete
    registered: bool
    seq: int
    done: bool
    buff_size: Incomplete
    uri: Incomplete
    protocol: Incomplete
    def __init__(self, name, service_class, handler, buff_size=..., error_handler: Incomplete | None = ...) -> None: ...
    def error_handler(self, e, exc_type, exc_value, tb) -> None: ...
    def shutdown(self, reason: str = ...) -> None: ...
    def spin(self) -> None: ...
    def handle(self, transport, header) -> None: ...

class Service(ServiceImpl):
    def __init__(self, name, service_class, handler, buff_size=..., error_handler: Incomplete | None = ...) -> None: ...
