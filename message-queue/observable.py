from abc import ABC, abstractmethod

class Observable(ABC):
    @abstractmethod
    def addSubscriber(self):
        raise NotImplementedError()

    @abstractmethod
    def notifySubscribers(self):
        raise NotImplementedError()