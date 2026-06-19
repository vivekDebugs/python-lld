from uuid import uuid4

class Database:

    # static variable
    instance = None

    @staticmethod
    def getInstance():
        if Database.instance is None:
            Database()
        return Database.instance

    def __init__(self):
        if Database.instance is None:
            self.rand = uuid4()
            Database.instance = self

if __name__ == "__main__":
    db = Database.getInstance()
    db2 = Database.getInstance()
    db3 = Database.getInstance()
    print(db.rand)
    print(db2.rand)
    print(db3.rand)