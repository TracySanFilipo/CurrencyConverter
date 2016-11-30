import unittest
from CurrencyConverter import Converter
from Currency import Currency
from CurrencyConverter import UnknownCurrencyCodeError


class TestConverter(unittest.TestCase):

    def test_converter_has_dictionary(self):
        converter_init = Converter({'usd': 1, 'eur': 0.94})
        self.assertIsInstance(converter_init, Converter)

    def test_converter_makes_same_currency_the_same(self):
        converter_init = Converter({'usd': 1, 'eur': 0.94})
        one_dollar = Currency('usd', 1)
        other_dollar = converter_init.convert(Currency('usd', 1), 'usd')
        self.assertEqual(one_dollar, other_dollar)

    def test_converter_handles_changing_currency_code(self):
        converter_init = Converter({'usd': 1, 'eur': 0.94})
        one_dollar_to_euro = converter_init.convert(Currency('usd', 1), 'eur')
        self.assertEqual(one_dollar_to_euro, Currency('eur', 0.94))

    def test_converter_handles_bigger_dictionary(self):
        converter_init = Converter({'usd': 1.0, 'eur': 0.94, 'aud': 1.34, 'jpy': 112.48})
        one_dollar_to_yen = converter_init.convert(Currency('usd', 1), 'jpy')
        self.assertEqual(one_dollar_to_yen, Currency('jpy', 112.48))

    def test_converter_handles_changing_currency_code(self):
        converter_init = Converter({'usd': 1.0, 'eur': 0.94, 'aud': 1.34, 'jpy': 112.48})
        euro_to_yen = converter_init.convert(Currency('eur', 1), 'jpy')
        self.assertEqual(euro_to_yen, Currency('jpy', 119.66))

    def test_get_error_if_unknown_currency_code(self):
        converter_init = Converter({'usd': 1.0, 'eur': 0.94, 'aud': 1.34})
        euro_to_yen = converter_init.convert(Currency('eur', 1), 'jpy')
        self.assertRaises(UnknownCurrencyCodeError)


if __name__ == '__main__':
    unittest.main()
