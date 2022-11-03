import customtkinter
import tkinter
from tkinter import *
from currency_exchanges import exchanges, currency_symbols
import os
import tkinter.ttk as ttk
import datetime
from datetime import datetime
import requests


class App:
    def __init__(self):
        self.root = customtkinter.CTk()
        self.root.title("Calculator")
        self.root.iconbitmap("darkModeV.ico")
        self.root.geometry("280x340") # L x H change back to 270 or 280?
        self.root.config(background="#282828")

        # label here
        self.label_pack = customtkinter.CTkFrame(self.root, fg_color='#282828')
        self.label_pack.pack(side=TOP, anchor="w", padx=(15, 0), pady=(10, 0))

        self.header_label = customtkinter.CTkLabel(self.label_pack, text="Standard", bg_color="#282828", height=0, width=0, text_font=("Arial", 14, "bold"))
        self.header_label.pack() # pady=(top, bottom) padx=(left, right) in px


        # entry box here
        self.entry_pack = customtkinter.CTkFrame(self.root, fg_color='#282828')
        self.entry_pack.pack(side=TOP, anchor="w", padx=(15, 0))

        # entry box widget
        self.entry = customtkinter.CTkEntry(self.entry_pack, text_font=("Arial", 26), width=255, height=44)
        self.entry.grid(row=1, column=0, columnspan=3)


        # first set of standard calculator buttons
        self.first_pack = customtkinter.CTkFrame(self.root, fg_color='#282828')
        self.first_pack.pack(side=LEFT, anchor="nw", padx=(15, 0), pady=(5, 0))


        #########################################
        # button frame
        self.first_set_cals_frame = customtkinter.CTkFrame(self.first_pack, fg_color='#282828')
        self.first_set_cals_frame.pack(side=TOP, anchor='w', padx=(5, 0))

        # key press c button 
        self.c_btn = tkinter.Button(self.first_set_cals_frame, text="C", width=4, font=("Arial", 16), bg="#404040", fg="white", relief='flat') # command=self.c_key2
        self.c_btn.grid(row=0, column=0, sticky="w", padx=2, pady=2)
        # simple fg and bg change when hovered over.
        self.c_btn.bind('<Enter>', lambda e: self.c_btn.config(fg='black', bg='#4D4D4D'))
        self.c_btn.bind('<Leave>', lambda e: self.c_btn.config(fg='white', bg='#404040'))
        # keyboard press events **
        self.root.bind("c", lambda e: self.c_key("c"))



        # number / button
        self.btn_div = tkinter.Button(self.first_set_cals_frame, text="/", width=4, font=("Arial", 16), bg="#404040", fg="white", relief='flat') # command=lambda:self.div_func2("/")
        self.btn_div.grid(row=0, column=1, sticky="w", padx=2, pady=2)
        # simple fg and bg change when hovered over.
        self.btn_div.bind('<Enter>', lambda e: self.btn_div.config(fg='black', bg='#4D4D4D'))
        self.btn_div.bind('<Leave>', lambda e: self.btn_div.config(fg='white', bg='#404040'))
        # keyboard press events **
        self.root.bind("/", lambda e: self.div_func("/"))


        # number * button
        self.btn_mut = tkinter.Button(self.first_set_cals_frame, text="*", width=4, font=("Arial", 16), bg="#404040", fg="white", relief='flat') # command=lambda:self.mut_key2("*")
        self.btn_mut.grid(row=0, column=2, sticky="w", padx=2, pady=2)
        # simple fg and bg change when hovered over.
        self.btn_mut.bind('<Enter>', lambda e: self.btn_mut.config(fg='black', bg='#4D4D4D'))
        self.btn_mut.bind('<Leave>', lambda e: self.btn_mut.config(fg='white', bg='#404040'))
        # keyboard press events **
        self.root.bind("*", lambda e: self.mut_key("*"))


        # number - button
        self.btn_sub = tkinter.Button(self.first_set_cals_frame, text="-", width=4, font=("Arial", 16), bg="#404040", fg="white", relief='flat') # command=lambda:self.sub_key2("-")
        self.btn_sub.grid(row=0, column=3, sticky="w", padx=2, pady=2)
        # simple fg and bg change when hovered over.
        self.btn_sub.bind('<Enter>', lambda e: self.btn_sub.config(fg='black', bg='#4D4D4D'))
        self.btn_sub.bind('<Leave>', lambda e: self.btn_sub.config(fg='white', bg='#404040'))
        # keyboard press events **
        self.root.bind("-", lambda e: self.sub_key("-"))



        # second button frame #################################################################################

        self.second_btn_frame = customtkinter.CTkFrame(self.first_pack, fg_color='#282828')
        self.second_btn_frame.pack(side=TOP, anchor='w', padx=(5, 0))
        
        # number 7 button
        self.btn_7 = tkinter.Button(self.second_btn_frame, text="7", width=4, font=("Arial", 16), bg="#404040", fg="white", relief='flat', command=lambda:self.btn_click_7("7"))
        self.btn_7.grid(row=0, column=0, sticky="n", padx=2, pady=2)
        # simple fg and bg change when hovered over.
        self.btn_7.bind('<Enter>', lambda e: self.btn_7.config(fg='black', bg='#4D4D4D'))
        self.btn_7.bind('<Leave>', lambda e: self.btn_7.config(fg='white', bg='#404040'))
        # keyboard press events **
        self.root.bind("7", lambda e: self.key_7("7"))



        # number 8 button
        self.btn_8 = tkinter.Button(self.second_btn_frame, text="8", width=4, font=("Arial", 16), bg="#404040", fg="white", relief='flat') # command=lambda:self.key_8("8")
        self.btn_8.grid(row=0, column=1, sticky="n", padx=2, pady=2)
        # simple fg and bg change when hovered over.
        self.btn_8.bind('<Enter>', lambda e: self.btn_8.config(fg='black', bg='#4D4D4D'))
        self.btn_8.bind('<Leave>', lambda e: self.btn_8.config(fg='white', bg='#404040'))
        # keyboard press events **
        self.root.bind("8", lambda e: self.key_8("8"))



        # number 9 button
        self.btn_9 = tkinter.Button(self.second_btn_frame, text="9", width=4, font=("Arial", 16), bg="#404040", fg="white", relief='flat') # command=lambda:self.key_9("9")
        self.btn_9.grid(row=0, column=2, sticky="n", padx=2, pady=2)
        # simple fg and bg change when hovered over.
        self.btn_9.bind('<Enter>', lambda e: self.btn_9.config(fg='black', bg='#4D4D4D'))
        self.btn_9.bind('<Leave>', lambda e: self.btn_9.config(fg='white', bg='#404040'))
        # keyboard press events **
        self.root.bind("9", lambda e: self.key_9("9"))


        # number add button
        self.btn_add = tkinter.Button(self.second_btn_frame, text="+", width=4, font=("Arial", 16), bg="#404040", fg="white", height=3, relief='flat') # command=lambda:self.add_func2("+")
        self.btn_add.grid(row=0, column=3, padx=2, pady=2, rowspan=2)
        # simple fg and bg change when hovered over.
        self.btn_add.bind('<Enter>', lambda e: self.btn_add.config(fg='black', bg='#4D4D4D'))
        self.btn_add.bind('<Leave>', lambda e: self.btn_add.config(fg='white', bg='#404040'))
        # keyboard press events **
        self.root.bind("+", lambda e: self.add_func("+"))
        
        ##########

        # number 4 button
        self.btn_4 = tkinter.Button(self.second_btn_frame, text="4", width=4, font=("Arial", 16), bg="#404040", fg="white", relief='flat') # command=lambda:self.key_4("4")
        self.btn_4.grid(row=1, column=0, sticky="n", padx=2, pady=2)
        # simple fg and bg change when hovered over.
        self.btn_4.bind('<Enter>', lambda e: self.btn_4.config(fg='black', bg='#4D4D4D'))
        self.btn_4.bind('<Leave>', lambda e: self.btn_4.config(fg='white', bg='#404040'))
        # keyboard press events **
        self.root.bind("4", lambda e: self.key_4("4"))



        # number 5 button
        self.btn_5 = tkinter.Button(self.second_btn_frame, text="5", width=4, font=("Arial", 16), bg="#404040", fg="white", relief='flat') # command=lambda:self.key_5("5")
        self.btn_5.grid(row=1, column=1, sticky="n", padx=2, pady=2)
        # simple fg and bg change when hovered over.
        self.btn_5.bind('<Enter>', lambda e: self.btn_5.config(fg='black', bg='#4D4D4D'))
        self.btn_5.bind('<Leave>', lambda e: self.btn_5.config(fg='white', bg='#404040'))
        # keyboard press events **
        self.root.bind("5", lambda e: self.key_5("5"))


        # number 6 button
        self.btn_6 = tkinter.Button(self.second_btn_frame, text="6", width=4, font=("Arial", 16), bg="#404040", fg="white", relief='flat') # command=lambda:self.key_6("6")
        self.btn_6.grid(row=1, column=2, sticky="n", padx=2, pady=2)
        # simple fg and bg change when hovered over.
        self.btn_6.bind('<Enter>', lambda e: self.btn_6.config(fg='black', bg='#4D4D4D'))
        self.btn_6.bind('<Leave>', lambda e: self.btn_6.config(fg='white', bg='#404040'))
        # keyboard press events **
        self.root.bind("6", lambda e: self.key_6("6"))

      
        # third button frame #############################################################
        self.third_btn_frame = customtkinter.CTkFrame(self.first_pack, fg_color='#282828')
        self.third_btn_frame.pack(side=TOP, anchor='w', padx=(5, 0))

        
        # number 1 button
        self.btn_1 = tkinter.Button(self.third_btn_frame, text="1", width=4, font=("Arial", 16), bg="#404040", fg="white", relief='flat') # command=lambda:self.key_1("1")
        self.btn_1.grid(row=0, column=0, sticky="n", padx=2, pady=2)
        # simple fg and bg change when hovered over.
        self.btn_1.bind('<Enter>', lambda e: self.btn_1.config(fg='black', bg='#4D4D4D'))
        self.btn_1.bind('<Leave>', lambda e: self.btn_1.config(fg='white', bg='#404040'))
        # keyboard press events **
        self.root.bind("1", lambda e: self.key_1("1"))


        # number 2 button
        self.btn_2 = tkinter.Button(self.third_btn_frame, text="2", width=4, font=("Arial", 16), bg="#404040", fg="white", relief='flat') # command=lambda:self.key_2("2")
        self.btn_2.grid(row=0, column=1, sticky="n", padx=2, pady=2)
        # simple fg and bg change when hovered over.
        self.btn_2.bind('<Enter>', lambda e: self.btn_2.config(fg='black', bg='#4D4D4D'))
        self.btn_2.bind('<Leave>', lambda e: self.btn_2.config(fg='white', bg='#404040'))
        # keyboard press events **
        self.root.bind("2", lambda e: self.key_2("2"))


        # number 3 button
        self.btn_3 = tkinter.Button(self.third_btn_frame, text="3", width=4, font=("Arial", 16), bg="#404040", fg="white", relief='flat') # command=lambda:self.key_3("3")
        self.btn_3.grid(row=0, column=2, sticky="n", padx=2, pady=2)
        # simple fg and bg change when hovered over.
        self.btn_3.bind('<Enter>', lambda e: self.btn_3.config(fg='black', bg='#4D4D4D'))
        self.btn_3.bind('<Leave>', lambda e: self.btn_3.config(fg='white', bg='#404040'))
        # keyboard press events **
        self.root.bind("3", lambda e: self.key_3("3"))


        # number enter button
        self.btn_en = tkinter.Button(self.third_btn_frame, text="Enter", width=4, font=("Arial", 16), bg="#3D59AB", fg="white", height=3, relief='flat') # command=self.enter_key2
        self.btn_en.grid(row=0, column=3, padx=2, pady=2, rowspan=2)
        # simple fg and bg change when hovered over.
        self.btn_en.bind('<Enter>', lambda e: self.btn_en.config(fg='black', bg='#104E8B'))
        self.btn_en.bind('<Leave>', lambda e: self.btn_en.config(fg='white', bg='#3D59AB'))
        # keyboard press events **
        self.root.bind("<Return>", lambda e: self.enter_key())
        
        ##########

        # number 0 button
        self.btn_0 = tkinter.Button(self.third_btn_frame, text="0", width=9, font=("Arial", 16), bg="#404040", fg="white", relief='flat', command=lambda:self.key_0("0"))
        self.btn_0.grid(row=1, column=0, sticky="n", padx=2, pady=2, columnspan=2)
        # simple fg and bg change when hovered over.
        self.btn_0.bind('<Enter>', lambda e: self.btn_0.config(fg='black', bg='#4D4D4D'))
        self.btn_0.bind('<Leave>', lambda e: self.btn_0.config(fg='white', bg='#404040'))
        # keyboard press events **
        self.root.bind("0", lambda e: self.key_0("0"))

        # number dot button
        self.btn_dot = tkinter.Button(self.third_btn_frame, text=".", width=4, font=("Arial", 16), bg="#404040", fg="white", relief='flat') # command=lambda:self.key_dot(".")
        self.btn_dot.grid(row=1, column=2, sticky="n", padx=2, pady=2)
        # simple fg and bg change when hovered over.
        self.btn_dot.bind('<Enter>', lambda e: self.btn_dot.config(fg='black', bg='#4D4D4D'))
        self.btn_dot.bind('<Leave>', lambda e: self.btn_dot.config(fg='white', bg='#404040'))
        # keyboard press events **
        self.root.bind(".", lambda e: self.key_dot("."))

        # end of first pack standard calculations

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

        # destorys the app if user presses escape key (convenience)
        self.root.bind("<Escape>", lambda e: self.root.destroy())
        # deleting stuff
        self.root.bind("<BackSpace>", lambda e: self.backspace_key())
        # stops the user from resizing the app
        self.root.resizable(False,False)


        self.root.mainloop()
    

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
        self.root.geometry("280x550")
        self.entry.delete(0, END)
        
        
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
        self.btn_8 = tkinter.Button(self.second_exchange_set, text="8", width=6, font=("Arial", 16), bg="#404040", fg="white", relief='flat', command=lambda: self.exchange_8_btn("8"))
        self.btn_8.grid(row=0, column=1, sticky="n", padx=2, pady=2)
        # simple fg and bg change when hovered over.
        self.btn_8.bind('<Enter>', lambda e: self.btn_8.config(fg='black', bg='#4D4D4D'))
        self.btn_8.bind('<Leave>', lambda e: self.btn_8.config(fg='white', bg='#404040'))
        # keyboard press events **
        self.root.bind("8", lambda e: self.exchange_8_btn("8"))


        # number 9 button
        self.btn_9 = tkinter.Button(self.second_exchange_set, text="9", width=6, font=("Arial", 16), bg="#404040", fg="white", relief='flat', command=lambda: self.exchange_9_btn("9"))
        self.btn_9.grid(row=0, column=2, sticky="n", padx=2, pady=2)
        # simple fg and bg change when hovered over.
        self.btn_9.bind('<Enter>', lambda e: self.btn_9.config(fg='black', bg='#4D4D4D'))
        self.btn_9.bind('<Leave>', lambda e: self.btn_9.config(fg='white', bg='#404040'))
        # keyboard press events **
        self.root.bind("9", lambda e: self.exchange_9_btn("9"))  



        # third button frame
        self.third_exchange_set = customtkinter.CTkFrame(self.currency_exchange_buttons_frame)
        self.third_exchange_set.grid(row=2, column=0, sticky='e')
        
        # number 4 button
        self.btn_4 = tkinter.Button(self.third_exchange_set, text="4", width=6, font=("Arial", 16), bg="#404040", fg="white", relief='flat', command=lambda:self.exchange_4_btn("4"))
        self.btn_4.grid(row=1, column=0, sticky="n", padx=2, pady=2)
        # simple fg and bg change when hovered over.
        self.btn_4.bind('<Enter>', lambda e: self.btn_4.config(fg='black', bg='#4D4D4D'))
        self.btn_4.bind('<Leave>', lambda e: self.btn_4.config(fg='white', bg='#404040'))
        # keyboard press events **
        self.root.bind("4", lambda e: self.exchange_4_btn("4"))


        # number 5 button
        self.btn_5 = tkinter.Button(self.third_exchange_set, text="5", width=6, font=("Arial", 16), bg="#404040", fg="white", relief='flat', command=lambda:self.exchange_5_btn("5"))
        self.btn_5.grid(row=1, column=1, sticky="n", padx=2, pady=2)
        # simple fg and bg change when hovered over.
        self.btn_5.bind('<Enter>', lambda e: self.btn_5.config(fg='black', bg='#4D4D4D'))
        self.btn_5.bind('<Leave>', lambda e: self.btn_5.config(fg='white', bg='#404040'))
        # keyboard press events **
        self.root.bind("5", lambda e: self.exchange_5_btn("5"))


        # number 6 button
        self.btn_6 = tkinter.Button(self.third_exchange_set, text="6", width=6, font=("Arial", 16), bg="#404040", fg="white", relief='flat', command=lambda:self.exchange_6_btn("6"))
        self.btn_6.grid(row=1, column=2, sticky="n", padx=2, pady=2)
        # simple fg and bg change when hovered over.
        self.btn_6.bind('<Enter>', lambda e: self.btn_6.config(fg='black', bg='#4D4D4D'))
        self.btn_6.bind('<Leave>', lambda e: self.btn_6.config(fg='white', bg='#404040'))
        # keyboard press events **
        self.root.bind("6", lambda e: self.exchange_6_btn("6"))



        # fourth button frame
        self.fourth_exchange_set = customtkinter.CTkFrame(self.currency_exchange_buttons_frame)
        self.fourth_exchange_set.grid(row=3, column=0, sticky='e')
        

        # number 1 button
        self.btn_1 = tkinter.Button(self.fourth_exchange_set, text="1", width=6, font=("Arial", 16), bg="#404040", fg="white", relief='flat', command=lambda:self.exchange_1_btn("1"))
        # simple fg and bg change when hovered over.
        self.btn_1.bind('<Enter>', lambda e: self.btn_1.config(fg='black', bg='#4D4D4D'))
        self.btn_1.bind('<Leave>', lambda e: self.btn_1.config(fg='white', bg='#404040'))
        # keyboard press events **
        self.root.bind("1", lambda e: self.exchange_1_btn("1"))


        # number 2 button
        self.btn_2 = tkinter.Button(self.fourth_exchange_set, text="2", width=6, font=("Arial", 16), bg="#404040", fg="white", relief='flat', command=lambda:self.exchange_2_btn("2"))
        self.btn_2.grid(row=0, column=1, sticky="n", padx=2, pady=2)
        # simple fg and bg change when hovered over.
        self.btn_2.bind('<Enter>', lambda e: self.btn_2.config(fg='black', bg='#4D4D4D'))
        self.btn_2.bind('<Leave>', lambda e: self.btn_2.config(fg='white', bg='#404040'))
        # keyboard press events **
        self.root.bind("2", lambda e: self.exchange_2_btn("2"))


        # number 3 button
        self.btn_3 = tkinter.Button(self.fourth_exchange_set, text="3", width=6, font=("Arial", 16), bg="#404040", fg="white", relief='flat', command=lambda:self.exchange_3_btn("3"))
        self.btn_3.grid(row=0, column=2, sticky="n", padx=2, pady=2)
        # simple fg and bg change when hovered over.
        self.btn_3.bind('<Enter>', lambda e: self.btn_3.config(fg='black', bg='#4D4D4D'))
        self.btn_3.bind('<Leave>', lambda e: self.btn_3.config(fg='white', bg='#404040'))
        # keyboard press events **
        self.root.bind("3", lambda e: self.exchange_3_btn("3"))


        # fifth button frame
        self.fifth_exchange_set = customtkinter.CTkFrame(self.currency_exchange_buttons_frame)
        self.fifth_exchange_set.grid(row=4, column=0, sticky='e')

        # number 0 button
        self.btn_0 = tkinter.Button(self.fifth_exchange_set, text="0", width=6, font=("Arial", 16), bg="#404040", fg="white", relief='flat', command=lambda: self.exchange_0_btn("0"))
        self.btn_0.grid(row=1, column=0, sticky="n", padx=2, pady=2)
        # simple fg and bg change when hovered over.
        self.btn_0.bind('<Enter>', lambda e: self.btn_0.config(fg='black', bg='#4D4D4D'))
        self.btn_0.bind('<Leave>', lambda e: self.btn_0.config(fg='white', bg='#404040'))
        # keyboard press events **
        self.root.bind("0", lambda e: self.exchange_0_btn("0"))

        # number dot button
        self.btn_dot = tkinter.Button(self.fifth_exchange_set, text=".", width=6, font=("Arial", 16), bg="#404040", fg="white", relief='flat', state='disabled')
        self.btn_dot.grid(row=1, column=2, sticky="n", padx=2, pady=2)



        self.last_exchange_frame = customtkinter.CTkFrame(self.root)
        self.last_exchange_frame.pack(side=BOTTOM)

        self.powered_by_api = customtkinter.CTkLabel(self.last_exchange_frame, text="Powered by ExchangeRate API", text_font=("Arial", 7), width=0, height=0, fg_color="#282828")
        self.powered_by_api.pack()


        self.root.bind("r", lambda e: self.return_standard("0"))
        self.root.bind("a", lambda e: self.return_advanced("1"))
        self.root.resizable(False,False)


    # Method for returning to standard, currency exchange to standard
    def return_standard(self, e):
        self.currency_label_frame.pack_forget()
        self.input_convert_frame.pack_forget()
        self.output_convert_frame.pack_forget()
        self.conversion_rates_frame.pack_forget()
        self.currency_exchange_buttons_frame.pack_forget()
        self.last_exchange_frame.pack_forget()
        self.input_currency_input.grid_forget()

        self.root.title("Calculator")
        self.root.geometry('280x340')

        self.label_pack.pack(side=TOP, anchor="w", padx=(15, 0), pady=(10, 0))
        self.entry_pack.pack(side=TOP, anchor="w", padx=(15, 0))
        self.first_pack.pack(side=LEFT, anchor="nw", padx=(15, 0), pady=(5, 0))
        self.second_pack.pack(side=LEFT, anchor="ne", padx=(15, 0), pady=(5, 0))
        self.root.bind("1", lambda e: self.key_1("1"))
        self.root.bind("2", lambda e: self.key_2("2"))
        self.root.bind("3", lambda e: self.key_3("3"))
        self.root.bind("4", lambda e: self.key_4("4"))
        self.root.bind("5", lambda e: self.key_5("5"))
        self.root.bind("6", lambda e: self.key_6("6"))
        self.root.bind("7", lambda e: self.key_7("7"))
        self.root.bind("8", lambda e: self.key_8("8"))
        self.root.bind("9", lambda e: self.key_9("9"))
        self.root.bind("0", lambda e: self.key_0("0"))
        self.root.bind("c", lambda e: self.c_key("c"))


    # method for putting out currency symbols
    def first_currency_selector_function(self, selected):
        """Method that gets the first ComboBox value

        Args:
            selected (None): None
        """
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
        
        self.update_current_value = self.input_zero_base.get()
        
        if self.update_current_value == "0":
            pass
        elif self.update_current_value != "0":
            self.value1 = self.input_zero_base.get() # number that is in the first label
            self.value2 = self.output_zero_base.get() # number that is in the second label
            
            self.label_thing = self.converion[self.get_currency_code] # = 1
            self.label_thing2 = self.converion[self.get_currency_code2] # 0.99
            
            self.update_calculate = int(self.value1) * float(self.label_thing2)
            self.update_calculate_split = str(self.update_calculate).split(".")
            self.update_calculate_index = self.update_calculate_split[1]
            
            if len(self.update_calculate_index) <= 4:
                self.update_cal_del = str(self.update_calculate)
                self.output_zero_base.set(value=self.update_cal_del)
                
            elif len(self.update_calculate_index) > 4:
                self.number_del = len(self.update_calculate_index) - 2
                self.number_del2 = str(self.update_calculate)[:-self.number_del]
                self.output_zero_base.set(value=str(self.number_del2))
                

    # method for putting out currency symbols
    def second_currency_selector_function(self, selected):
        """Method that gets the second ComboBox value

        Args:
            selected (None): None
        """
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
        self.root.title("Calculator - Advanced")
        self.root.geometry("570x340")
        
        self.currency_label_frame.pack_forget()
        self.input_convert_frame.pack_forget()
        self.output_convert_frame.pack_forget()
        self.conversion_rates_frame.pack_forget()
        self.currency_exchange_buttons_frame.pack_forget()
        self.last_exchange_frame.pack_forget()

        self.label_pack.pack(side=TOP, anchor="w", padx=(15, 0), pady=(10, 0))
        self.entry_pack.pack(side=TOP, anchor="w", padx=(15, 0))
        self.first_pack.pack(side=LEFT, anchor="nw", padx=(15, 0), pady=(5, 0))
        self.second_pack.pack(side=LEFT, anchor="ne", padx=(15, 0), pady=(5, 0))
        self.root.bind("1", lambda e: self.key_1("1"))
        self.root.bind("2", lambda e: self.key_2("2"))
        self.root.bind("3", lambda e: self.key_3("3"))
        self.root.bind("4", lambda e: self.key_4("4"))
        self.root.bind("5", lambda e: self.key_5("5"))
        self.root.bind("6", lambda e: self.key_6("6"))
        self.root.bind("7", lambda e: self.key_7("7"))
        self.root.bind("8", lambda e: self.key_8("8"))
        self.root.bind("9", lambda e: self.key_9("9"))
        self.root.bind("0", lambda e: self.key_0("0"))
        self.root.bind("c", lambda e: self.c_key("c"))


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
        

  # exchange button for number 1
    def exchange_1_btn(self, e):
        """Method for when the user presses 1 key instead of clicking button"""
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
            self.input_zero_base.set(value='1') # sets of value of label to 9

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
                self.output_zero_base.set(value=str(self.final_value))
            elif len(self.return_value) <= 4:
                self.output_zero_base.set(value=str(self.calculate))


        elif self.thing != "0":
            self.new_value = self.input_zero_base.get()
            self.input_zero_base.set(self.thing + "1")
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


 # exchange button for number 1
    def exchange_2_btn(self, e):
        """Method for when the user presses 2 key instead of clicking button"""
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
            self.input_zero_base.set(value='2') # sets of value of label to 9

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
                self.output_zero_base.set(value=str(self.final_value))
            elif len(self.return_value) <= 4:
                self.output_zero_base.set(value=str(self.calculate))


        elif self.thing != "0":
            self.new_value = self.input_zero_base.get()
            self.input_zero_base.set(self.thing + "2")
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


 # exchange button for number 1
    def exchange_3_btn(self, e):
        """Method for when the user presses 3 key instead of clicking button"""
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
            self.input_zero_base.set(value='3') # sets of value of label to 9

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
                self.output_zero_base.set(value=str(self.final_value))
            elif len(self.return_value) <= 4:
                self.output_zero_base.set(value=str(self.calculate))


        elif self.thing != "0":
            self.new_value = self.input_zero_base.get()
            self.input_zero_base.set(self.thing + "3")
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



 # exchange button for number 1
    def exchange_4_btn(self, e):
        """Method for when the user presses 4 key instead of clicking button"""
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
            self.input_zero_base.set(value='4') # sets of value of label to 9

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
                self.output_zero_base.set(value=str(self.final_value))
            elif len(self.return_value) <= 4:
                self.output_zero_base.set(value=str(self.calculate))


        elif self.thing != "0":
            self.new_value = self.input_zero_base.get()
            self.input_zero_base.set(self.thing + "4")
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



 # exchange button for number 1
    def exchange_5_btn(self, e):
        """Method for when the user presses 5 key instead of clicking button"""
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
            self.input_zero_base.set(value='5') # sets of value of label to 9

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
                self.output_zero_base.set(value=str(self.final_value))
            elif len(self.return_value) <= 4:
                self.output_zero_base.set(value=str(self.calculate))


        elif self.thing != "0":
            self.new_value = self.input_zero_base.get()
            self.input_zero_base.set(self.thing + "5")
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



 # exchange button for number 1
    def exchange_6_btn(self, e):
        """Method for when the user presses 6 key instead of clicking button"""
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
            self.input_zero_base.set(value='6') # sets of value of label to 9

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
                self.output_zero_base.set(value=str(self.final_value))
            elif len(self.return_value) <= 4:
                self.output_zero_base.set(value=str(self.calculate))


        elif self.thing != "0":
            self.new_value = self.input_zero_base.get()
            self.input_zero_base.set(self.thing + "6")
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


    # exchange button for number 7
    def exchange_7_btn(self, e):
        """Method for when the user presses 7 key instead of clicking button

        Args:
            e (None): Needed to pass in something for lambda
        """
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
                self.output_zero_base.set(value=str(self.final_value))
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


    # exchange button for number 8
    def exchange_8_btn(self, e):
        """Method for when the user presses 8 key instead of clicking button"""
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
            self.input_zero_base.set(value='8') # sets of value of label to 8

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
                self.output_zero_base.set(value=str(self.final_value))
            elif len(self.return_value) <= 4:
                self.output_zero_base.set(value=str(self.calculate))


        elif self.thing != "0":
            self.new_value = self.input_zero_base.get()
            self.input_zero_base.set(self.thing + "8")
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


    # exchange button for number 9
    def exchange_9_btn(self, e):
        """Method for when the user presses 9 key instead of clicking button"""
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
            self.input_zero_base.set(value='9') # sets of value of label to 9

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
                self.output_zero_base.set(value=str(self.final_value))
            elif len(self.return_value) <= 4:
                self.output_zero_base.set(value=str(self.calculate))


        elif self.thing != "0":
            self.new_value = self.input_zero_base.get()
            self.input_zero_base.set(self.thing + "9")
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


    # exchange button for number 0
    def exchange_0_btn(self, e):
        """Method for when the user presses 0 key instead of clicking button"""
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
            pass

        elif self.thing != "0":
            self.new_value = self.input_zero_base.get()
            self.input_zero_base.set(self.thing + "0")
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

        self.values_calculated = float(self.final_value) * float(self.get_second_rate)
        self.str_convert = str(self.values_calculated)
        
        if len(self.str_convert) == 4:
            self.new_thing = self.str_convert[:-1]
            self.convert = float(self.new_thing)
        elif len(self.str_convert) > 4:
            self.to_cut = len(self.str_convert) - 4
            self.cutting = self.str_convert[:-self.to_cut]
            self.convert = float(self.cutting)
            
        return self.convert


    # exchange command for backspace key event
    def exchange_backspace(self, e):
        """Method used for when the user presses the backspace key

        Args:
            e (None): Needed something to pass into lambda
        """
        self.value_to_del = self.input_zero_base.get()

        if self.value_to_del == "0":
            self.input_zero_base.set(value="0")
            self.output_zero_base.set(value="0")

        elif self.value_to_del != "0" and len(self.value_to_del) == 1:
            self.input_zero_base.set(value="0")
            self.output_zero_base.set(value="0")

        elif self.value_to_del != "0" and len(self.value_to_del) >= 2 :
            self.minus_1 = self.value_to_del[:-1]
            self.input_zero_base.set(value=self.minus_1)
            self.new_output = self.get_output_calculated()
            self.output_zero_base.set(value=self.new_output)



    # -----------------------------------------------------------------------------------------
    def advanced_option(self, e):
        self.label_pack.pack_forget()
        self.entry_pack.pack_forget()
        self.first_pack.pack_forget()
        self.root.geometry("235x340") # L x H change back to 270 or 280?
        self.root.title("Advanced")
        
    
        # label here
        self.label_pack = customtkinter.CTkFrame(self.root, fg_color='#282828')
        self.label_pack.pack(side=TOP, anchor="w", padx=(5, 0), pady=(10, 0))

        self.header_label = customtkinter.CTkLabel(self.label_pack, text="Advanced", bg_color="#282828", height=0, width=0, text_font=("Arial", 14, "bold"))
        self.header_label.pack() # pady=(top, bottom) padx=(left, right) in px


        # entry box here
        self.entry_pack = customtkinter.CTkFrame(self.root, fg_color='#282828')
        self.entry_pack.pack(padx=(10, 15), fill=X)

        # entry box widget
        self.advanced_zero_base_input = customtkinter.StringVar(value="0")
        self.entry_label = customtkinter.CTkLabel(self.entry_pack, textvariable=self.advanced_zero_base_input, text_font=("Arial", 26), width=0, height=0)
        self.entry_label.pack(side=LEFT)
     
        # first set of standard calculator buttons
        self.first_pack = customtkinter.CTkFrame(self.root, fg_color='#282828')
        self.first_pack.pack(side=LEFT, anchor="nw", padx=(0, 0), pady=(5, 0))


        #########################################
        # button frame
        self.first_set_cals_frame = customtkinter.CTkFrame(self.first_pack, fg_color='#282828')
        self.first_set_cals_frame.pack(side=TOP, anchor='w', padx=(0, 0))
        
        

        # key press CE button 
        self.c_btn = tkinter.Button(self.first_set_cals_frame, text="CE", width=3, font=("Arial", 14), bg="#404040", fg="white", relief='flat') # command=self.c_key2
        self.c_btn.grid(row=0, column=0, sticky="w", padx=2, pady=2)
        # simple fg and bg change when hovered over.
        self.c_btn.bind('<Enter>', lambda e: self.c_btn.config(fg='black', bg='#4D4D4D'))
        self.c_btn.bind('<Leave>', lambda e: self.c_btn.config(fg='white', bg='#404040'))
        # keyboard press events **
        self.root.bind("c", lambda e: self.advanced_ce_btn("c"))
        


        # Pi Button
        self.btn_div = tkinter.Button(self.first_set_cals_frame, text="π", width=3, font=("Arial", 14), bg="#404040", fg="white", relief='flat') # command=lambda:self.div_func2("/")
        self.btn_div.grid(row=0, column=1, sticky="w", padx=2, pady=2)
        # simple fg and bg change when hovered over.
        self.btn_div.bind('<Enter>', lambda e: self.btn_div.config(fg='black', bg='#4D4D4D'))
        self.btn_div.bind('<Leave>', lambda e: self.btn_div.config(fg='white', bg='#404040'))
        # keyboard press events **


        # ? button
        self.btn_mut = tkinter.Button(self.first_set_cals_frame, text="e", width=3, font=("Arial", 14), bg="#404040", fg="white", relief='flat') # command=lambda:self.mut_key2("*")
        self.btn_mut.grid(row=0, column=2, sticky="w", padx=2, pady=2)
        # simple fg and bg change when hovered over.
        self.btn_mut.bind('<Enter>', lambda e: self.btn_mut.config(fg='black', bg='#4D4D4D'))
        self.btn_mut.bind('<Leave>', lambda e: self.btn_mut.config(fg='white', bg='#404040'))
        

        # Exp Button
        self.btn_exp = tkinter.Button(self.first_set_cals_frame, text="exp", width=3, font=("Arial", 14), bg="#404040", fg="white", relief='flat') # command=lambda:self.sub_key2("-")
        self.btn_exp.grid(row=0, column=3, sticky="w", padx=2, pady=2)
        # simple fg and bg change when hovered over.
        self.btn_exp.bind('<Enter>', lambda e: self.btn_exp.config(fg='black', bg='#4D4D4D'))
        self.btn_exp.bind('<Leave>', lambda e: self.btn_exp.config(fg='white', bg='#404040'))

        
        
        # Mod button
        self.btn_mod = tkinter.Button(self.first_set_cals_frame, text="mod", width=3, font=("Arial", 14), bg="#404040", fg="white", relief='flat') # command=lambda:self.sub_key2("-")
        self.btn_mod.grid(row=0, column=4, sticky="w", padx=2, pady=2)
        # simple fg and bg change when hovered over.
        self.btn_mod.bind('<Enter>', lambda e: self.btn_mod.config(fg='black', bg='#4D4D4D'))
        self.btn_mod.bind('<Leave>', lambda e: self.btn_mod.config(fg='white', bg='#404040'))




        # ---------------------------- Second Button Frame -------------------------------------- #

        self.advanced_second_btn_frame = customtkinter.CTkFrame(self.first_pack, fg_color='#282828')
        self.advanced_second_btn_frame.pack(side=TOP, anchor='w', padx=(0, 0))

        
        # Square Root Button
        self.btn_sqro = tkinter.Button(self.advanced_second_btn_frame, text="√", width=3, font=("Arial", 14), bg="#404040", fg="white", relief='flat', command=lambda:self.btn_click_7("7"))
        self.btn_sqro.grid(row=0, column=0, sticky="n", padx=2, pady=2)
        # simple fg and bg change when hovered over.
        self.btn_sqro.bind('<Enter>', lambda e: self.btn_sqro.config(fg='black', bg='#4D4D4D'))
        self.btn_sqro.bind('<Leave>', lambda e: self.btn_sqro.config(fg='white', bg='#404040'))


        # Left Parentheses Button
        self.btn_leftP = tkinter.Button(self.advanced_second_btn_frame, text="(", width=3, font=("Arial", 14), bg="#404040", fg="white", relief='flat') # command=lambda:self.key_8("8")
        self.btn_leftP.grid(row=0, column=1, sticky="n", padx=2, pady=2)
        # simple fg and bg change when hovered over.
        self.btn_leftP.bind('<Enter>', lambda e: self.btn_leftP.config(fg='black', bg='#4D4D4D'))
        self.btn_leftP.bind('<Leave>', lambda e: self.btn_leftP.config(fg='white', bg='#404040'))



        # Right Parentheses Button
        self.btn_rightP = tkinter.Button(self.advanced_second_btn_frame, text=")", width=3, font=("Arial", 14), bg="#404040", fg="white", relief='flat') # command=lambda:self.key_9("9")
        self.btn_rightP.grid(row=0, column=2, sticky="n", padx=2, pady=2)
        # simple fg and bg change when hovered over.
        self.btn_rightP.bind('<Enter>', lambda e: self.btn_rightP.config(fg='black', bg='#4D4D4D'))
        self.btn_rightP.bind('<Leave>', lambda e: self.btn_rightP.config(fg='white', bg='#404040'))


        # Natural Number Button
        self.ad_btn_n = tkinter.Button(self.advanced_second_btn_frame, text="n", width=3, font=("Arial", 14), bg="#404040", fg="white", relief='flat') # command=lambda:self.add_func2("+")
        self.ad_btn_n.grid(row=0, column=3, padx=2, pady=2)
        # simple fg and bg change when hovered over.
        self.ad_btn_n.bind('<Enter>', lambda e: self.ad_btn_n.config(fg='black', bg='#4D4D4D'))
        self.ad_btn_n.bind('<Leave>', lambda e: self.ad_btn_n.config(fg='white', bg='#404040'))

        
        # ##########

        # Advanced Divsion Button
        self.btn_div2 = tkinter.Button(self.advanced_second_btn_frame, text="÷", width=3, font=("Arial", 14), bg="#404040", fg="white", relief='flat') # command=lambda:self.key_4("4")
        self.btn_div2.grid(row=0, column=4, sticky="n", padx=2, pady=2)
        # simple fg and bg change when hovered over.
        self.btn_div2.bind('<Enter>', lambda e: self.btn_div2.config(fg='black', bg='#4D4D4D'))
        self.btn_div2.bind('<Leave>', lambda e: self.btn_div2.config(fg='white', bg='#404040'))
        # keyboard press events **
        self.root.bind("/", lambda e: self.advanced_divion_btn("/"))
        
        self.root.bind("r", lambda e: self.return_resize(e))



      
        # ----------------------------- Third Button Frame ---------------------------- #
        
        
        self.third_btn_frame = customtkinter.CTkFrame(self.first_pack, fg_color='#282828')
        self.third_btn_frame.pack(side=TOP, anchor='w', padx=(0, 0))

        
        # X2 Button
        self.btn_x2 = tkinter.Button(self.third_btn_frame, text="x2", width=3, font=("Arial", 14), bg="#404040", fg="white", relief='flat') # command=lambda:self.key_1("1")
        self.btn_x2.grid(row=0, column=0, sticky="n", padx=2, pady=2)
        # simple fg and bg change when hovered over.
        self.btn_x2.bind('<Enter>', lambda e: self.btn_x2.config(fg='black', bg='#4D4D4D'))
        self.btn_x2.bind('<Leave>', lambda e: self.btn_x2.config(fg='white', bg='#404040'))


        # Number 7 Button
        self.btn_7 = tkinter.Button(self.third_btn_frame, text="7", width=3, font=("Arial", 14), bg="#525252", fg="white", relief='flat') # command=lambda:self.key_2("2")
        self.btn_7.grid(row=0, column=1, sticky="n", padx=2, pady=2)
        # simple fg and bg change when hovered over.
        self.btn_7.bind('<Enter>', lambda e: self.btn_7.config(fg='black', bg='#4D4D4D'))
        self.btn_7.bind('<Leave>', lambda e: self.btn_7.config(fg='white', bg='#525252'))
        # keyboard press events **
        self.root.bind("7", lambda e: self.advanced_n7_btn("7"))


        # Number 8 Button
        self.btn_8 = tkinter.Button(self.third_btn_frame, text="8", width=3, font=("Arial", 14), bg="#525252", fg="white", relief='flat') # command=lambda:self.key_3("3")
        self.btn_8.grid(row=0, column=2, sticky="n", padx=2, pady=2)
        # simple fg and bg change when hovered over.
        self.btn_8.bind('<Enter>', lambda e: self.btn_8.config(fg='black', bg='#4D4D4D'))
        self.btn_8.bind('<Leave>', lambda e: self.btn_8.config(fg='white', bg='#525252'))
        # keyboard press events **
        self.root.bind("8", lambda e: self.advanced_n8_btn("8"))


        # Number 9 Button
        self.btn_9 = tkinter.Button(self.third_btn_frame, text="9", width=3, font=("Arial", 14), bg="#525252", fg="white", relief='flat') # command=self.enter_key2
        self.btn_9.grid(row=0, column=3, padx=2, pady=2)
        # simple fg and bg change when hovered over.
        self.btn_9.bind('<Enter>', lambda e: self.btn_9.config(fg='black', bg='#4D4D4D'))
        self.btn_9.bind('<Leave>', lambda e: self.btn_9.config(fg='white', bg='#525252'))
        # keyboard press events **
        self.root.bind("9", lambda e: self.advanced_n9_btn("9"))


        # Multiplication Button
        self.btn_x = tkinter.Button(self.third_btn_frame, text="X", width=3, font=("Arial", 14), bg="#404040", fg="white", relief='flat', command=lambda:self.key_0("0"))
        self.btn_x.grid(row=0, column=4, sticky="n", padx=2, pady=2)
        # simple fg and bg change when hovered over.
        self.btn_x.bind('<Enter>', lambda e: self.btn_x.config(fg='black', bg='#4D4D4D'))
        self.btn_x.bind('<Leave>', lambda e: self.btn_x.config(fg='white', bg='#404040'))
        # keyboard press events **
        self.root.bind("*", lambda e: self.advanced_multiplication_btn("*"))
        
        
        
        # --------------------------- Fourth Button Frame -------------------------------------- #
        self.advanced_fourth_btn_frame = customtkinter.CTkFrame(self.first_pack, fg_color='#282828')
        self.advanced_fourth_btn_frame.pack(side=TOP, anchor='w', padx=(0, 0))
        
        
        # |x| Button
        self.btn_abs = tkinter.Button(self.advanced_fourth_btn_frame, text="|x|", width=3, font=("Arial", 14), bg="#404040", fg="white", relief='flat', command=lambda:self.key_0("0"))
        self.btn_abs.grid(row=0, column=0, sticky="n", padx=2, pady=2)
        # simple fg and bg change when hovered over.
        self.btn_abs.bind('<Enter>', lambda e: self.btn_abs.config(fg='black', bg='#4D4D4D'))
        self.btn_abs.bind('<Leave>', lambda e: self.btn_abs.config(fg='white', bg='#404040'))
        
        
        # Number 4 Button
        self.ad_btn_4 = tkinter.Button(self.advanced_fourth_btn_frame, text="4", width=3, font=("Arial", 14), bg="#525252", fg="white", relief='flat', command=lambda:self.key_0("0"))
        self.ad_btn_4.grid(row=0, column=1, sticky="n", padx=2, pady=2)
        # simple fg and bg change when hovered over.
        self.ad_btn_4.bind('<Enter>', lambda e: self.ad_btn_4.config(fg='black', bg='#4D4D4D'))
        self.ad_btn_4.bind('<Leave>', lambda e: self.ad_btn_4.config(fg='white', bg='#525252'))
        # keyboard press events **
        self.root.bind("4", lambda e: self.advanced_n4_btn("4"))
        
        
        # Number 5 Button
        self.ad_btn_5 = tkinter.Button(self.advanced_fourth_btn_frame, text="5", width=3, font=("Arial", 14), bg="#525252", fg="white", relief='flat', command=lambda:self.key_0("0"))
        self.ad_btn_5.grid(row=0, column=2, sticky="n", padx=2, pady=2)
        # simple fg and bg change when hovered over.
        self.ad_btn_5.bind('<Enter>', lambda e: self.ad_btn_5.config(fg='black', bg='#4D4D4D'))
        self.ad_btn_5.bind('<Leave>', lambda e: self.ad_btn_5.config(fg='white', bg='#525252'))
        # keyboard press events **
        self.root.bind("5", lambda e: self.advanced_n5_btn("5"))
        
        
        # Number 6 Button
        self.ad_btn_6 = tkinter.Button(self.advanced_fourth_btn_frame, text="6", width=3, font=("Arial", 14), bg="#525252", fg="white", relief='flat', command=lambda:self.key_0("0"))
        self.ad_btn_6.grid(row=0, column=3, sticky="n", padx=2, pady=2)
        # simple fg and bg change when hovered over.
        self.ad_btn_6.bind('<Enter>', lambda e: self.ad_btn_6.config(fg='black', bg='#4D4D4D'))
        self.ad_btn_6.bind('<Leave>', lambda e: self.ad_btn_6.config(fg='white', bg='#525252'))
        # keyboard press events **
        self.root.bind("6", lambda e: self.advanced_n6_btn("6"))
        
        
        # Advanced Subtraction Button
        self.ad_btn_minus = tkinter.Button(self.advanced_fourth_btn_frame, text="-", width=3, font=("Arial", 14), bg="#404040", fg="white", relief='flat', command=lambda:self.key_0("0"))
        self.ad_btn_minus.grid(row=0, column=4, sticky="n", padx=2, pady=2)
        # simple fg and bg change when hovered over.
        self.ad_btn_minus.bind('<Enter>', lambda e: self.ad_btn_minus.config(fg='black', bg='#4D4D4D'))
        self.ad_btn_minus.bind('<Leave>', lambda e: self.ad_btn_minus.config(fg='white', bg='#404040'))
        # keyboard press events **
        self.root.bind("-", lambda e: self.advanced_subtraction_btn("-"))




        # ----------------------------- Fifth Button Frame -------------------------------------- #
        self.advanced_fifth_btn_frame = customtkinter.CTkFrame(self.first_pack, fg_color='#282828')
        self.advanced_fifth_btn_frame.pack(side=TOP, anchor='w', padx=(0, 0))
        
        
        # log Button
        self.btn_log = tkinter.Button(self.advanced_fifth_btn_frame, text="log", width=3, font=("Arial", 14), bg="#404040", fg="white", relief='flat', command=lambda:self.key_0("0"))
        self.btn_log.grid(row=0, column=0, sticky="n", padx=2, pady=2)
        # simple fg and bg change when hovered over.
        self.btn_log.bind('<Enter>', lambda e: self.btn_log.config(fg='black', bg='#4D4D4D'))
        self.btn_log.bind('<Leave>', lambda e: self.btn_log.config(fg='white', bg='#404040'))

        
        
        # Number 1 Button
        self.ad_btn_1 = tkinter.Button(self.advanced_fifth_btn_frame, text="1", width=3, font=("Arial", 14), bg="#525252", fg="white", relief='flat', command=lambda:self.key_0("0"))
        self.ad_btn_1.grid(row=0, column=1, sticky="n", padx=2, pady=2)
        # simple fg and bg change when hovered over.
        self.ad_btn_1.bind('<Enter>', lambda e: self.ad_btn_1.config(fg='black', bg='#4D4D4D'))
        self.ad_btn_1.bind('<Leave>', lambda e: self.ad_btn_1.config(fg='white', bg='#525252'))
        # keyboard press events **
        self.root.bind("1", lambda e: self.advanced_n1_btn("1"))
        
        
        # Number 2 Button
        self.ad_btn_2 = tkinter.Button(self.advanced_fifth_btn_frame, text="2", width=3, font=("Arial", 14), bg="#525252", fg="white", relief='flat', command=lambda:self.key_0("0"))
        self.ad_btn_2.grid(row=0, column=2, sticky="n", padx=2, pady=2)
        # simple fg and bg change when hovered over.
        self.ad_btn_2.bind('<Enter>', lambda e: self.ad_btn_2.config(fg='black', bg='#4D4D4D'))
        self.ad_btn_2.bind('<Leave>', lambda e: self.ad_btn_2.config(fg='white', bg='#525252'))
        # keyboard press events **
        self.root.bind("2", lambda e: self.advanced_n2_btn("2"))
        
        
        # Number 3 Button
        self.ad_btn_3 = tkinter.Button(self.advanced_fifth_btn_frame, text="3", width=3, font=("Arial", 14), bg="#525252", fg="white", relief='flat', command=lambda:self.key_0("0"))
        self.ad_btn_3.grid(row=0, column=3, sticky="n", padx=2, pady=2)
        # simple fg and bg change when hovered over.
        self.ad_btn_3.bind('<Enter>', lambda e: self.ad_btn_3.config(fg='black', bg='#4D4D4D'))
        self.ad_btn_3.bind('<Leave>', lambda e: self.ad_btn_3.config(fg='white', bg='#525252'))
        # keyboard press events **
        self.root.bind("3", lambda e: self.advanced_n3_btn("3"))
        
        
        # Advanced Addition Button
        self.ad_btn_plus = tkinter.Button(self.advanced_fifth_btn_frame, text="+", width=3, font=("Arial", 14), bg="#404040", fg="white", relief='flat', command=lambda:self.key_0("0"))
        self.ad_btn_plus.grid(row=0, column=4, sticky="n", padx=2, pady=2)
        # simple fg and bg change when hovered over.
        self.ad_btn_plus.bind('<Enter>', lambda e: self.ad_btn_plus.config(fg='black', bg='#4D4D4D'))
        self.ad_btn_plus.bind('<Leave>', lambda e: self.ad_btn_plus.config(fg='white', bg='#404040'))
        # keyboard press events **
        self.root.bind("+", lambda e: self.advanced_addition_btn("+"))
        
        
        
        
        
        
        # ------------------------------- Sixth Button Frame ----------------------------------- #
        self.advanced_sixth_btn_frame = customtkinter.CTkFrame(self.first_pack, fg_color='#282828')
        self.advanced_sixth_btn_frame.pack(side=TOP, anchor='w', padx=(0, 0))
        
        
        # In Button
        self.btn_in = tkinter.Button(self.advanced_sixth_btn_frame, text="in", width=3, font=("Arial", 14), bg="#404040", fg="white", relief='flat', command=lambda:self.key_0("0"))
        self.btn_in.grid(row=0, column=0, sticky="n", padx=2, pady=2)
        # simple fg and bg change when hovered over.
        self.btn_in.bind('<Enter>', lambda e: self.btn_in.config(fg='black', bg='#4D4D4D'))
        self.btn_in.bind('<Leave>', lambda e: self.btn_in.config(fg='white', bg='#404040'))

        
        
        # Plus/Minus button
        self.ad_plus_minus = tkinter.Button(self.advanced_sixth_btn_frame, text="±", width=3, font=("Arial", 14), bg="#404040", fg="white", relief='flat', command=lambda:self.key_0("0"))
        self.ad_plus_minus.grid(row=0, column=1, sticky="n", padx=2, pady=2)
        # simple fg and bg change when hovered over.
        self.ad_plus_minus.bind('<Enter>', lambda e: self.ad_plus_minus.config(fg='black', bg='#4D4D4D'))
        self.ad_plus_minus.bind('<Leave>', lambda e: self.ad_plus_minus.config(fg='white', bg='#404040'))
        
        
        # Number 0 Button
        self.ad_btn_0 = tkinter.Button(self.advanced_sixth_btn_frame, text="0", width=3, font=("Arial", 14), bg="#525252", fg="white", relief='flat', command=lambda:self.key_0("0"))
        self.ad_btn_0.grid(row=0, column=2, sticky="n", padx=2, pady=2)
        # simple fg and bg change when hovered over.
        self.ad_btn_0.bind('<Enter>', lambda e: self.ad_btn_0.config(fg='black', bg='#4D4D4D'))
        self.ad_btn_0.bind('<Leave>', lambda e: self.ad_btn_0.config(fg='white', bg='#525252'))
        # keyboard press events **
        self.root.bind("0", lambda e: self.advanced_n0_btn("0"))
        
        
        # Number Dot Button
        self.ad_btn_dot = tkinter.Button(self.advanced_sixth_btn_frame, text=".", width=3, font=("Arial", 14), bg="#404040", fg="white", relief='flat', command=lambda:self.key_0("0"))
        self.ad_btn_dot.grid(row=0, column=3, sticky="n", padx=2, pady=2)
        # simple fg and bg change when hovered over.
        self.ad_btn_dot.bind('<Enter>', lambda e: self.ad_btn_dot.config(fg='black', bg='#4D4D4D'))
        self.ad_btn_dot.bind('<Leave>', lambda e: self.ad_btn_dot.config(fg='white', bg='#404040'))
        # keyboard press events **
        self.root.bind(".", lambda e: self.advanced_dot_btn("0"))
        
        
        # Advanced Equals Button
        self.ad_btn_equals = tkinter.Button(self.advanced_sixth_btn_frame, text="=", width=3, font=("Arial", 14), bg="#808A87", fg="white", relief='flat', command=lambda:self.key_0("0"))
        self.ad_btn_equals.grid(row=0, column=4, sticky="n", padx=2, pady=2)
        # simple fg and bg change when hovered over.
        self.ad_btn_equals.bind('<Enter>', lambda e: self.ad_btn_equals.config(fg='black', bg='#4D4D4D'))
        self.ad_btn_equals.bind('<Leave>', lambda e: self.ad_btn_equals.config(fg='white', bg='#808A87'))
        # keyboard press events **
        self.root.bind("<Enter>", lambda e: self.advanced_enter_btn("0"))


    
    
    
    
    # -----------------------------------------------------------------------------------------



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
            self.btn_0.bind('<Enter>', lambda e: self.btn_0.config(fg='black', bg='#4D4D4D'))
            self.btn_0.bind('<Leave>', lambda e: self.btn_0.config(fg='white', bg='#404040'))

        elif self.entry.get() == "NA":
            self.entry.delete(0, END)
            self.entry.insert(0, a)

        else:
            self.entry.insert(END, a)
            self.btn_0.bind('<Enter>', lambda e: self.btn_0.config(fg='black', bg='#4D4D4D'))
            self.btn_0.bind('<Leave>', lambda e: self.btn_0.config(fg='white', bg='#404040'))

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



    
    def return_resize(self, e):
        self.label_pack.pack()
        self.entry_pack.pack()
        self.first_pack.pack()
        self.root.geometry("280x340")
        self.entry.configure(width=245)
        self.root.title("Calculator")
        self.header_label.configure(text="Standard")
        self.root.bind("4", lambda e: self.key_4("4"))
        self.root.bind("9", lambda e: self.key_9("9"))
        self.root.bind("8", lambda e: self.key_8("8"))
        self.root.bind("7", lambda e: self.key_7("7"))
        self.root.bind("c", lambda e: self.c_key("c"))




app = App()