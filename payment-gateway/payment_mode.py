from enum import Enum
from abc import ABC, abstractmethod


class PaymentMode(Enum):
    """Enum for different payment modes supported by the gateway"""
    UPI = "UPI"
    CREDIT_CARD = "CREDIT_CARD"
    DEBIT_CARD = "DEBIT_CARD"
    NET_BANKING = "NET_BANKING"


class PaymentInstrument(ABC):
    """Abstract base class for payment instruments"""
    
    def __init__(self, payment_mode: PaymentMode):
        self.payment_mode = payment_mode
    
    @abstractmethod
    def validate(self) -> bool:
        """Validate the payment instrument details"""
        pass
    
    @abstractmethod
    def get_payment_details(self) -> dict:
        """Get payment details as dictionary"""
        pass


class UPIInstrument(PaymentInstrument):
    """UPI payment instrument"""
    
    def __init__(self, vpa: str):
        super().__init__(PaymentMode.UPI)
        self.vpa = vpa
    
    def validate(self) -> bool:
        """Validate UPI VPA format"""
        return self.vpa and "@" in self.vpa and len(self.vpa.split("@")) == 2
    
    def get_payment_details(self) -> dict:
        return {
            "payment_mode": self.payment_mode.value,
            "vpa": self.vpa
        }


class CardInstrument(PaymentInstrument):
    """Base class for card payments"""
    
    def __init__(self, payment_mode: PaymentMode, card_number: str, expiry_month: int, 
                 expiry_year: int, cvv: str, card_holder_name: str):
        super().__init__(payment_mode)
        self.card_number = card_number
        self.expiry_month = expiry_month
        self.expiry_year = expiry_year
        self.cvv = cvv
        self.card_holder_name = card_holder_name
    
    def validate(self) -> bool:
        """Validate card details"""
        return (self.card_number and len(self.card_number) >= 13 and 
                self.expiry_month and 1 <= self.expiry_month <= 12 and
                self.expiry_year and self.expiry_year >= 2024 and
                self.cvv and len(self.cvv) in [3, 4] and
                self.card_holder_name)
    
    def get_payment_details(self) -> dict:
        return {
            "payment_mode": self.payment_mode.value,
            "card_number": self.card_number[-4:],  # Only last 4 digits for security
            "expiry_month": self.expiry_month,
            "expiry_year": self.expiry_year,
            "card_holder_name": self.card_holder_name
        }


class CreditCardInstrument(CardInstrument):
    """Credit card payment instrument"""
    
    def __init__(self, card_number: str, expiry_month: int, expiry_year: int, 
                 cvv: str, card_holder_name: str):
        super().__init__(PaymentMode.CREDIT_CARD, card_number, expiry_month, 
                        expiry_year, cvv, card_holder_name)


class DebitCardInstrument(CardInstrument):
    """Debit card payment instrument"""
    
    def __init__(self, card_number: str, expiry_month: int, expiry_year: int, 
                 cvv: str, card_holder_name: str):
        super().__init__(PaymentMode.DEBIT_CARD, card_number, expiry_month, 
                        expiry_year, cvv, card_holder_name)


class NetBankingInstrument(PaymentInstrument):
    """Net banking payment instrument"""
    
    def __init__(self, username: str, password: str, bank_code: str):
        super().__init__(PaymentMode.NET_BANKING)
        self.username = username
        self.password = password
        self.bank_code = bank_code
    
    def validate(self) -> bool:
        """Validate net banking credentials"""
        return (self.username and self.password and self.bank_code and
                len(self.username) >= 3 and len(self.password) >= 4)
    
    def get_payment_details(self) -> dict:
        return {
            "payment_mode": self.payment_mode.value,
            "username": self.username,
            "bank_code": self.bank_code
            # Password not included for security
        }