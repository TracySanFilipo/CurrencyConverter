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

    def test_currency_amount_and_code_negative(self):
        one_dollar = Currency('usd', 1)
        two_dollar = Currency('usd', 2)
        self.assertNotEqual(one_dollar, two_dollar)

    def test_currency_amount_and_code_negative2(self):
        one_dollar = Currency('usd', 1)
        two_dollar = Currency('eur', 1)
        self.assertNotEqual(one_dollar, two_dollar)

    def test_add(self):
        five_dollar = Currency('usd', 5)
        three_dollar = Currency('usd', 3)
        self.assertEqual(five_dollar + three_dollar, Currency('usd', 8))


if __name__ == '__main__':
    unittest.main()
