from Currency import Currency


class UnknownCurrencyCodeError(Exception):
    pass


class Converter():
    def __init__(self, dictionary):
        self.dictionary = dictionary

    def convert(self, currency, currency_code):
        self.currency = currency
        self.currency_code = currency_code
        if currency.nation in self.dictionary and currency_code in self.dictionary:
            new_value = round((currency.value * self.dictionary[currency_code])/self.dictionary[currency.nation], 2)
            return Currency(currency_code, new_value)
        else:
            UnknownCurrencyCodeError()
