from typing import TYPE_CHECKING
from idGenService import IDGenService

if TYPE_CHECKING:
    from restaurant import Restaurant

class MenuItem:
    def __init__(self, name: str, price: float, restaurant: 'Restaurant'):
        self.id = IDGenService.generate()
        self.name = name
        self.price = price
        self.restaurant = restaurant
        self.is_available: bool = True
