from idGenService import IDGenService
from notifiable import Notifiable

class Rider(Notifiable):
    def __init__(self, name: str, phone: str):
        self.id = IDGenService.generate()
        self.name = name
        self.phone = phone
