from typing import TYPE_CHECKING
from idGenService import IDGenService

if TYPE_CHECKING:
    from vehicleType import VehicleType


class Vehicle:
    def __init__(self, licencePlate: str, vehicleType: 'VehicleType'):
        self.id = IDGenService.generate()
        self.licencePlate = licencePlate
        self.vehicleType = vehicleType
