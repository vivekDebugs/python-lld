from hall import Hall
from seat import Seat
from cinema import Cinema
from seatType import SeatType
from city import City

class CinemaService:
    def createCinema(self, name: str, city: City) -> Cinema:
        cinema = Cinema(name, city)
        city.addCinema(cinema)
        return cinema

    def createHall(self, hallNumber: str, cinema: Cinema) -> Hall:
        hall = Hall(hallNumber, cinema)
        cinema.addHall(hall)
        return hall

    def createSeat(self, hall: Hall, seatNumber: str, seatType: SeatType) -> Seat:
        seat = Seat(seatNumber, seatType)
        hall.addSeat(seat)
        return seat