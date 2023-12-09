from rospy.core import *
from _typeshed import Incomplete
from rosgraph.xmlrpc import XmlRpcHandler
from rospy.impl.paramserver import get_param_server_cache as get_param_server_cache
from rospy.impl.registration import RegManager as RegManager, get_topic_manager as get_topic_manager
from rospy.impl.validators import ParameterInvalid as ParameterInvalid, non_empty as non_empty

STATUS: int
MSG: int
VAL: int

def is_publishers_list(paramName): ...

LOG_API: bool

def apivalidate(error_return_value, validators=...): ...

class ROSHandler(XmlRpcHandler):
    masterUri: Incomplete
    name: Incomplete
    uri: Incomplete
    done: bool
    protocol_handlers: Incomplete
    reg_man: Incomplete
    def __init__(self, name, master_uri) -> None: ...
    @classmethod
    def remappings(cls, methodName): ...
    def getUri(self, caller_id): ...
    def getName(self, caller_id): ...
    def getBusStats(self, caller_id): ...
    def getBusInfo(self, caller_id): ...
    def getMasterUri(self, caller_id): ...
    def shutdown(self, caller_id, msg: str = ...): ...
    def getPid(self, caller_id): ...
    def getSubscriptions(self, caller_id): ...
    def getPublications(self, caller_id): ...
    def paramUpdate(self, caller_id, parameter_key, parameter_value): ...
    def publisherUpdate(self, caller_id, topic, publishers): ...
    def requestTopic(self, caller_id, topic, protocols): ...
