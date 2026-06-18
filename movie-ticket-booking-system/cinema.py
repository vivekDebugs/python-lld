from typing import List, TYPE_CHECKING
from idGenService import IdGenService

if TYPE_CHECKING:
    from hall import Hall
    from city import City

class Cinema:
    def __init__(self, name: str, city: 'City'):
        self.id = IdGenService.generate()
        self.name = name
        self.city = city
        self.halls: List['Hall'] = []

    def addHall(self, hall: 'Hall'):
        self.halls.append(hall)