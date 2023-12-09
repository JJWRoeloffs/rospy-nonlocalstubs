from rospy.core import *
from rospy.impl.transport import *
from _typeshed import Incomplete
from rospy.impl.registration import Registration as Registration, get_registration_listeners as get_registration_listeners, set_service_manager as set_service_manager

logger: Incomplete

class ServiceException(Exception): ...

class _Service:
    resolved_name: Incomplete
    service_class: Incomplete
    request_class: Incomplete
    response_class: Incomplete
    uri: Incomplete
    def __init__(self, name, service_class) -> None: ...

class ServiceManager:
    map: Incomplete
    lock: Incomplete
    registration_listeners: Incomplete
    def __init__(self, registration_listeners: Incomplete | None = ...) -> None: ...
    def get_services(self): ...
    def unregister_all(self) -> None: ...
    def register(self, resolved_service_name, service) -> None: ...
    def unregister(self, resolved_service_name, service) -> None: ...
    def get_service(self, resolved_service_name): ...
