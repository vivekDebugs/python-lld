# Design Cab Booking System

## Requirements:
- Support multiple types of cabs (Mini, Sedan, XL)
- Riders can search for nearby cabs and book a trip
- Drivers can accept or reject ride requests
- Calculate fare based on distance, time, and cab type
- Real-time tracking of the trip
- Support for multiple payment methods
- Rating and review system for both riders and drivers

## Design
### Journey
- Rider creates a ride and gets the fare estimate
- Rider requests the ride
- The ride request is send to the driver
- Driver accepts/rejects the ride request
- Driver picks up the rider
- Dirver completes the ride

### Entities
- Location
- Vehicle
- Driver
- Rider
- Ride

**Location**
- lat: int
- long: int

**VehicleType(Enum)**
- MINI
- SEDAN
- XL

**Vehicle**
- licencePlate: str
- vehicleType: VehicleType

**DriverStatus**
- AVAILABLE
- BOOKED
- OFFLINE

**Driver**
- name: str
- phone: str
- vehicle: Vehicle
- location: Location
- status: DriverStatus

**Rider**
- name: str
- phone: str

**RiderStatus(Enum)**
- REQUESTED
- ACCEPTED
- PICKED_UP
- COMPLETED

**Ride**
- rider: Rider
- fromLocation: Location
- toLocation: Location
- vehicleType: VehicleType
- fare: float
- status: RiderStatus
- driver: Driver

**DriverAssignmentStrategy(ABC)**
- assignDriver(): Any

**FirstAvailableDriverAssignmentStrategy(DriverAssignmentStrategy)**

**NearestDriverAssignmentStrategy(DriverAssignmentStrategy)**

**FareCalculationStrategy(ABC)**
- calculateFare(): float

**DistanceBasedFareCalculationStrategy(FareCalculationStrategy)**

**FixedRateFareCalculationStrategy(FareCalculationStrategy)**

**RideService**
- driverAssignmentStrategy: DriverAssignmentStrategy
- fareCalculationStrategy: FareCalculationStrategy
- createRide(): Ride
- requestRide(): None
- pickupRider(): None
- completeRide(): None

**CabBookingSystem**
- riders: Dict[str, Rider]
- drivers: Dict[str, Driver]
- rides: Dict[str, Ride]
- vehicles: Dict[str, Vehicle]
- rideService: RideService
- createRider(): Rider
- createVehicle(): Vehicle
- createDriver(): Driver
- getFareEstimate(): Ride
- requestRider(): None
- pickupRider(): None
- completeRide(): None
