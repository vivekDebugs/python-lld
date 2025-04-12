from car_service import CarService
from reservation_service import ReservationService
from customer_service import CustomerService

class CarRentalSystem:
    def __init__(self):
        self.car_service = CarService()
        self.reservation_service = ReservationService()
        self.customer_service = CustomerService()

    def add_car(
        self,
        make: str,
        model: str,
        year: int,
        car_type: str,
        license_plate: str,
        availability_status: str,
        price_per_day: float
    ):
        return self.car_service.add_car(
            make=make,
            model=model,
            year=year,
            car_type=car_type,
            license_plate=license_plate,
            availability_status=availability_status,
            price_per_day=price_per_day
    )

    def add_customer(
        self,
        name: str,
        email: str,
        phone: str,
        license_number: str
    ):
        return self.customer_service.add_customer(
            name=name,
            email=email,
            phone=phone,
            license_number=license_number
    )

    def search_cars(
        self,
        start_date: str,
        end_date: str,
        car_types: list
    ):
        return self.car_service.search_cars(
            start_date=start_date,
            end_date=end_date,
            car_types=car_types
    )

    def reserve_car(
        self,
        car_id: str,
        customer_id: str,
        start_date: str,
        end_date: str
    ):
        return self.reservation_service.reserve_car(
            car_id=car_id,
            customer_id=customer_id,
            start_date=start_date,
            end_date=end_date
    )