import math

class Currency:
    def __init__(self, nation, value):
        self.nation = nation
        self.value = value

    def __eq__(self, other):
        return self.__dict__ == other.__dict__
