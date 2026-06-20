from typing import Dict, List
from orderService import OrderService
from restaurantService import RestaurantService
from user import User
from deliveryAgent import DeliveryAgent
from restaurant import Restaurant
from menuItem import MenuItem
from order import Order
from orderItem import OrderItem
from deliveryAgentAssignmentStrategy import DeliveryAgentAssignmentStrategy
from firstAvailableDeliveryAssignmentStrategy import FirstAvailableDeliveryAgentAssignmentStrategy
from deliveryChargesCalculationStrategy import DeliveryChargesCalculationStrategy
from percentageBasedDeliveryChargesCalculationStrategy import PercentageBasedDeliveryChargesCalculationStrategy

class FoodDeliverySystem:
    def __init__(self):
        self.orderService = OrderService()
        self.restaurantService = RestaurantService()
        self.deliveryAgentAssignmentStrategy: DeliveryAgentAssignmentStrategy = FirstAvailableDeliveryAgentAssignmentStrategy()
        self.deliveryChargesCalculationStrategy: DeliveryChargesCalculationStrategy = PercentageBasedDeliveryChargesCalculationStrategy()

        # datastore
        self.users: Dict[str, User] = {}
        self.deliveryAgents: Dict[str, DeliveryAgent] = {}
        self.restaurants: Dict[str, Restaurant] = {}
        self.menuItems: Dict[str, MenuItem] = {}
        self.orders: Dict[str, Order] = {}

    def createUser(self, name: str, phone: str) -> User:
        user = User(name, phone)
        self.users[user.id] = user
        return user

    def createDeliveryAgent(self, name: str, phone: str) -> DeliveryAgent:
        deliveryAgent = DeliveryAgent(name, phone)
        self.deliveryAgents[deliveryAgent.id] = deliveryAgent
        return deliveryAgent

    def createRestaurant(self, name: str) -> Restaurant:
        restaurant = Restaurant(name)
        self.restaurants[restaurant.id] = restaurant
        return restaurant

    def createMenuItem(self, name: str, price: float, restaurantId: str) -> MenuItem:
        restaurant = self.restaurants[restaurantId]
        menuItem = MenuItem(name, price, restaurant)
        self.menuItems[menuItem.id] = menuItem
        restaurant.addMenuItem(menuItem)
        return menuItem

    def placeOrder(self, userId: str, restaurantId: str, orderItems: List[OrderItem]) -> Order:
        user = self.users[userId]
        restaurant = self.restaurants[restaurantId]

        # creating order
        order = self.orderService.placeOrder(user, restaurant, orderItems)

        # calculating delivery info
        deliveryAgent = self.deliveryAgentAssignmentStrategy.assignDeliveryAgent(order, self.deliveryAgents)
        deliveryCharges = self.deliveryChargesCalculationStrategy.calculateDeliveryCharges(order)

        # updating delivery info
        self.orderService.updateDeliveryAgent(order, deliveryAgent)
        self.orderService.updateDeliveryCharges(order, deliveryCharges)

        # storing order in datastore
        self.orders[order.id] = order

        return order

    def createOrderItem(self, menuItemId: str, quantity: int) -> OrderItem:
        menuItem = self.menuItems[menuItemId]
        return self.orderService.createOrderItem(menuItem, quantity)

    def pickOrder(self, orderId: str) -> None:
        order = self.orders[orderId]
        self.orderService.pickOrder(order)

    def deliverOrder(self, orderId: str) -> None:
        order = self.orders[orderId]
        self.orderService.deliverOrder(order)

    def printOrderInvoice(self, orderId: str) -> None:
        order = self.orders[orderId]
        
        print("\n" + "="*50)
        print("ORDER INVOICE")
        print("="*50)
        print(f"Order ID: {order.id}")
        print(f"Restaurant: {order.restaurant.name}")
        print("-"*50)
        print(f"{'Item':<30} {'Qty':<5} {'Price':<10}")
        print("-"*50)
        
        for orderItem in order.orderItems:
            itemName = orderItem.menuItem.name
            quantity = orderItem.quantity
            price = orderItem.menuItem.price * quantity
            print(f"{itemName:<30} {quantity:<5} Rs.{price:<9.2f}")
        
        print("-"*50)
        print(f"{'Subtotal':<35} Rs.{order.getOrderSubtotal():<9.2f}")
        print(f"{'Delivery Charges':<35} Rs.{order.deliveryCharges:<9.2f}")
        print("="*50)
        print(f"{'TOTAL':<35} Rs.{order.getOrderSubtotal() + order.deliveryCharges:<9.2f}")
        print("="*50 + "\n")
