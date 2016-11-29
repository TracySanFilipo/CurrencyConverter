import unittest
from CurrencyConverter import Converter
# from CurrencyConverter import UnknownCurrencyCodeError


class TestConverter(unittest.TestCase):

    def test_converter_has_dictionary(self):
        converter = Converter({'usd': 1, 'eur': 0.94})
        self.assertIsInstance(converter, Converter)


if __name__ == '__main__':
    unittest.main()
