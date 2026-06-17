import random
from abc import ABC, abstractmethod
from typing import Dict, Any
from payment_mode import PaymentMode


class PaymentResult:
    """Class to represent payment processing result"""
    
    def __init__(self, success: bool, transaction_id: str = None, 
                 error_message: str = None, bank_name: str = None):
        self.success = success
        self.transaction_id = transaction_id
        self.error_message = error_message
        self.bank_name = bank_name
    
    def __str__(self):
        if self.success:
            return f"Payment Success - Transaction ID: {self.transaction_id}, Bank: {self.bank_name}"
        else:
            return f"Payment Failed - Error: {self.error_message}"


class Bank(ABC):
    """Abstract base class for bank implementations"""
    
    def __init__(self, name: str, supported_payment_modes: list):
        self.name = name
        self.supported_payment_modes = supported_payment_modes
        self.success_rate = random.uniform(0.7, 0.95)  # Random success rate between 70-95%
    
    @abstractmethod
    def process_payment(self, amount: float, payment_details: Dict[str, Any]) -> PaymentResult:
        """Process payment and return result"""
        pass
    
    def supports_payment_mode(self, payment_mode: PaymentMode) -> bool:
        """Check if bank supports given payment mode"""
        return payment_mode in self.supported_payment_modes
    
    def _simulate_payment_processing(self, amount: float, payment_mode: str) -> bool:
        """Simulate payment processing with random success/failure"""
        # Add some business logic based on amount or payment mode
        if amount <= 0:
            return False
        
        # Simulate network/processing issues
        return random.random() < self.success_rate


class HDFCBank(Bank):
    """HDFC Bank implementation"""
    
    def __init__(self):
        supported_modes = [PaymentMode.CREDIT_CARD, PaymentMode.DEBIT_CARD, PaymentMode.UPI]
        super().__init__("HDFC", supported_modes)
    
    def process_payment(self, amount: float, payment_details: Dict[str, Any]) -> PaymentResult:
        """Process payment through HDFC Bank"""
        success = self._simulate_payment_processing(amount, payment_details.get("payment_mode"))
        
        if success:
            transaction_id = f"HDFC_{random.randint(100000, 999999)}"
            return PaymentResult(success=True, transaction_id=transaction_id, bank_name=self.name)
        else:
            return PaymentResult(success=False, error_message="HDFC Bank processing failed", 
                               bank_name=self.name)


class ICICIBank(Bank):
    """ICICI Bank implementation"""
    
    def __init__(self):
        supported_modes = [PaymentMode.NET_BANKING, PaymentMode.DEBIT_CARD, PaymentMode.UPI]
        super().__init__("ICICI", supported_modes)
    
    def process_payment(self, amount: float, payment_details: Dict[str, Any]) -> PaymentResult:
        """Process payment through ICICI Bank"""
        success = self._simulate_payment_processing(amount, payment_details.get("payment_mode"))
        
        if success:
            transaction_id = f"ICICI_{random.randint(100000, 999999)}"
            return PaymentResult(success=True, transaction_id=transaction_id, bank_name=self.name)
        else:
            return PaymentResult(success=False, error_message="ICICI Bank processing failed", 
                               bank_name=self.name)


class SBIBank(Bank):
    """SBI Bank implementation"""
    
    def __init__(self):
        supported_modes = [PaymentMode.NET_BANKING, PaymentMode.CREDIT_CARD, 
                          PaymentMode.DEBIT_CARD, PaymentMode.UPI]
        super().__init__("SBI", supported_modes)
    
    def process_payment(self, amount: float, payment_details: Dict[str, Any]) -> PaymentResult:
        """Process payment through SBI Bank"""
        success = self._simulate_payment_processing(amount, payment_details.get("payment_mode"))
        
        if success:
            transaction_id = f"SBI_{random.randint(100000, 999999)}"
            return PaymentResult(success=True, transaction_id=transaction_id, bank_name=self.name)
        else:
            return PaymentResult(success=False, error_message="SBI Bank processing failed", 
                               bank_name=self.name)


class AxisBank(Bank):
    """Axis Bank implementation"""
    
    def __init__(self):
        supported_modes = [PaymentMode.CREDIT_CARD, PaymentMode.UPI, PaymentMode.NET_BANKING]
        super().__init__("AXIS", supported_modes)
    
    def process_payment(self, amount: float, payment_details: Dict[str, Any]) -> PaymentResult:
        """Process payment through Axis Bank"""
        success = self._simulate_payment_processing(amount, payment_details.get("payment_mode"))
        
        if success:
            transaction_id = f"AXIS_{random.randint(100000, 999999)}"
            return PaymentResult(success=True, transaction_id=transaction_id, bank_name=self.name)
        else:
            return PaymentResult(success=False, error_message="Axis Bank processing failed", 
                               bank_name=self.name)