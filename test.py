# TODO remove all the background color things
# TODO make an option for updating menu for when the user is on advanced it says standard
# TODO add functionality too all menu commands
# TODO finish advanced settings
# TODO improve jumping from standard to advanced to currency all routes fixed
# TODO add more currencies this weekend to dicts

import customtkinter
import tkinter
from tkinter import *
import requests
from datetime import datetime
import tkinter as tk
import tkinter.ttk as ttk
import os
from currency_exchanges import currency_symbols, exchanges



class App:
    def __init__(self):
        self.root = customtkinter.CTk()
        self.root.iconbitmap("darkModeV.ico")
        self.root.geometry("280x550") # L x H
        self.root.config(background="#282828")

        # Currency Label Frame #
        self.currency_label_frame = customtkinter.CTkFrame(self.root)
        self.currency_label_frame.pack(side=TOP, anchor="w", padx=(15, 0), pady=(10, 0))
        # Currency Exchange Label #
        self.currency_label = customtkinter.CTkLabel(self.currency_label_frame, text="Currency Exchange", bg_color="#282828", height=0, width=0, text_font=("Arial", 14, "bold"))
        self.currency_label.pack()


        # input
      
        # Frame for the input stuff
        self.input_convert_frame = customtkinter.CTkFrame(self.root, fg_color='#282828')
        self.input_convert_frame.pack(side=TOP, anchor="w", padx=(15, 0), pady=(10, 0))

        # The currency symbol for the input
        self.input_currency_symbol = customtkinter.CTkLabel(self.input_convert_frame, text="$", bg_color="#282828", height=0, width=0, text_font=("Arial", 16, "bold"))
        self.input_currency_symbol.grid(row=0, column=0, sticky='w')
        # The output label
        self.input_zero_base = customtkinter.StringVar(value="0")
        self.input_currency_input = customtkinter.CTkLabel(self.input_convert_frame, textvariable=self.input_zero_base, bg_color="#282828", height=0, width=0, text_font=("Arial", 30))
        self.input_currency_input.grid(row=0, column=1, sticky='we', padx=(0, 200), columnspan=3)
        # The input currency selector (comboBox)

        style = ttk.Style()
        style.configure('my.TCombobox', arrowsize=30)
        style.configure('Vertical.TScrollbar', arrowsize=28)
        self.currency_selector = customtkinter.CTkComboBox(self.input_convert_frame, values=sorted(list(exchanges.keys())), width=170, command=self.first_currency_selector_function)
        self.currency_selector.set(list(exchanges.keys())[0])
        self.currency_selector.grid(row=1, column=0, columnspan=2, sticky='e', pady=(3, 0))

        # end of input section

      
        # ********************************************** # TODO maybe change button reliefs
      

        # start of output section
      
        # Frame for the out stuff
        self.output_convert_frame = customtkinter.CTkFrame(self.root, fg_color="#282828")
        self.output_convert_frame.pack(side=TOP, anchor="w", padx=(15, 0), pady=(10, 0))
        # The currency symbol for the output
        self.output_currency_symbol = customtkinter.CTkLabel(self.output_convert_frame, text="€", bg_color="#282828", height=0, width=0, text_font=("Arial", 16, "bold"))
        self.output_currency_symbol.grid(row=0, column=0, sticky="w")
        # The output label
        self.output_zero_base = customtkinter.StringVar(value="0")
        self.output_currency_output = customtkinter.CTkLabel(self.output_convert_frame, textvariable=self.output_zero_base, bg_color="#282828", height=0, width=0, text_font=("Arial", 30), text_color='#BABABA')
        self.output_currency_output.grid(row=0, column=1, padx=(0, 200), columnspan=3, sticky='we')
        # The output currency selector (comboBox)
        self.currency_selector2 = customtkinter.CTkComboBox(self.output_convert_frame, values=sorted(list(exchanges.keys())), width=170, command=self.second_currency_selector_function)
        self.currency_selector2.set(list(exchanges.keys())[3])
        self.currency_selector2.grid(row=1, column=0, columnspan=2, sticky='e', pady=(3, 0))

        # end of output section

        # **************************************************************

        # stuff to update the time each time app is opened
        self.now = datetime.now()
        self.current_time = self.now.strftime("%I:%M:%p").split(":")
        self.zero_base_times = ["01", "02", "02", "03", "04", "05", "06", "07", "08", "09"]

        self.hour = self.current_time[0]
        self.minute = self.current_time[1]
        self.pm_am = self.current_time[2]

        self.current_date = str(datetime.now()).split(" ")[0].split("-")

        self.day = self.current_date[2]
        self.month = self.current_date[1]
        self.year = self.current_date[0]

        if self.hour in self.zero_base_times:
            self.hour = self.current_time[0].replace('0', '')
            self.minute = self.current_time[1]
            self.pm_am = self.current_time[2]
        else:
            self.hour = self.current_time[0]
            self.minute = self.current_time[1]
            self.pm_am = self.current_time[2]

        # start of conversion rates label section

        # Frame for the conversion rates labels and stuff
        self.conversion_rates_frame = customtkinter.CTkFrame(self.root, fg_color='#282828')
        self.conversion_rates_frame.pack(side=TOP, anchor="w", padx=(15, 0), pady=(10, 0))
        # The conversion rates label
        self.conversion_rates_conversion_label = customtkinter.CTkLabel(self.conversion_rates_frame, text=f"1 USD = 1.0005 EUR\nUpdated: {self.month}/{self.day}/{self.year} {self.hour}:{self.minute} {self.pm_am}", text_font=("Arial", 10))
        self.conversion_rates_conversion_label.grid(row=0, column=0, sticky='w')
        # The update rates button
        self.update_rates_button = customtkinter.CTkButton(self.conversion_rates_frame, text="Update Rates", height=0, width=0, bg_color='#282828', command=self.update_rates_btn)
        self.update_rates_button.grid(row=1, column=0, pady=(2, 0), sticky='w')

        # end of conversion rates label section

        # ************************************************************

        # start of button stuff


        # frame of the buttons / main button frame
        self.currency_exchange_buttons_frame = customtkinter.CTkFrame(self.root, fg_color="#282828")
        self.currency_exchange_buttons_frame.pack(side=TOP, anchor="n", padx=(0, 0), pady=(15, 0))

        # frame for the exchange set of buttons
        self.first_exchange_set = customtkinter.CTkFrame(self.currency_exchange_buttons_frame, fg_color="#282828")
        self.first_exchange_set.grid(row=0, column=0, sticky='e')

        # number AC button
        self.btn_mut = tkinter.Button(self.first_exchange_set, text="AC", width=6, font=("Arial", 16), bg="#404040", fg="white", relief='flat', command=lambda:self.exchange_ac_btn("*"))
        self.btn_mut.grid(row=0, column=2, sticky="w", padx=2, pady=2)
        # simple fg and bg change when hovered over.
        self.btn_mut.bind('<Enter>', lambda e: self.btn_mut.config(fg='black', bg='#4D4D4D'))
        self.btn_mut.bind('<Leave>', lambda e: self.btn_mut.config(fg='white', bg='#404040'))
        # keyboard press events **
        self.root.bind("c", lambda e: self.exchange_ac_btn("c"))


        # number Backspace button 
        self.btn_sub = tkinter.Button(self.first_exchange_set, text="⌫", width=6, font=("Arial", 16), bg="#404040", fg="white", relief='flat') # command=lambda:self.sub_key2("-")
        self.btn_sub.grid(row=0, column=3, sticky="w", padx=2, pady=2)
        # simple fg and bg change when hovered over.
        self.btn_sub.bind('<Enter>', lambda e: self.btn_sub.config(fg='black', bg='#4D4D4D'))
        self.btn_sub.bind('<Leave>', lambda e: self.btn_sub.config(fg='white', bg='#404040'))
        # keyboard press events **
        self.root.bind("<BackSpace>", lambda e: self.exchange_backspace(" "))


        # second button frame #################################################################################

        self.second_exchange_set = customtkinter.CTkFrame(self.currency_exchange_buttons_frame)
        self.second_exchange_set.grid(row=1, column=0, sticky='e')
        
        # number 7 button
        self.btn_7 = tkinter.Button(self.second_exchange_set, text="7", width=6, font=("Arial", 16), bg="#404040", fg="white", relief='flat', command=lambda: self.exchange_7_btn("7"))
        self.btn_7.grid(row=0, column=0, sticky="n", padx=2, pady=2)
        # simple fg and bg change when hovered over.
        self.btn_7.bind('<Enter>', lambda e: self.btn_7.config(fg='black', bg='#4D4D4D'))
        self.btn_7.bind('<Leave>', lambda e: self.btn_7.config(fg='white', bg='#404040'))
        # keyboard press events **
        self.root.bind("7", lambda e: self.exchange_7_btn("7"))


        # number 8 button
        self.btn_8 = tkinter.Button(self.second_exchange_set, text="8", width=6, font=("Arial", 16), bg="#404040", fg="white", relief='flat') # command=lambda:self.key_8("8")
        self.btn_8.grid(row=0, column=1, sticky="n", padx=2, pady=2)
        # simple fg and bg change when hovered over.
        self.btn_8.bind('<Enter>', lambda e: self.btn_8.config(fg='black', bg='#4D4D4D'))
        self.btn_8.bind('<Leave>', lambda e: self.btn_8.config(fg='white', bg='#404040'))
        # keyboard press events **
        self.root.bind("8", lambda e: self.key_8("8"))


        # number 9 button
        self.btn_9 = tkinter.Button(self.second_exchange_set, text="9", width=6, font=("Arial", 16), bg="#404040", fg="white", relief='flat') # command=lambda:self.key_9("9")
        self.btn_9.grid(row=0, column=2, sticky="n", padx=2, pady=2)
        # simple fg and bg change when hovered over.
        self.btn_9.bind('<Enter>', lambda e: self.btn_9.config(fg='black', bg='#4D4D4D'))
        self.btn_9.bind('<Leave>', lambda e: self.btn_9.config(fg='white', bg='#404040'))
        # keyboard press events **
        self.root.bind("9", lambda e: self.key_9("9"))  



        # third button frame
        self.third_exchange_set = customtkinter.CTkFrame(self.currency_exchange_buttons_frame)
        self.third_exchange_set.grid(row=2, column=0, sticky='e')
        
        # number 4 button
        self.btn_4 = tkinter.Button(self.third_exchange_set, text="4", width=6, font=("Arial", 16), bg="#404040", fg="white", relief='flat') # command=lambda:self.key_4("4")
        self.btn_4.grid(row=1, column=0, sticky="n", padx=2, pady=2)
        # simple fg and bg change when hovered over.
        self.btn_4.bind('<Enter>', lambda e: self.btn_4.config(fg='black', bg='#4D4D4D'))
        self.btn_4.bind('<Leave>', lambda e: self.btn_4.config(fg='white', bg='#404040'))
        # keyboard press events **
        self.root.bind("4", lambda e: self.key_4("4"))


        # number 5 button
        self.btn_5 = tkinter.Button(self.third_exchange_set, text="5", width=6, font=("Arial", 16), bg="#404040", fg="white", relief='flat') # command=lambda:self.key_5("5")
        self.btn_5.grid(row=1, column=1, sticky="n", padx=2, pady=2)
        # simple fg and bg change when hovered over.
        self.btn_5.bind('<Enter>', lambda e: self.btn_5.config(fg='black', bg='#4D4D4D'))
        self.btn_5.bind('<Leave>', lambda e: self.btn_5.config(fg='white', bg='#404040'))
        # keyboard press events **
        self.root.bind("5", lambda e: self.key_5("5"))


        # number 6 button
        self.btn_6 = tkinter.Button(self.third_exchange_set, text="6", width=6, font=("Arial", 16), bg="#404040", fg="white", relief='flat') # command=lambda:self.key_6("6")
        self.btn_6.grid(row=1, column=2, sticky="n", padx=2, pady=2)
        # simple fg and bg change when hovered over.
        self.btn_6.bind('<Enter>', lambda e: self.btn_6.config(fg='black', bg='#4D4D4D'))
        self.btn_6.bind('<Leave>', lambda e: self.btn_6.config(fg='white', bg='#404040'))
        # keyboard press events **
        self.root.bind("6", lambda e: self.key_6("6"))



        # fourth button frame
        self.fourth_exchange_set = customtkinter.CTkFrame(self.currency_exchange_buttons_frame)
        self.fourth_exchange_set.grid(row=3, column=0, sticky='e')
        

        # number 1 button
        self.btn_1 = tkinter.Button(self.fourth_exchange_set, text="1", width=6, font=("Arial", 16), bg="#404040", fg="white", relief='flat') # command=lambda:self.key_1("1")
        self.btn_1.grid(row=0, column=0, sticky="n", padx=2, pady=2)
        # simple fg and bg change when hovered over.
        self.btn_1.bind('<Enter>', lambda e: self.btn_1.config(fg='black', bg='#4D4D4D'))
        self.btn_1.bind('<Leave>', lambda e: self.btn_1.config(fg='white', bg='#404040'))
        # keyboard press events **
        self.root.bind("1", lambda e: self.key_1("1"))


        # number 2 button
        self.btn_2 = tkinter.Button(self.fourth_exchange_set, text="2", width=6, font=("Arial", 16), bg="#404040", fg="white", relief='flat') # command=lambda:self.key_2("2")
        self.btn_2.grid(row=0, column=1, sticky="n", padx=2, pady=2)
        # simple fg and bg change when hovered over.
        self.btn_2.bind('<Enter>', lambda e: self.btn_2.config(fg='black', bg='#4D4D4D'))
        self.btn_2.bind('<Leave>', lambda e: self.btn_2.config(fg='white', bg='#404040'))
        # keyboard press events **
        self.root.bind("2", lambda e: self.key_2("2"))


        # number 3 button
        self.btn_3 = tkinter.Button(self.fourth_exchange_set, text="3", width=6, font=("Arial", 16), bg="#404040", fg="white", relief='flat') # command=lambda:self.key_3("3")
        self.btn_3.grid(row=0, column=2, sticky="n", padx=2, pady=2)
        # simple fg and bg change when hovered over.
        self.btn_3.bind('<Enter>', lambda e: self.btn_3.config(fg='black', bg='#4D4D4D'))
        self.btn_3.bind('<Leave>', lambda e: self.btn_3.config(fg='white', bg='#404040'))
        # keyboard press events **
        self.root.bind("3", lambda e: self.key_3("3"))


        # fifth button frame
        self.fifth_exchange_set = customtkinter.CTkFrame(self.currency_exchange_buttons_frame)
        self.fifth_exchange_set.grid(row=4, column=0, sticky='e')

        # number 0 button
        self.btn_0 = tkinter.Button(self.fifth_exchange_set, text="0", width=6, font=("Arial", 16), bg="#404040", fg="white", relief='flat') # command=lambda:self.key_0("0")
        self.btn_0.grid(row=1, column=0, sticky="n", padx=2, pady=2)
        # simple fg and bg change when hovered over.
        self.btn_0.bind('<Enter>', lambda e: self.btn_0.config(fg='black', bg='#4D4D4D'))
        self.btn_0.bind('<Leave>', lambda e: self.btn_0.config(fg='white', bg='#404040'))
        # keyboard press events **
        self.root.bind("0", lambda e: self.key_0("0"))

        # number dot button
        self.btn_dot = tkinter.Button(self.fifth_exchange_set, text=".", width=6, font=("Arial", 16), bg="#404040", fg="white", relief='flat') # command=lambda:self.key_dot(".")
        self.btn_dot.grid(row=1, column=2, sticky="n", padx=2, pady=2)
        # simple fg and bg change when hovered over.
        self.btn_dot.bind('<Enter>', lambda e: self.btn_dot.config(fg='black', bg='#4D4D4D'))
        self.btn_dot.bind('<Leave>', lambda e: self.btn_dot.config(fg='white', bg='#404040'))
        # keyboard press events **
        self.root.bind(".", lambda e: self.key_dot("."))

        self.last_exchange_frame = customtkinter.CTkFrame(self.root)
        self.last_exchange_frame.pack(side=BOTTOM)

        self.powered_by_api = customtkinter.CTkLabel(self.last_exchange_frame, text="Powered by ExchangeRate API", text_font=("Arial", 7), width=0, height=0, fg_color="#282828")
        self.powered_by_api.pack()


        self.root.bind("r", lambda e: self.return_standard("0"))
        self.root.bind("a", lambda e: self.return_advanced("1"))

        self.root.mainloop()


    # Method for returning to standard
    def return_standard(self, e):
        self.input_convert_frame.pack_forget()
        self.currency_label_frame.pack_forget()
        self.input_convert_frame.pack_forget()
        self.output_convert_frame.pack_forget()

        self.root.title("Simple Calculator")

        self.label_pack.pack(side=TOP, anchor="w", padx=(15, 0), pady=(10, 0))
        self.entry_pack.pack(side=TOP, anchor="w", padx=(15, 0))
        self.first_pack.pack(side=LEFT, anchor="nw", padx=(15, 0), pady=(5, 0))
        self.second_pack.pack(side=LEFT, anchor="ne", padx=(15, 0), pady=(5, 0))


    # method for putting out currency symbols
    def first_currency_selector_function(self, selected):
        self.current = self.currency_selector.get() # United States - Dollar
        self.get_currency_code = exchanges[self.current]
        self.get_symbol = currency_symbols[self.get_currency_code]
        self.input_currency_symbol.configure(text=self.get_symbol)


        self.api_key = os.environ.get("currency_api_key")
        # current_value = currency_selector.get() # United States - Dollar
        self.current_value1 = self.currency_selector.get()
        self.current_value2 = self.currency_selector2.get()

        self.get_currency_code = exchanges[self.current_value1]
        self.get_currency_code2 = exchanges[self.current_value2]

        self.url = f"https://v6.exchangerate-api.com/v6/{self.api_key}/latest/{self.get_currency_code}"
        self.response = requests.get(self.url)
        self.response_json = self.response.json()

        self.time = self.response_json['time_last_update_utc']
        self.for_label = self.time.split(" ")
        self.day = self.for_label[1]
        self.month = self.for_label[2]
        self.year = self.for_label[3]

        self.for_label1 = f"Updated: {self.month}/{self.day}/{self.year}"

        self.converion = self.response_json['conversion_rates'] # thing you index with "USD"
        self.label_thing = self.converion[self.get_currency_code] # = 1
        self.label_thing2 = self.converion[self.get_currency_code2] # 0.99

        self.thing_for_label = f"{self.label_thing} {self.get_currency_code} = {self.label_thing2} {self.get_currency_code2}\n{self.for_label1}"
        self.conversion_rates_conversion_label.configure(text=self.thing_for_label)


    # method for putting out currency symbols
    def second_currency_selector_function(self, selected):
        self.current = self.currency_selector2.get() # United States - Dollar
        self.get_currency_code = exchanges[self.current]
        self.get_symbol = currency_symbols[self.get_currency_code]
        self.output_currency_symbol.configure(text=self.get_symbol)


        self.api_key = os.environ.get("currency_api_key")
        # current_value = currency_selector.get() # United States - Dollar
        self.current_value1 = self.currency_selector.get()
        self.current_value2 = self.currency_selector2.get()

        self.get_currency_code = exchanges[self.current_value1]
        self.get_currency_code2 = exchanges[self.current_value2]

        self.url = f"https://v6.exchangerate-api.com/v6/{self.api_key}/latest/{self.get_currency_code}"
        self.response = requests.get(self.url)
        self.response_json = self.response.json()

        self.time = self.response_json['time_last_update_utc']
        self.for_label = self.time.split(" ")
        self.day = self.for_label[1]
        self.month = self.for_label[2]
        self.year = self.for_label[3]

        self.for_label1 = f"Updated: {self.month}/{self.day}/{self.year}"

        self.converion = self.response_json['conversion_rates'] # thing you index with "USD"
        self.label_thing = self.converion[self.get_currency_code] # = 1
        self.label_thing2 = self.converion[self.get_currency_code2] # 0.99

        self.thing_for_label = f"{self.label_thing} {self.get_currency_code} = {self.label_thing2} {self.get_currency_code2}\n{self.for_label1}"
        self.conversion_rates_conversion_label.configure(text=self.thing_for_label)


    # Method for exchanging the two inputs
    def exchange_rate(self, first_input, second_input, combo1, combo2):
        # self.api_key = os.environ.get("currency_api_key")

        # url = f"https://v6.exchangerate-api.com/v6/{self.api_key}/latest/{combo1}"
        # response = requests.get(url)
        # response_json = response.json()
        # time = response_json['time_last_update_utc']
        # converion = response_json['conversion_rates']

        # output_1 = converion[combo1.upper()]
        # output_2 = converion[combo2.upper()]
        pass


    def return_advanced(self, e):
        self.root.geometry("570x340")

        self.label_pack.pack(side=TOP, anchor="w", padx=(15, 0), pady=(10, 0))
        self.entry_pack.pack(side=TOP, anchor="w", padx=(15, 0))
        self.first_pack.pack(side=LEFT, anchor="nw", padx=(15, 0), pady=(5, 0))
        self.second_pack.pack(side=LEFT, anchor="ne", padx=(15, 0), pady=(5, 0))

        self.currency_label_frame.pack_forget()


    def update_rates_btn(self):
        self.api_key = os.environ.get("currency_api_key")
        self.current = self.currency_selector.get() # United States - Dollar
        self.get_base_rate = exchanges[self.current] # USD

        self.second_current = self.currency_selector2.get() # Europe - Euro
        self.get_second_rate_l = exchanges[self.second_current] # EUR


        self.url = f"https://v6.exchangerate-api.com/v6/{self.api_key}/latest/{self.get_base_rate}"

        self.response = requests.get(self.url).json()
        self.time_response = self.response['time_last_update_unix']
        self.rates_response = self.response['conversion_rates']

        self.get_first_rate = self.rates_response[self.get_base_rate] # 1
        self.get_second_rate = self.rates_response[self.get_second_rate_l] # 0.99


        self.unix_convert_int = int(self.time_response)
        self.date = datetime.utcfromtimestamp(self.unix_convert_int).strftime('%Y-%m-%d %I:%M %p').split("-")
        self.update_day = self.date[2].split(" ")[0]
        self.update_month = self.date[1]
        self.update_year = self.date[0]

        self.update_time = self.date[2].split(" ")[1] + " "
        self.am_pm = self.date[2].split(" ")[2]

        self.to_update = f"""{self.get_first_rate} {self.get_base_rate} = {self.get_second_rate} {self.get_second_rate_l}\nUpdated: {self.update_month}/{self.update_day}/{self.update_year} {self.update_time}{self.am_pm}"""

        self.conversion_rates_conversion_label.configure(text=self.to_update)


    # buttons for the exchange option

    # exchange button all clear
    def exchange_ac_btn(self, e):
        self.get_value = self.input_zero_base.get()
        if self.get_value == "0":
            pass
        elif self.get_value != "0":
            self.input_zero_base.set(value="0")
            self.output_zero_base.set(value="0")
        

    # exchange button for number 7
    def exchange_7_btn(self, e):
        """Method for when the user presses 7 key instead of clicking button"""
        self.api_key = os.environ.get("currency_api_key")
        self.current = self.currency_selector.get() # United States - Dollar
        self.get_base_rate = exchanges[self.current] # USD

        self.second_current = self.currency_selector2.get() # Europe - Euro
        self.get_second_rate_l = exchanges[self.second_current] # EUR

        self.url = f"https://v6.exchangerate-api.com/v6/{self.api_key}/latest/{self.get_base_rate}"

        self.response = requests.get(self.url).json()
        self.time_response = self.response['time_last_update_unix']
        self.rates_response = self.response['conversion_rates']

        self.get_first_rate = self.rates_response[self.get_base_rate] # 1
        self.get_second_rate = self.rates_response[self.get_second_rate_l] # 0.99



        self.thing = self.input_zero_base.get() # gets the value
        if self.thing == "0":
            self.input_zero_base.set(value='7') # sets of value of label to 7

            self.value = self.input_zero_base.get() # gets that value

            # creates new variable that equals (int(first rate) * int(value of label)) * float(second rate)
            self.calculate = (int(self.get_first_rate) * int(self.value)) * float(self.get_second_rate)
            self.return_value = str(self.calculate)

            if len(self.return_value) > 4:
                self.new_return_value = self.return_value.split(".")
                self.second_value = self.new_return_value[1]
                self.number = len(self.second_value)
                self.to_del = int(self.number) - 2
                self.final_value = self.return_value[:-self.to_del]
                self.output_zero_base.set(value=str(self.return_value)[:-2])
            elif len(self.return_value) <= 4:
                self.output_zero_base.set(value=str(self.calculate))


        elif self.thing != "0":
            self.new_value = self.input_zero_base.get()
            self.input_zero_base.set(self.thing + "7")
            self.new_value = self.input_zero_base.get()
            self.calculate = (int(self.get_first_rate) * int(self.new_value)) * float(self.get_second_rate)
            self.elif_value = str(self.calculate)

            if len(self.elif_value) > 4:
                self.elif_split = self.elif_value.split(".")
                self.elif_second = self.elif_split[1]
                self.elif_number = len(self.elif_second)
                self.elif_to_del = int(self.elif_number) - 2
                self.elif_final = self.elif_value[:-self.elif_to_del]
                self.output_zero_base.set(value=self.elif_final)
            elif self.elif_value <= 4:
                self.output_zero_base.set(value=self.elif_final)


    def get_output_calculated(self):
        """This method is to get the input currency and return the calculated output currency

        Returns:
            int: calculates selected input currency with the exchange rate and returns that output
        """
        self.api_key = os.environ.get("currency_api_key")
        self.current = self.currency_selector.get() # United States - Dollar
        self.get_base_rate = exchanges[self.current] # USD

        self.second_current = self.currency_selector2.get() # Europe - Euro
        self.get_second_rate_l = exchanges[self.second_current] # EUR

        self.url = f"https://v6.exchangerate-api.com/v6/{self.api_key}/latest/{self.get_base_rate}"

        self.response = requests.get(self.url).json()
        self.rates_response = self.response['conversion_rates']

        self.get_first_rate = self.rates_response[self.get_base_rate] # 1
        self.get_second_rate = self.rates_response[self.get_second_rate_l] # 0.99


        self.first_value = self.input_zero_base.get() # number that is typed in

        self.values_calculated = float(self.final_value) * int(self.get_second_rate)

        return self.values_calculated



    # exchange command for backspace key event
    def exchange_backspace(self, e):
        self.value_to_del = self.input_zero_base.get()

        if self.value_to_del == "0":
            self.input_zero_base.set(value="0")
            self.output_zero_base.set(value="0")

        elif self.value_to_del != "0" and len(self.value_to_del) == 1:
            self.input_zero_base.set(value="0")
            self.output_zero_base.set(value="0")

        elif self.value_to_del != "0" and len(self.value_to_del) >= 2 :
            minus_1 = self.value_to_del[:-1]
            self.input_zero_base.set(value=minus_1)
            self.new_output = self.get_output_calculated()
            self.output_zero_base.set(value=self.new_output)





app = App()

