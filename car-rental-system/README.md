# Desgin Car Rental System

## Requirements
- The car rental system should allow customers to browse and reserve available cars for specific dates.
- Each car should have details such as make, model, year, license plate number, and rental price per day.
- Customers should be able to search for cars based on various criteria, such as car type, price range, and availability.
- The system should handle reservations, including creating, modifying, and canceling reservations.
- The system should keep track of the availability of cars and update their status accordingly.
- The system should handle customer information, including name, contact details, and driver's license information.
- The system should handle payment processing for reservations.
- The system should be able to handle concurrent reservations and ensure data consistency.

## Design
**CarAvailabilityStatus**
- AVAILABLE
- NOT_AVAILABLE

**CarType**
- SUV
- SEDAN
- HATCHBACK

**Car**
- make: String
- mode: String
- year: Integer
- car_type: CarType
- licence_plate: String
- availability_status: CarAvailabilityStatus
- price_per_day: Float

**Customer**
- name: String
- email: String
- phone: String
- license_number: String

**Reservation**
- customer: Customer
- car: Car
- start_date: Date
- end_date: Date
- total_price: Float

**PaymentProcessor**
- process_payment(): Boolean

**ReservationService**
- reservations: Dict[String, Reservation]
- get_reservations(car_id: String): List[Reservation]
- reverse_car(car_id: String, customer_id: String, start_date: DateTime, end_date: DateTime): Reservation
- cancel_reservation(reservation_id: String): Reservation

**CarService**
- cars: Dict[String, Car]
- search_cars(start_date: DateTime, end_date: DateTime, car_types: List[CarType]): List[Car]
- is_car_available(car_id: str): Boolean
- add_car(car: Car): Car
- remove_car(car_id: String): Car

**CarRentalSystem**
- reservation_service: ReservationService
- cars_service: CarsService
- add_car(make: String, model: String, year: Integer, license_plate: String, availability_status: CarAvailabilityStatus, car_type: CarType, price_per_day: Float): Car
- search_cars(start_date: DateTime, end_date: DateTime, car_types: List[CarType]): List[Car]
- reverse_car(car_id: String, customer_id: String, start_date: DateTime, end_date: DateTime): Reservation
- add_customer(name, email, phone, license_number): Customer