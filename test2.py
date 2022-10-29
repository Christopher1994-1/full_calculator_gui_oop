import requests
import os
from currency_exchanges import exchanges, currency_symbols
    
    
def exchange_7_btn():
    """Method for when the user presses 7 key instead of clicking button"""
    api_key = os.environ.get("currency_api_key")
    current = "United States - Dollar" # currency_selector.get() # 
    get_base_rate = exchanges[current] # USD

    second_current = "Europe - Euro" # currency_selector2.get()
    get_second_rate_l = exchanges[second_current] # EUR

    url = f"https://v6.exchangerate-api.com/v6/{api_key}/latest/{get_base_rate}"

    response = requests.get(url).json()
    time_response = response['time_last_update_unix']
    rates_response = response['conversion_rates']

    get_first_rate = rates_response[get_base_rate] # 1
    get_second_rate = rates_response[get_second_rate_l] # 0.99



    thing = "7" # input_zero_base.get()
    if thing == "0":
        # input_zero_base.set(value='7') # adds 7 onto the screen
        value = "7" # input_zero_base.get() # gets the value there
        calculate = (int(get_first_rate) * int(value)) * int(get_second_rate)
        # output_zero_base.set(value=str(calculate))
        print(calculate)

    elif thing != "0":
        new_value = thing

    #     new_value = input_zero_base.get()
    #     input_zero_base.set(thing + "7")


exchange_7_btn()