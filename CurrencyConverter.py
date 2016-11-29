from Currency import Currency

class Converter():
    def __init__(self, dictionary):
        self.dictionary = dictionary

    def convert(self, currency, currency_code):
        self.currency = currency
        self.currency_code = currency_code
        new_value = (currency.value * self.dictionary[currency_code])/self.dictionary[currency.nation]
        return Currency(currency_code, new_value)
