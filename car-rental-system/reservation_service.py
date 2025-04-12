from typing import Dict
from reservation import Reservation
from datetime import datetime
from uuid import uuid4
from car_service import CarService
from car_availability_status import CarAvailabilityStatus
from customer_service import CustomerService

class ReservationService:
    def __init__(self):
        self.reservations: Dict[str, Reservation] = {}
        self.car_service = CarService()
        self.customer_service = CustomerService()

    def get_reversations(self, car_id: str):
        result = []
        for reservation in self.reservations.values():
            if reservation.car.id == car_id:
                result.append(reservation)
        return result

    def reserve_car(self, car_id: str, customer_id: str, start_date: datetime, end_date: datetime):
        # check if car is available
        car = self.car_service.get_car(car_id)
        available_cars = self.car_service.search_cars(start_date, end_date, [car.car_type])
        if car.id not in [c.id for c in available_cars]:
            raise Exception("Car is not available for the selected dates")

        # check if customer exists
        customer = self.customer_service.get_customer(customer_id)

        # reserve the car
        car.availability_status = CarAvailabilityStatus.RESERVED
        reservation = Reservation(
            id=self.__generate_reservation_id(),
            car=car,
            customer=customer,
            start_date=start_date,
            end_date=end_date
        )

        self.reservations[reservation.id] = reservation
        return reservation

    def cancel_reservation(self, reservation_id: str):
        # check if reservation exists
        if reservation_id not in self.reservations:
            raise Exception("Reservation not found")

        # cancel the reservation
        reservation = self.reservations.pop(reservation_id)
        car = reservation.car

        # update car availability status
        self.car_service.update_car_availability(car.id)

        return reservation

    def __generate_reservation_id(self):
        return "RS-" + str(uuid4())