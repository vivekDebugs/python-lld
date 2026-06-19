from typing import TYPE_CHECKING
from observer import Observer

if TYPE_CHECKING:
    from message import Message

class Subscriber(Observer):
    def __init__(self, name):
        self.name = name

    def notify(self, message: 'Message'):
        print(self.name + " received message: " + message.body)