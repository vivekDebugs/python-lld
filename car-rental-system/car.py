from car_type import CarType
from car_availability_status import CarAvailabilityStatus

class Car:
    def __init__(
        self,
        id: str,
        make: str,
        model: str,
        year: int,
        car_type: CarType,
        license_plate: str,
        availability_status: CarAvailabilityStatus,
        price_per_day: float
    ):
        self.id = id
        self.make = make
        self.model = model
        self.year = year
        self.car_type = car_type
        self.license_plate = license_plate
        self.availability_status = availability_status
        self.price_per_day = price_per_day

    def __str__(self):
        return f"Car ID: {self.id}, Make: {self.make}, Model: {self.model}, Year: {self.year}, Type: {self.car_type}, License Plate: {self.license_plate}, Availability Status: {self.availability_status}, Price per Day: {self.price_per_day}"