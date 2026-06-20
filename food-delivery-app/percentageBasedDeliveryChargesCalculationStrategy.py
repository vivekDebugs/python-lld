from deliveryChargesCalculationStrategy import DeliveryChargesCalculationStrategy

class PercentageBasedDeliveryChargesCalculationStrategy(DeliveryChargesCalculationStrategy):
    def calculateDeliveryCharges(self, order):
        percentage = 0.10
        orderTotal = order.getOrderSubtotal()
        return orderTotal * percentage