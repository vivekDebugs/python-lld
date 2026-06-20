from enum import Enum


class RideStatus(Enum):
    CREATED = "CREATED"
    REQUESTED = "REQUESTED"
    ACCEPTED = "ACCEPTED"
    PICKED_UP = "PICKED_UP"
    COMPLETED = "COMPLETED"
