from movie import Movie

class MovieService:
    def createMovie(self, name: str, duration: int):
        return Movie(name, duration)