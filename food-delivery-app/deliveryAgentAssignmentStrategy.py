from typing import TYPE_CHECKING, Dict, Optional
from abc import ABC, abstractmethod

if TYPE_CHECKING:
    from order import Order
    from deliveryAgent import DeliveryAgent

class DeliveryAgentAssignmentStrategy(ABC):
    @abstractmethod
    def assignDeliveryAgent(self, order: 'Order', deliveryAgents: Dict[str, 'DeliveryAgent']) -> Optional['DeliveryAgent']:
        raise NotImplementedError()