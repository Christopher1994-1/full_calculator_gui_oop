import customtkinter
import tkinter
from tkinter import *
from currency_exchanges import exchanges, currency_symbols
import os
import requests


class App:
    def __init__(self):
        self.root = customtkinter.CTk()
        self.root.title("Simple Calculator")
        self.root.iconbitmap("darkModeV.ico")
        self.root.geometry("280x340") # L x H change back to 270 or 280?

        # label here
        self.label_pack = customtkinter.CTkFrame(self.root)
        self.label_pack.pack(side=TOP, anchor="w", padx=(15, 0), pady=(10, 0))

        self.header_label = customtkinter.CTkLabel(self.label_pack, text="Standard", bg_color="#282828", height=0, width=0, text_font=("Arial", 14, "bold"))
        self.header_label.pack() # pady=(top, bottom) padx=(left, right) in px


        # entry box here
        self.entry_pack = customtkinter.CTkFrame(self.root)
        self.entry_pack.pack(side=TOP, anchor="w", padx=(15, 0))

        # entry box widget
        self.entry = customtkinter.CTkEntry(self.entry_pack, text_font=("Arial", 26), width=255, height=44)
        self.entry.grid(row=1, column=0, columnspan=3)


        # first set of standard calculator buttons
        self.first_pack = customtkinter.CTkFrame(self.root)
        self.first_pack.pack(side=LEFT, anchor="nw", padx=(15, 0), pady=(5, 0))


        #########################################
        # button frame
        self.first_set_cals_frame = customtkinter.CTkFrame(self.first_pack)
        self.first_set_cals_frame.pack(side=TOP, anchor='w', padx=(5, 0))

        # key press c button 
        self.btn_pi = tkinter.Button(self.first_set_cals_frame, text="C", width=4, font=("Arial", 16), bg="grey", fg="white") # command=self.c_key2
        self.btn_pi.grid(row=0, column=0, sticky="w", padx=2, pady=2)
        # simple fg and bg change when hovered over.
        self.btn_pi.bind('<Enter>', lambda e: self.btn_pi.config(fg='black', bg='lightgrey'))
        self.btn_pi.bind('<Leave>', lambda e: self.btn_pi.config(fg='white', bg='grey'))
        # keyboard press events **
        self.root.bind("c", lambda e: self.c_key("c"))



        # number / button
        self.btn_div = tkinter.Button(self.first_set_cals_frame, text="/", width=4, font=("Arial", 16), bg="grey", fg="white") # command=lambda:self.div_func2("/")
        self.btn_div.grid(row=0, column=1, sticky="w", padx=2, pady=2)
        # simple fg and bg change when hovered over.
        self.btn_div.bind('<Enter>', lambda e: self.btn_div.config(fg='black', bg='lightgrey'))
        self.btn_div.bind('<Leave>', lambda e: self.btn_div.config(fg='white', bg='grey'))
        # keyboard press events **
        self.root.bind("/", lambda e: self.div_func("/"))


        # number * button
        self.btn_mut = tkinter.Button(self.first_set_cals_frame, text="*", width=4, font=("Arial", 16), bg="grey", fg="white") # command=lambda:self.mut_key2("*")
        self.btn_mut.grid(row=0, column=2, sticky="w", padx=2, pady=2)
        # simple fg and bg change when hovered over.
        self.btn_mut.bind('<Enter>', lambda e: self.btn_mut.config(fg='black', bg='lightgrey'))
        self.btn_mut.bind('<Leave>', lambda e: self.btn_mut.config(fg='white', bg='grey'))
        # keyboard press events **
        self.root.bind("*", lambda e: self.mut_key("*"))


        # number - button
        self.btn_sub = tkinter.Button(self.first_set_cals_frame, text="-", width=4, font=("Arial", 16), bg="grey", fg="white") # command=lambda:self.sub_key2("-")
        self.btn_sub.grid(row=0, column=3, sticky="w", padx=2, pady=2)
        # simple fg and bg change when hovered over.
        self.btn_sub.bind('<Enter>', lambda e: self.btn_sub.config(fg='black', bg='lightgrey'))
        self.btn_sub.bind('<Leave>', lambda e: self.btn_sub.config(fg='white', bg='grey'))
        # keyboard press events **
        self.root.bind("-", lambda e: self.sub_key("-"))



        # second button frame #################################################################################

        self.second_btn_frame = customtkinter.CTkFrame(self.first_pack)
        self.second_btn_frame.pack(side=TOP, anchor='w', padx=(5, 0))
        
        # number 7 button
        self.btn_7 = tkinter.Button(self.second_btn_frame, text="7", width=4, font=("Arial", 16), bg="grey", fg="white") # command=lambda:self.btn_click_7("7")
        self.btn_7.grid(row=0, column=0, sticky="n", padx=2, pady=2)
        # simple fg and bg change when hovered over.
        self.btn_7.bind('<Enter>', lambda e: self.btn_7.config(fg='black', bg='lightgrey'))
        self.btn_7.bind('<Leave>', lambda e: self.btn_7.config(fg='white', bg='grey'))
        # keyboard press events **
        self.root.bind("7", lambda e: self.key_7("7"))


        # number 8 button
        self.btn_8 = tkinter.Button(self.second_btn_frame, text="8", width=4, font=("Arial", 16), bg="grey", fg="white") # command=lambda:self.key_8("8")
        self.btn_8.grid(row=0, column=1, sticky="n", padx=2, pady=2)
        # simple fg and bg change when hovered over.
        self.btn_8.bind('<Enter>', lambda e: self.btn_8.config(fg='black', bg='lightgrey'))
        self.btn_8.bind('<Leave>', lambda e: self.btn_8.config(fg='white', bg='grey'))
        # keyboard press events **
        self.root.bind("8", lambda e: self.key_8("8"))


        # number 9 button
        self.btn_9 = tkinter.Button(self.second_btn_frame, text="9", width=4, font=("Arial", 16), bg="grey", fg="white") # command=lambda:self.key_9("9")
        self.btn_9.grid(row=0, column=2, sticky="n", padx=2, pady=2)
        # simple fg and bg change when hovered over.
        self.btn_9.bind('<Enter>', lambda e: self.btn_9.config(fg='black', bg='lightgrey'))
        self.btn_9.bind('<Leave>', lambda e: self.btn_9.config(fg='white', bg='grey'))
        # keyboard press events **
        self.root.bind("9", lambda e: self.key_9("9"))

        # number add button
        self.btn_add = tkinter.Button(self.second_btn_frame, text="+", width=4, font=("Arial", 16), bg="grey", fg="white", height=3) # command=lambda:self.add_func2("+")
        self.btn_add.grid(row=0, column=3, padx=2, pady=2, rowspan=2)
        # simple fg and bg change when hovered over.
        self.btn_add.bind('<Enter>', lambda e: self.btn_add.config(fg='black', bg='lightgrey'))
        self.btn_add.bind('<Leave>', lambda e: self.btn_add.config(fg='white', bg='grey'))
        # keyboard press events **
        self.root.bind("+", lambda e: self.add_func("+"))
        
        ##########

        # number 4 button
        self.btn_4 = tkinter.Button(self.second_btn_frame, text="4", width=4, font=("Arial", 16), bg="grey", fg="white") # command=lambda:self.key_4("4")
        self.btn_4.grid(row=1, column=0, sticky="n", padx=2, pady=2)
        # simple fg and bg change when hovered over.
        self.btn_4.bind('<Enter>', lambda e: self.btn_4.config(fg='black', bg='lightgrey'))
        self.btn_4.bind('<Leave>', lambda e: self.btn_4.config(fg='white', bg='grey'))
        # keyboard press events **
        self.root.bind("4", lambda e: self.key_4("4"))


        # number 5 button
        self.btn_5 = tkinter.Button(self.second_btn_frame, text="5", width=4, font=("Arial", 16), bg="grey", fg="white") # command=lambda:self.key_5("5")
        self.btn_5.grid(row=1, column=1, sticky="n", padx=2, pady=2)
        # simple fg and bg change when hovered over.
        self.btn_5.bind('<Enter>', lambda e: self.btn_5.config(fg='black', bg='lightgrey'))
        self.btn_5.bind('<Leave>', lambda e: self.btn_5.config(fg='white', bg='grey'))
        # keyboard press events **
        self.root.bind("5", lambda e: self.key_5("5"))


        # number 6 button
        self.btn_6 = tkinter.Button(self.second_btn_frame, text="6", width=4, font=("Arial", 16), bg="grey", fg="white") # command=lambda:self.key_6("6")
        self.btn_6.grid(row=1, column=2, sticky="n", padx=2, pady=2)
        # simple fg and bg change when hovered over.
        self.btn_6.bind('<Enter>', lambda e: self.btn_6.config(fg='black', bg='lightgrey'))
        self.btn_6.bind('<Leave>', lambda e: self.btn_6.config(fg='white', bg='grey'))
        # keyboard press events **
        self.root.bind("6", lambda e: self.key_6("6"))

      
        # third button frame #############################################################
        self.third_btn_frame = customtkinter.CTkFrame(self.first_pack)
        self.third_btn_frame.pack(side=TOP, anchor='w', padx=(5, 0))

        
        # number 1 button
        self.btn_1 = tkinter.Button(self.third_btn_frame, text="1", width=4, font=("Arial", 16), bg="grey", fg="white") # command=lambda:self.key_1("1")
        self.btn_1.grid(row=0, column=0, sticky="n", padx=2, pady=2)
        # simple fg and bg change when hovered over.
        self.btn_1.bind('<Enter>', lambda e: self.btn_1.config(fg='black', bg='lightgrey'))
        self.btn_1.bind('<Leave>', lambda e: self.btn_1.config(fg='white', bg='grey'))
        # keyboard press events **
        self.root.bind("1", lambda e: self.key_1("1"))


        # number 2 button
        self.btn_2 = tkinter.Button(self.third_btn_frame, text="2", width=4, font=("Arial", 16), bg="grey", fg="white") # command=lambda:self.key_2("2")
        self.btn_2.grid(row=0, column=1, sticky="n", padx=2, pady=2)
        # simple fg and bg change when hovered over.
        self.btn_2.bind('<Enter>', lambda e: self.btn_2.config(fg='black', bg='lightgrey'))
        self.btn_2.bind('<Leave>', lambda e: self.btn_2.config(fg='white', bg='grey'))
        # keyboard press events **
        self.root.bind("2", lambda e: self.key_2("2"))


        # number 3 button
        self.btn_3 = tkinter.Button(self.third_btn_frame, text="3", width=4, font=("Arial", 16), bg="grey", fg="white") # command=lambda:self.key_3("3")
        self.btn_3.grid(row=0, column=2, sticky="n", padx=2, pady=2)
        # simple fg and bg change when hovered over.
        self.btn_3.bind('<Enter>', lambda e: self.btn_3.config(fg='black', bg='lightgrey'))
        self.btn_3.bind('<Leave>', lambda e: self.btn_3.config(fg='white', bg='grey'))
        # keyboard press events **
        self.root.bind("3", lambda e: self.key_3("3"))


        # number enter button
        self.btn_en = tkinter.Button(self.third_btn_frame, text="Enter", width=4, font=("Arial", 16), bg="#6495ED", fg="white", height=3) # command=self.enter_key2
        self.btn_en.grid(row=0, column=3, padx=2, pady=2, rowspan=2)
        # simple fg and bg change when hovered over.
        self.btn_en.bind('<Enter>', lambda e: self.btn_en.config(fg='black', bg='#3D59AB'))
        self.btn_en.bind('<Leave>', lambda e: self.btn_en.config(fg='white', bg='#6495ED'))
        # keyboard press events **
        self.root.bind("<Return>", lambda e: self.enter_key())
        
        ##########

        # number 0 button
        self.btn_0 = tkinter.Button(self.third_btn_frame, text="0", width=9, font=("Arial", 16), bg="grey", fg="white") # command=lambda:self.key_0("0")
        self.btn_0.grid(row=1, column=0, sticky="n", padx=2, pady=2, columnspan=2)
        # simple fg and bg change when hovered over.
        self.btn_0.bind('<Enter>', lambda e: self.btn_0.config(fg='black', bg='lightgrey'))
        self.btn_0.bind('<Leave>', lambda e: self.btn_0.config(fg='white', bg='grey'))
        # keyboard press events **
        self.root.bind("0", lambda e: self.key_0("0"))

        # number dot button
        self.btn_dot = tkinter.Button(self.third_btn_frame, text=".", width=4, font=("Arial", 16), bg="grey", fg="white") # command=lambda:self.key_dot(".")
        self.btn_dot.grid(row=1, column=2, sticky="n", padx=2, pady=2)
        # simple fg and bg change when hovered over.
        self.btn_dot.bind('<Enter>', lambda e: self.btn_dot.config(fg='black', bg='lightgrey'))
        self.btn_dot.bind('<Leave>', lambda e: self.btn_dot.config(fg='white', bg='grey'))
        # keyboard press events **
        self.root.bind(".", lambda e: self.key_dot("."))

        # end of first pack standard calculations


        # start of second pack advanced calculations

        # second set of advanced calcuations
        self.second_pack = customtkinter.CTkFrame(self.root)
        self.second_pack.pack(side=LEFT, anchor="ne", padx=(15, 0), pady=(5, 0))


        #########################################
        # button frame
        self.second_set_cals_frame = customtkinter.CTkFrame(self.second_pack)
        self.second_set_cals_frame.pack(side=TOP, anchor='e', padx=(5, 0))


        # key press c button 
        self.btn_pi = tkinter.Button(self.second_set_cals_frame, text="π", width=4, font=("Arial", 16), bg="grey", fg="white") # command=self.c_key2
        self.btn_pi.grid(row=0, column=0, sticky="w", padx=2, pady=2)
        # simple fg and bg change when hovered over.
        self.btn_pi.bind('<Enter>', lambda e: self.btn_pi.config(fg='black', bg='lightgrey'))
        self.btn_pi.bind('<Leave>', lambda e: self.btn_pi.config(fg='white', bg='grey'))
        # keyboard press events **
        self.root.bind("p", lambda e: self.c_key("p")) # change to pi thing

        # end of first pack advanced calculations

        # menu
        my_menu = Menu(self.root)


        # create menu items
        file_menu = Menu(my_menu, tearoff=0, background='#303030', fg='white')
        my_menu.add_cascade(label="File", menu=file_menu)

        file_menu.add_command(label="Clear:", accelerator="C key ") # command=lambda:self.c_key(' ')

        file_menu.add_command(label="Errors", accelerator="H key") # command=lambda:self.errors_win("e")
        # self.root.bind("h", lambda e: self.errors_win(e))

        file_menu.add_command(label="Advanced", accelerator="A key") # command=lambda:self.advanced_option("0")
        self.root.bind("a", lambda e: self.advanced_option("1"))


        file_menu.add_separator()
        file_menu.add_command(label="Currency", accelerator="Ctrl+c")
        self.root.bind("<Control-c>", lambda e: self.currancy_exchange("1"))

        edit_menu = Menu(my_menu, tearoff=0, background='#303030', fg='white')
        my_menu.add_cascade(label="Edit", menu=edit_menu)
        edit_menu.add_command(label="Theme", accelerator="T key")
        edit_menu.add_command(label="Last Cal", accelerator="Z key")

        self.root.config(menu=my_menu)


        self.root.bind("a", lambda e: self.advanced_option("1"))
        # destorys the app if user presses escape key (convenience)
        self.root.bind("<Escape>", lambda e: self.root.destroy())
        # deleting stuff
        self.root.bind("<BackSpace>", lambda e: self.backspace_key())
        # stops the user from resizing the app
        self.root.resizable(False,False)


        self.root.mainloop()
    
    def advanced_option(self, e):
      self.root.geometry("570x340")
      self.root.title("Simple Calculator - Advanced")
      self.header_label.configure(text="Advanced")
      self.entry.configure(width=540)
      self.root.bind("r", lambda e: self.return_resize(e))

    def return_resize(self, e):
      self.root.geometry("280x340")
      self.root.title("Simple Calculator")
      self.header_label.configure(text="Standard")
      self.entry.configure(width=255)
   
    # Methods for the currancy exchange option
    def currancy_exchange(self, e):
      self.label_pack.pack_forget()
      self.entry_pack.pack_forget()
      self.first_pack.pack_forget()
      self.second_pack.pack_forget()

      self.root.title("Currency Exchange")
      self.root.geometry("280x340")
      self.entry.delete(0, END)
      


      # Currency Label Frame #
      self.currency_label_frame = customtkinter.CTkFrame(self.root)
      self.currency_label_frame.pack(side=TOP, anchor="w", padx=(15, 0), pady=(10, 0))
      # Currency Exchange Label #
      self.currency_label = customtkinter.CTkLabel(self.currency_label_frame, text="Currency Exchange", bg_color="#282828", height=0, width=0, text_font=("Arial", 14, "bold"))
      self.currency_label.pack()


      # input
      
      # Frame for the input stuff
      self.input_convert_frame = customtkinter.CTkFrame(self.root)
      self.input_convert_frame.pack(side=TOP, anchor="w", padx=(15, 0), pady=(10, 0))

      # The currency symbol for the input
      self.input_currency_symbol = customtkinter.CTkLabel(self.input_convert_frame, text="$", bg_color="#282828", height=0, width=0, text_font=("Arial", 16, "bold"))
      self.input_currency_symbol.grid(row=0, column=0)
      # The input entry
      self.input_currency_input = customtkinter.CTkEntry(self.input_convert_frame, width=170, bg_color="#282828")
      self.input_currency_input.grid(row=0, column=1)
      # The input currency selector (comboBox)
      self.currency_selector = customtkinter.CTkComboBox(self.input_convert_frame, values=list(exchanges.keys()), width=170, command=self.first_currency_selector_function)
      self.currency_selector.set(list(exchanges.keys())[0])
      self.currency_selector.grid(row=1, column=0, columnspan=2, sticky='e', pady=(3, 0))

      # end of input section

      
      # **********************************************
      

      # start of output section
      
      # Frame for the out stuff
      self.output_convert_frame = customtkinter.CTkFrame(self.root)
      self.output_convert_frame.pack(side=TOP, anchor="w", padx=(15, 0), pady=(10, 0))
      # The currency symbol for the output
      self.output_currency_symbol = customtkinter.CTkLabel(self.output_convert_frame, text="€", bg_color="#282828", height=0, width=0, text_font=("Arial", 16, "bold"))
      self.output_currency_symbol.grid(row=0, column=0)
      # The output entry
      self.output_currency_input = customtkinter.CTkEntry(self.output_convert_frame, width=170, bg_color="#282828", state="disabled")
      self.output_currency_input.grid(row=0, column=1)
      # The output currency selector (comboBox)
      self.currency_selector2 = customtkinter.CTkComboBox(self.output_convert_frame, values=list(exchanges.keys()), width=170, command=self.second_currency_selector_function)
      self.currency_selector2.set(list(exchanges.keys())[3])
      self.currency_selector2.grid(row=1, column=0, columnspan=2, sticky='e', pady=(3, 0))

      # end of output section

      # **************************************************************

      # start of conversion rates label section

      # Frame for the conversion rates labels and stuff
      self.conversion_rates_frame = customtkinter.CTkFrame(self.root)
      self.conversion_rates_frame.pack(side=TOP, anchor="w", padx=(15, 0), pady=(10, 0))
      # The conversion rates label
      self.conversion_rates_conversion_label = customtkinter.CTkLabel(self.conversion_rates_frame, text="1 USD = 0.98 EUR\nUpdated: 10/27/22", bg_color="#282828", text_font=("Arial", 10, "bold"))
      self.conversion_rates_conversion_label.grid(row=0, column=0)
      # The update rates button
      self.update_rates_button = customtkinter.CTkButton(self.conversion_rates_frame, text="Update Rates", height=0, width=0, command=self.update_rates_btn)
      self.update_rates_button.grid(row=1, column=0, pady=(2, 0))

      # end of conversion rates label section

      # ************************************************************

      # start of button stuff

      # frame of the buttons
      self.currency_exchange_buttons_frame = customtkinter.CTkFrame(self.root, fg_color="#333537")
      self.currency_exchange_buttons_frame.pack(side=TOP, anchor="w", padx=(15, 0), pady=(7, 0))
      
      self.first_exchange_set = customtkinter.CTkFrame(self.currency_exchange_buttons_frame, fg_color="#333537")
      self.first_exchange_set.pack(side=TOP, anchor='w', padx=(5, 0))


      self.ex_c_btn = tkinter.Button(self.first_exchange_set, text="C", width=4, font=("Arial", 16), bg="grey", fg="white") # command=self.c_key2
      self.ex_c_btn.grid(row=0, column=0, sticky="w", padx=2, pady=2)


      self.ex_c_btn.bind('<Enter>', lambda e: self.ex_c_btn.config(fg='black', bg='lightgrey'))
      self.ex_c_btn.bind('<Leave>', lambda e: self.ex_c_btn.config(fg='white', bg='grey'))


      self.root.bind("c", lambda e: self.c_key("c"))




      self.root.bind("r", lambda e: self.return_standard("0"))
      self.root.bind("a", lambda e: self.return_advanced("1"))


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

    # end of currency exchange methods



    # methods for buttons/keyboard events ********

    # method to add numbers via keyboard press event *
    def add_func(self, a):
        if len(self.entry.get()) == 0:
            self.entry.insert(0, a + " ")

        elif len(self.entry.get()) != 0:
            spce_add = len(self.entry.get()) + 1
            self.entry.insert(int(spce_add), " " + a + " ")

        else:
            self.entry.insert(END, a + " ")
    # method to add numbers via button click event *
    def add_func2(self, a):
        if len(self.entry.get()) == 0:
            self.entry.insert(0, a + " ")

        elif len(self.entry.get()) != 0:
            spce_add = len(self.entry.get()) + 1
            self.entry.insert(int(spce_add), " " + a + " ")

        else:
            self.entry.insert(END, a + " ")
    

    # method to clear entry input via keyboard presss event
    def c_key(self, a):
        self.entry.delete(0, END)
    # method to clear entry input via button click
    def c_key2(self):
        self.entry.delete(0, END)


    # method to enter entry value and calculate value via keyboard press event
    def enter_key(self):
        toBeCal = self.entry.get().split(" ")
        measured = len(toBeCal)

        # checks to see if the list contains the str version of the addition operator
        if toBeCal.count("+") and measured == 3:
            first_num = toBeCal[0]
            second_num = toBeCal[2]
            self.entry.delete(0, END)
            result = int(first_num) + int(second_num)
            self.entry.insert(0, result)


        # checks to see if the list contains the str version of the divison operator
        elif toBeCal.count("/") and measured == 3:
            first_num = toBeCal[0]
            second_num = toBeCal[2]
            self.entry.delete(0, END)
            if second_num == "0":
                self.entry.insert(0, "Error")
            else:
                result = int(first_num) // int(second_num)
                self.entry.insert(0, result)
        
        # checks to see if the list contains the str version of the multiplication operator
        elif toBeCal.count("*") and measured == 3:
            first_num = toBeCal[0]
            second_num = toBeCal[2]
            self.entry.delete(0, END)
            result = int(first_num) * int(second_num)
            self.entry.insert(0, result)

        # checks to see if the list contains the str version of the subtraction operator
        elif toBeCal.count("-") and measured == 3:
            first_num = toBeCal[0]
            second_num = toBeCal[2]
            self.entry.delete(0, END)
            result = int(first_num) - int(second_num)
            self.entry.insert(0, result)
        
        elif measured == 5:
            # what returns -> ['5', '+', '8', '*', '2']
            value_1 = toBeCal[0]
            value_2 = toBeCal[2]
            value_3 = toBeCal[4]

            op_value1 = toBeCal[1]
            op_value2 = toBeCal[3]


            # addition for int 3 values #
            if op_value1 == "+" and op_value2 == "+":
                result = int(value_1) + int(value_2) + int(value_3)
                self.entry.delete(0, END)
                self.entry.insert(0, result)

            elif op_value1 == "+" and op_value2 == "*":
                result = (int(value_1) + int(value_2)) * int(value_3)
                self.entry.delete(0, END)
                self.entry.insert(0, result)

            elif op_value1 == "+" and op_value2 == "/":

                if value_3 == "0":
                    self.entry.delete(0, END)
                    self.entry.insert(0, "Error 99")
                else:
                    result = (int(value_1) + int(value_2)) // int(value_3)
                    self.entry.delete(0, END)
                    self.entry.insert(0, result)

            elif op_value1 == "+" and op_value2 == "-":
                result = (int(value_1) + int(value_2)) - int(value_3)
                self.entry.delete(0, END)
                self.entry.insert(0, result)
            # end of addition 3 int results #


            # multiplication for int 3 values #
            if op_value1 == "*" and op_value2 == "+":
                result = (int(value_1) * int(value_2)) + int(value_3)
                self.entry.delete(0, END)
                self.entry.insert(0, result)

            elif op_value1 == "*" and op_value2 == "/":
                if value_3 == "0":
                    self.entry.delete(0, END)
                    self.entry.insert(0, "Error 99")
                else:
                    result = (int(value_1) * int(value_2)) // int(value_3)
                    self.entry.delete(0, END)
                    self.entry.insert(0, result)

            elif op_value1 == "*" and op_value2 == "*":
                result = (int(value_1) * int(value_2)) * int(value_3)
                self.entry.delete(0, END)
                self.entry.insert(0, result)

            elif op_value1 == "*" and op_value2 == "-":
                result = (int(value_1) * int(value_2)) - int(value_3)
                self.entry.delete(0, END)
                self.entry.insert(0, result)
            # end of multiplication 3 int results #


            # subtraction for int 3 values #
            if op_value1 == "-" and op_value2 == "+":
                result = (int(value_1) - int(value_2)) + int(value_3)
                self.entry.delete(0, END)
                self.entry.insert(0, result)

            elif op_value1 == "-" and op_value2 == "/":

                if value_3 == "0":
                    self.entry.delete(0, END)
                    self.entry.insert(0, "Error 99")
                else:
                    result = (int(value_1) - int(value_2)) // int(value_3)
                    self.entry.delete(0, END)
                    self.entry.insert(0, result)

            elif op_value1 == "-" and op_value2 == "*":
                result = (int(value_1) - int(value_2)) * int(value_3)
                self.entry.delete(0, END)
                self.entry.insert(0, result)

            elif op_value1 == "-" and op_value2 == "-":
                result = (int(value_1) - int(value_2)) - int(value_3)
                self.entry.delete(0, END)
                self.entry.insert(0, result)
            # end of subtraction 3 int results #
            

            # divsion for int 3 values #
            if op_value1 == "/" and op_value2 == "+":
                if value_2 == "0":
                    self.entry.delete(0, END)
                    self.entry.insert(0, "Error 99")
                else:
                    result = (int(value_1) // int(value_2)) + int(value_3)
                    self.entry.delete(0, END)
                    self.entry.insert(0, result)

            elif op_value1 == "/" and op_value2 == "/":
                if value_3 == "0":
                    self.entry.delete(0, END)
                    self.entry.insert(0, "Error 99")
                elif value_2 == "0":
                    self.entry.delete(0, END)
                    self.entry.insert(0, "Error 99")
                else:
                    result = (int(value_1) // int(value_2)) // int(value_3)
                    self.entry.delete(0, END)
                    self.entry.insert(0, result)

            elif op_value1 == "/" and op_value2 == "*":
                result = (int(value_1) // int(value_2)) * int(value_3)
                self.entry.delete(0, END)
                self.entry.insert(0, result)

            elif op_value1 == "/" and op_value2 == "-":
                result = (int(value_1) // int(value_2)) - int(value_3)
                self.entry.delete(0, END)
                self.entry.insert(0, result)
            # end of divsion 3 int results #

    # method to enter entry value and calculate value via button click
    def enter_key2(self):
        toBeCal = self.entry.get().split(" ")
        measured = len(toBeCal)

        # checks to see if the list contains the str version of the addition operator
        if toBeCal.count("+") and measured == 3:
            first_num = toBeCal[0]
            second_num = toBeCal[2]
            self.entry.delete(0, END)
            result = int(first_num) + int(second_num)
            self.entry.insert(0, result)


        # checks to see if the list contains the str version of the divison operator
        elif toBeCal.count("/") and measured == 3:
            first_num = toBeCal[0]
            second_num = toBeCal[2]
            self.entry.delete(0, END)
            if second_num == "0":
                self.entry.insert(0, "Error 99")
            else:
                result = int(first_num) // int(second_num)
                self.entry.insert(0, result)
        
        # checks to see if the list contains the str version of the multiplication operator
        elif toBeCal.count("*") and measured == 3:
            first_num = toBeCal[0]
            second_num = toBeCal[2]
            self.entry.delete(0, END)
            result = int(first_num) * int(second_num)
            self.entry.insert(0, result)

        # checks to see if the list contains the str version of the subtraction operator
        elif toBeCal.count("-") and measured == 3:
            first_num = toBeCal[0]
            second_num = toBeCal[2]
            self.entry.delete(0, END)
            result = int(first_num) - int(second_num)
            self.entry.insert(0, result)
        
        elif measured == 5:
            # what returns -> ['5', '+', '8', '*', '2'] example
            value_1 = toBeCal[0]
            value_2 = toBeCal[2]
            value_3 = toBeCal[4]

            op_value1 = toBeCal[1]
            op_value2 = toBeCal[3]


            # addition for int 3 values #
            if op_value1 == "+" and op_value2 == "+":
                result = int(value_1) + int(value_2) + int(value_3)
                self.entry.delete(0, END)
                self.entry.insert(0, result)

            elif op_value1 == "+" and op_value2 == "*":
                result = (int(value_1) + int(value_2)) * int(value_3)
                self.entry.delete(0, END)
                self.entry.insert(0, result)

            elif op_value1 == "+" and op_value2 == "/":

                if value_3 == "0":
                    self.entry.delete(0, END)
                    self.entry.insert(0, "Error 99")
                else:
                    result = (int(value_1) + int(value_2)) // int(value_3)
                    self.entry.delete(0, END)
                    self.entry.insert(0, result)

            elif op_value1 == "+" and op_value2 == "-":
                result = (int(value_1) + int(value_2)) - int(value_3)
                self.entry.delete(0, END)
                self.entry.insert(0, result)
            # end of addition 3 int results #


            # multiplication for int 3 values #
            if op_value1 == "*" and op_value2 == "+":
                result = (int(value_1) * int(value_2)) + int(value_3)
                self.entry.delete(0, END)
                self.entry.insert(0, result)

            elif op_value1 == "*" and op_value2 == "/":
                if value_3 == "0":
                    self.entry.delete(0, END)
                    self.entry.insert(0, "Error 99")
                else:
                    result = (int(value_1) * int(value_2)) // int(value_3)
                    self.entry.delete(0, END)
                    self.entry.insert(0, result)

            elif op_value1 == "*" and op_value2 == "*":
                result = (int(value_1) * int(value_2)) * int(value_3)
                self.entry.delete(0, END)
                self.entry.insert(0, result)

            elif op_value1 == "*" and op_value2 == "-":
                result = (int(value_1) * int(value_2)) - int(value_3)
                self.entry.delete(0, END)
                self.entry.insert(0, result)
            # end of multiplication 3 int results #


            # subtraction for int 3 values #
            if op_value1 == "-" and op_value2 == "+":
                result = (int(value_1) - int(value_2)) + int(value_3)
                self.entry.delete(0, END)
                self.entry.insert(0, result)

            elif op_value1 == "-" and op_value2 == "/":

                if value_3 == "0":
                    self.entry.delete(0, END)
                    self.entry.insert(0, "Error 99")
                else:
                    result = (int(value_1) - int(value_2)) // int(value_3)
                    self.entry.delete(0, END)
                    self.entry.insert(0, result)

            elif op_value1 == "-" and op_value2 == "*":
                result = (int(value_1) - int(value_2)) * int(value_3)
                self.entry.delete(0, END)
                self.entry.insert(0, result)

            elif op_value1 == "-" and op_value2 == "-":
                result = (int(value_1) - int(value_2)) - int(value_3)
                self.entry.delete(0, END)
                self.entry.insert(0, result)
            # end of subtraction 3 int results #
            

            # divsion for int 3 values #
            if op_value1 == "/" and op_value2 == "+":
                if value_2 == "0":
                    self.entry.delete(0, END)
                    self.entry.insert(0, "Error 99")
                else:
                    result = (int(value_1) // int(value_2)) + int(value_3)
                    self.entry.delete(0, END)
                    self.entry.insert(0, result)

            elif op_value1 == "/" and op_value2 == "/":
                if value_3 == "0":
                    self.entry.delete(0, END)
                    self.entry.insert(0, "Error 99")
                elif value_2 == "0":
                    self.entry.delete(0, END)
                    self.entry.insert(0, "Error 99")
                else:
                    result = (int(value_1) // int(value_2)) // int(value_3)
                    self.entry.delete(0, END)
                    self.entry.insert(0, result)

            elif op_value1 == "/" and op_value2 == "*":
                result = (int(value_1) // int(value_2)) * int(value_3)
                self.entry.delete(0, END)
                self.entry.insert(0, result)

            elif op_value1 == "/" and op_value2 == "-":
                result = (int(value_1) // int(value_2)) - int(value_3)
                self.entry.delete(0, END)
                self.entry.insert(0, result)
            # end of divsion 3 int results #
            

    # method to divide entry input via keyboard event #
    def div_func(self, a):
        if len(self.entry.get()) == 0:
            self.entry.insert(0, a + " ")

        elif len(self.entry.get()) != 0:
            spce_add = len(self.entry.get()) + 1
            self.entry.insert(int(spce_add), " " + a + " ")

        else:
            self.entry.insert(END, a + " ")

    # method to divide entry input via button click event #
    def div_func2(self, a):
        if len(self.entry.get()) == 0:
            self.entry.insert(0, a + " ")

        elif len(self.entry.get()) != 0:
            spce_add = len(self.entry.get()) + 1
            self.entry.insert(int(spce_add), " " + a + " ")

        else:
            self.entry.insert(END, a + " ")



    # method to multiply entry input via keyboard event #
    def mut_key(self, a):
        if len(self.entry.get()) == 0:
            self.entry.insert(0, a + " ")

        elif len(self.entry.get()) != 0:
            spce_add = len(self.entry.get()) + 1
            self.entry.insert(int(spce_add), " " + a + " ")

        else:
            self.entry.insert(END, a + " ")


    # method to multiply entry input via button click event #
    def mut_key2(self, a):
        if len(self.entry.get()) == 0:
            self.entry.insert(0, a + " ")

        elif len(self.entry.get()) != 0:
            spce_add = len(self.entry.get()) + 1
            self.entry.insert(int(spce_add), " " + a + " ")

        else:
            self.entry.insert(END, a + " ")




    # method to subtract entry input via keyboard event #
    def sub_key(self, a):
        if len(self.entry.get()) == 0:
            self.entry.insert(0, a + " ")

        elif len(self.entry.get()) != 0:
            spce_add = len(self.entry.get()) + 1
            self.entry.insert(int(spce_add), " " + a + " ")

        else:
            self.entry.insert(END, a + " ")

    # method to subtract entry input via button click event #
    def sub_key2(self, a):
        if len(self.entry.get()) == 0:
            self.entry.insert(0, a + " ")

        elif len(self.entry.get()) != 0:
            spce_add = len(self.entry.get()) + 1
            self.entry.insert(int(spce_add), " " + a + " ")

        else:
            self.entry.insert(END, a + " ")



    # method for keyboard press 7
    def key_7(self, a):
      if len(self.entry.get()) == 0:
         self.entry.insert(0, a)

      elif self.entry.get() == "NA":
         self.entry.delete(0, END)
         self.entry.insert(0, a)

      else:
         self.entry.insert(END, a)

    # method for button click 7
    def btn_click_7(self, a):
        if len(self.entry.get()) == 0:
            self.entry.insert(0, a)
        else:
            self.entry.insert(END, a)




    # method for keyboard press 8
    def key_8(self, a):
      if len(self.entry.get()) == 0:
         self.entry.insert(0, a)

      elif self.entry.get() == "NA":
         self.entry.delete(0, END)
         self.entry.insert(0, a)

      else:
         self.entry.insert(END, a)

    # method for button click 8
    def btn_click_8(self, a):
        if len(self.entry.get()) == 0:
            self.entry.insert(0, a)
        else:
            self.entry.insert(END, a)



    # method for keyboard press 9
    def key_9(self, a):
        if len(self.entry.get()) == 0:
            self.entry.insert(0, a)

        elif self.entry.get() == "NA":
            self.entry.delete(0, END)
            self.entry.insert(0, a)

        else:
            self.entry.insert(END, a)

    # method for button click 9
    def btn_click_9(self, a):
        if len(self.entry.get()) == 0:
            self.entry.insert(0, a)
        else:
            self.entry.insert(END, a)



    # method for keyboard press 4
    def key_4(self, a):
        if len(self.entry.get()) == 0:
            self.entry.insert(0, a)

        elif self.entry.get() == "NA":
            self.entry.delete(0, END)
            self.entry.insert(0, a)

        else:
            self.entry.insert(END, a)

    # method for button click 4
    def btn_click_4(self, a):
        if len(self.entry.get()) == 0:
            self.entry.insert(0, a)
        else:
            self.entry.insert(END, a)





    # method for keyboard press 5
    def key_5(self, a):
        if len(self.entry.get()) == 0:
            self.entry.insert(0, a)

        elif self.entry.get() == "NA":
            self.entry.delete(0, END)
            self.entry.insert(0, a)

        else:
            self.entry.insert(END, a)

    # method for button click 5
    def btn_click_5(self, a):
        if len(self.entry.get()) == 0:
            self.entry.insert(0, a)
        else:
            self.entry.insert(END, a)



    # method for keyboard press 6
    def key_6(self, a):
        if len(self.entry.get()) == 0:
            self.entry.insert(0, a)

        elif self.entry.get() == "NA":
            self.entry.delete(0, END)
            self.entry.insert(0, a)

        else:
            self.entry.insert(END, a)

    # method for button click 6
    def btn_click_6(self, a):
        if len(self.entry.get()) == 0:
            self.entry.insert(0, a)
        else:
            self.entry.insert(END, a)



    # method for keyboard press 1
    def key_1(self, a):
        if len(self.entry.get()) == 0:
            self.entry.insert(0, a)

        elif self.entry.get() == "NA":
            self.entry.delete(0, END)
            self.entry.insert(0, a)

        else:
            self.entry.insert(END, a)

    # method for button click 1
    def btn_click_1(self, a):
        if len(self.entry.get()) == 0:
            self.entry.insert(0, a)
        else:
            self.entry.insert(END, a)



    # method for keyboard press 2
    def key_2(self, a):
        if len(self.entry.get()) == 0:
            self.entry.insert(0, a)

        elif self.entry.get() == "NA":
            self.entry.delete(0, END)
            self.entry.insert(0, a)

        else:
            self.entry.insert(END, a)

    # method for button click 2
    def btn_click_2(self, a):
        if len(self.entry.get()) == 0:
            self.entry.insert(0, a)
        else:
            self.entry.insert(END, a)



    # method for keyboard press 3
    def key_3(self, a):
        if len(self.entry.get()) == 0:
            self.entry.insert(0, a)

        elif self.entry.get() == "NA":
            self.entry.delete(0, END)
            self.entry.insert(0, a)

        else:
            self.entry.insert(END, a)

    # method for button click 3
    def btn_click_3(self, a):
        if len(self.entry.get()) == 0:
            self.entry.insert(0, a)
        else:
            self.entry.insert(END, a)



    # method for keyboard press 0
    def key_0(self, a):
        if len(self.entry.get()) == 0:
            self.entry.insert(0, a)

        elif self.entry.get() == "NA":
            self.entry.delete(0, END)
            self.entry.insert(0, a)

        else:
            self.entry.insert(END, a)

    # method for button click 0
    def btn_click_0(self, a):
        if len(self.entry.get()) == 0:
            self.entry.insert(0, a)
        else:
            self.entry.insert(END, a)



    # method for keyboard press dot
    def key_dot(self, a):
        if len(self.entry.get()) == 0:
            self.entry.insert(0, a)

        elif self.entry.get() == "NA":
            self.entry.delete(0, END)
            self.entry.insert(0, a)

        else:
            self.entry.insert(END, a)

    # method for button click dot
    def btn_click_dot(self, a):
        if len(self.entry.get()) == 0:
            self.entry.insert(0, a)
        else:
            self.entry.insert(END, a)
    

    def backspace_key(self):
        if len(self.entry.get()) != 0:
            get_input = self.entry.get()
            length = len(get_input)
            last_char = length - 1
            self.entry.delete(last_char, END)
        else:
            self.entry.insert(0, "NA")
            
    #### methods for the menu commands ####



    # method for the command for opening up errors window
    def errors_win(self, e):
        self.window = customtkinter.CTkToplevel()
        self.window.title("Calculator Errors")
        self.window.iconbitmap("darkModeV.ico")
        self.window.geometry("280x360") # L x H

        # main frame that holds all the errors
        self.error99_frame = customtkinter.CTkFrame(self.window)
        self.error99_frame.pack(pady=10)

        # error code 99 label and desciption
        # error label
        self.error_99_label = customtkinter.CTkLabel(self.error99_frame, 
            text="Error 99:", 
            text_font=("Arial", 10), 
            height=0, 
            width=0, 
            text_color="white")
        self.error_99_label.grid(row=0, column=0, pady=(5, 0))
        # error desciption
        self.error_99_desciption = customtkinter.CTkLabel(self.error99_frame,
            text="Cannot Divide by Zero:", 
            text_font=("Arial", 10), 
            height=0, 
            width=0, 
            text_color="white")
        self.error_99_desciption.grid(row=1, column=0, pady=(0, 7))


        # create another frame with error code


        # error code 99 label and desciption
        # error label
        # self.error_99_label = customtkinter.CTkLabel(self.errors_frame, 
        #     text="Error 99:", 
        #     text_font=("Arial", 10), 
        #     height=0, 
        #     width=0, 
        #     text_color="white")
        # self.error_99_label.grid(row=0, column=0, pady=(5, 0))
        # # error desciption
        # self.error_99_desciption = customtkinter.CTkLabel(self.errors_frame,
        #     text="Cannot divide by zero:", 
        #     text_font=("Arial", 10), 
        #     height=0, 
        #     width=0, 
        #     text_color="white")
        # self.error_99_desciption.grid(row=1, column=0, pady=(0, 7))




        # destorys the app if user presses escape key (convenience)
        self.window.bind("<Escape>", lambda e: self.window.destroy())


    # method for the command for swiching to the advanced option
    def advanced_option(self, e):
        self.root.geometry("600x340") # L x H
        self.root.title("Simple Calculator - Advanced")
        self.header_label.configure(text="Advanced")
        self.entry.configure(width=570)
        self.advanced_frame.pack(side=LEFT, anchor='e')
        self.hopeful.pack(side=TOP, anchor='ne')




        self.root.bind("r", lambda e: self.return_resize(e))

    
    def return_resize(self, e):
        self.root.geometry("280x340")
        self.entry.configure(width=245)
        self.root.title("Simple Calculator")
        self.header_label.configure(text="Standard")
        self.advanced_frame.pack_forget()
        self.hopeful.pack_forget()





app = App()