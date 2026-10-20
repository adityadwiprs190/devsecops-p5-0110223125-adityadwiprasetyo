import unittest
from src.config import AppConfig
from src.auth import AuthManager
from src.inventory import InventoryManager
from src.utils import sanitize_input, calculate_discount

class TestSecureInventoryApp(unittest.TestCase):

    def setUp(self):
        self.auth = AuthManager()
        self.inventory = InventoryManager()

    def test_config_summary(self):
        summary = AppConfig.get_summary()
        self.assertEqual(summary["app_name"], "SecureInventoryApp")

    def test_user_registration_and_login(self):
        self.assertTrue(self.auth.register_user("admin", "SecurePass123!"))
        self.assertTrue(self.auth.verify_user("admin", "SecurePass123!"))
        self.assertFalse(self.auth.verify_user("admin", "WrongPassword"))

    def test_inventory_operations(self):
        self.inventory.add_item("SKU01", "Router Enterprise", 10, 1500000.0)
        self.assertEqual(self.inventory.update_stock("SKU01", -3), 7)
        self.assertEqual(self.inventory.get_total_valuation(), 10500000.0)

    def test_utils_validation(self):
        self.assertEqual(sanitize_input("<script>alert('xss')</script>"), "scriptalert(xss)/script")
        self.assertEqual(calculate_discount(200000, 15), 170000.0)

if __name__ == "__main__":
    unittest.main()