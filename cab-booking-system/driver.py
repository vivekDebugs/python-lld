from typing import TYPE_CHECKING
from vehicle import Vehicle
from location import Location
from driverStatus import DriverStatus
from idGenService import IDGenService
from random import random
from notifiable import Notifiable

if TYPE_CHECKING:
    from ride import Ride


class Driver(Notifiable):
    def __init__(self, name: str, phone: str, vehicle: Vehicle):
        self.id = IDGenService.generate()
        self.name = name
        self.phone = phone
        self.vehicle = vehicle
        self.location: Location = None
        self.status: DriverStatus = DriverStatus.OFFLINE

    def online(self):
        self.status = DriverStatus.AVAILABLE

    def sendRideRequest(self, ride: 'Ride') -> bool:
        if random() < 0.5:
            return True # ride accepted
        else:
            return False # ride rejected