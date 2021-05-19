# write your code here!
import requests
import json


# get_rate send a get request to the floatrates.com server and returns a python
# dictionary object
def get_rate(_in_code):
    currency_code = _in_code.lower()
    req = requests.get(
        f"http://www.floatrates.com/daily/{currency_code}.json")
    data_json = req.text
    output = json.loads(data_json)
    return output


# check function lookout in the cache for the key and if the key is
# absent it adds the key-value pair to the cache
def check(_out_code, _cache, _currency_rates):
    print("Checking the cache...")
    if _out_code in _cache:
        print("Oh! It is in the cache!")
    else:
        print("Sorry, but it is not in the cache!")
        _cache[_out_code] = _currency_rates.get(_out_code)["rate"]


def main():
    # in_code takes the initially currency user have as its input
    in_code = str(input()).lower()
    # currency rate is requested from floatrates.com
    currency_rates = get_rate(in_code)
    cache = {}

    # cache is filled as key-value pair where key is currency code
    # and value is conversion rate from in_code to the currency code in key
    if "usd" not in cache and "usd" in currency_rates:
        cache["usd"] = currency_rates.get("usd")["rate"]
    if "eur" not in cache and "eur" in currency_rates:
        cache["eur"] = currency_rates.get("eur")["rate"]
    while True:
        # this while loop keeps asking for the amount
        # and the currency code until currency code is empty
        out_code = str(input()).lower()
        if out_code == "":
            break
        in_amount = float(input())
        check(out_code, cache, currency_rates)
        r = cache[out_code]  # conversion rate is obtained from cache
        out_amount = round(in_amount * r, 2)
        print(f"You received {str(out_amount)} {out_code.upper()}.")


if __name__ == "__main__":
    main()
