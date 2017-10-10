import unittest
from inherit import ITEmployee
class EmployeeWithoutPositionTests(unittest.TestCase):
    def setUp(self):
        self.emp = ITEmployee("Elena", "Pian")

    def test_names(self):
        self.assertEqual(self.emp.name, "Elena")
        self.assertEqual(self.emp.surname, "Pian")
