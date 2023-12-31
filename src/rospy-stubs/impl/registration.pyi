from _typeshed import Incomplete
from rospy.core import add_preshutdown_hook as add_preshutdown_hook, is_shutdown as is_shutdown, is_shutdown_requested as is_shutdown_requested, logdebug as logdebug, logerr as logerr, logfatal as logfatal, loginfo as loginfo, logwarn as logwarn, signal_shutdown as signal_shutdown, xmlrpcapi as xmlrpcapi
from rospy.names import get_caller_id as get_caller_id, get_namespace as get_namespace

def set_topic_manager(tm) -> None: ...
def get_topic_manager(): ...
def set_service_manager(sm) -> None: ...
def get_service_manager(): ...

class Registration:
    PUB: str
    SUB: str
    SRV: str

class RegistrationListener:
    def reg_added(self, resolved_name, data_type_or_uri, reg_type) -> None: ...
    def reg_removed(self, resolved_name, data_type_or_uri, reg_type) -> None: ...

class RegistrationListeners:
    listeners: Incomplete
    lock: Incomplete
    def __init__(self) -> None: ...
    def add_listener(self, l) -> None: ...
    def notify_removed(self, resolved_name, data_type_or_uri, reg_type) -> None: ...
    def notify_added(self, resolved_name, data_type, reg_type) -> None: ...
    def clear(self) -> None: ...

def get_registration_listeners(): ...

class RegManager(RegistrationListener):
    logger: Incomplete
    handler: Incomplete
    uri: Incomplete
    updates: Incomplete
    cond: Incomplete
    registered: bool
    def __init__(self, handler) -> None: ...
    master_uri: Incomplete
    def start(self, uri, master_uri) -> None: ...
    def is_registered(self): ...
    def run(self) -> None: ...
    def cleanup(self, reason) -> None: ...
    def reg_removed(self, resolved_name, data_type_or_uri, reg_type) -> None: ...
    def reg_added(self, resolved_name, data_type_or_uri, reg_type) -> None: ...
    def publisher_update(self, resolved_name, uris) -> None: ...
