class Customer:
    def __init__(self, id: str, name: str, email: str, phone: str, license_number: str):
        self.id = id
        self.name = name
        self.email = email
        self.phone = phone
        self.license_number = license_number

    def __str__(self):
        return f"Customer ID: {self.id}, Name: {self.name}, Email: {self.email}, Phone: {self.phone}, License Number: {self.license_number}"