import os
import requests

exchanges = ["USD", "CAD", "AUS"]
currency = {"USD": "United States Dollar", "CAD": "Canadian Dollar", "AUD": "Australian Dollar"}
currency_symbols = {"USD": "$", "CAD": "$", "AUD": "$"}


api_key = os.environ.get("currency_api_key")
combo1 = "USD"

url = f"https://v6.exchangerate-api.com/v6/{api_key}/latest/{combo1}"
respone = requests.get(url)
ss = respone.json()
time = ss['time_last_update_utc']
converion = ss['conversion_rates']

combo1 = input("> ")
combo2 = input("> ")

first_input = input(f"{combo1}: ")
second_input = input(f"{combo2}: ")

output_1 = converion[combo1.upper()]
output_2 = converion[combo2.upper()]

# TODO redo the whole currency thing because its asking the user how much of what currency they want to convert
# no need to have two entry widgets


result = f"{currency_symbols[combo1.upper()]}{first_input} = {currency_symbols[combo2.upper()]}"

print(result)


