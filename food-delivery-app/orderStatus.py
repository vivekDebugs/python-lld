from enum import Enum

class OrderStatus(Enum):
    PLACED = "PLACED"
    ON_THE_WAY = "ON_THE_WAY"
    DELIVERED = "DELIVERED"
