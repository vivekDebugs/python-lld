from driverFindingStrategy import DriverFindingStrategy
from driverStatus import DriverStatus


class NearestDriverFindingStrategy(DriverFindingStrategy):
    def findDrivers(self, ride, drivers):
        # ideal approach (not implemented) -> filter the avialble drivers, and sort them based on distance

        # dummy approach -> not sorting
        return [driver for driver in drivers.values() if driver.status == DriverStatus.AVAILABLE and driver.vehicle.vehicleType == ride.vehicleType]
