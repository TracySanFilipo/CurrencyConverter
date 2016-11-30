#h1 CurrencyConverter

##h5 Currency.py
This file contains a currency class. Currency instances with currency codes and values can be created, and instances with the same code can be added and subtracted. The class and its methods can be imported into other files and used.

##h5 Currency_tests.py
This file contains a series of tests for the class objects in Currency.py. The it can be run in command line with: python -m unittest Currency_tests.py

##h5 CurrencyConverter.py
This file contains a converter class. If this class is initialized with a dictionary of currency conversion rates, it can convert between a given Currency object and a currency code, assuming both of these codes are in the dictionary it was initialized with.


##h5 Converter_tests.py
This file contains a series of unit tests for CurrencyConverter.py. It can be run in command line with: python -m unittest Converter_tests.py
