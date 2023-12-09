from _typeshed import Incomplete

INBOUND: str
OUTBOUND: str
BIDIRECTIONAL: str

class Transport:
    transport_type: str
    name: Incomplete
    direction: Incomplete
    done: bool
    cleanup_cb: Incomplete
    endpoint_id: str
    id: Incomplete
    stat_bytes: int
    stat_num_msg: int
    local_endpoint: Incomplete
    remote_endpoint: Incomplete
    def __init__(self, direction, name: str = ...) -> None: ...
    def fileno(self) -> None: ...
    def set_cleanup_callback(self, cleanup_callback) -> None: ...
    def close(self) -> None: ...
    def write_data(self, data) -> None: ...
    def get_transport_info(self) -> None: ...

class DeadTransport(Transport):
    transport_type: Incomplete
    id: Incomplete
    stat_bytes: Incomplete
    stat_num_msg: Incomplete
    done: bool
    endpoint_id: Incomplete
    local_endpoint: Incomplete
    remote_endpoint: Incomplete
    def __init__(self, transport) -> None: ...
    def get_transport_info(self): ...

class ProtocolHandler:
    def shutdown(self) -> None: ...
    def create_transport(self, topic, pub_uri, protocol_params) -> None: ...
    def supports(self, protocol): ...
    def get_supported(self): ...
    def init_publisher(self, topic, protocol) -> None: ...
