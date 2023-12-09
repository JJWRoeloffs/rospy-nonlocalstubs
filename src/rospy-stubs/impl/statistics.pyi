from _typeshed import Incomplete

class SubscriberStatisticsLogger:
    @classmethod
    def is_enabled(cls): ...
    subscriber_name: Incomplete
    connections: Incomplete
    def __init__(self, subscriber) -> None: ...
    min_elements: Incomplete
    max_elements: Incomplete
    min_window: Incomplete
    max_window: Incomplete
    def read_parameters(self) -> None: ...
    def callback(self, msg, publisher, stat_bytes) -> None: ...
    def shutdown(self) -> None: ...

class ConnectionStatisticsLogger:
    topic: Incomplete
    subscriber: Incomplete
    publisher: Incomplete
    pub: Incomplete
    last_pub_time: Incomplete
    pub_frequency: Incomplete
    age_list_: Incomplete
    arrival_time_list_: Incomplete
    last_seq_: int
    dropped_msgs_: int
    window_start: Incomplete
    stat_bytes_last_: int
    stat_bytes_window_: int
    def __init__(self, topic, subscriber, publisher) -> None: ...
    def sendStatistics(self, subscriber_statistics_logger) -> None: ...
    def callback(self, subscriber_statistics_logger, msg, stat_bytes) -> None: ...
    def shutdown(self) -> None: ...
