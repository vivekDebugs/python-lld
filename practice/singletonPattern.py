class Database:

    # static variable
    instance = None

    @staticmethod
    def getInstance():
        if Database.instance is None:
            Database()
        return Database.instance

    def __init__(self):
        if Database.instance is not None:
            raise Exception("Cannot have multiple instances of Database")
        Database.instance = self

if __name__ == "__main__":
    db = Database.getInstance()
    db2 = Database.getInstance()

    db.val = 29876346
    print(db2.val)