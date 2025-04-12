from typing import Dict, List
from car import Car
from car_type import CarType
from uuid import uuid4
from reservation_service import ReservationService
from car_availability_status import CarAvailabilityStatus
from datetime import datetime
from reservation import Reservation

class CarService:
    def __init__(self):
        self.cars: Dict[str, Car] = {}
        self.reservation_service = ReservationService()

    def update_car_availability(self, car_id: str):
        car = self.get_car(car_id)
        car_reservations: List[Reservation] = self.reservation_service.get_reversations(car_id=car.id)
        if not car_reservations:
            car.availability_status = CarAvailabilityStatus.AVAILABLE
        else:
            all_reservations_over = True
            for reservation in car_reservations:
                if reservation.end_date >= datetime.now():
                    all_reservations_over = False
                    break
            if all_reservations_over:
                car.availability_status = CarAvailabilityStatus.AVAILABLE
            else:
                car.availability_status = CarAvailabilityStatus.RESERVED

    def search_cars(self, start_date: datetime, end_date: datetime, car_types: List[CarType]):
        available_cars = []
        for car in self.cars.values():
            if car.car_type in car_types:
                if car.availability_status == CarAvailabilityStatus.AVAILABLE:
                    available_cars.append(car)
                elif car.availability_status == CarAvailabilityStatus.RESERVED:
                    car_reservations = self.reservation_service.get_reversations(car_id=car.id)
                    for reservation in car_reservations:
                        if not self.__is_date_overlapping((reservation.start_date, reservation.end_date), (start_date, end_date)):
                            available_cars.append(car)
        return available_cars
    
    def __is_date_overlapping(self, date_range1: tuple, date_range2: tuple):
        return not(date_range1[1] < date_range2[0] or date_range2[1] < date_range1[0])

    def add_car(self,
        make: str,
        model: str,
        year: int,
        car_type: CarType,
        license_plate: str,
        availability_status: str,
        price_per_day: float
    ):
        car = Car(
            id=self.__generate_car_id(),
            make=make,
            model=model,
            year=year,
            car_type=car_type,
            license_plate=license_plate,
            availability_status=availability_status,
            price_per_day=price_per_day
        )
        self.cars[car.id] = car
        return car

    def remove_car(self, car_id: str):
        if car_id in self.cars:
            return self.cars.pop(car_id)
        else:
            raise ValueError(f"Car with ID {car_id} not found.")

    def get_car(self, car_id: str):
        if car_id in self.cars:
            return self.cars[car_id]
        else:
            raise ValueError(f"Car with ID {car_id} not found.")

    def update_car_availabilities(self):
        for car in self.cars.values():
            self.update_car_availability(car.id)

    def __generate_car_id(self):
        return "CR-" + str(uuid4())
