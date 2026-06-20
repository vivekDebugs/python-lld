from notifiable import Notifiable
from idGenService import IDGenService

class User(Notifiable):
    def __init__(self, name: str, phone: str):
        super().__init__()
        self.id = IDGenService.generate()
        self.name = name
        self.phone = phone

if __name__ == "__main__":
    user = User("John", "290873")
    user.notify(";lkjlkjsdflkj")