import math


class DifferentCurrencyCodeError(Exception):
    pass


class Currency:
    def __init__(self, nation, value):
        self.nation = nation
        self.value = value

    def __eq__(self, other):
        return self.__dict__ == other.__dict__

    def __add__(self, other):
        if self.nation == other.nation:
            return Currency(self.nation, self.value + other.value)
        # else:
        #     raise DifferentCurrencyCodeError()

    def __sub__(self, other):
        if self.nation == other.nation:
            return Currency(self.nation, self.value - other.value)
        else:
            raise DifferentCurrencyCodeError()
