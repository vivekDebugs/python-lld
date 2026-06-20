from typing import Dict
from menuItem import MenuItem
from notifiable import Notifiable
from idGenService import IDGenService

class Restaurant(Notifiable):
    def __init__(self, name: str, menuItems: Dict[str, MenuItem] = {}):
        super().__init__()
        self.id = IDGenService.generate()
        self.name = name
        self.menuItems = menuItems

    def addMenuItem(self, menuItem: MenuItem):
        self.menuItems[menuItem.id] = menuItem

    def findMenuItem(self, id: str):
        return self.menuItems[id]
