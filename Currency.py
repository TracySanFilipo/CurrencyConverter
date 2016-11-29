import math


class DifferentCurrencyCodeError(Exception):
    pass


class Currency:
    symbols = ['$', '€', '£', '¥', '₽', '₩', '฿', '₺', '₮', '₱', '₭', '₴', '₦']
    embedded_symbols = {'$':'usd', '€': 'eur', '£': 'gbp', '¥': 'jpy', '₽': 'rub', '₩': 'krw', '฿':'thb', '₺': 'try', '₮': 'mnt', '₱': 'mxn', '₭': 'laj', '₴': 'uah', '₦': 'ngn'}

    def __init__(self, nation, value=None):
        if nation[0] in Currency.symbols:
            self.nation = Currency.embedded_symbols[nation[0]]
            self.value = float(nation[1:])
        else:
            self.nation = nation
            self.value = value

    def __eq__(self, other):
        return self.__dict__ == other.__dict__

    def __add__(self, other):
        if self.nation == other.nation:
            return Currency(self.nation, self.value + other.value)
        else:
            raise DifferentCurrencyCodeError()

    def __sub__(self, other):
        if self.nation == other.nation:
            return Currency(self.nation, self.value - other.value)
        else:
            raise DifferentCurrencyCodeError()

    def __mul__(self, number):
        if type(number) == int or type(number) == float:
            return Currency(self.nation, self.value * number)
