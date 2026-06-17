import random
from typing import List, Dict, Optional, Tuple
from payment_mode import PaymentMode
from bank import Bank


class RoutingRule:
    """Class to represent routing rules for payment processing"""
    
    def __init__(self, payment_mode: PaymentMode, bank: Bank, percentage: float = 100.0):
        self.payment_mode = payment_mode
        self.bank = bank
        self.percentage = percentage
        self.priority = 0  # Lower number = higher priority
    
    def __str__(self):
        return f"Route({self.payment_mode.value} -> {self.bank.name}: {self.percentage}%)"


class PaymentRouter:
    """Router class to handle payment routing logic"""
    
    def __init__(self):
        # Dictionary mapping payment_mode to list of routing rules
        self.routing_rules: Dict[PaymentMode, List[RoutingRule]] = {}
        # Track bank success rates for dynamic routing
        self.bank_success_history: Dict[str, List[bool]] = {}
        self.dynamic_routing_enabled = False
    
    def add_routing_rule(self, payment_mode: PaymentMode, bank: Bank, percentage: float = 100.0):
        """Add a routing rule for a payment mode"""
        if payment_mode not in self.routing_rules:
            self.routing_rules[payment_mode] = []
        
        # Check if total percentage doesn't exceed 100
        current_total = sum(rule.percentage for rule in self.routing_rules[payment_mode])
        if current_total + percentage > 100:
            raise ValueError(f"Total percentage for {payment_mode.value} would exceed 100%")
        
        rule = RoutingRule(payment_mode, bank, percentage)
        self.routing_rules[payment_mode].append(rule)
    
    def remove_routing_rule(self, payment_mode: PaymentMode, bank_name: str):
        """Remove a routing rule"""
        if payment_mode in self.routing_rules:
            self.routing_rules[payment_mode] = [
                rule for rule in self.routing_rules[payment_mode] 
                if rule.bank.name != bank_name
            ]
    
    def get_bank_for_payment(self, payment_mode: PaymentMode) -> Optional[Bank]:
        """Get bank based on routing rules and percentage distribution"""
        if payment_mode not in self.routing_rules:
            return None
        
        rules = self.routing_rules[payment_mode]
        if not rules:
            return None
        
        # If dynamic routing is enabled, prioritize banks with better success rates
        if self.dynamic_routing_enabled:
            rules = self._sort_rules_by_success_rate(rules)
        
        # Use weighted random selection based on percentage
        return self._select_bank_by_percentage(rules)
    
    def _select_bank_by_percentage(self, rules: List[RoutingRule]) -> Optional[Bank]:
        """Select bank based on percentage distribution"""
        if not rules:
            return None
        
        # Calculate cumulative percentages
        total_percentage = sum(rule.percentage for rule in rules)
        if total_percentage == 0:
            return None
        
        # Generate random number between 0 and total_percentage
        random_value = random.uniform(0, total_percentage)
        
        # Find the bank based on weighted selection
        cumulative = 0
        for rule in rules:
            cumulative += rule.percentage
            if random_value <= cumulative:
                return rule.bank
        
        # Fallback to first bank
        return rules[0].bank
    
    def _sort_rules_by_success_rate(self, rules: List[RoutingRule]) -> List[RoutingRule]:
        """Sort rules by bank success rate (for dynamic routing)"""
        def get_success_rate(rule):
            history = self.bank_success_history.get(rule.bank.name, [])
            if not history:
                return 0.5  # Default neutral rate
            return sum(history) / len(history)
        
        return sorted(rules, key=get_success_rate, reverse=True)
    
    def record_payment_result(self, bank_name: str, success: bool):
        """Record payment result for dynamic routing"""
        if bank_name not in self.bank_success_history:
            self.bank_success_history[bank_name] = []
        
        # Keep only last 100 records to avoid memory issues
        history = self.bank_success_history[bank_name]
        history.append(success)
        if len(history) > 100:
            history.pop(0)
    
    def enable_dynamic_routing(self):
        """Enable dynamic routing based on success rates"""
        self.dynamic_routing_enabled = True
    
    def disable_dynamic_routing(self):
        """Disable dynamic routing"""
        self.dynamic_routing_enabled = False
    
    def get_routing_distribution(self) -> Dict[str, Dict[str, float]]:
        """Get current routing distribution"""
        distribution = {}
        for payment_mode, rules in self.routing_rules.items():
            distribution[payment_mode.value] = {}
            for rule in rules:
                distribution[payment_mode.value][rule.bank.name] = rule.percentage
        return distribution
    
    def get_supported_payment_modes(self) -> List[PaymentMode]:
        """Get all payment modes that have routing rules"""
        return list(self.routing_rules.keys())
    
    def update_bank_percentage(self, payment_mode: PaymentMode, bank_name: str, new_percentage: float):
        """Update percentage for a specific bank routing rule"""
        if payment_mode not in self.routing_rules:
            raise ValueError(f"No routing rules found for {payment_mode.value}")
        
        # Find the rule to update
        rule_to_update = None
        for rule in self.routing_rules[payment_mode]:
            if rule.bank.name == bank_name:
                rule_to_update = rule
                break
        
        if not rule_to_update:
            raise ValueError(f"No routing rule found for {bank_name} and {payment_mode.value}")
        
        # Check if total percentage would exceed 100
        current_total = sum(rule.percentage for rule in self.routing_rules[payment_mode] 
                           if rule != rule_to_update)
        if current_total + new_percentage > 100:
            raise ValueError(f"Total percentage for {payment_mode.value} would exceed 100%")
        
        rule_to_update.percentage = new_percentage