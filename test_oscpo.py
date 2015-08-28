from oscpo import *
import unittest

class OscpoTest(unittest.TestCase):
    """Tests for oscpo"""

    def test_formatpostcode(self):
        self.assertEqual(formatpostcode('W1 2AA'), 'W1  2AA')
        self.assertEqual(formatpostcode('SW7 2AZ'), 'SW7 2AZ')
        self.assertEqual(formatpostcode('WC2H 8LG'), 'WC2H8LG')
