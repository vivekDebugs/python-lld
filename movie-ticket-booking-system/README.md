# Design Movie Ticket Booking System

## Requirements

Build an online movie ticket booking system that can support the following requirements:

* Support for multiple cities
* Each city will have multiple cinemas
* Each cinema can have multiple halls
* Each hall will play one movie at a time
* A cinema will play multiple movies
* Each hall can have multiple types of seats
  * GOLD
  * DIAMOND
  * PLATINUM
* Allow the user to search a movie by name
* Allow the user to filter movies by the following fields
  * Location
  * Cinema
  * Language
  * Rating
  * Category
* Each movie can have multiple slots
* Users can book tickets and pay via multiple payment methods
  * UPI
  * Credit Card
  * Netbanking
* A user can apply a coupon or a promo code at checkout
* A user can see the availability of seats in a hall
* The price of a ticket will be decided by multiple parameters
  * Seat Type
  * Day of the week
  * Time of the Day
  * Movie
  * Cinema hall
* A user can also cancel or update a booking
* A user cannot book or cancel after the cutoff time which is 1 hour before the movie starts

## Design
### Entities
- City
- Cinema
- Hall
- Seat
- Movie
- Show
- ShowSeat

**City**
- name: String
- cinemas: List[Cinema]

**Cinema**
- name: String
- address: String
- city: City
- halls: List[Hall]
- shows: List[Show]

**SeatType(Enum)**
- SILVER
- GOLD
- DIAMOND
- PLATINUM

**Seat**
- name: String
- seatType: SeatType

**Hall**
- name: String
- seats: List[Seat]
- shows: List[Show]
- cinema: Cinema

**Actor**
- name: String
- movies: List[Movie]

**Movie**
- name: String
- cast: List[Actor]
- duration: Integer
- rating: Float
- shows: List[Show]
- addShow(): None

**ShowSeatStatus**
- AVAILABLE
- LOCKED
- BOOKED

**ShowSeat**
- seat: Seat
- show: Show
- status: ShowSeatStatus

**Show**
- movie: Movie
- time: DateTime
- showSeats: List[ShowSeat]
- hall: Hall
- addShowSeat(): None

**User**
- name
- email

**Ticket**
- show: Show
- showSeats: List[ShowSeat]
- totalPrice: Float
- purchaseTime: DateTime
- user: User

**BookingService**
- lockShowSeats(): None
- confirmBooking(): None
