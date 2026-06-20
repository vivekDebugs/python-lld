from rider import Rider
from driver import Driver
from location import Location
from vehicleType import VehicleType
from rideStatus import RideStatus
from idGenService import IDGenService


class Ride:
    def __init__(self, rider: Rider, fromLocation: Location, toLocation: Location, vehicleType: VehicleType):
        self.id = IDGenService.generate()
        self.rider = rider
        self.fromLocation = fromLocation
        self.toLocation = toLocation
        self.vehicleType = vehicleType
        self.status: RideStatus = RideStatus.CREATED
        self.fare: float = None
        self.driver: Driver = None
