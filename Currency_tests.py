import unittest
from Currency import Currency


class TestCurrency(unittest.TestCase):

    def test_currency_amount_and_code(self):
        one_dollar = Currency('usd', 1)
        self.assertIsInstance(one_dollar, Currency)


if __name__ == '__main__':
    unittest.main()
