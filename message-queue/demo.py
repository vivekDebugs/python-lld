from messageQueueSystem import MessageQueueSystem

class Demo:
    def run(self):
        self.system = MessageQueueSystem()

        # creating queue and topics
        omsQueue = self.system.createQueue("oms")
        ordersTopic = self.system.createTopic(omsQueue.name, "orders")
        productsTopic = self.system.createTopic(omsQueue.name, "products")

        # creating and adding order subscibers
        ordersSubscriber1 = self.system.createSubscriber("orders-subscriber-1")
        ordersSubscriber2 = self.system.createSubscriber("orders-subscriber-2")
        self.system.addSubscriber(omsQueue.name, ordersTopic.name, ordersSubscriber1.name)
        self.system.addSubscriber(omsQueue.name, ordersTopic.name, ordersSubscriber2.name)

        # creating and adding product subscibers
        productsSubscriber1 = self.system.createSubscriber("products-subscriber-1")
        self.system.addSubscriber(omsQueue.name, productsTopic.name, productsSubscriber1.name)

        # publishing messages to orders topic
        self.system.publishMessage(omsQueue.name, ordersTopic.name, "order-123 created")
        self.system.publishMessage(omsQueue.name, ordersTopic.name, "order-345 created")
        self.system.publishMessage(omsQueue.name, ordersTopic.name, "order-123 updated")

        # publishing messages to products topic
        self.system.publishMessage(omsQueue.name, productsTopic.name, "product-123 created")
        self.system.publishMessage(omsQueue.name, productsTopic.name, "product-123 updated")

if __name__ == "__main__":
    Demo().run()