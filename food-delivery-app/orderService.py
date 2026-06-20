from typing import List
from orderStatus import OrderStatus
from order import Order
from menuItem import MenuItem
from orderItem import OrderItem
from restaurant import Restaurant
from user import User
from deliveryAgent import DeliveryAgent

class OrderService:
    def placeOrder(self, user: User, restaurant: Restaurant, orderItems: List[OrderItem]) -> Order:
        order = Order(user, restaurant, orderItems)
        restaurant.notify(f"You have a new order [{order.id}]")
        user.notify(f"Your order [{order.id}] is placed successfully!")
        return order

    def updateDeliveryCharges(self, order: Order, deliveryCharges: float):
        order.deliveryCharges = deliveryCharges

    def updateDeliveryAgent(self, order: Order, deliveryAgent: DeliveryAgent):
        order.deliveryAgent = deliveryAgent
        deliveryAgent.notify(f"You have a new order [{order.id}] to deliver")

    def pickOrder(self, order: Order) -> None:
        order.status = OrderStatus.ON_THE_WAY
        order.user.notify(f"Your order [{order.id}] is picked up, and is on the way!!")

    def deliverOrder(self, order: Order) -> None:
        order.status = OrderStatus.DELIVERED
        order.restaurant.notify(f"Order [{order.id}] is delivered.")

    def createOrderItem(self, menuItem: MenuItem, quantity: int):
        return OrderItem(menuItem, quantity)