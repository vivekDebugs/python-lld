from typing import Dict
from customer import Customer
from uuid import uuid4

class CustomerService:
    def __init__(self):
        self.customers: Dict[str, Customer] = {}

    def add_customer(self, name: str, email: str, phone: str, license_number: str):
        customer = Customer(
            id=self.__generate_customer_id(),
            name=name,
            email=email,
            phone=phone,
            license_number=license_number
        )
        self.customers[customer.id] = customer
        return customer
    
    def remove_customer(self, customer_id: str):
        if customer_id in self.customers:
            return self.customers.pop(customer_id)
        else:
            raise ValueError(f"Customer with ID {customer_id} not found.")

    def get_customer(self, customer_id: str):
        if customer_id in self.customers:
            return self.customers[customer_id]
        else:
            raise ValueError(f"Customer with ID {customer_id} not found.")

    def __generate_customer_id(self):
        return "CS-" + str(uuid4())