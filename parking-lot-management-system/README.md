# Design Parking Lot Management System

## Requirements
What will be 10 requirements of the system, according to you?
Do not worry about the correctness of the requirements, just write down whatever comes to your mind.
Your job is not to generate the requirements, but get better at understanding problem statements and anticipating the functionalities your application might need.

Build an online parking lot management system that can support the following requirements:
* Should have multiple floors.
* Multiple entries and exit points.
* A person has to collect a ticket at entry and pay at or before exit.
* Pay at:
    * Exit counter (Cash to the parking attendant)
    * Dedicated automated booth on each floor
    * Online
* Pay via:
    * Cash
    * Credit Card
    * UPI
* Allow entry for a vehicle if a slot is available for it. Show on the display at entry if a slot is not available.
* Parking Spots of 3 types:
    * Large
    * Medium
    * Small
* A car can only be parked at its slot. Not on any other (even larger).
* A display on each floor with the status of that floor.
* Fees calculated based on per hour price: e.g. 50 rs for the first hour, then 80 rs per extra hour.
  * Small - 50, 80
  * Medium - 80, 100
  * Large - 100, 120

## Design
### Entities
- ParkingLot
- ParkingLotFloor
- ParkingSlot
- Gate
    - EntryGate
    - ExitGate
- Vehicle
- Ticket
- Payment

**VehicleType**
- SUV
- HATCHBACK
- SEDAN
- BIKE
- TRUCK

**Vehicle**
- ownerName: String
- vehicleType: VehicleType

**ParkingSlotType(Enum)**
- SMALL
- MEDIUM
- LARGE

**ParkingSlot**
- id: String
- slotType: ParkingSlotType
- vehicle: Vehicle

**ParkingLotFloor**
- id: String
- slots: List[ParkingSlot]

**GateType**
- ENTRY
- EXIT

**Gate**
- id: String
- gateType: GateType

**EntryGate**
- enter(): Ticket

**ExitGate**
- exit(): Ticket

**ParkingLot**
- id: String
- floors: List[ParkingLotFoor]
- entryGates: List[EntryGate]
- exitGates: List[ExitGate]
- slotAllotmentConfig: Dict // map between vehicle type and slot type
- slotAllotmentStrategies: List[SlotAllotmentStrategy]
- enterVehicle(): Ticket
- exitVehicle(): Ticket

**PaymentGateway(Enum)**
- PAYU_MONEY
- RAZORPAY
- PAYTM

**Payment**
- paymentLink: String
- paymentRef: String
- paymentTime: DateTime
- paymentGateway: PaymentGateway

**Ticket**
- vehicle: Vehicle
- entryTime: DateTime
- entryGate: entryGate
- parkingSlot: ParkingSlot
- exitTime: DateTime
- exitGate: exitGate
- price: Float
- payment: Payment

**SlotAllotmentStrategy**
- alloteSlot(): ParkingSlot

**SerialisedSlotAllotmentStrategy(SlotAllotmentStrategy)**

**RandomSlotAllotmentStrategy(SlotAllotmentStrategy)**

**OptimisedSlotAllotmentStrategy(SlotAllotmentStrategy)**
