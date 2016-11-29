import unittest
from Currency import Currency
from Currency import DifferentCurrencyCodeError


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

    def test_subtract(self):
        ten_dollar = Currency('usd', 10)
        three_dollar = Currency('usd', 3)
        self.assertEqual(ten_dollar - three_dollar, Currency('usd', 7))

    def test_subtract_error(self):
        with self.assertRaises(DifferentCurrencyCodeError):
            Currency('usd', 10) - Currency('eur', 3)

    def test_add_error(self):
        with self.assertRaises(DifferentCurrencyCodeError):
            Currency('usd', 10) + Currency('eur', 3)

    def test_int_multiply(self):
        self.assertEqual(Currency('usd', 5) * 10, Currency('usd', 50))

    def test_float_multiply(self):
        self.assertEqual(Currency('usd', 5) * 10.5, Currency('usd', 52.5))

    def test_embedded_symbols(self):
        self.assertEqual(Currency('usd', 30), Currency('$30'))


if __name__ == '__main__':
    unittest.main()
