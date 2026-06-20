from time import sleep
from typing import Dict, Optional
from driverFindingStrategy import DriverFindingStrategy
from fareCalculationStrategy import FareCalculationStrategy
from ride import Ride
from rideStatus import RideStatus
from rider import Rider
from location import Location
from vehicleType import VehicleType
from driverStatus import DriverStatus
from driver import Driver

class RideService:
    def __init__(self, driverFindingStrategy: DriverFindingStrategy, fareCalculationStrategy: FareCalculationStrategy):
        self.driverFindingStrategy = driverFindingStrategy
        self.fareCalculationStrategy = fareCalculationStrategy

    def createRide(self, rider: Rider, fromLocation: Location, toLocation: Location, vehicleType: VehicleType) -> Ride:
        ride = Ride(rider, fromLocation, toLocation, vehicleType)
        ride.fare = self.fareCalculationStrategy.calculateFare(ride)
        rider.notify(f"Your ride will cost Rs.{ride.fare}")
        return ride

    def requestRide(self, ride: Ride, drivers: Dict[str, Driver]) -> Optional[Driver]:
        ride.status = RideStatus.REQUESTED
        ride.rider.notify("Finding drivers near you...")
        availableDrivers = self.driverFindingStrategy.findDrivers(ride, drivers)
        for driver in availableDrivers:
            if driver.status == DriverStatus.AVAILABLE:
                driver.notify(f"{ride.fromLocation.name} -> {ride.toLocation.name} | Rs.{ride.fare} | [ACCEPT] OR [REJECT]")
                sleep(2)
                if driver.sendRideRequest(ride):
                    ride.status = RideStatus.ACCEPTED
                    ride.driver = driver
                    driver.status = DriverStatus.BOOKED
                    driver.notify(f"Please reach {ride.fromLocation.name} ({str(ride.fromLocation.lat)}, {str(ride.toLocation.long)}) for pickup")
                    ride.rider.notify(f"Driver found. {driver.name} is coming to pick you up..")
                    return driver

    def pickupRider(self, ride: Ride):
        ride.status = RideStatus.PICKED_UP

    def completeRide(self, ride: Ride):
        ride.status = RideStatus.COMPLETED
        ride.driver.status = DriverStatus.AVAILABLE
        ride.driver.notify(f"Please collect Rs.{ride.fare} from {ride.rider.name}")
        ride.rider.notify(f"Please pay Rs.{ride.fare} to {ride.driver.name}")
