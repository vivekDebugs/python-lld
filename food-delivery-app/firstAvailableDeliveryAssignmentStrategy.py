from deliveryAgentAssignmentStrategy import DeliveryAgentAssignmentStrategy
from deliveryAgentStatus import DeliveryAgentStatus

class FirstAvailableDeliveryAgentAssignmentStrategy(DeliveryAgentAssignmentStrategy):
    def assignDeliveryAgent(self, order, deliveryAgents):
        for deliveryAgent in deliveryAgents.values():
            if deliveryAgent.status == DeliveryAgentStatus.AVAILABLE:
                return deliveryAgent