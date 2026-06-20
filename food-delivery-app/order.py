from typing import List
from restaurant import Restaurant
from orderItem import OrderItem
from user import User
from deliveryAgent import DeliveryAgent
from orderStatus import OrderStatus
from idGenService import IDGenService

class Order:
    def __init__(self, user: User, restaurant: Restaurant, orderItems: List[OrderItem]):
        self.id = IDGenService.generate()
        self.user = user
        self.restaurant = restaurant
        self.orderItems = orderItems
        self.status = OrderStatus.PLACED
        self.deliveryCharges: float = 0.0
        self.deliveryAgent: DeliveryAgent = None

    def getOrderSubtotal(self):
        return sum((orderItem.menuItem.price * orderItem.quantity) for orderItem in self.orderItems)
