from movieBookingSystem import MovieBookingSystem
from seatType import SeatType
from datetime import datetime, timedelta

class Demo:
    def run(self):
        system = MovieBookingSystem()

        # creating first cinema
        city1 = system.createCity("KOL", "Kolkata")
        cinema1 = system.createCinema("PVR", city1.code)
        hall1 = system.createHall("1", cinema1.id)
        system.createSeat("1", SeatType.GOLD, hall1.id)
        system.createSeat("2", SeatType.DIAMOND, hall1.id)

        # # creating second cinema
        city2 = system.createCity("DUR", "Durgapur")
        cinema2 = system.createCinema("INOX", city2.code)
        hall2 = system.createHall("2", cinema2.id)
        system.createSeat("3", SeatType.GOLD, hall2.id)
        system.createSeat("4", SeatType.DIAMOND, hall2.id)

        # creating movie
        movie1 = system.createMovie("Dhurandar", 200)

        # creating show
        show1 = system.createShow(movie1.name, hall1.id, datetime.now() + timedelta(days=10))

        # creating user
        user1 = system.createUser("John", "johndoe@gmail.com")

        # booking seats
        showSeats = [show1.showSeats[0]]
        ticket = system.processBooking(show1.id, [x.seat.seatNumber for x in showSeats], user1.id)
        ticket.printTicket()
        

        print("Success")

if __name__ == "__main__":
    demo = Demo()
    demo.run()