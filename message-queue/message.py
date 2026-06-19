from typing import Any

class Message:
    def __init__(self, queue: str, topic: str, body: Any):
        self.queue = queue
        self.topic = topic
        self.body = body