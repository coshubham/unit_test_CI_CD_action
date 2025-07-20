import pytest
import unittest
from greeter import Greeter

class TestGreeter(unittest.TestCase):
    def test_say_hello(self):
        g = Greeter("Shubham")
        self.assertEqual(g.say_hello(), "Hello, Shubham!")

if __name__ == "__main__":
    unittest.main()
