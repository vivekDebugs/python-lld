from car_rental_system import CarRentalSystem
from car_availability_status import CarAvailabilityStatus
from car_type import CarType
from datetime import datetime

class Demo:
    def __init__(self):
        self.car_rental_system = None

    def run(self):
        # initialize the car rental system
        self.car_rental_system = CarRentalSystem()

        # add cars
        car1 = self.car_rental_system.add_car(
            make="Toyota",
            model="Camry",
            year=2020,
            car_type=CarType.SEDAN,
            license_plate="ABC123",
            availability_status=CarAvailabilityStatus.AVAILABLE,
            price_per_day=50.0
        )
        car2 = self.car_rental_system.add_car(
            make="Honda",
            model="Civic",
            year=2021,
            car_type=CarType.SEDAN,
            license_plate="XYZ789",
            availability_status=CarAvailabilityStatus.AVAILABLE,
            price_per_day=60.0
        )
        car3 = self.car_rental_system.add_car(
            make="Ford",
            model="Explorer",
            year=2022,
            car_type=CarType.SUV,
            license_plate="SUV456",
            availability_status=CarAvailabilityStatus.AVAILABLE,
            price_per_day=80.0
        )
        car4 = self.car_rental_system.add_car(
            make="Hyundai",
            model="i20",
            year=2019,
            car_type=CarType.HATCHBACK,
            license_plate="HATCH123",
            availability_status=CarAvailabilityStatus.AVAILABLE,
            price_per_day=40.0
        )

        # add customers
        customer1 = self.car_rental_system.add_customer(
            name="John Doe",
            email="john.doe@gmail.com",
            phone="1234567890",
            license_number="D1234567"
        )
        customer2 = self.car_rental_system.add_customer(
            name="Jane Smith",
            email="jane.smith@gmail.com",
            phone="0987654321",
            license_number="S1234567"
        )

        # search for available cars
        available_cars = self.car_rental_system.search_cars(
            start_date=self.__create_datetime("2023-10-01"),
            end_date=self.__create_datetime("2023-10-10"),
            car_types=[CarType.SEDAN, CarType.SUV, CarType.HATCHBACK]
        )
        print(available_cars)

        # reserve a car
        car = available_cars[0]
        reservation = self.car_rental_system.reserve_car(
            car_id=car.id,
            customer_id=customer1.id,
            start_date=self.__create_datetime("2023-10-01"),
            end_date=self.__create_datetime("2023-10-10")
        )
        print(reservation)

    def __create_datetime(self, date_str: str):
        return datetime.strptime(date_str, "%Y-%m-%d")

if __name__ == "__main__":
    Demo().run()