from forex_python.converter import CurrencyRates
c = CurrencyRates()
result = c.get_rates('THB')
print(result)