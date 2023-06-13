""" 
Sample tests
"""
from django.test import SingleTestCase

from app import calc

class CalcTests(SingleTestCase):
    """Test the calc module."""

    def test_add_numbers(self):
        """Test adding numbers together."""
        res = calc.add(5, 6)

        self.assertEqual(res, 11)