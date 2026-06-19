from typing import Dict, Any
from messageQueue import MessageQueue
from topic import Topic
from subscriber import Subscriber
from message import Message

class MessageQueueSystem:
    def __init__(self):
        self.queues: Dict[str, MessageQueue] = {}
        self.subscribers: Dict[str, Subscriber] = {}

    def createQueue(self, name: str):
        queue = MessageQueue(name)
        self.queues[name] = queue
        return queue

    def createTopic(self, queueName: str, topicName: str):
        queue = self.queues[queueName]
        topic = Topic(topicName)
        queue.topics[topicName] = topic
        return topic

    def createSubscriber(self, name: str):
        subscriber = Subscriber(name)
        self.subscribers[name] = subscriber
        return subscriber

    def addSubscriber(self, queueName: str, topicName: str, subscriberName: str):
        queue = self.queues[queueName]
        topic = queue.topics[topicName]
        subscriber = self.subscribers[subscriberName]
        topic.addSubscriber(subscriber)

    def publishMessage(self, queueName: str, topicName: str, body: Any):
        message = Message(queueName, topicName, body)
        queue = self.queues[queueName]
        topic = queue.topics[topicName]
        topic.notifySubscribers(message)
