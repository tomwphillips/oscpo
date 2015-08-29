from oscpo import *
import unittest

class OscpoTest(unittest.TestCase):
    """Tests for oscpo"""

    @classmethod
    def setUpClass(cls):
        database.init('oscpo.db')

    @classmethod
    def tearDownClass(cls):
        database.close()

    def test_formatpostcode(self):
        self.assertEqual(formatpostcode('W1 2AA'), 'W1  2AA')
        self.assertEqual(formatpostcode('SW7 2AZ'), 'SW7 2AZ')
        self.assertEqual(formatpostcode('WC2H 8LG'), 'WC2H8LG')

    def test_eastings_northings(self):
        e_n = eastings_northings('WC2H 8LG')
        self.assertIsInstance(e_n, tuple)
        self.assertEqual(len(e_n), 2)
        self.assertIsInstance(e_n[0], int)
        self.assertIsInstance(e_n[1], int)

if __name__ == '__main__':
    unittest.main()
