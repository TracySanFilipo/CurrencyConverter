import unittest
from Currency import Currency


class TestCurrency(unittest.TestCase):

    def test_currency_instance(self):
        one_dollar = Currency('usd', 1)
        self.assertIsInstance(one_dollar, Currency)

    def test_currency_amount_and_code(self):
        two_dollar = Currency('usd', 2)
        second_dollar = Currency('usd', 2)
        self.assertEqual(two_dollar, second_dollar)


if __name__ == '__main__':
    unittest.main()
