from typing import Dict, Optional
from rider import Rider
from driver import Driver
from vehicle import Vehicle
from vehicleType import VehicleType
from ride import Ride
from location import Location
from rideService import RideService
from nearestDriverFindingStrategy import NearestDriverFindingStrategy
from fixedRateFareCalculationStrategy import FixedRateFareCalculationStrategy

class CabBookingSystem:
    def __init__(self):
        self.rideService = RideService(
            driverFindingStrategy=NearestDriverFindingStrategy(),
            fareCalculationStrategy=FixedRateFareCalculationStrategy(),
        )

        # datastore
        self.riders: Dict[str, Rider] = {}
        self.drivers: Dict[str, Driver] = {}
        self.rides: Dict[str, Ride] = {}
        self.vehicles: Dict[str, Vehicle] = {}

    def createRider(self, name: str, phone: str) -> Rider:
        rider = Rider(name, phone)
        self.riders[rider.id] = rider
        return rider

    def createVehicle(self, licencePlate: str, vehicleType: VehicleType) -> Vehicle:
        vehicle = Vehicle(licencePlate, vehicleType)
        self.vehicles[vehicle.id] = vehicle
        return vehicle

    def createDriver(self, name: str, phone: str, vehicleId: str) -> Driver:
        vehicle = self.vehicles[vehicleId]
        driver = Driver(name, phone, vehicle)
        self.drivers[driver.id] = driver
        return driver

    def createLocation(self, lat: int, long: int) -> Location:
        return Location(lat, long)

    def getFareEstimate(self, riderId: str, fromLocation: Location, toLocation: Location, vehicleType: VehicleType) -> Ride:
        rider = self.riders[riderId]
        ride = self.rideService.createRide(rider, fromLocation, toLocation, vehicleType)
        self.rides[ride.id] = ride
        return ride

    def requestRide(self, rideId: str) -> Optional[Driver]:
        ride = self.rides[rideId]
        return self.rideService.requestRide(ride, self.drivers)

    def pickupRider(self, rideId: str) -> None:
        ride = self.rides[rideId]
        self.rideService.pickupRider(ride)

    def completeRide(self, rideId: str) -> None:
        ride = self.rides[rideId]
        self.rideService.completeRide(ride)
