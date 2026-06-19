class Database:

    def __init__(self, host, port, username, password):
        self.host = host
        self.port = port
        self.usenrame = username
        self.password = password

    class Builder:

        def __init__(self):
            self.host = None
            self.port = None
            self.username = None
            self.password = None

        def setHost(self, host):
            self.host = host
            return self

        def setPort(self, port):
            self.port = port
            return self

        def setUsername(self, username):
            self.username = username
            return self

        def setPassword(self, password):
            self.password = password
            return self

        def build(self):
            if None in (self.host, self.port, self.username, self.password):
                raise ValueError("All values needed")
            return Database(
                self.host,
                self.port,
                self.username,
                self.password,
            )

if __name__ == "__main__":
    db = Database.Builder().setHost("prod.db.com").setPort("3452").setUsername("johndoe").setPassword("lkjnliu@43lkjlk").build()
    print(db.host)
