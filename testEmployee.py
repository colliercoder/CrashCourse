import unittest
from Employee import Employee


class TestEmployee(unittest.TestCase):
    def setUp(self):
        self.daniel=Employee('Daniel','Gauerke',100000)
    def test_give_default_raise(self):
        self.daniel.give_raise()
        self.assertEqual(self.daniel.salary, 105000)  # add assertion here
    def test_give_custome_raise(self):
        self.daniel.give_raise(2000)
        self.assertEqual(self.daniel.salary,102000)

if __name__ == '__main__':
    unittest.main()
