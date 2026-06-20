from notifiable import Notifiable
from deliveryAgentStatus import DeliveryAgentStatus
from idGenService import IDGenService

class DeliveryAgent(Notifiable):
    def __init__(self, name: str, phone: str):
        super().__init__()
        self.id = IDGenService.generate()
        self.name = name
        self.phone = phone
        self.status = DeliveryAgentStatus.OFFLINE

    def online(self):
        self.status = DeliveryAgentStatus.AVAILABLE

    def offline(self):
        self.status = DeliveryAgentStatus.OFFLINE
