from typing import Dict, TYPE_CHECKING

if TYPE_CHECKING:
    from topic import Topic


class MessageQueue:
    def __init__(self, name):
        self.name = name
        self.topics: Dict[str, 'Topic'] = {}