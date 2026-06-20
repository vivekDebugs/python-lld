from restaurant import Restaurant
from menuItem import MenuItem

class RestaurantService:
    def createRestaurant(self, name: str) -> Restaurant:
        return Restaurant(name)
    
    def createMenuItem(self, name: str, price: float, isAvailable: bool, restaurant: Restaurant) -> MenuItem:
        menuItem = MenuItem(name, price, isAvailable)
        restaurant.addMenuItem(menuItem)
        return menuItem

    def findMenuItem(self, id, restaurant: Restaurant) -> MenuItem:
        return restaurant.findMenuItem(id)