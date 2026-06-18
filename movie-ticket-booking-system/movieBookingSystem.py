from cinema import Cinema
from hall import Hall
from city import City
from seatType import SeatType
from typing import List, Dict, Optional
from bookingService import BookingService, SeatLockFailedException, SeatNotLockedException
from userService import UserService
from cinemaService import CinemaService
from movieService import MovieService
from showService import ShowService
from showSeat import ShowSeat
from show import Show
from user import User
from ticket import Ticket
from movie import Movie
from seat import Seat
from datetime import datetime

class MovieBookingSystem:
    def __init__(self):
        self.seatPrices: Dict[SeatType, float] = None

        # inits
        self.initSeatPrices()

        # services
        self.bookingService = BookingService()
        self.userService = UserService()
        self.cinemaService = CinemaService()
        self.movieService = MovieService()
        self.showService = ShowService()

        # datastore
        self.cities: Dict[str, City] = {}
        self.movies: Dict[str, Movie] = {}
        self.cinemas: Dict[str, Cinema] = {}
        self.halls: Dict[str, Hall] = {}
        self.users: Dict[str, User] = {}
        self.shows: Dict[str, Show] = {}

    def initSeatPrices(self):
        self.seatPrices = {
            SeatType.SILVER : 10,
            SeatType.GOLD : 15,
            SeatType.DIAMOND : 25,
            SeatType.PLATINUM : 40,
        }

    def createCity(self, code: str, name: str) -> City:
        city = City(code, name)
        self.cities[code] = city
        return city

    def createMovie(self, name: str, duration: int) -> Movie:
        movie = self.movieService.createMovie(name, duration)
        self.movies[name] = movie
        return movie

    def createCinema(self, name: str, cityCode: str) -> Cinema:
        city = self.cities[cityCode]
        cinema = self.cinemaService.createCinema(name, city)
        self.cinemas[cinema.id] = cinema
        return cinema

    def createHall(self, hallNumber: str, cinemaId: str) -> Hall:
        cinema = self.cinemas[cinemaId]
        hall = self.cinemaService.createHall(hallNumber, cinema)
        self.halls[hall.id] = hall
        return hall

    def createSeat(self, seatNumber: str, seatType: SeatType, hallId: str) -> Seat:
        hall = self.halls[hallId]
        seat = Seat(seatNumber, seatType)
        hall.addSeat(seat)

    def createUser(self, name: str, email: str) -> User:
        user = self.userService.createUser(name, email)
        self.users[user.id] = user
        return user

    def createShow(self, movieName: str, hallId: str, startTime: datetime) -> Show:
        movie = self.movies[movieName]
        hall = self.halls[hallId]
        show = self.showService.createShow(movie, hall, startTime)
        self.shows[show.id] = show
        show.initShowSeats(self.seatPrices)
        return show

    def processBooking(self, showId: str, showSeatNumbers: List[str], userId: str) -> Optional[Ticket]:
        show = self.shows[showId]
        user = self.users[userId]
        showSeats = self.showService.getShowSeats(show, showSeatNumbers)
        try:
            self.bookingService.lockShowSeats(showSeats)
            return self.bookingService.confirmBooking(show, showSeats, user)
        except SeatLockFailedException as e:
            print("Failed to lock seats. Try another seat.")
        except SeatNotLockedException as e:
            print("Seat is not locked. Lock the seat and try again.")