from Currency import Currency

class Converter():
    def __init__(self, dictionary):
        self.dictionary = dictionary

    def convert(self, currency, currency_code):
        self.currency = currency
        self.currency_code = currency_code
        new_value = round((currency.value * self.dictionary[currency_code])/self.dictionary[currency.nation], 2)
        return Currency(currency_code, new_value)
