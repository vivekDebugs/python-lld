from enum import Enum

class CarAvailabilityStatus(Enum):
    AVAILABLE = "AVAILABLE" # available for rent
    UNAVAILABLE = "UNAVAILABLE" # currently rented
    RESERVED = "RESERVED" # rented for a future date