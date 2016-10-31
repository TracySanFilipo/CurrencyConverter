import unittest
from Currency import Currency

class TestCurrency(unittest.TestCase):

    def test_currency(self):
        one_dollar = Currency('usd', 1)


if __name__ == '__main__':
    unittest.main()
