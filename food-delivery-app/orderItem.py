from menuItem import MenuItem
from idGenService import IDGenService

class OrderItem:
    def __init__(self, menuItem: MenuItem, quantity: int):
        self.id = IDGenService.generate()
        self.menuItem = menuItem
        self.quantity = quantity
