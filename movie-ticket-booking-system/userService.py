from user import User

class UserService:
    def createUser(self, name: str, email: str):
        return User(name, email)