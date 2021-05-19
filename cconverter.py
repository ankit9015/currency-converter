# write your code here!
import rates

conicoin = float(input())

for key, value in rates.rates.items():
    amount = round(rates.convert(value, conicoin), 2)
    print(f"I will get {amount} {key.upper()} from the sale of {conicoin} conicoins.")

