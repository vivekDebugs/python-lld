from foodDeliverySystem import FoodDeliverySystem
from time import sleep

class Demo:
    def run(self):
        self.system = FoodDeliverySystem()

        # creating users
        user1 = self.system.createUser("John Doe", "+1238712334")
        user2 = self.system.createUser("Gyan Singh", "+1297364836")

        # creating delivery agents
        deliveryAgent1 = self.system.createDeliveryAgent("Rakesh Kumar", "+1239842138")
        deliveryAgent2 = self.system.createDeliveryAgent("Panna Lal", "+1239822761")
        deliveryAgent1.online()
        deliveryAgent2.online()

        # creating restaurants
        restaurant1 = self.system.createRestaurant("Domino's")

        # creating menu items
        menuItem1 = self.system.createMenuItem("Pizza", 300, restaurant1.id)
        menuItem2 = self.system.createMenuItem("Burger", 180, restaurant1.id)
        menuItem3 = self.system.createMenuItem("Taco", 250, restaurant1.id)

        # creating order items
        orderItem1 = self.system.createOrderItem(menuItem1.id, 1)
        orderItem2 = self.system.createOrderItem(menuItem3.id, 2)

        # placing order
        order1 = self.system.placeOrder(user1.id, restaurant1.id, [orderItem1, orderItem2])

        # ops
        sleep(1)
        self.system.pickOrder(order1.id)
        sleep(3)
        self.system.deliverOrder(order1.id)
        self.system.printOrderInvoice(order1.id)

        print("Success")


if __name__ == "__main__":
    Demo().run()