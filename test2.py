import requests
import os
from currency_exchanges import exchanges, currency_symbols
    
    
# exchange command for backspace key event
def exchange_backspace():
    value_to_del = "7" # self.input_zero_base.get()

    if value_to_del == "0":
        # self.input_zero_base.set(value="0")
        # self.output_zero_base.set(value="0")
        print("0")
    elif value_to_del != "0" and len(value_to_del) == 1:
        print("First elif runs " + value_to_del)
        # input_zero_base.set(value="0")
        # output_zero_base.set(value="0")
    elif value_to_del != "0" and len(value_to_del) >= 2 :
        minus_1 = value_to_del[:-1]
        # self.input_zero_base.set(value=minus_1)
        print("Second elif runs " + minus_1)


exchange_backspace()