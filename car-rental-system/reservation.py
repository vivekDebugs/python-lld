from customer import Customer
from car import Car

class Reservation:
    def __init__(
        self,
        id: str,
        customer: Customer,
        car: Car,
        start_date: str,
        end_date: str,
        total_price: float
    ):
        self.id = id
        self.customer = customer
        self.car = car
        self.start_date = start_date
        self.end_date = end_date
        self.total_price = total_price

    def __str__(self):
        return f"Reservation ID: {self.id}, Customer: {self.customer.name}, Car: {self.car.make} {self.car.model} - {self.car.license_plate}, Start Date: {self.start_date}, End Date: {self.end_date}, Total Price: ${self.total_price:.2f}"