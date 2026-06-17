"""
Test suite for Payment Gateway System
Demonstrates unit testing for all major components
"""

import unittest
from unittest.mock import Mock, patch
from payment_gateway import PaymentGateway
from payment_mode import PaymentMode, UPIInstrument, CreditCardInstrument, NetBankingInstrument
from bank import HDFCBank, ICICIBank, PaymentResult
from client import Client
from payment_router import PaymentRouter, RoutingRule


class TestPaymentInstruments(unittest.TestCase):
    """Test cases for payment instruments"""
    
    def test_upi_instrument_valid(self):
        """Test valid UPI instrument"""
        upi = UPIInstrument("user@paytm")
        self.assertTrue(upi.validate())
        self.assertEqual(upi.payment_mode, PaymentMode.UPI)
        
        details = upi.get_payment_details()
        self.assertEqual(details["payment_mode"], "UPI")
        self.assertEqual(details["vpa"], "user@paytm")
    
    def test_upi_instrument_invalid(self):
        """Test invalid UPI instrument"""
        upi_invalid1 = UPIInstrument("invalid_vpa")
        upi_invalid2 = UPIInstrument("user@@paytm")
        upi_invalid3 = UPIInstrument("")
        
        self.assertFalse(upi_invalid1.validate())
        self.assertFalse(upi_invalid2.validate())
        self.assertFalse(upi_invalid3.validate())
    
    def test_credit_card_instrument_valid(self):
        """Test valid credit card instrument"""
        cc = CreditCardInstrument("4532123456789012", 12, 2025, "123", "John Doe")
        self.assertTrue(cc.validate())
        self.assertEqual(cc.payment_mode, PaymentMode.CREDIT_CARD)
        
        details = cc.get_payment_details()
        self.assertEqual(details["payment_mode"], "CREDIT_CARD")
        self.assertEqual(details["card_number"], "9012")  # Last 4 digits
    
    def test_credit_card_instrument_invalid(self):
        """Test invalid credit card instrument"""
        cc_invalid = CreditCardInstrument("123", 13, 2023, "12345", "")
        self.assertFalse(cc_invalid.validate())
    
    def test_netbanking_instrument(self):
        """Test netbanking instrument"""
        nb = NetBankingInstrument("username", "password", "ICICI001")
        self.assertTrue(nb.validate())
        self.assertEqual(nb.payment_mode, PaymentMode.NET_BANKING)
        
        details = nb.get_payment_details()
        self.assertEqual(details["payment_mode"], "NET_BANKING")
        self.assertEqual(details["bank_code"], "ICICI001")
        self.assertNotIn("password", details)  # Password should not be in details


class TestClient(unittest.TestCase):
    """Test cases for client functionality"""
    
    def setUp(self):
        self.client = Client("CLIENT1", "Test Client")
    
    def test_client_initialization(self):
        """Test client initialization"""
        self.assertEqual(self.client.client_id, "CLIENT1")
        self.assertEqual(self.client.name, "Test Client")
        self.assertTrue(self.client.is_active)
        self.assertEqual(len(self.client.supported_payment_modes), 4)  # All modes by default
    
    def test_client_payment_mode_management(self):
        """Test adding and removing payment modes"""
        client = Client("CLIENT2", "Test Client 2", set())
        self.assertEqual(len(client.supported_payment_modes), 0)
        
        client.add_payment_mode_support(PaymentMode.UPI)
        self.assertTrue(client.supports_payment_mode(PaymentMode.UPI))
        self.assertFalse(client.supports_payment_mode(PaymentMode.CREDIT_CARD))
        
        client.remove_payment_mode_support(PaymentMode.UPI)
        self.assertFalse(client.supports_payment_mode(PaymentMode.UPI))
    
    def test_client_activation(self):
        """Test client activation/deactivation"""
        self.client.deactivate()
        self.assertFalse(self.client.is_active)
        
        self.client.activate()
        self.assertTrue(self.client.is_active)


class TestBank(unittest.TestCase):
    """Test cases for bank functionality"""
    
    def test_hdfc_bank_initialization(self):
        """Test HDFC bank initialization"""
        hdfc = HDFCBank()
        self.assertEqual(hdfc.name, "HDFC")
        self.assertTrue(hdfc.supports_payment_mode(PaymentMode.CREDIT_CARD))
        self.assertTrue(hdfc.supports_payment_mode(PaymentMode.UPI))
        self.assertFalse(hdfc.supports_payment_mode(PaymentMode.NET_BANKING))
    
    def test_icici_bank_initialization(self):
        """Test ICICI bank initialization"""
        icici = ICICIBank()
        self.assertEqual(icici.name, "ICICI")
        self.assertTrue(icici.supports_payment_mode(PaymentMode.NET_BANKING))
        self.assertTrue(icici.supports_payment_mode(PaymentMode.UPI))
        self.assertFalse(icici.supports_payment_mode(PaymentMode.CREDIT_CARD))
    
    @patch('random.random')
    def test_bank_payment_processing_success(self, mock_random):
        """Test successful payment processing"""
        mock_random.return_value = 0.8  # Simulate success
        hdfc = HDFCBank()
        hdfc.success_rate = 0.9
        
        payment_details = {"payment_mode": "CREDIT_CARD"}
        result = hdfc.process_payment(1000.0, payment_details)
        
        self.assertTrue(result.success)
        self.assertIsNotNone(result.transaction_id)
        self.assertEqual(result.bank_name, "HDFC")
    
    @patch('random.random')
    def test_bank_payment_processing_failure(self, mock_random):
        """Test failed payment processing"""
        mock_random.return_value = 0.1  # Simulate failure
        hdfc = HDFCBank()
        hdfc.success_rate = 0.05  # Set very low success rate to ensure failure
        
        payment_details = {"payment_mode": "CREDIT_CARD"}
        result = hdfc.process_payment(1000.0, payment_details)
        
        self.assertFalse(result.success)
        self.assertIsNotNone(result.error_message)


class TestPaymentRouter(unittest.TestCase):
    """Test cases for payment router"""
    
    def setUp(self):
        self.router = PaymentRouter()
        self.hdfc = HDFCBank()
        self.icici = ICICIBank()
    
    def test_add_routing_rule(self):
        """Test adding routing rules"""
        self.router.add_routing_rule(PaymentMode.CREDIT_CARD, self.hdfc, 70.0)
        self.router.add_routing_rule(PaymentMode.CREDIT_CARD, self.icici, 30.0)
        
        rules = self.router.routing_rules[PaymentMode.CREDIT_CARD]
        self.assertEqual(len(rules), 2)
    
    def test_routing_percentage_validation(self):
        """Test routing percentage validation"""
        self.router.add_routing_rule(PaymentMode.CREDIT_CARD, self.hdfc, 70.0)
        
        with self.assertRaises(ValueError):
            self.router.add_routing_rule(PaymentMode.CREDIT_CARD, self.icici, 40.0)  # Total would be 110%
    
    def test_get_bank_for_payment(self):
        """Test bank selection for payment"""
        self.router.add_routing_rule(PaymentMode.UPI, self.hdfc, 100.0)
        
        bank = self.router.get_bank_for_payment(PaymentMode.UPI)
        self.assertEqual(bank.name, "HDFC")
        
        # Test non-existent payment mode
        bank = self.router.get_bank_for_payment(PaymentMode.CREDIT_CARD)
        self.assertIsNone(bank)
    
    def test_routing_distribution(self):
        """Test routing distribution display"""
        self.router.add_routing_rule(PaymentMode.UPI, self.hdfc, 60.0)
        self.router.add_routing_rule(PaymentMode.UPI, self.icici, 40.0)
        
        distribution = self.router.get_routing_distribution()
        self.assertEqual(distribution["UPI"]["HDFC"], 60.0)
        self.assertEqual(distribution["UPI"]["ICICI"], 40.0)
    
    def test_dynamic_routing(self):
        """Test dynamic routing functionality"""
        self.assertFalse(self.router.dynamic_routing_enabled)
        
        self.router.enable_dynamic_routing()
        self.assertTrue(self.router.dynamic_routing_enabled)
        
        # Record some payment results
        self.router.record_payment_result("HDFC", True)
        self.router.record_payment_result("HDFC", True)
        self.router.record_payment_result("ICICI", False)
        
        history = self.router.bank_success_history
        self.assertEqual(len(history["HDFC"]), 2)
        self.assertEqual(len(history["ICICI"]), 1)


class TestPaymentGateway(unittest.TestCase):
    """Test cases for payment gateway"""
    
    def setUp(self):
        self.pg = PaymentGateway("TestGateway")
        self.hdfc = HDFCBank()
        self.icici = ICICIBank()
        self.pg.add_bank(self.hdfc)
        self.pg.add_bank(self.icici)
        self.pg.add_support_for_paymode(PaymentMode.UPI)
        self.pg.add_support_for_paymode(PaymentMode.CREDIT_CARD)
    
    def test_client_management(self):
        """Test client management operations"""
        # Add client
        result = self.pg.add_client("CLIENT1", "Test Client")
        self.assertTrue(result)
        self.assertTrue(self.pg.has_client("CLIENT1"))
        
        # Try to add duplicate client
        result = self.pg.add_client("CLIENT1", "Duplicate Client")
        self.assertFalse(result)
        
        # Remove client
        result = self.pg.remove_client("CLIENT1")
        self.assertTrue(result)
        self.assertFalse(self.pg.has_client("CLIENT1"))
        
        # Try to remove non-existent client
        result = self.pg.remove_client("NON_EXISTENT")
        self.assertFalse(result)
    
    def test_bank_management(self):
        """Test bank management operations"""
        # Banks are already added in setUp
        self.assertTrue("HDFC" in self.pg.banks)
        self.assertTrue("ICICI" in self.pg.banks)
        
        # Remove bank
        result = self.pg.remove_bank("HDFC")
        self.assertTrue(result)
        self.assertFalse("HDFC" in self.pg.banks)
    
    def test_payment_mode_management(self):
        """Test payment mode management"""
        # Add client with specific payment modes
        self.pg.add_client("CLIENT1", "Test Client", {PaymentMode.UPI})
        
        # Test gateway level payment modes
        gateway_modes = self.pg.list_supported_paymodes()
        self.assertIn(PaymentMode.UPI, gateway_modes)
        self.assertIn(PaymentMode.CREDIT_CARD, gateway_modes)
        
        # Test client level payment modes
        client_modes = self.pg.list_supported_paymodes("CLIENT1")
        self.assertIn(PaymentMode.UPI, client_modes)
        self.assertNotIn(PaymentMode.CREDIT_CARD, client_modes)
        
        # Add payment mode to client
        self.pg.add_support_for_paymode(PaymentMode.CREDIT_CARD, "CLIENT1")
        client_modes = self.pg.list_supported_paymodes("CLIENT1")
        self.assertIn(PaymentMode.CREDIT_CARD, client_modes)
    
    def test_routing_management(self):
        """Test routing management"""
        # Add routing rule
        result = self.pg.add_routing_rule(PaymentMode.UPI, "HDFC", 100.0)
        self.assertTrue(result)
        
        # Try to add rule for unsupported payment mode by bank
        result = self.pg.add_routing_rule(PaymentMode.NET_BANKING, "HDFC")  # HDFC doesn't support NET_BANKING
        self.assertFalse(result)
        
        # Test routing distribution
        distribution = self.pg.show_distribution()
        self.assertIn("UPI", distribution)
        self.assertEqual(distribution["UPI"]["HDFC"], 100.0)
    
    @patch('random.random')
    def test_successful_payment(self, mock_random):
        """Test successful payment processing"""
        mock_random.return_value = 0.8  # Simulate success
        
        # Setup
        self.pg.add_client("CLIENT1", "Test Client", {PaymentMode.UPI})
        self.pg.add_routing_rule(PaymentMode.UPI, "HDFC", 100.0)
        
        # Make payment
        upi_instrument = UPIInstrument("user@paytm")
        result = self.pg.make_payment("CLIENT1", upi_instrument, 1000.0)
        
        self.assertTrue(result.success)
        self.assertIsNotNone(result.transaction_id)
    
    def test_failed_payment_invalid_client(self):
        """Test payment failure due to invalid client"""
        upi_instrument = UPIInstrument("user@paytm")
        result = self.pg.make_payment("NON_EXISTENT", upi_instrument, 1000.0)
        
        self.assertFalse(result.success)
        self.assertIn("Invalid or inactive client", result.error_message)
    
    def test_failed_payment_unsupported_mode(self):
        """Test payment failure due to unsupported payment mode"""
        self.pg.add_client("CLIENT1", "Test Client", {PaymentMode.UPI})  # Only UPI supported
        
        cc_instrument = CreditCardInstrument("4532123456789012", 12, 2025, "123", "John Doe")
        result = self.pg.make_payment("CLIENT1", cc_instrument, 1000.0)
        
        self.assertFalse(result.success)
        self.assertIn("doesn't support CREDIT_CARD", result.error_message)
    
    def test_failed_payment_invalid_instrument(self):
        """Test payment failure due to invalid payment instrument"""
        self.pg.add_client("CLIENT1", "Test Client", {PaymentMode.UPI})
        self.pg.add_routing_rule(PaymentMode.UPI, "HDFC", 100.0)
        
        invalid_upi = UPIInstrument("invalid_vpa")  # Missing @
        result = self.pg.make_payment("CLIENT1", invalid_upi, 1000.0)
        
        self.assertFalse(result.success)
        self.assertIn("Invalid payment instrument", result.error_message)
    
    def test_gateway_stats(self):
        """Test gateway statistics"""
        self.pg.add_client("CLIENT1", "Test Client")
        
        stats = self.pg.get_gateway_stats()
        self.assertEqual(stats["gateway_name"], "TestGateway")
        self.assertEqual(stats["total_clients"], 1)
        self.assertEqual(stats["active_clients"], 1)
        self.assertEqual(stats["total_banks"], 2)


class TestIntegration(unittest.TestCase):
    """Integration tests for complete payment flow"""
    
    def setUp(self):
        """Setup complete payment gateway environment"""
        self.pg = PaymentGateway("IntegrationTestGateway")
        
        # Add banks
        self.pg.add_bank(HDFCBank())
        self.pg.add_bank(ICICIBank())
        
        # Add payment mode support
        for mode in PaymentMode:
            self.pg.add_support_for_paymode(mode)
        
        # Add clients
        self.pg.add_client("FLIPKART", "Flipkart", 
                          {PaymentMode.UPI, PaymentMode.CREDIT_CARD, PaymentMode.NET_BANKING})
        self.pg.add_client("AMAZON", "Amazon", 
                          {PaymentMode.UPI, PaymentMode.CREDIT_CARD})
        
        # Setup routing rules
        self.pg.add_routing_rule(PaymentMode.UPI, "HDFC", 50.0)
        self.pg.add_routing_rule(PaymentMode.UPI, "ICICI", 50.0)
        self.pg.add_routing_rule(PaymentMode.CREDIT_CARD, "HDFC", 100.0)
        self.pg.add_routing_rule(PaymentMode.NET_BANKING, "ICICI", 100.0)
    
    @patch('random.random')
    def test_complete_payment_flow(self, mock_random):
        """Test complete payment processing flow"""
        mock_random.return_value = 0.8  # Simulate success
        
        # Set high success rate for all banks
        for bank in self.pg.banks.values():
            bank.success_rate = 0.95
        
        # Test UPI payment
        upi_instrument = UPIInstrument("customer@paytm")
        result = self.pg.make_payment("FLIPKART", upi_instrument, 1000.0)
        self.assertTrue(result.success)
        self.assertIn(result.bank_name, ["HDFC", "ICICI"])
        
        # Test Credit Card payment
        cc_instrument = CreditCardInstrument("4532123456789012", 12, 2025, "123", "John Doe")
        result = self.pg.make_payment("FLIPKART", cc_instrument, 2000.0)
        self.assertTrue(result.success)
        self.assertEqual(result.bank_name, "HDFC")
        
        # Test Net Banking payment
        nb_instrument = NetBankingInstrument("user123", "password123", "ICICI001")
        result = self.pg.make_payment("FLIPKART", nb_instrument, 1500.0)
        self.assertTrue(result.success)
        self.assertEqual(result.bank_name, "ICICI")
    
    def test_client_restrictions(self):
        """Test client payment mode restrictions"""
        # Amazon doesn't support Net Banking
        nb_instrument = NetBankingInstrument("user123", "password123", "ICICI001")
        result = self.pg.make_payment("AMAZON", nb_instrument, 1500.0)
        self.assertFalse(result.success)
        self.assertIn("doesn't support NET_BANKING", result.error_message)


def run_tests():
    """Run all test suites"""
    # Create test suite
    test_suite = unittest.TestSuite()
    
    # Add test classes
    test_classes = [
        TestPaymentInstruments,
        TestClient,
        TestBank,
        TestPaymentRouter,
        TestPaymentGateway,
        TestIntegration
    ]
    
    for test_class in test_classes:
        tests = unittest.TestLoader().loadTestsFromTestCase(test_class)
        test_suite.addTests(tests)
    
    # Run tests
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(test_suite)
    
    return result.wasSuccessful()


if __name__ == "__main__":
    print("Running Payment Gateway Test Suite...")
    print("="*60)
    
    success = run_tests()
    
    print("\n" + "="*60)
    if success:
        print("All tests passed successfully!")
    else:
        print("Some tests failed. Please check the output above.")