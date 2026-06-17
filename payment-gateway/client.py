from typing import Set
from payment_mode import PaymentMode


class Client:
    """Class representing a client of the payment gateway"""
    
    def __init__(self, client_id: str, name: str, supported_payment_modes: Set[PaymentMode] = None):
        self.client_id = client_id
        self.name = name
        if supported_payment_modes is None:
            self.supported_payment_modes = set(PaymentMode)
        else:
            self.supported_payment_modes = supported_payment_modes
        self.is_active = True
    
    def add_payment_mode_support(self, payment_mode: PaymentMode):
        """Add support for a payment mode"""
        self.supported_payment_modes.add(payment_mode)
    
    def remove_payment_mode_support(self, payment_mode: PaymentMode):
        """Remove support for a payment mode"""
        if payment_mode in self.supported_payment_modes:
            self.supported_payment_modes.remove(payment_mode)
    
    def supports_payment_mode(self, payment_mode: PaymentMode) -> bool:
        """Check if client supports given payment mode"""
        return payment_mode in self.supported_payment_modes
    
    def get_supported_payment_modes(self) -> Set[PaymentMode]:
        """Get all supported payment modes"""
        return self.supported_payment_modes.copy()
    
    def deactivate(self):
        """Deactivate the client"""
        self.is_active = False
    
    def activate(self):
        """Activate the client"""
        self.is_active = True
    
    def __str__(self):
        return f"Client(id={self.client_id}, name={self.name}, active={self.is_active})"
    
    def __eq__(self, other):
        if isinstance(other, Client):
            return self.client_id == other.client_id
        return False
    
    def __hash__(self):
        return hash(self.client_id)