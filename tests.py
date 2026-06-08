import unittest
from utils import format_currency, calculate_percentage, validate_transaction_amount

class TestFinPulseUtils(unittest.TestCase):
    
    def test_format_currency(self):
        """Test if the currency formatter works correctly."""
        self.assertEqual(format_currency(1500.5), "₹1,500.50")
        self.assertEqual(format_currency(0), "₹0.00")

    def test_calculate_percentage(self):
        """Test the percentage calculator, including zero-division safety."""
        self.assertEqual(calculate_percentage(50, 100), "50.0%")
        self.assertEqual(calculate_percentage(50, 0), "0.0%")

    def test_validate_transaction(self):
        """Test if invalid amounts are caught."""
        self.assertTrue(validate_transaction_amount(100.0))
        self.assertFalse(validate_transaction_amount(-50.0))
        self.assertFalse(validate_transaction_amount(0))

if __name__ == '__main__':
    unittest.main()
