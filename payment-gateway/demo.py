"""
Demo script for Payment Gateway System
This demonstrates the usage of the payment gateway with various scenarios
"""

from payment_gateway import PaymentGateway
from payment_mode import PaymentMode, UPIInstrument, CreditCardInstrument, DebitCardInstrument, NetBankingInstrument
from bank import HDFCBank, ICICIBank, SBIBank, AxisBank
from client import Client


def demo_payment_gateway():
    """Demonstrate the payment gateway functionality"""
    
    print("="*60)
    print("Payment Gateway System Demo")
    print("="*60)
    
    # Initialize Payment Gateway
    pg = PaymentGateway("RazorPay")
    
    # Add banks
    print("\n1. Adding Banks...")
    hdfc = HDFCBank()
    icici = ICICIBank()
    sbi = SBIBank()
    axis = AxisBank()
    
    pg.add_bank(hdfc)
    pg.add_bank(icici)
    pg.add_bank(sbi)
    pg.add_bank(axis)
    
    # Add supported payment modes to gateway
    print("\n2. Adding Payment Mode Support to Gateway...")
    pg.add_support_for_paymode(PaymentMode.UPI)
    pg.add_support_for_paymode(PaymentMode.CREDIT_CARD)
    pg.add_support_for_paymode(PaymentMode.DEBIT_CARD)
    pg.add_support_for_paymode(PaymentMode.NET_BANKING)
    
    # Add clients
    print("\n3. Adding Clients...")
    # Flipkart - supports all payment modes
    pg.add_client("FLIPKART", "Flipkart", {PaymentMode.UPI, PaymentMode.CREDIT_CARD, 
                                          PaymentMode.DEBIT_CARD, PaymentMode.NET_BANKING})
    
    # Amazon - supports only UPI and cards
    pg.add_client("AMAZON", "Amazon", {PaymentMode.UPI, PaymentMode.CREDIT_CARD, PaymentMode.DEBIT_CARD})
    
    # Paytm - supports only UPI
    pg.add_client("PAYTM", "Paytm", {PaymentMode.UPI})
    
    # Setup routing rules
    print("\n4. Setting up Routing Rules...")
    
    # Credit card transactions go to HDFC (70%) and SBI (30%)
    pg.add_routing_rule(PaymentMode.CREDIT_CARD, "HDFC", 70.0)
    pg.add_routing_rule(PaymentMode.CREDIT_CARD, "SBI", 30.0)
    
    # Net banking goes to ICICI (60%) and SBI (40%)
    pg.add_routing_rule(PaymentMode.NET_BANKING, "ICICI", 60.0)
    pg.add_routing_rule(PaymentMode.NET_BANKING, "SBI", 40.0)
    
    # UPI transactions split between all supporting banks
    pg.add_routing_rule(PaymentMode.UPI, "HDFC", 30.0)
    pg.add_routing_rule(PaymentMode.UPI, "ICICI", 30.0)
    pg.add_routing_rule(PaymentMode.UPI, "SBI", 25.0)
    pg.add_routing_rule(PaymentMode.UPI, "AXIS", 15.0)
    
    # Debit card transactions go to ICICI (50%) and SBI (50%)
    pg.add_routing_rule(PaymentMode.DEBIT_CARD, "ICICI", 50.0)
    pg.add_routing_rule(PaymentMode.DEBIT_CARD, "SBI", 50.0)
    
    # Display gateway information
    print("\n5. Gateway Information:")
    pg.print_gateway_info()
    
    # Test various payment scenarios
    print("\n" + "="*60)
    print("Testing Payment Scenarios")
    print("="*60)
    
    # Scenario 1: Successful UPI payment
    print("\nScenario 1: UPI Payment by Flipkart")
    upi_instrument = UPIInstrument("customer@paytm")
    result = pg.make_payment("FLIPKART", upi_instrument, 1000.0)
    print(f"Result: {result}")
    
    # Scenario 2: Credit card payment
    print("\nScenario 2: Credit Card Payment by Amazon")
    cc_instrument = CreditCardInstrument("4532123456789012", 12, 2025, "123", "John Doe")
    result = pg.make_payment("AMAZON", cc_instrument, 2500.0)
    print(f"Result: {result}")
    
    # Scenario 3: Net banking payment (Amazon doesn't support - should fail)
    print("\nScenario 3: Net Banking Payment by Amazon (Should Fail)")
    nb_instrument = NetBankingInstrument("user123", "password123", "ICICI001")
    result = pg.make_payment("AMAZON", nb_instrument, 1500.0)
    print(f"Result: {result}")
    
    # Scenario 4: Net banking payment by Flipkart (should succeed)
    print("\nScenario 4: Net Banking Payment by Flipkart")
    result = pg.make_payment("FLIPKART", nb_instrument, 1500.0)
    print(f"Result: {result}")
    
    # Scenario 5: Debit card payment
    print("\nScenario 5: Debit Card Payment by Flipkart")
    dc_instrument = DebitCardInstrument("5234567890123456", 6, 2026, "456", "Jane Smith")
    result = pg.make_payment("FLIPKART", dc_instrument, 750.0)
    print(f"Result: {result}")
    
    # Test multiple payments to see routing distribution
    print("\n" + "="*60)
    print("Testing Routing Distribution (Multiple Payments)")
    print("="*60)
    
    print("\nProcessing 10 UPI payments to see routing distribution...")
    upi_results = {}
    for i in range(10):
        result = pg.make_payment("FLIPKART", upi_instrument, 100.0)
        if result.success:
            bank_name = result.bank_name
            upi_results[bank_name] = upi_results.get(bank_name, 0) + 1
    
    print("UPI Payment Distribution:")
    for bank, count in upi_results.items():
        print(f"  {bank}: {count} payments")
    
    # Test client management operations
    print("\n" + "="*60)
    print("Testing Client Management Operations")
    print("="*60)
    
    # Check if clients exist
    print(f"\nHas client FLIPKART: {pg.has_client('FLIPKART')}")
    print(f"Has client NONEXISTENT: {pg.has_client('NONEXISTENT')}")
    
    # List supported payment modes for clients
    print(f"\nFlipkart supported modes: {[mode.value for mode in pg.list_supported_paymodes('FLIPKART')]}")
    print(f"Amazon supported modes: {[mode.value for mode in pg.list_supported_paymodes('AMAZON')]}")
    print(f"Gateway supported modes: {[mode.value for mode in pg.list_supported_paymodes()]}")
    
    # Add payment mode to specific client
    print(f"\nAdding NET_BANKING support to Amazon...")
    pg.add_support_for_paymode(PaymentMode.NET_BANKING, "AMAZON")
    print(f"Amazon supported modes after update: {[mode.value for mode in pg.list_supported_paymodes('AMAZON')]}")
    
    # Test dynamic routing
    print("\n" + "="*60)
    print("Testing Dynamic Routing")
    print("="*60)
    
    print("Enabling dynamic routing...")
    pg.enable_dynamic_routing()
    
    # Process some payments to build success history
    print("Processing payments to build success history...")
    for i in range(20):
        result = pg.make_payment("FLIPKART", upi_instrument, 100.0)
    
    # Show final statistics
    print("\n" + "="*60)
    print("Final Gateway Statistics")
    print("="*60)
    
    stats = pg.get_gateway_stats()
    for key, value in stats.items():
        print(f"{key}: {value}")


def demo_error_scenarios():
    """Demonstrate error handling scenarios"""
    
    print("\n" + "="*60)
    print("Testing Error Scenarios")
    print("="*60)
    
    pg = PaymentGateway("TestGateway")
    
    # Add a bank and client
    hdfc = HDFCBank()
    pg.add_bank(hdfc)
    pg.add_support_for_paymode(PaymentMode.UPI)
    pg.add_client("TEST_CLIENT", "Test Client", {PaymentMode.UPI})
    pg.add_routing_rule(PaymentMode.UPI, "HDFC", 100.0)
    
    print("\n1. Testing invalid payment instrument...")
    invalid_upi = UPIInstrument("invalid_vpa_format")  # Missing @
    result = pg.make_payment("TEST_CLIENT", invalid_upi, 1000.0)
    print(f"Result: {result}")
    
    print("\n2. Testing payment with non-existent client...")
    valid_upi = UPIInstrument("test@paytm")
    result = pg.make_payment("NON_EXISTENT", valid_upi, 1000.0)
    print(f"Result: {result}")
    
    print("\n3. Testing payment with unsupported payment mode...")
    cc_instrument = CreditCardInstrument("4532123456789012", 12, 2025, "123", "John Doe")
    result = pg.make_payment("TEST_CLIENT", cc_instrument, 1000.0)  # Client only supports UPI
    print(f"Result: {result}")
    
    print("\n4. Testing invalid routing percentage...")
    try:
        pg.add_routing_rule(PaymentMode.UPI, "HDFC", 50.0)  # This would make total 150%
    except Exception as e:
        print(f"Error as expected: {e}")


if __name__ == "__main__":
    demo_payment_gateway()
    demo_error_scenarios()