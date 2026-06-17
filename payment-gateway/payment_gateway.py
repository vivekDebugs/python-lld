from typing import Dict, List, Set, Optional
from payment_mode import PaymentMode, PaymentInstrument
from bank import Bank, PaymentResult
from client import Client
from payment_router import PaymentRouter


class PaymentGateway:
    """Main Payment Gateway class that orchestrates payment processing"""
    
    def __init__(self, gateway_name: str):
        self.gateway_name = gateway_name
        self.clients: Dict[str, Client] = {}
        self.banks: Dict[str, Bank] = {}
        self.router = PaymentRouter()
        self.supported_payment_modes: Set[PaymentMode] = set()
    
    # Client Management Methods
    def add_client(self, client_id: str, client_name: str, 
                   supported_payment_modes: Set[PaymentMode] = None) -> bool:
        """Add a new client to the payment gateway"""
        if client_id in self.clients:
            print(f"Client {client_id} already exists")
            return False
        
        client = Client(client_id, client_name, supported_payment_modes)
        self.clients[client_id] = client
        print(f"Client {client_name} added successfully with ID: {client_id}")
        return True
    
    def remove_client(self, client_id: str) -> bool:
        """Remove a client from the payment gateway"""
        if client_id not in self.clients:
            print(f"Client {client_id} not found")
            return False
        
        removed_client = self.clients.pop(client_id)
        print(f"Client {removed_client.name} removed successfully")
        return True
    
    def has_client(self, client_id: str) -> bool:
        """Check if a client exists in the payment gateway"""
        return client_id in self.clients and self.clients[client_id].is_active
    
    # Bank Management Methods
    def add_bank(self, bank: Bank) -> bool:
        """Add a bank to the payment gateway"""
        if bank.name in self.banks:
            print(f"Bank {bank.name} already exists")
            return False
        
        self.banks[bank.name] = bank
        print(f"Bank {bank.name} added successfully")
        return True
    
    def remove_bank(self, bank_name: str) -> bool:
        """Remove a bank from the payment gateway"""
        if bank_name not in self.banks:
            print(f"Bank {bank_name} not found")
            return False
        
        # Remove all routing rules for this bank
        for payment_mode in list(self.router.routing_rules.keys()):
            self.router.remove_routing_rule(payment_mode, bank_name)
        
        removed_bank = self.banks.pop(bank_name)
        print(f"Bank {bank_name} removed successfully")
        return True
    
    # Payment Mode Management Methods
    def list_supported_paymodes(self, client_id: str = None) -> List[PaymentMode]:
        """List supported payment modes for PG or specific client"""
        if client_id:
            if client_id not in self.clients:
                print(f"Client {client_id} not found")
                return []
            return list(self.clients[client_id].get_supported_payment_modes())
        else:
            return list(self.supported_payment_modes)
    
    def add_support_for_paymode(self, payment_mode: PaymentMode, client_id: str = None) -> bool:
        """Add payment mode support to PG or specific client"""
        if client_id:
            if client_id not in self.clients:
                print(f"Client {client_id} not found")
                return False
            self.clients[client_id].add_payment_mode_support(payment_mode)
            print(f"Payment mode {payment_mode.value} added for client {client_id}")
        else:
            self.supported_payment_modes.add(payment_mode)
            print(f"Payment mode {payment_mode.value} added to payment gateway")
        return True
    
    def remove_paymode(self, payment_mode: PaymentMode, client_id: str = None) -> bool:
        """Remove payment mode support from PG or specific client"""
        if client_id:
            if client_id not in self.clients:
                print(f"Client {client_id} not found")
                return False
            self.clients[client_id].remove_payment_mode_support(payment_mode)
            print(f"Payment mode {payment_mode.value} removed for client {client_id}")
        else:
            if payment_mode in self.supported_payment_modes:
                self.supported_payment_modes.remove(payment_mode)
                print(f"Payment mode {payment_mode.value} removed from payment gateway")
        return True
    
    # Routing Management Methods
    def add_routing_rule(self, payment_mode: PaymentMode, bank_name: str, percentage: float = 100.0):
        """Add routing rule for payment mode to specific bank"""
        if bank_name not in self.banks:
            print(f"Bank {bank_name} not found")
            return False
        
        bank = self.banks[bank_name]
        if not bank.supports_payment_mode(payment_mode):
            print(f"Bank {bank_name} doesn't support {payment_mode.value}")
            return False
        
        try:
            self.router.add_routing_rule(payment_mode, bank, percentage)
            print(f"Routing rule added: {payment_mode.value} -> {bank_name} ({percentage}%)")
            return True
        except ValueError as e:
            print(f"Error adding routing rule: {e}")
            return False
    
    def show_distribution(self) -> Dict:
        """Show current routing distribution"""
        distribution = self.router.get_routing_distribution()
        print("Current Routing Distribution:")
        for payment_mode, banks in distribution.items():
            print(f"  {payment_mode}:")
            for bank_name, percentage in banks.items():
                print(f"    {bank_name}: {percentage}%")
        return distribution
    
    def update_routing_percentage(self, payment_mode: PaymentMode, bank_name: str, percentage: float):
        """Update routing percentage for specific bank and payment mode"""
        try:
            self.router.update_bank_percentage(payment_mode, bank_name, percentage)
            print(f"Updated routing: {payment_mode.value} -> {bank_name} ({percentage}%)")
            return True
        except ValueError as e:
            print(f"Error updating routing: {e}")
            return False
    
    # Payment Processing Methods
    def make_payment(self, client_id: str, payment_instrument: PaymentInstrument, 
                    amount: float) -> PaymentResult:
        """Process a payment request"""
        
        # Validate client
        if not self.has_client(client_id):
            return PaymentResult(success=False, error_message="Invalid or inactive client")
        
        client = self.clients[client_id]
        
        # Validate client supports this payment mode
        if not client.supports_payment_mode(payment_instrument.payment_mode):
            return PaymentResult(success=False, 
                               error_message=f"Client doesn't support {payment_instrument.payment_mode.value}")
        
        # Validate payment gateway supports this payment mode
        if payment_instrument.payment_mode not in self.supported_payment_modes:
            return PaymentResult(success=False, 
                               error_message=f"Payment gateway doesn't support {payment_instrument.payment_mode.value}")
        
        # Validate payment instrument
        if not payment_instrument.validate():
            return PaymentResult(success=False, error_message="Invalid payment instrument details")
        
        # Get bank from router
        bank = self.router.get_bank_for_payment(payment_instrument.payment_mode)
        if not bank:
            return PaymentResult(success=False, 
                               error_message=f"No bank available for {payment_instrument.payment_mode.value}")
        
        # Process payment through selected bank
        payment_details = payment_instrument.get_payment_details()
        result = bank.process_payment(amount, payment_details)
        
        # Record result for dynamic routing
        self.router.record_payment_result(bank.name, result.success)
        
        return result
    
    # Utility Methods
    def enable_dynamic_routing(self):
        """Enable dynamic routing based on bank success rates"""
        self.router.enable_dynamic_routing()
        print("Dynamic routing enabled")
    
    def disable_dynamic_routing(self):
        """Disable dynamic routing"""
        self.router.disable_dynamic_routing()
        print("Dynamic routing disabled")
    
    def get_gateway_stats(self) -> Dict:
        """Get payment gateway statistics"""
        return {
            "gateway_name": self.gateway_name,
            "total_clients": len(self.clients),
            "active_clients": len([c for c in self.clients.values() if c.is_active]),
            "total_banks": len(self.banks),
            "supported_payment_modes": [mode.value for mode in self.supported_payment_modes],
            "routing_rules_count": sum(len(rules) for rules in self.router.routing_rules.values()),
            "dynamic_routing_enabled": self.router.dynamic_routing_enabled
        }
    
    def print_gateway_info(self):
        """Print comprehensive gateway information"""
        print(f"\n=== Payment Gateway: {self.gateway_name} ===")
        
        print("\nClients:")
        for client in self.clients.values():
            status = "Active" if client.is_active else "Inactive"
            print(f"  - {client.name} ({client.client_id}) - {status}")
            payment_modes = [mode.value for mode in client.supported_payment_modes]
            print(f"    Supported modes: {', '.join(payment_modes)}")
        
        print("\nBanks:")
        for bank in self.banks.values():
            print(f"  - {bank.name}")
            supported_modes = [mode.value for mode in bank.supported_payment_modes]
            print(f"    Supported modes: {', '.join(supported_modes)}")
        
        print(f"\nGateway Supported Payment Modes: {[mode.value for mode in self.supported_payment_modes]}")
        
        print("\nRouting Distribution:")
        self.show_distribution()