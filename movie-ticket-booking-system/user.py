from idGenService import IdGenService

class User:
    def __init__(self, name: str, email: str):
        self.id = IdGenService.generate()
        self.name = name
        self.email = email