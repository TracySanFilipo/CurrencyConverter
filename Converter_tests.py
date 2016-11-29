import unittest
from CurrencyConverter import Converter
from Currency import Currency
# from CurrencyConverter import UnknownCurrencyCodeError


class TestConverter(unittest.TestCase):

    def test_converter_has_dictionary(self):
        converter_init = Converter({'usd': 1, 'eur': 0.94})
        self.assertIsInstance(converter_init, Converter)

    def test_converter_makes_same_currency_the_same(self):
        converter_init = Converter({'usd': 1, 'eur': 0.94})
        one_dollar = Currency('usd', 1)
        other_dollar = converter_init.convert(Currency('usd', 1), 'usd')
        self.assertEqual(one_dollar, other_dollar)

if __name__ == '__main__':
    unittest.main()
