import customtkinter
import tkinter
from tkinter import *
from currency_exchanges import exchanges, currency_symbols
import os
import re
import tkinter.ttk as ttk
import datetime
from datetime import datetime
import requests


class App:
    def __init__(self):
        self.root = customtkinter.CTk()
        self.root.title("Calculator")
        self.root.iconbitmap("darkModeV.ico")
        self.root.geometry("248x330") # L x H change back to 270 or 280?
        self.root.config(background="#282828")

        # label here
        self.label_pack = customtkinter.CTkFrame(self.root, fg_color='#282828')
        self.label_pack.pack(side=TOP, anchor="w", padx=(10, 0), pady=(15, 0))

        self.header_label = customtkinter.CTkLabel(self.label_pack, text="Standard", bg_color="#282828", height=0, width=0, text_font=("Arial", 14, "bold"))
        self.header_label.pack() # pady=(top, bottom) padx=(left, right) in px


        # Main Label Zero Input
        self.standard_zero_label_input = customtkinter.CTkFrame(self.root, fg_color='#282828')
        self.standard_zero_label_input.pack(padx=(10, 15), fill=X)

        # Label widget
        self.standard_zero_base_input = customtkinter.StringVar(value="0")
        self.zero_standard_label_widget = customtkinter.CTkLabel(self.standard_zero_label_input, textvariable=self.standard_zero_base_input, text_font=("Arial", 26), width=0, height=0)
        self.zero_standard_label_widget.pack(side=LEFT)
        
        
        # first set of standard calculator buttons
        self.first_pack = customtkinter.CTkFrame(self.root, fg_color='#282828')
        self.first_pack.pack(side=BOTTOM, anchor="nw", padx=(0, 0), pady=(5, 0))


        #########################################
        # button frame
        self.first_set_cals_frame = customtkinter.CTkFrame(self.first_pack, fg_color='#282828')
        self.first_set_cals_frame.pack(side=TOP, anchor='w', padx=(0, 0))

        # key press c button 
        self.standard_c_btn = tkinter.Button(self.first_set_cals_frame, text="C", width=4, font=("Arial", 16), bg="#404040", fg="white", relief='flat') # command=self.c_key2
        self.standard_c_btn.grid(row=0, column=0, sticky="w", padx=2, pady=2)
        # simple fg and bg change when hovered over.
        self.standard_c_btn.bind('<Enter>', lambda e: self.standard_c_btn.config(fg='black', bg='#4D4D4D'))
        self.standard_c_btn.bind('<Leave>', lambda e: self.standard_c_btn.config(fg='white', bg='#404040'))
        # keyboard press events **
        self.root.bind("c", lambda e: self.standard_ce_btn("c"))



        # number / button
        self.btn_div = tkinter.Button(self.first_set_cals_frame, text="/", width=4, font=("Arial", 16), bg="#404040", fg="white", relief='flat') # command=lambda:self.div_func2("/")
        self.btn_div.grid(row=0, column=1, sticky="w", padx=2, pady=2)
        # simple fg and bg change when hovered over.
        self.btn_div.bind('<Enter>', lambda e: self.btn_div.config(fg='black', bg='#4D4D4D'))
        self.btn_div.bind('<Leave>', lambda e: self.btn_div.config(fg='white', bg='#404040'))
        # keyboard press events **
        self.root.bind("/", lambda e: self.standard_divion_input("/"))


        # number * button
        self.btn_mut = tkinter.Button(self.first_set_cals_frame, text="*", width=4, font=("Arial", 16), bg="#404040", fg="white", relief='flat') # command=lambda:self.mut_key2("*")
        self.btn_mut.grid(row=0, column=2, sticky="w", padx=2, pady=2)
        # simple fg and bg change when hovered over.
        self.btn_mut.bind('<Enter>', lambda e: self.btn_mut.config(fg='black', bg='#4D4D4D'))
        self.btn_mut.bind('<Leave>', lambda e: self.btn_mut.config(fg='white', bg='#404040'))
        # keyboard press events **
        self.root.bind("*", lambda e: self.standard_multiplication_input("*"))


        # number - button
        self.btn_sub = tkinter.Button(self.first_set_cals_frame, text="-", width=4, font=("Arial", 16), bg="#404040", fg="white", relief='flat') # command=lambda:self.sub_key2("-")
        self.btn_sub.grid(row=0, column=3, sticky="w", padx=2, pady=2)
        # simple fg and bg change when hovered over.
        self.btn_sub.bind('<Enter>', lambda e: self.btn_sub.config(fg='black', bg='#4D4D4D'))
        self.btn_sub.bind('<Leave>', lambda e: self.btn_sub.config(fg='white', bg='#404040'))
        # keyboard press events **
        self.root.bind("-", lambda e: self.standard_subtraction_input("-"))



        # second button frame #################################################################################

        self.second_btn_frame = customtkinter.CTkFrame(self.first_pack, fg_color='#282828')
        self.second_btn_frame.pack(side=TOP, anchor='w', padx=(0, 0))
        
        # number 7 button
        self.btn_7 = tkinter.Button(self.second_btn_frame, text="7", width=4, font=("Arial", 16), bg="#404040", fg="white", relief='flat', command=lambda:self.btn_click_7("7"))
        self.btn_7.grid(row=0, column=0, sticky="n", padx=2, pady=2)
        # simple fg and bg change when hovered over.
        self.btn_7.bind('<Enter>', lambda e: self.btn_7.config(fg='black', bg='#4D4D4D'))
        self.btn_7.bind('<Leave>', lambda e: self.btn_7.config(fg='white', bg='#404040'))
        # keyboard press events **
        self.root.bind("7", lambda e: self.standard_n7_btn("7"))



        # number 8 button
        self.btn_8 = tkinter.Button(self.second_btn_frame, text="8", width=4, font=("Arial", 16), bg="#404040", fg="white", relief='flat') # command=lambda:self.key_8("8")
        self.btn_8.grid(row=0, column=1, sticky="n", padx=2, pady=2)
        # simple fg and bg change when hovered over.
        self.btn_8.bind('<Enter>', lambda e: self.btn_8.config(fg='black', bg='#4D4D4D'))
        self.btn_8.bind('<Leave>', lambda e: self.btn_8.config(fg='white', bg='#404040'))
        # keyboard press events **
        self.root.bind("8", lambda e: self.standard_n8_btn("8"))



        # number 9 button
        self.btn_9 = tkinter.Button(self.second_btn_frame, text="9", width=4, font=("Arial", 16), bg="#404040", fg="white", relief='flat') # command=lambda:self.key_9("9")
        self.btn_9.grid(row=0, column=2, sticky="n", padx=2, pady=2)
        # simple fg and bg change when hovered over.
        self.btn_9.bind('<Enter>', lambda e: self.btn_9.config(fg='black', bg='#4D4D4D'))
        self.btn_9.bind('<Leave>', lambda e: self.btn_9.config(fg='white', bg='#404040'))
        # keyboard press events **
        self.root.bind("9", lambda e: self.standard_n9_btn("9"))


        # number add button
        self.btn_add = tkinter.Button(self.second_btn_frame, text="+", width=4, font=("Arial", 16), bg="#404040", fg="white", height=3, relief='flat') # command=lambda:self.add_func2("+")
        self.btn_add.grid(row=0, column=3, padx=2, pady=2, rowspan=2)
        # simple fg and bg change when hovered over.
        self.btn_add.bind('<Enter>', lambda e: self.btn_add.config(fg='black', bg='#4D4D4D'))
        self.btn_add.bind('<Leave>', lambda e: self.btn_add.config(fg='white', bg='#404040'))
        # keyboard press events **
        self.root.bind("+", lambda e: self.standard_addition_input("+"))
        
        ##########

        # number 4 button
        self.btn_4 = tkinter.Button(self.second_btn_frame, text="4", width=4, font=("Arial", 16), bg="#404040", fg="white", relief='flat') # command=lambda:self.key_4("4")
        self.btn_4.grid(row=1, column=0, sticky="n", padx=2, pady=2)
        # simple fg and bg change when hovered over.
        self.btn_4.bind('<Enter>', lambda e: self.btn_4.config(fg='black', bg='#4D4D4D'))
        self.btn_4.bind('<Leave>', lambda e: self.btn_4.config(fg='white', bg='#404040'))
        # keyboard press events **
        self.root.bind("4", lambda e: self.standard_n4_btn("4"))



        # number 5 button
        self.btn_5 = tkinter.Button(self.second_btn_frame, text="5", width=4, font=("Arial", 16), bg="#404040", fg="white", relief='flat') # command=lambda:self.key_5("5")
        self.btn_5.grid(row=1, column=1, sticky="n", padx=2, pady=2)
        # simple fg and bg change when hovered over.
        self.btn_5.bind('<Enter>', lambda e: self.btn_5.config(fg='black', bg='#4D4D4D'))
        self.btn_5.bind('<Leave>', lambda e: self.btn_5.config(fg='white', bg='#404040'))
        # keyboard press events **
        self.root.bind("5", lambda e: self.standard_n5_btn("5"))


        # number 6 button
        self.btn_6 = tkinter.Button(self.second_btn_frame, text="6", width=4, font=("Arial", 16), bg="#404040", fg="white", relief='flat') # command=lambda:self.key_6("6")
        self.btn_6.grid(row=1, column=2, sticky="n", padx=2, pady=2)
        # simple fg and bg change when hovered over.
        self.btn_6.bind('<Enter>', lambda e: self.btn_6.config(fg='black', bg='#4D4D4D'))
        self.btn_6.bind('<Leave>', lambda e: self.btn_6.config(fg='white', bg='#404040'))
        # keyboard press events **
        self.root.bind("6", lambda e: self.standard_n6_btn("6"))

      
        # third button frame #############################################################
        self.third_btn_frame = customtkinter.CTkFrame(self.first_pack, fg_color='#282828')
        self.third_btn_frame.pack(side=TOP, anchor='w', padx=(0, 0))

        
        # number 1 button
        self.btn_1 = tkinter.Button(self.third_btn_frame, text="1", width=4, font=("Arial", 16), bg="#404040", fg="white", relief='flat') # command=lambda:self.key_1("1")
        self.btn_1.grid(row=0, column=0, sticky="n", padx=2, pady=2)
        # simple fg and bg change when hovered over.
        self.btn_1.bind('<Enter>', lambda e: self.btn_1.config(fg='black', bg='#4D4D4D'))
        self.btn_1.bind('<Leave>', lambda e: self.btn_1.config(fg='white', bg='#404040'))
        # keyboard press events **
        self.root.bind("1", lambda e: self.standard_n1_btn("1"))


        # number 2 button
        self.btn_2 = tkinter.Button(self.third_btn_frame, text="2", width=4, font=("Arial", 16), bg="#404040", fg="white", relief='flat') # command=lambda:self.key_2("2")
        self.btn_2.grid(row=0, column=1, sticky="n", padx=2, pady=2)
        # simple fg and bg change when hovered over.
        self.btn_2.bind('<Enter>', lambda e: self.btn_2.config(fg='black', bg='#4D4D4D'))
        self.btn_2.bind('<Leave>', lambda e: self.btn_2.config(fg='white', bg='#404040'))
        # keyboard press events **
        self.root.bind("2", lambda e: self.standard_n2_btn("2"))


        # number 3 button
        self.btn_3 = tkinter.Button(self.third_btn_frame, text="3", width=4, font=("Arial", 16), bg="#404040", fg="white", relief='flat') # command=lambda:self.key_3("3")
        self.btn_3.grid(row=0, column=2, sticky="n", padx=2, pady=2)
        # simple fg and bg change when hovered over.
        self.btn_3.bind('<Enter>', lambda e: self.btn_3.config(fg='black', bg='#4D4D4D'))
        self.btn_3.bind('<Leave>', lambda e: self.btn_3.config(fg='white', bg='#404040'))
        # keyboard press events **
        self.root.bind("3", lambda e: self.standard_n3_btn("3"))


        # number enter button
        self.btn_en = tkinter.Button(self.third_btn_frame, text="Enter", width=4, font=("Arial", 16), bg="#3D59AB", fg="white", height=3, relief='flat') # command=self.enter_key2
        self.btn_en.grid(row=0, column=3, padx=2, pady=2, rowspan=2)
        # simple fg and bg change when hovered over.
        self.btn_en.bind('<Enter>', lambda e: self.btn_en.config(fg='black', bg='#104E8B'))
        self.btn_en.bind('<Leave>', lambda e: self.btn_en.config(fg='white', bg='#3D59AB'))
        # keyboard press events **
        self.root.bind("<Return>", lambda e: self.standard_enter_btn("0"))
        
        ##########

        # number 0 button
        self.btn_0 = tkinter.Button(self.third_btn_frame, text="0", width=9, font=("Arial", 16), bg="#404040", fg="white", relief='flat', command=lambda:self.key_0("0"))
        self.btn_0.grid(row=1, column=0, sticky="n", padx=2, pady=2, columnspan=2)
        # simple fg and bg change when hovered over.
        self.btn_0.bind('<Enter>', lambda e: self.btn_0.config(fg='black', bg='#4D4D4D'))
        self.btn_0.bind('<Leave>', lambda e: self.btn_0.config(fg='white', bg='#404040'))
        # keyboard press events **
        self.root.bind("0", lambda e: self.standard_n0_btn("0"))

        # number dot button
        self.btn_dot = tkinter.Button(self.third_btn_frame, text=".", width=4, font=("Arial", 16), bg="#404040", fg="white", relief='flat') # command=lambda:self.key_dot(".")
        self.btn_dot.grid(row=1, column=2, sticky="n", padx=2, pady=2)
        # simple fg and bg change when hovered over.
        self.btn_dot.bind('<Enter>', lambda e: self.btn_dot.config(fg='black', bg='#4D4D4D'))
        self.btn_dot.bind('<Leave>', lambda e: self.btn_dot.config(fg='white', bg='#404040'))
        # keyboard press events **
        self.root.bind(".", lambda e: self.standard_dot_btn("."))

        # end of first pack standard calculations

        # menu
        my_menu = Menu(self.root)


        # create menu items
        file_menu = Menu(my_menu, tearoff=0, background='#303030', fg='white')
        my_menu.add_cascade(label="File", menu=file_menu)

        file_menu.add_command(label="Clear:", accelerator="C key ") # command=lambda:self.c_key(' ')

        file_menu.add_command(label="Errors", accelerator="H key") # command=lambda:self.errors_win("e")
        # self.root.bind("h", lambda e: self.errors_win(e))

        file_menu.add_command(label="Advanced", accelerator="A key") # command=lambda:self.execute_advanced_option("0")
        self.root.bind("a", lambda e: self.execute_advanced_option("1"))


        file_menu.add_separator()
        file_menu.add_command(label="Currency", accelerator="Ctrl+c")
        self.root.bind("<Control-c>", lambda e: self.execute_currancy_exchange("1"))

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
        


    # ------------------------------ Standard Option Methods ---------------------------------- #
        
        
        
    # ------------------------- Standard X Number Press Event Methods ----------------------------- #
    
    # -- Advanced Event Btn 9 -- #
    def standard_n9_btn(self, e):
        
        # Number x that is passed in when key event pressed
        self.number_value = e
        
        # Number StrVariable that is set
        self.advanced_zero_value = self.standard_zero_base_input.get()
        
        # Checking to see if the StrVariable is x
        if self.advanced_zero_value == "0":
            self.standard_zero_base_input.set(value="9")
        elif self.advanced_zero_value != "0":
            self.standard_zero_base_input.set(value=self.advanced_zero_value + "9")


    # -- Advanced Event Btn 8 -- #
    def standard_n8_btn(self, e):
        
        # Number x that is passed in when key event pressed
        self.number_value = e
        
        # Number StrVariable that is set
        self.advanced_zero_value = self.standard_zero_base_input.get()
        
        # Checking to see if the StrVariable is x
        if self.advanced_zero_value == "0":
            self.standard_zero_base_input.set(value="8")
        elif self.advanced_zero_value != "0":
            self.standard_zero_base_input.set(value=self.advanced_zero_value + "8")
    
    
    # -- Advanced Event Btn 7 -- #
    def standard_n7_btn(self, e):
        
        # Number x that is passed in when key event pressed
        self.number_value = e
        
        # Number StrVariable that is set
        self.advanced_zero_value = self.standard_zero_base_input.get()
        
        # Checking to see if the StrVariable is x
        if self.advanced_zero_value == "0":
            self.standard_zero_base_input.set(value="7")
        elif self.advanced_zero_value != "0":
            self.standard_zero_base_input.set(value=self.advanced_zero_value + "7")
    
    
    # -- Advanced Event Btn 6 -- #
    def standard_n6_btn(self, e):
        
        # Number x that is passed in when key event pressed
        self.number_value = e
        
        # Number StrVariable that is set
        self.advanced_zero_value = self.standard_zero_base_input.get()
        
        # Checking to see if the StrVariable is x
        if self.advanced_zero_value == "0":
            self.standard_zero_base_input.set(value="6")
        elif self.advanced_zero_value != "0":
            self.standard_zero_base_input.set(value=self.advanced_zero_value + "6")
     
     
    # -- Advanced Event Btn 5 -- #
    def standard_n5_btn(self, e):
        
        # Number x that is passed in when key event pressed
        self.number_value = e
        
        # Number StrVariable that is set
        self.advanced_zero_value = self.standard_zero_base_input.get()
        
        # Checking to see if the StrVariable is x
        if self.advanced_zero_value == "0":
            self.standard_zero_base_input.set(value="5")
        elif self.advanced_zero_value != "0":
            self.standard_zero_base_input.set(value=self.advanced_zero_value + "5")
    
    
    # -- Advanced Event Btn 4 -- #
    def standard_n4_btn(self, e):
        
        # Number x that is passed in when key event pressed
        self.number_value = e
        
        # Number StrVariable that is set
        self.advanced_zero_value = self.standard_zero_base_input.get()
        
        # Checking to see if the StrVariable is x
        if self.advanced_zero_value == "0":
            self.standard_zero_base_input.set(value="4")
        elif self.advanced_zero_value != "0":
            self.standard_zero_base_input.set(value=self.advanced_zero_value + "4")
    
    
    # -- Advanced Event Btn 3 -- #
    def standard_n3_btn(self, e):
        
        # Number x that is passed in when key event pressed
        self.number_value = e
        
        # Number StrVariable that is set
        self.advanced_zero_value = self.standard_zero_base_input.get()
        
        # Checking to see if the StrVariable is x
        if self.advanced_zero_value == "0":
            self.standard_zero_base_input.set(value="3")
        elif self.advanced_zero_value != "0":
            self.standard_zero_base_input.set(value=self.advanced_zero_value + "3")
    
    
    # -- Advanced Event Btn 2 -- #
    def standard_n2_btn(self, e):
        
        # Number x that is passed in when key event pressed
        self.number_value = e
        
        # Number StrVariable that is set
        self.advanced_zero_value = self.standard_zero_base_input.get()
        
        # Checking to see if the StrVariable is x
        if self.advanced_zero_value == "0":
            self.standard_zero_base_input.set(value="2")
        elif self.advanced_zero_value != "0":
            self.standard_zero_base_input.set(value=self.advanced_zero_value + "2")
    
    
    # -- Advanced Event Btn 1 -- #    
    def standard_n1_btn(self, e):
        
        # Number x that is passed in when key event pressed
        self.number_value = e
        
        # Number StrVariable that is set
        self.advanced_zero_value = self.standard_zero_base_input.get()
        
        # Checking to see if the StrVariable is x
        if self.advanced_zero_value == "0":
            self.standard_zero_base_input.set(value="1")
        elif self.advanced_zero_value != "0":
            self.standard_zero_base_input.set(value=self.advanced_zero_value + "1")
    
    
    # -- Advanced Event Btn 0 -- #    
    def standard_n0_btn(self, e):
        
        # Number x that is passed in when key event pressed
        self.number_value = e
        
        # Number StrVariable that is set
        self.advanced_zero_value = self.standard_zero_base_input.get()
        
        # Checking to see if the StrVariable is x
        if self.advanced_zero_value == "0":
            self.standard_zero_base_input.set(value="0")
        elif self.advanced_zero_value != "0":
            self.standard_zero_base_input.set(value=self.advanced_zero_value + "0")
    
    # ------------------------ End Advanced X Number Press Event Methods ---------------------------- #
    
    
    
    # ---------------------------- Advanced Operater Press Event Methods ------------------------------- #
    
    def standard_addition_input(self, operater):
        self.set_value = self.standard_zero_base_input.get()
        
        if self.set_value == "0":
            self.zero_standard_label_widget.configure(text_font=("Arial", 18))
            self.standard_zero_base_input.set(value="Invaild Input!")
            
        elif self.set_value == "Invaild Input!":
            self.zero_standard_label_widget.configure(text_font=("Arial", 26))
            self.standard_zero_base_input.set(value="0")
            
        elif self.set_value != "0":
            self.standard_zero_base_input.set(value=self.set_value + " " + operater + " ")
    
    
    def standard_subtraction_input(self, operater):
        self.set_value = self.standard_zero_base_input.get()
        
        if self.set_value == "0":
            self.zero_standard_label_widget.configure(text_font=("Arial", 18))
            self.standard_zero_base_input.set(value="Invaild Input!")
            
        elif self.set_value == "Invaild Input!":
            self.zero_standard_label_widget.configure(text_font=("Arial", 26))
            self.standard_zero_base_input.set(value="0")
            
        elif self.set_value != "0":
            self.standard_zero_base_input.set(value=self.set_value + " " + operater + " ")
    
    
    def standard_multiplication_input(self, operater):
        self.set_value = self.standard_zero_base_input.get()
        
        if self.set_value == "0":
            self.zero_standard_label_widget.configure(text_font=("Arial", 18))
            self.standard_zero_base_input.set(value="Invaild Input!")
            
        elif self.set_value == "Invaild Input!":
            self.zero_standard_label_widget.configure(text_font=("Arial", 26))
            self.standard_zero_base_input.set(value="0")
            
        elif self.set_value != "0":
            self.standard_zero_base_input.set(value=self.set_value + " " + operater + " ")
    
    
    def standard_divion_input(self, operater):
        self.set_value = self.standard_zero_base_input.get()
        
        if self.set_value == "0":
            self.zero_standard_label_widget.configure(text_font=("Arial", 18))
            self.standard_zero_base_input.set(value="Invaild Input!")
            
        elif self.set_value == "Invaild Input!":
            self.zero_standard_label_widget.configure(text_font=("Arial", 26))
            self.standard_zero_base_input.set(value="0")
            
        elif self.set_value != "0":
            self.standard_zero_base_input.set(value=self.set_value + " " + operater + " ")
    
    
    # ------------------------- End Advanced Operater Press Event Methods ------------------------------- #
    
    
    
    
    # ---------------------------- Misc Advanced Press Event Methods ------------------------------------ #
    
    def standard_enter_btn(self, e):
        value_to_calculate = self.standard_zero_base_input.get()
        toBeCal = value_to_calculate.split(" ")
        measured = len(toBeCal)
        last_digit = re.search(r'\d+$', value_to_calculate)


        # ------------ Checks Addition Operator ------------ #
        
        if toBeCal.count("+") and measured == 3 and last_digit != None:
            first_num = toBeCal[0]
            second_num = toBeCal[2]
            result = int(first_num) + int(second_num)
            self.standard_zero_base_input.set(value=str(result))
            
            
        # ------------ Ends Addition Operator ------------ #
            
            
            
        # ------------ Checks Subtraction Operator ------------ #
        
        elif toBeCal.count("-") and measured == 3 and last_digit != None:
            first_num = toBeCal[0]
            second_num = toBeCal[2]
            result = int(first_num) - int(second_num)
            self.standard_zero_base_input.set(value=str(result))
        
        # ------------ Ends Subtraction Operator ------------ #
            
            
            
        # ------------ Checks Divison Operator ------------ #
        
        elif toBeCal.count("/") and measured == 3 and last_digit != None:
            first_num = toBeCal[0]
            second_num = toBeCal[2]
            if second_num == "0":
                self.zero_standard_label_widget.configure(text_font=("Arial", 16))
                self.standard_zero_base_input.set(value="Cannot Divide by 0")
            else:
                result = int(first_num) // int(second_num)
                self.standard_zero_base_input.set(value=str(result))
        
        # ------------ Ends Divison Operator ------------ #
        
        
        
                
        # ------------ Checks Multiplication Operator ------------ #
        
        elif toBeCal.count("*") and measured == 3 and last_digit != None:
            first_num = toBeCal[0]
            second_num = toBeCal[2]
            result = int(first_num) * int(second_num)
            self.standard_zero_base_input.set(value=str(result))
        # ------------ Ends Multiplication Operator ------------ #
   

    
    def standard_dot_btn(self, e):
        pass
    
    def standard_ce_btn(self, e):
        pass
        
        
    # ---------------------------- End Misc Standard Press Event Methods ------------------------------------ #
        
        
        # ------------------------------ End Standard Methods --------------------------------------- #
        
        
        
        
        
        
        
    # ---------------------------------- Start of Advanced Option ------------------------------------------ #
    
    
    def execute_advanced_option(self, e):
        self.label_pack.pack_forget()
        self.standard_zero_label_input.pack_forget()
        self.first_set_cals_frame.pack_forget()
        self.first_pack.pack_forget()
        self.root.title("Advanced")
        self.root.geometry("235x340") # L x H change back to 270 or 280?
        
    
    # ---------------------------------- End of Advanced Option ------------------------------------------ #



app = App()