from typing import List, TYPE_CHECKING
from observable import Observable

if TYPE_CHECKING:
    from subscriber import Subscriber
    from message import Message

class Topic(Observable): 
    def __init__(self, name):
        self.name = name
        self.subscribers: List['Subscriber'] = []

    def addSubscriber(self, subscriber: 'Subscriber'):
        self.subscribers.append(subscriber)

    def notifySubscribers(self, message: 'Message'):
        for subscriber in self.subscribers:
            subscriber.notify(message)