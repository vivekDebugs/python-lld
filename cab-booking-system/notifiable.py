class Notifiable:
    def __init__(self):
        self.name = "NO NAME"

    def notify(self, message: str):
        print(f"[NOTIFICATION] {self.name} : {message}")