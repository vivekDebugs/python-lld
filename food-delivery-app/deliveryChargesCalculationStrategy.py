from typing import TYPE_CHECKING
from abc import ABC, abstractmethod

if TYPE_CHECKING:
    from order import Order

class DeliveryChargesCalculationStrategy:
    @abstractmethod
    def calculateDeliveryCharges(self, order: 'Order') -> float:
        raise NotImplementedError()