from typing import List, TYPE_CHECKING

if TYPE_CHECKING:
    from cinema import Cinema

class City:
    def __init__(self, code: str, name: str):
        self.code = code
        self.name = name
        self.cinemas: List['Cinema'] = []

    def addCinema(self, cinema: 'Cinema'):
        self.cinemas.append(cinema)