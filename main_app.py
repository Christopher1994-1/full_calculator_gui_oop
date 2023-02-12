import customtkinter
import tkinter
from tkinter import *
from currency_exchanges import exchanges, currency_symbols, temps
import os
import re
import math
import tkinter.ttk as ttk
import datetime
from datetime import datetime
import requests


class App:
    def __init__(self):
        self.root = customtkinter.CTk()
        self.something = 0
        self.root.title("Calculator")
        self.root.geometry("248x330") # L x H change back to 270 or 280?
        self.root.config(background="#282828")

        # ------------ Standard Label Frame ------------ #
        self.label_pack = customtkinter.CTkFrame(self.root, fg_color='#282828')
        self.label_pack.pack(side=TOP, anchor="w", padx=(10, 0), pady=(15, 0))
        
        # ------------- Standard Label Label ----------------- #
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
        self.standard_c_btn = tkinter.Button(self.first_set_cals_frame, text="C", width=4, font=("Arial", 16), bg="#404040", fg="white", relief='flat', command=lambda:self.standard_ce_btn("0"))
        self.standard_c_btn.grid(row=0, column=0, sticky="w", padx=2, pady=2)
        # simple fg and bg change when hovered over.
        self.standard_c_btn.bind('<Enter>', lambda e: self.standard_c_btn.config(fg='black', bg='#4D4D4D'))
        self.standard_c_btn.bind('<Leave>', lambda e: self.standard_c_btn.config(fg='white', bg='#404040'))
        # keyboard press events **
        self.root.bind("c", lambda e: self.standard_ce_btn("c"))



        # number / button
        self.btn_div = tkinter.Button(self.first_set_cals_frame, text="/", width=4, font=("Arial", 16), bg="#404040", fg="white", relief='flat', command=lambda: self.standard_divion_input("/"))
        self.btn_div.grid(row=0, column=1, sticky="w", padx=2, pady=2)
        # simple fg and bg change when hovered over.
        self.btn_div.bind('<Enter>', lambda e: self.btn_div.config(fg='black', bg='#4D4D4D'))
        self.btn_div.bind('<Leave>', lambda e: self.btn_div.config(fg='white', bg='#404040'))
        # keyboard press events **
        self.root.bind("/", lambda e: self.standard_divion_input("/"))


        # number * button
        self.btn_mut = tkinter.Button(self.first_set_cals_frame, text="*", width=4, font=("Arial", 16), bg="#404040", fg="white", relief='flat', command=lambda: self.standard_multiplication_input("*"))
        self.btn_mut.grid(row=0, column=2, sticky="w", padx=2, pady=2)
        # simple fg and bg change when hovered over.
        self.btn_mut.bind('<Enter>', lambda e: self.btn_mut.config(fg='black', bg='#4D4D4D'))
        self.btn_mut.bind('<Leave>', lambda e: self.btn_mut.config(fg='white', bg='#404040'))
        # keyboard press events **
        self.root.bind("*", lambda e: self.standard_multiplication_input("*"))


        # number - button
        self.btn_sub = tkinter.Button(self.first_set_cals_frame, text="-", width=4, font=("Arial", 16), bg="#404040", fg="white", relief='flat', command=lambda: self.standard_subtraction_input("-"))
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
        self.btn_7 = tkinter.Button(self.second_btn_frame, text="7", width=4, font=("Arial", 16), bg="#404040", fg="white", relief='flat', command=lambda: self.standard_n7_btn("7"))
        self.btn_7.grid(row=0, column=0, sticky="n", padx=2, pady=2)
        # simple fg and bg change when hovered over.
        self.btn_7.bind('<Enter>', lambda e: self.btn_7.config(fg='black', bg='#4D4D4D'))
        self.btn_7.bind('<Leave>', lambda e: self.btn_7.config(fg='white', bg='#404040'))
        # keyboard press events **
        self.root.bind("7", lambda e: self.standard_n7_btn("7"))



        # number 8 button
        self.btn_8 = tkinter.Button(self.second_btn_frame, text="8", width=4, font=("Arial", 16), bg="#404040", fg="white", relief='flat', command=lambda: self.standard_n8_btn("8"))
        self.btn_8.grid(row=0, column=1, sticky="n", padx=2, pady=2)
        # simple fg and bg change when hovered over.
        self.btn_8.bind('<Enter>', lambda e: self.btn_8.config(fg='black', bg='#4D4D4D'))
        self.btn_8.bind('<Leave>', lambda e: self.btn_8.config(fg='white', bg='#404040'))
        # keyboard press events **
        self.root.bind("8", lambda e: self.standard_n8_btn("8"))



        # number 9 button
        self.btn_9 = tkinter.Button(self.second_btn_frame, text="9", width=4, font=("Arial", 16), bg="#404040", fg="white", relief='flat', command=lambda: self.standard_n9_btn("9"))
        self.btn_9.grid(row=0, column=2, sticky="n", padx=2, pady=2)
        # simple fg and bg change when hovered over.
        self.btn_9.bind('<Enter>', lambda e: self.btn_9.config(fg='black', bg='#4D4D4D'))
        self.btn_9.bind('<Leave>', lambda e: self.btn_9.config(fg='white', bg='#404040'))
        # keyboard press events **
        self.root.bind("9", lambda e: self.standard_n9_btn("9"))


        # number add button
        self.btn_add = tkinter.Button(self.second_btn_frame, text="+", width=4, font=("Arial", 16), bg="#404040", fg="white", height=3, relief='flat', command=lambda:self.standard_addition_input("+"))
        self.btn_add.grid(row=0, column=3, padx=2, pady=2, rowspan=2)
        # simple fg and bg change when hovered over.
        self.btn_add.bind('<Enter>', lambda e: self.btn_add.config(fg='black', bg='#4D4D4D'))
        self.btn_add.bind('<Leave>', lambda e: self.btn_add.config(fg='white', bg='#404040'))
        # keyboard press events **
        self.root.bind("+", lambda e: self.standard_addition_input("+"))
        
        ##########

        # number 4 button
        self.btn_4 = tkinter.Button(self.second_btn_frame, text="4", width=4, font=("Arial", 16), bg="#404040", fg="white", relief='flat', command=lambda:self.standard_n4_btn("4"))
        self.btn_4.grid(row=1, column=0, sticky="n", padx=2, pady=2)
        # simple fg and bg change when hovered over.
        self.btn_4.bind('<Enter>', lambda e: self.btn_4.config(fg='black', bg='#4D4D4D'))
        self.btn_4.bind('<Leave>', lambda e: self.btn_4.config(fg='white', bg='#404040'))
        # keyboard press events **
        self.root.bind("4", lambda e: self.standard_n4_btn("4"))



        # number 5 button
        self.btn_5 = tkinter.Button(self.second_btn_frame, text="5", width=4, font=("Arial", 16), bg="#404040", fg="white", relief='flat', command=lambda:self.standard_n5_btn("5"))
        self.btn_5.grid(row=1, column=1, sticky="n", padx=2, pady=2)
        # simple fg and bg change when hovered over.
        self.btn_5.bind('<Enter>', lambda e: self.btn_5.config(fg='black', bg='#4D4D4D'))
        self.btn_5.bind('<Leave>', lambda e: self.btn_5.config(fg='white', bg='#404040'))
        # keyboard press events **
        self.root.bind("5", lambda e: self.standard_n5_btn("5"))


        # number 6 button
        self.btn_6 = tkinter.Button(self.second_btn_frame, text="6", width=4, font=("Arial", 16), bg="#404040", fg="white", relief='flat', command=lambda: self.standard_n6_btn("6"))
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
        self.btn_1 = tkinter.Button(self.third_btn_frame, text="1", width=4, font=("Arial", 16), bg="#404040", fg="white", relief='flat', command=lambda: self.standard_n1_btn("1"))
        self.btn_1.grid(row=0, column=0, sticky="n", padx=2, pady=2)
        # simple fg and bg change when hovered over.
        self.btn_1.bind('<Enter>', lambda e: self.btn_1.config(fg='black', bg='#4D4D4D'))
        self.btn_1.bind('<Leave>', lambda e: self.btn_1.config(fg='white', bg='#404040'))
        # keyboard press events **
        self.root.bind("1", lambda e: self.standard_n1_btn("1"))


        # number 2 button
        self.btn_2 = tkinter.Button(self.third_btn_frame, text="2", width=4, font=("Arial", 16), bg="#404040", fg="white", relief='flat', command=lambda: self.standard_n2_btn("2"))
        self.btn_2.grid(row=0, column=1, sticky="n", padx=2, pady=2)
        # simple fg and bg change when hovered over.
        self.btn_2.bind('<Enter>', lambda e: self.btn_2.config(fg='black', bg='#4D4D4D'))
        self.btn_2.bind('<Leave>', lambda e: self.btn_2.config(fg='white', bg='#404040'))
        # keyboard press events **
        self.root.bind("2", lambda e: self.standard_n2_btn("2"))


        # number 3 button
        self.btn_3 = tkinter.Button(self.third_btn_frame, text="3", width=4, font=("Arial", 16), bg="#404040", fg="white", relief='flat', command=lambda: self.standard_n3_btn("3"))
        self.btn_3.grid(row=0, column=2, sticky="n", padx=2, pady=2)
        # simple fg and bg change when hovered over.
        self.btn_3.bind('<Enter>', lambda e: self.btn_3.config(fg='black', bg='#4D4D4D'))
        self.btn_3.bind('<Leave>', lambda e: self.btn_3.config(fg='white', bg='#404040'))
        # keyboard press events **
        self.root.bind("3", lambda e: self.standard_n3_btn("3"))


        # number enter button
        self.btn_en = tkinter.Button(self.third_btn_frame, text="Enter", width=4, font=("Arial", 16), bg="#696969", fg="white", height=3, relief='flat', command=lambda: self.standard_enter_btn("0"))
        self.btn_en.grid(row=0, column=3, padx=2, pady=2, rowspan=2)
        # simple fg and bg change when hovered over.
        self.btn_en.bind('<Enter>', lambda e: self.btn_en.config(fg='black', bg='#A9A9A9'))
        self.btn_en.bind('<Leave>', lambda e: self.btn_en.config(fg='white', bg='#696969'))
        # keyboard press events **
        self.root.bind("<Return>", lambda e: self.standard_enter_btn("0"))
        
        ##########

        # number 0 button
        self.btn_0 = tkinter.Button(self.third_btn_frame, text="0", width=9, font=("Arial", 16), bg="#404040", fg="white", relief='flat', command=lambda: self.standard_n0_btn("0"))
        self.btn_0.grid(row=1, column=0, sticky="n", padx=2, pady=2, columnspan=2)
        # simple fg and bg change when hovered over.
        self.btn_0.bind('<Enter>', lambda e: self.btn_0.config(fg='black', bg='#4D4D4D'))
        self.btn_0.bind('<Leave>', lambda e: self.btn_0.config(fg='white', bg='#404040'))
        # keyboard press events **
        self.root.bind("0", lambda e: self.standard_n0_btn("0"))

        # number dot button
        self.btn_dot = tkinter.Button(self.third_btn_frame, text=".", width=4, font=("Arial", 16), bg="#404040", fg="white", relief='flat', command=lambda: self.standard_dot_btn("."))
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
        my_menu.add_cascade(label="Calculators", menu=file_menu)
        
        file_menu.add_command(label="Standard Option", state="disabled")
        file_menu.add_command(label="Advanced Option",  command=lambda:self.execute_advanced_option("0"))
            


        edit_menu = Menu(my_menu, tearoff=0, background='#303030', fg='white')
        my_menu.add_cascade(label="Converters", menu=edit_menu)
        
        edit_menu.add_command(label="Currency Exchange", command=lambda:self.execute_currency_exchange_option())
        edit_menu.add_command(label="Temperature", command=lambda:self.execute_temp_option())
        
        self.root.config(menu=my_menu)

        # destorys the app if user presses escape key (convenience)
        self.root.bind("<Escape>", lambda e: self.root.destroy())
        # deleting stuff
        self.root.bind("<BackSpace>", lambda e: self.standard_backspace())
        # stops the user from resizing the app
        
        self.root.resizable(False,False)


        self.root.mainloop()
        


    # ------------------------------ Standard Option Methods ---------------------------------- #
        
        
        
    # ------------------------- Standard X Number Press Event Methods ----------------------------- #
    
    # -- Advanced Event Btn 9 -- #
    def standard_n9_btn(self, e):
        self.standard_line_check()
        
        # Number x that is passed in when key event pressed
        self.number_value = e
        
        # Number StrVariable that is set
        value = self.standard_zero_base_input.get()
        
        # Checking to see if the StrVariable is x
        
        if value == "Cannot Divide By Zero":
            self.zero_standard_label_widget.configure(text_font=("Arial", 24))
            self.standard_zero_base_input.set(value="9")
        
        elif value == "Invaild Input!":
            self.return_invaild_normal()
            self.standard_zero_base_input.set(value="9")
            
        elif value == "Excessed . Value":
            self.zero_standard_label_widget.configure(text_font=("Arial", 24))
            self.standard_zero_base_input.set(value="9")
            
            
        elif value == "0":
            self.standard_zero_base_input.set(value="9")
            
        elif value != "0":
            self.standard_zero_base_input.set(value=value + "9")
                    
    # -- Advanced Event Btn 8 -- #
    def standard_n8_btn(self, e):
        self.standard_line_check()
        
        # Number x that is passed in when key event pressed
        self.number_value = e
        
        # Number StrVariable that is set
        value = self.standard_zero_base_input.get()
        
        # Checking to see if the StrVariable is x
        
        if value == "Cannot Divide By Zero":
            self.zero_standard_label_widget.configure(text_font=("Arial", 24))
            self.standard_zero_base_input.set(value="8")
        
        elif value == "Invaild Input!":
            self.return_invaild_normal()
            self.standard_zero_base_input.set(value="8")
            
        elif value == "Excessed . Value":
            self.zero_standard_label_widget.configure(text_font=("Arial", 24))
            self.standard_zero_base_input.set(value="8")
            
            
        elif value == "0":
            self.standard_zero_base_input.set(value="8")
            
        elif value != "0":
            self.standard_zero_base_input.set(value=value + "8")        

    # -- Advanced Event Btn 7 -- #
    def standard_n7_btn(self, e):
        self.standard_line_check()
        
        # Number x that is passed in when key event pressed
        self.number_value = e
        
        # Number StrVariable that is set
        value = self.standard_zero_base_input.get()
        
        # Checking to see if the StrVariable is x
        
        if value == "Cannot Divide By Zero":
            self.zero_standard_label_widget.configure(text_font=("Arial", 24))
            self.standard_zero_base_input.set(value="7")
        
        elif value == "Invaild Input!":
            self.return_invaild_normal()
            self.standard_zero_base_input.set(value="7")
            
        elif value == "Excessed . Value":
            self.zero_standard_label_widget.configure(text_font=("Arial", 24))
            self.standard_zero_base_input.set(value="7")
            
            
        elif value == "0":
            self.standard_zero_base_input.set(value="7")
            
        elif value != "0":
            self.standard_zero_base_input.set(value=value + "7")
                 
    # -- Advanced Event Btn 6 -- #
    def standard_n6_btn(self, e):
        self.standard_line_check()
        
        # Number x that is passed in when key event pressed
        self.number_value = e
        
        # Number StrVariable that is set
        value = self.standard_zero_base_input.get()
        
        # Checking to see if the StrVariable is x
        
        if value == "Cannot Divide By Zero":
            self.zero_standard_label_widget.configure(text_font=("Arial", 24))
            self.standard_zero_base_input.set(value="6")
        
        elif value == "Invaild Input!":
            self.return_invaild_normal()
            self.standard_zero_base_input.set(value="6")
            
        elif value == "Excessed . Value":
            self.zero_standard_label_widget.configure(text_font=("Arial", 24))
            self.standard_zero_base_input.set(value="6")
            
            
        elif value == "0":
            self.standard_zero_base_input.set(value="6")
            
        elif value != "0":
            self.standard_zero_base_input.set(value=value + "6")
            
    # -- Advanced Event Btn 5 -- #
    def standard_n5_btn(self, e):
        self.standard_line_check()
        
        # Number x that is passed in when key event pressed
        self.number_value = e
        
        # Number StrVariable that is set
        value = self.standard_zero_base_input.get()
        
        # Checking to see if the StrVariable is x
        
        if value == "Cannot Divide By Zero":
            self.zero_standard_label_widget.configure(text_font=("Arial", 24))
            self.standard_zero_base_input.set(value="5")
        
        elif value == "Invaild Input!":
            self.return_invaild_normal()
            self.standard_zero_base_input.set(value="5")
            
        elif value == "Excessed . Value":
            self.zero_standard_label_widget.configure(text_font=("Arial", 24))
            self.standard_zero_base_input.set(value="5")
            
            
        elif value == "0":
            self.standard_zero_base_input.set(value="5")
            
        elif value != "0":
            self.standard_zero_base_input.set(value=value + "5")
                   
    # -- Advanced Event Btn 4 -- #
    def standard_n4_btn(self, e):
        self.standard_line_check()
        
        # Number x that is passed in when key event pressed
        self.number_value = e
        
        # Number StrVariable that is set
        value = self.standard_zero_base_input.get()
        
        # Checking to see if the StrVariable is x
        
        if value == "Cannot Divide By Zero":
            self.zero_standard_label_widget.configure(text_font=("Arial", 24))
            self.standard_zero_base_input.set(value="4")
        
        elif value == "Invaild Input!":
            self.return_invaild_normal()
            self.standard_zero_base_input.set(value="4")
            
        elif value == "Excessed . Value":
            self.zero_standard_label_widget.configure(text_font=("Arial", 24))
            self.standard_zero_base_input.set(value="4")
            
            
        elif value == "0":
            self.standard_zero_base_input.set(value="4")
            
        elif value != "0":
            self.standard_zero_base_input.set(value=value + "4")
                     
    # -- Advanced Event Btn 3 -- #
    def standard_n3_btn(self, e):
        self.standard_line_check()
        
        # Number x that is passed in when key event pressed
        self.number_value = e
        
        # Number StrVariable that is set
        value = self.standard_zero_base_input.get()
        
        # Checking to see if the StrVariable is x
        
        if value == "Cannot Divide By Zero":
            self.zero_standard_label_widget.configure(text_font=("Arial", 24))
            self.standard_zero_base_input.set(value="3")
        
        elif value == "Invaild Input!":
            self.return_invaild_normal()
            self.standard_zero_base_input.set(value="3")
            
        elif value == "Excessed . Value":
            self.zero_standard_label_widget.configure(text_font=("Arial", 24))
            self.standard_zero_base_input.set(value="3")
            
            
        elif value == "0":
            self.standard_zero_base_input.set(value="3")
            
        elif value != "0":
            self.standard_zero_base_input.set(value=value + "3")
               
    # -- Advanced Event Btn 2 -- #
    def standard_n2_btn(self, e):
        self.standard_line_check()
        
        # Number x that is passed in when key event pressed
        self.number_value = e
        
        # Number StrVariable that is set
        value = self.standard_zero_base_input.get()
        
        # Checking to see if the StrVariable is x
        
        if value == "Cannot Divide By Zero":
            self.zero_standard_label_widget.configure(text_font=("Arial", 24))
            self.standard_zero_base_input.set(value="2")
        
        elif value == "Invaild Input!":
            self.return_invaild_normal()
            self.standard_zero_base_input.set(value="2")
            
        elif value == "Excessed . Value":
            self.zero_standard_label_widget.configure(text_font=("Arial", 24))
            self.standard_zero_base_input.set(value="2")
            
            
        elif value == "0":
            self.standard_zero_base_input.set(value="2")
            
        elif value != "0":
            self.standard_zero_base_input.set(value=value + "2")    
    
    # -- Advanced Event Btn 1 -- #
    def standard_n1_btn(self, e):
        self.standard_line_check()
        
        # Number x that is passed in when key event pressed
        self.number_value = e
        
        # Number StrVariable that is set
        value = self.standard_zero_base_input.get()
        
        # Checking to see if the StrVariable is x
        
        if value == "Cannot Divide By Zero":
            self.zero_standard_label_widget.configure(text_font=("Arial", 24))
            self.standard_zero_base_input.set(value="1")
        
        elif value == "Invaild Input!":
            self.return_invaild_normal()
            self.standard_zero_base_input.set(value="1")
            
        elif value == "Excessed . Value":
            self.zero_standard_label_widget.configure(text_font=("Arial", 24))
            self.standard_zero_base_input.set(value="1")
            
            
        elif value == "0":
            self.standard_zero_base_input.set(value="1")
            
        elif value != "0":
            self.standard_zero_base_input.set(value=value + "1")   
    
    # -- Advanced Event Btn 0 -- #
    def standard_n0_btn(self, e):
        self.standard_line_check()
        
        # Number x that is passed in when key event pressed
        self.number_value = e
        
        # Number StrVariable that is set
        value = self.standard_zero_base_input.get()
        
        # Checking to see if the StrVariable is x
        
        if value == "Cannot Divide By Zero":
            self.zero_standard_label_widget.configure(text_font=("Arial", 24))
            self.standard_zero_base_input.set(value="0")
        
        elif value == "Invaild Input!":
            self.return_invaild_normal()
            self.standard_zero_base_input.set(value="0")
            
        elif value == "Excessed . Value":
            self.zero_standard_label_widget.configure(text_font=("Arial", 24))
            self.standard_zero_base_input.set(value="0")
            
            
        elif value == "0":
            self.standard_zero_base_input.set(value="0")
            
        elif value != "0":
            self.standard_zero_base_input.set(value=value + "0")
            
    # ------------------------ End Advanced X Number Press Event Methods ---------------------------- #
    
    
    
    # ---------------------------- Advanced Operater Press Event Methods ------------------------------- #
    
    def standard_addition_input(self, operater):
        self.set_value = self.standard_zero_base_input.get()
        value_split = self.set_value.split(" ")
        
        if self.set_value == "0":
            self.standard_invaild_input()
            
        elif self.set_value == "Invaild Input!":
            self.return_invaild_normal()
        
        # if '+' is already there, when the user presses + again or any other operater
        elif self.set_value.count("+"):
            # checking to see if any of the values is a float for +
            if self.set_value.count("."):
                first_num = value_split[0]
                second_num = value_split[2]
                    
                if first_num.count(".") and not second_num.count("."):
                    result = float(first_num) + int(second_num)
                    self.standard_zero_base_input.set(value=str(result))
                    
                elif second_num.count(".") and not first_num.count("."):
                    result = int(first_num) + float(second_num)
                    self.standard_zero_base_input.set(value=str(result))
                    
                elif second_num.count(".") and first_num.count("."):
                    result = float(first_num) + float(second_num)
                    self.standard_zero_base_input.set(value=str(result))
                    
            else:
                first_num = value_split[0]
                second_num = value_split[2]
                result = int(first_num) + int(second_num)
                self.standard_zero_base_input.set(value=str(result) + " + ")
        
        
        
        elif self.set_value.count("*"):
            # checking to see if any of the values is a float for +
            if self.set_value.count("."):
                first_num = value_split[0]
                second_num = value_split[2]
                    
                if first_num.count(".") and not second_num.count("."):
                    result = float(first_num) * int(second_num)
                    self.standard_zero_base_input.set(value=str(result))
                    
                elif second_num.count(".") and not first_num.count("."):
                    result = int(first_num) * float(second_num)
                    self.standard_zero_base_input.set(value=str(result))
                    
                elif second_num.count(".") and first_num.count("."):
                    result = float(first_num) * float(second_num)
                    self.standard_zero_base_input.set(value=str(result))
                    
            else:
                first_num = value_split[0]
                second_num = value_split[2]
                result = int(first_num) * int(second_num)
                self.standard_zero_base_input.set(value=str(result) + " + ")
            
        elif self.set_value.count("-"):
            # checking to see if any of the values is a float for +
            if self.set_value.count("."):
                first_num = value_split[0]
                second_num = value_split[2]
                    
                if first_num.count(".") and not second_num.count("."):
                    result = float(first_num) - int(second_num)
                    self.standard_zero_base_input.set(value=str(result))
                    
                elif second_num.count(".") and not first_num.count("."):
                    result = int(first_num) - float(second_num)
                    self.standard_zero_base_input.set(value=str(result))
                    
                elif second_num.count(".") and first_num.count("."):
                    result = float(first_num) - float(second_num)
                    self.standard_zero_base_input.set(value=str(result))
                    
            else:
                first_num = value_split[0]
                second_num = value_split[2]
                result = int(first_num) - int(second_num)
                self.standard_zero_base_input.set(value=str(result) + " + ")
    
    
    
        elif self.set_value.count("/"):
            # checking to see if any of the values is a float for +
            if self.set_value.count("."):
                first_num = value_split[0]
                second_num = value_split[2]
                    
                if first_num.count(".") and not second_num.count("."):
                    if second_num == "0":
                        self.cannot_divide_by_zero()
                    else:
                        result = float(first_num) / int(second_num)
                        self.standard_zero_base_input.set(value=str(result))
                    
                elif second_num.count(".") and not first_num.count("."):
                    if second_num == "0.0":
                        self.cannot_divide_by_zero()
                    else:
                        result = int(first_num) / float(second_num)
                        self.standard_zero_base_input.set(value=str(result))
                    
                elif second_num.count(".") and first_num.count("."):
                    if second_num == "0.0":
                        self.cannot_divide_by_zero()
                    else:
                        result = float(first_num) / float(second_num)
                        self.standard_zero_base_input.set(value=str(result))
                    
            else:
                if second_num == "0":
                    self.cannot_divide_by_zero()
                else:
                    first_num = value_split[0]
                    second_num = value_split[2]
                    result = int(first_num) / int(second_num)
                    self.standard_zero_base_input.set(value=str(result) + " + ")
            
        
            
        elif self.set_value != "0":
            self.standard_zero_base_input.set(value=self.set_value + " " + operater + " ")
    
    
    def standard_subtraction_input(self, operater):
        self.set_value = self.standard_zero_base_input.get()
        value_split = self.set_value.split(" ")
        
        if self.set_value == "0":
            self.standard_invaild_input()
            
        elif self.set_value == "Invaild Input!":
            self.return_invaild_normal()
        
        # if '+' is already there, when the user presses + again or any other operater
        elif self.set_value.count("-"):
            # checking to see if any of the values is a float for +
            if self.set_value.count("."):
                first_num = value_split[0]
                second_num = value_split[2]
                    
                if first_num.count(".") and not second_num.count("."):
                    result = float(first_num) - int(second_num)
                    self.standard_zero_base_input.set(value=str(result))
                    
                elif second_num.count(".") and not first_num.count("."):
                    result = int(first_num) - float(second_num)
                    self.standard_zero_base_input.set(value=str(result))
                    
                elif second_num.count(".") and first_num.count("."):
                    result = float(first_num) - float(second_num)
                    self.standard_zero_base_input.set(value=str(result))
                    
            else:
                first_num = value_split[0]
                second_num = value_split[2]
                result = int(first_num) - int(second_num)
                self.standard_zero_base_input.set(value=str(result) + " - ")
        
        
        
        elif self.set_value.count("*"):
            # checking to see if any of the values is a float for +
            if self.set_value.count("."):
                first_num = value_split[0]
                second_num = value_split[2]
                    
                if first_num.count(".") and not second_num.count("."):
                    result = float(first_num) * int(second_num)
                    self.standard_zero_base_input.set(value=str(result))
                    
                elif second_num.count(".") and not first_num.count("."):
                    result = int(first_num) * float(second_num)
                    self.standard_zero_base_input.set(value=str(result))
                    
                elif second_num.count(".") and first_num.count("."):
                    result = float(first_num) * float(second_num)
                    self.standard_zero_base_input.set(value=str(result))
                    
            else:
                first_num = value_split[0]
                second_num = value_split[2]
                result = int(first_num) * int(second_num)
                self.standard_zero_base_input.set(value=str(result) + " - ")
            
            
        elif self.set_value.count("-"):
            # checking to see if any of the values is a float for +
            if self.set_value.count("."):
                first_num = value_split[0]
                second_num = value_split[2]
                    
                if first_num.count(".") and not second_num.count("."):
                    result = float(first_num) - int(second_num)
                    self.standard_zero_base_input.set(value=str(result))
                    
                elif second_num.count(".") and not first_num.count("."):
                    result = int(first_num) - float(second_num)
                    self.standard_zero_base_input.set(value=str(result))
                    
                elif second_num.count(".") and first_num.count("."):
                    result = float(first_num) - float(second_num)
                    self.standard_zero_base_input.set(value=str(result))
                    
            else:
                first_num = value_split[0]
                second_num = value_split[2]
                result = int(first_num) - int(second_num)
                self.standard_zero_base_input.set(value=str(result) + " - ")
    
    
    
        elif self.set_value.count("/"):
            # checking to see if any of the values is a float for +
            if self.set_value.count("."):
                first_num = value_split[0]
                second_num = value_split[2]
                    
                if first_num.count(".") and not second_num.count("."):
                    if second_num == "0":
                        self.cannot_divide_by_zero()
                    else:
                        result = float(first_num) / int(second_num)
                        self.standard_zero_base_input.set(value=str(result))
                    
                elif second_num.count(".") and not first_num.count("."):
                    if second_num == "0.0":
                        self.cannot_divide_by_zero()
                    else:
                        result = int(first_num) / float(second_num)
                        self.standard_zero_base_input.set(value=str(result))
                    
                elif second_num.count(".") and first_num.count("."):
                    if second_num == "0.0":
                        self.cannot_divide_by_zero()
                    else:
                        result = float(first_num) / float(second_num)
                        self.standard_zero_base_input.set(value=str(result))
                    
            else:
                if second_num == "0":
                    self.cannot_divide_by_zero()
                else:
                    first_num = value_split[0]
                    second_num = value_split[2]
                    result = int(first_num) / int(second_num)
                    self.standard_zero_base_input.set(value=str(result) + " - ")
            
        
            
        elif self.set_value != "0":
            self.standard_zero_base_input.set(value=self.set_value + " " + operater + " ")
    
    
    def standard_multiplication_input(self, operater):
        self.set_value = self.standard_zero_base_input.get()
        value_split = self.set_value.split(" ")
        
        if self.set_value == "0":
            self.standard_invaild_input()
            
        elif self.set_value == "Invaild Input!":
            self.return_invaild_normal()
        
        # if '+' is already there, when the user presses + again or any other operater
        elif self.set_value.count("*"):
            # checking to see if any of the values is a float for +
            if self.set_value.count("."):
                first_num = value_split[0]
                second_num = value_split[2]
                    
                if first_num.count(".") and not second_num.count("."):
                    result = float(first_num) * int(second_num)
                    self.standard_zero_base_input.set(value=str(result))
                    
                elif second_num.count(".") and not first_num.count("."):
                    result = int(first_num) * float(second_num)
                    self.standard_zero_base_input.set(value=str(result))
                    
                elif second_num.count(".") and first_num.count("."):
                    result = float(first_num) * float(second_num)
                    self.standard_zero_base_input.set(value=str(result))
                    
            else:
                first_num = value_split[0]
                second_num = value_split[2]
                result = int(first_num) + int(second_num)
                self.standard_zero_base_input.set(value=str(result) + " * ")
        
        
        
        elif self.set_value.count("+"):
            # checking to see if any of the values is a float for +
            if self.set_value.count("."):
                first_num = value_split[0]
                second_num = value_split[2]
                    
                if first_num.count(".") and not second_num.count("."):
                    result = float(first_num) * int(second_num)
                    self.standard_zero_base_input.set(value=str(result))
                    
                elif second_num.count(".") and not first_num.count("."):
                    result = int(first_num) * float(second_num)
                    self.standard_zero_base_input.set(value=str(result))
                    
                elif second_num.count(".") and first_num.count("."):
                    result = float(first_num) * float(second_num)
                    self.standard_zero_base_input.set(value=str(result))
                    
            else:
                first_num = value_split[0]
                second_num = value_split[2]
                result = int(first_num) * int(second_num)
                self.standard_zero_base_input.set(value=str(result) + " * ")
            
            
        elif self.set_value.count("-"):
            # checking to see if any of the values is a float for +
            if self.set_value.count("."):
                first_num = value_split[0]
                second_num = value_split[2]
                    
                if first_num.count(".") and not second_num.count("."):
                    result = float(first_num) - int(second_num)
                    self.standard_zero_base_input.set(value=str(result))
                    
                elif second_num.count(".") and not first_num.count("."):
                    result = int(first_num) - float(second_num)
                    self.standard_zero_base_input.set(value=str(result))
                    
                elif second_num.count(".") and first_num.count("."):
                    result = float(first_num) - float(second_num)
                    self.standard_zero_base_input.set(value=str(result))
                    
            else:
                first_num = value_split[0]
                second_num = value_split[2]
                result = int(first_num) - int(second_num)
                self.standard_zero_base_input.set(value=str(result) + " * ")
    
    
    
        elif self.set_value.count("/"):
            # checking to see if any of the values is a float for +
            if self.set_value.count("."):
                first_num = value_split[0]
                second_num = value_split[2]
                    
                if first_num.count(".") and not second_num.count("."):
                    if second_num == "0":
                        self.cannot_divide_by_zero()
                    else:
                        result = float(first_num) / int(second_num)
                        self.standard_zero_base_input.set(value=str(result))
                    
                elif second_num.count(".") and not first_num.count("."):
                    if second_num == "0.0":
                        self.cannot_divide_by_zero()
                    else:
                        result = int(first_num) / float(second_num)
                        self.standard_zero_base_input.set(value=str(result))
                    
                elif second_num.count(".") and first_num.count("."):
                    if second_num == "0.0":
                        self.cannot_divide_by_zero()
                    else:
                        result = float(first_num) / float(second_num)
                        self.standard_zero_base_input.set(value=str(result))
                    
            else:
                if second_num == "0":
                    self.cannot_divide_by_zero()
                else:
                    first_num = value_split[0]
                    second_num = value_split[2]
                    result = int(first_num) / int(second_num)
                    self.standard_zero_base_input.set(value=str(result) + " * ")
            
        
            
        elif self.set_value != "0":
            self.standard_zero_base_input.set(value=self.set_value + " " + operater + " ")
    
    
    def standard_divion_input(self, operater):
        self.set_value = self.standard_zero_base_input.get()
        value_split = self.set_value.split(" ")
        
        if self.set_value == "0":
            self.standard_invaild_input()
            
        elif self.set_value == "Invaild Input!":
            self.return_invaild_normal()
        
        # if '+' is already there, when the user presses + again or any other operater
        elif self.set_value.count("+"):
            # checking to see if any of the values is a float for +
            if self.set_value.count("."):
                first_num = value_split[0]
                second_num = value_split[2]
                    
                if first_num.count(".") and not second_num.count("."):
                    result = float(first_num) / int(second_num)
                    self.standard_zero_base_input.set(value=str(result))
                    
                elif second_num.count(".") and not first_num.count("."):
                    result = int(first_num) / float(second_num)
                    self.standard_zero_base_input.set(value=str(result))
                    
                elif second_num.count(".") and first_num.count("."):
                    result = float(first_num) / float(second_num)
                    self.standard_zero_base_input.set(value=str(result))
                    
            else:
                first_num = value_split[0]
                second_num = value_split[2]
                result = int(first_num) + int(second_num)
                self.standard_zero_base_input.set(value=str(result) + " / ")
        
        
        
        elif self.set_value.count("*"):
            # checking to see if any of the values is a float for +
            if self.set_value.count("."):
                first_num = value_split[0]
                second_num = value_split[2]
                    
                if first_num.count(".") and not second_num.count("."):
                    result = float(first_num) * int(second_num)
                    self.standard_zero_base_input.set(value=str(result))
                    
                elif second_num.count(".") and not first_num.count("."):
                    result = int(first_num) * float(second_num)
                    self.standard_zero_base_input.set(value=str(result))
                    
                elif second_num.count(".") and first_num.count("."):
                    result = float(first_num) * float(second_num)
                    self.standard_zero_base_input.set(value=str(result))
                    
            else:
                first_num = value_split[0]
                second_num = value_split[2]
                result = int(first_num) * int(second_num)
                self.standard_zero_base_input.set(value=str(result) + " / ")
            
        elif self.set_value.count("-"):
            # checking to see if any of the values is a float for +
            if self.set_value.count("."):
                first_num = value_split[0]
                second_num = value_split[2]
                    
                if first_num.count(".") and not second_num.count("."):
                    result = float(first_num) - int(second_num)
                    self.standard_zero_base_input.set(value=str(result))
                    
                elif second_num.count(".") and not first_num.count("."):
                    result = int(first_num) - float(second_num)
                    self.standard_zero_base_input.set(value=str(result))
                    
                elif second_num.count(".") and first_num.count("."):
                    result = float(first_num) - float(second_num)
                    self.standard_zero_base_input.set(value=str(result))
                    
            else:
                first_num = value_split[0]
                second_num = value_split[2]
                result = int(first_num) - int(second_num)
                self.standard_zero_base_input.set(value=str(result) + " / ")
    
    
    
        elif self.set_value.count("/"):
            # checking to see if any of the values is a float for +
            if self.set_value.count("."):
                first_num = value_split[0]
                second_num = value_split[2]
                    
                if first_num.count(".") and not second_num.count("."):
                    if second_num == "0":
                        self.cannot_divide_by_zero()
                    else:
                        result = float(first_num) / int(second_num)
                        self.standard_zero_base_input.set(value=str(result))
                    
                elif second_num.count(".") and not first_num.count("."):
                    if second_num == "0.0":
                        self.cannot_divide_by_zero()
                    else:
                        result = int(first_num) / float(second_num)
                        self.standard_zero_base_input.set(value=str(result))
                    
                elif second_num.count(".") and first_num.count("."):
                    if second_num == "0.0":
                        self.cannot_divide_by_zero()
                    else:
                        result = float(first_num) / float(second_num)
                        self.standard_zero_base_input.set(value=str(result))
                    
            else:
                if second_num == "0":
                    self.cannot_divide_by_zero()
                else:
                    first_num = value_split[0]
                    second_num = value_split[2]
                    result = int(first_num) / int(second_num)
                    self.standard_zero_base_input.set(value=str(result) + " / ")
            
        
            
        elif self.set_value != "0":
            self.standard_zero_base_input.set(value=self.set_value + " " + operater + " ")

    # ------------------------- End Advanced Operater Press Event Methods ------------------------------- #
    
    
    
    
    # ---------------------------- Misc Advanced Press Event Methods ------------------------------------ #
    
    def standard_enter_btn(self, e):
        self.standard_line_check()
        value_to_calculate = self.standard_zero_base_input.get()
        toBeCal = value_to_calculate.split(" ")
        measured = len(toBeCal)
        last_digit = re.search(r'\d+$', value_to_calculate)
        
        
        if value_to_calculate == "Cannot Divide By Zero":
            self.return_invaild_normal()


        # ------------ Checks Addition Operator ------------ #
        
        elif toBeCal.count("+") and measured == 3 and last_digit != None:
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
                self.cannot_divide_by_zero()
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
        
        nothing_var = None
    
    
    def standard_dot_btn(self, dot):
        input_value = self.standard_zero_base_input.get()
        
        if input_value == "0":
            self.standard_zero_base_input.set(value="0" + dot)
            
            
        elif input_value == "0.":
            self.zero_standard_label_widget.configure(text_font=("Arial", 14))
            self.standard_zero_base_input.set(value="Excessed . Value")
            
            
        elif input_value != "0" and input_value != "Excessed . Value":
            self.standard_zero_base_input.set(value=input_value + dot)
            
            
        elif input_value == "Excessed . Value":
            self.zero_standard_label_widget.configure(text_font=("Arial", 26))
            self.standard_zero_base_input.set(value="0" + dot)
            
        else:
            self.zero_standard_label_widget.configure(text_font=("Arial", 14))
            self.standard_zero_base_input.set(value="Excessed . Value")
    
    
    def cannot_divide_by_zero(self):
        self.standard_zero_base_input.set("Cannot Divide By Zero")
        self.zero_standard_label_widget.configure(text_font=("Arial", 14))
    
    
    def standard_ce_btn(self, e):
        value = self.standard_zero_base_input.get()
        
        if value == "0":
            pass
        
        elif value == "Invaild Input!":
            self.return_invaild_normal()
            
        else:
            self.zero_standard_label_widget.configure(text_font=("Arial", 24))
            self.standard_zero_base_input.set(value="0")
        
    
    def standard_line_check(self):
        input_value = self.standard_zero_base_input.get() # gets the value
        value_length = len(input_value) # length of input
        
        if input_value != "0" and value_length in range(11, 16):
            self.zero_standard_label_widget.configure(text_font=("Arial", 18))
            
        elif input_value != "0" and value_length in range(16, 20):
            self.zero_standard_label_widget.configure(text_font=("Arial", 14))
        
        elif input_value != "0" and value_length in range(20, 25):
            self.zero_standard_label_widget.configure(text_font=("Arial", 10))
    
    
    def standard_invaild_input(self):
        self.zero_standard_label_widget.configure(text_font=("Arial", 18))
        self.standard_zero_base_input.set(value="Invaild Input!")
        self.btn_div.configure(state="disabled")
        self.btn_mut.configure(state="disabled")
        self.btn_sub.configure(state="disabled")
        self.btn_en.configure(state="disabled")
        self.btn_add.configure(state="disabled")
    
    
    def return_invaild_normal(self):
        self.zero_standard_label_widget.configure(text_font=("Arial", 24))
        self.standard_zero_base_input.set(value="0")
        self.btn_div.configure(state="normal")
        self.btn_mut.configure(state="normal")
        self.btn_sub.configure(state="normal")
        self.btn_en.configure(state="normal")
        self.btn_add.configure(state="normal")
        
    
    def standard_backspace(self):
        value_to_del = self.standard_zero_base_input.get()
        
        if value_to_del == "0" and len(value_to_del) == 1:
            self.standard_zero_base_input.set(value="0")
            
        elif value_to_del != "0" and len(value_to_del) == 1:
            self.standard_zero_base_input.set(value="0")
            
        elif value_to_del != "0" and len(value_to_del) > 1:
            self.standard_zero_base_input.set(value=value_to_del[:-1])
    # ---------------------------- End Misc Standard Press Event Methods ------------------------------------ #
    
    # ---------------------------- Start Standard Switch Option Methods ------------------------------------ #
    
    
    # Method to return to standard from advanced option
    def return_standard_from_advanced(self):
        self.root.title("Calculator")
        
        self.label_pack.pack_forget()
        self.header_label.pack_forget()
        self.zero_label_input.pack_forget()
        self.zero_label_widget.pack_forget()
        self.first_pack.pack_forget()
        self.first_set_cals_frame.pack_forget()
        self.advanced_second_btn_frame.pack_forget()
        self.third_btn_frame.pack_forget()
        self.advanced_fourth_btn_frame.pack_forget()
        self.advanced_fifth_btn_frame.pack_forget()
        self.advanced_sixth_btn_frame.pack_forget()
        
        self.standard_look()
    
    # Method to return to standard from acurrency exchange option
    def return_standard_from_exchange(self):
        self.currency_label_frame.pack_forget()
        self.currency_label.pack_forget()
        self.input_convert_frame.pack_forget()
        self.output_convert_frame.pack_forget()
        self.conversion_rates_frame.pack_forget()
        self.currency_exchange_buttons_frame.pack_forget()
        self.last_exchange_frame.pack_forget()
        self.powered_by_api.pack_forget()
    
        self.standard_look()
    
    # Method to return to standard from tempertaure converter option
    def return_standard_from_temp(self):
        
        
        self.standard_look()
    
    # Method for calling the standard set of frames, buttons etc
    def standard_look(self):
        self.something = 0
        self.root.title("Calculator")
        self.root.iconbitmap("darkModeV.ico")
        self.root.geometry("248x340") # L x H change back to 270 or 280?

        # ------------ Standard Label Frame ------------ #
        self.label_pack = customtkinter.CTkFrame(self.root, fg_color='#282828')
        self.label_pack.pack(side=TOP, anchor="w", padx=(10, 0), pady=(15, 0))
        
        # ------------- Standard Label Label ----------------- #
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
        self.standard_c_btn = tkinter.Button(self.first_set_cals_frame, text="C", width=4, font=("Arial", 16), bg="#404040", fg="white", relief='flat', command=lambda:self.standard_ce_btn("0"))
        self.standard_c_btn.grid(row=0, column=0, sticky="w", padx=2, pady=2)
        # simple fg and bg change when hovered over.
        self.standard_c_btn.bind('<Enter>', lambda e: self.standard_c_btn.config(fg='black', bg='#4D4D4D'))
        self.standard_c_btn.bind('<Leave>', lambda e: self.standard_c_btn.config(fg='white', bg='#404040'))
        # keyboard press events **
        self.root.bind("c", lambda e: self.standard_ce_btn("c"))



        # number / button
        self.btn_div = tkinter.Button(self.first_set_cals_frame, text="/", width=4, font=("Arial", 16), bg="#404040", fg="white", relief='flat', command=lambda: self.standard_divion_input("/"))
        self.btn_div.grid(row=0, column=1, sticky="w", padx=2, pady=2)
        # simple fg and bg change when hovered over.
        self.btn_div.bind('<Enter>', lambda e: self.btn_div.config(fg='black', bg='#4D4D4D'))
        self.btn_div.bind('<Leave>', lambda e: self.btn_div.config(fg='white', bg='#404040'))
        # keyboard press events **
        self.root.bind("/", lambda e: self.standard_divion_input("/"))


        # number * button
        self.btn_mut = tkinter.Button(self.first_set_cals_frame, text="*", width=4, font=("Arial", 16), bg="#404040", fg="white", relief='flat', command=lambda: self.standard_multiplication_input("*"))
        self.btn_mut.grid(row=0, column=2, sticky="w", padx=2, pady=2)
        # simple fg and bg change when hovered over.
        self.btn_mut.bind('<Enter>', lambda e: self.btn_mut.config(fg='black', bg='#4D4D4D'))
        self.btn_mut.bind('<Leave>', lambda e: self.btn_mut.config(fg='white', bg='#404040'))
        # keyboard press events **
        self.root.bind("*", lambda e: self.standard_multiplication_input("*"))


        # number - button
        self.btn_sub = tkinter.Button(self.first_set_cals_frame, text="-", width=4, font=("Arial", 16), bg="#404040", fg="white", relief='flat', command=lambda: self.standard_subtraction_input("-"))
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
        self.btn_7 = tkinter.Button(self.second_btn_frame, text="7", width=4, font=("Arial", 16), bg="#404040", fg="white", relief='flat', command=lambda: self.standard_n7_btn("7"))
        self.btn_7.grid(row=0, column=0, sticky="n", padx=2, pady=2)
        # simple fg and bg change when hovered over.
        self.btn_7.bind('<Enter>', lambda e: self.btn_7.config(fg='black', bg='#4D4D4D'))
        self.btn_7.bind('<Leave>', lambda e: self.btn_7.config(fg='white', bg='#404040'))
        # keyboard press events **
        self.root.bind("7", lambda e: self.standard_n7_btn("7"))



        # number 8 button
        self.btn_8 = tkinter.Button(self.second_btn_frame, text="8", width=4, font=("Arial", 16), bg="#404040", fg="white", relief='flat', command=lambda: self.standard_n8_btn("8"))
        self.btn_8.grid(row=0, column=1, sticky="n", padx=2, pady=2)
        # simple fg and bg change when hovered over.
        self.btn_8.bind('<Enter>', lambda e: self.btn_8.config(fg='black', bg='#4D4D4D'))
        self.btn_8.bind('<Leave>', lambda e: self.btn_8.config(fg='white', bg='#404040'))
        # keyboard press events **
        self.root.bind("8", lambda e: self.standard_n8_btn("8"))



        # number 9 button
        self.btn_9 = tkinter.Button(self.second_btn_frame, text="9", width=4, font=("Arial", 16), bg="#404040", fg="white", relief='flat', command=lambda: self.standard_n9_btn("9"))
        self.btn_9.grid(row=0, column=2, sticky="n", padx=2, pady=2)
        # simple fg and bg change when hovered over.
        self.btn_9.bind('<Enter>', lambda e: self.btn_9.config(fg='black', bg='#4D4D4D'))
        self.btn_9.bind('<Leave>', lambda e: self.btn_9.config(fg='white', bg='#404040'))
        # keyboard press events **
        self.root.bind("9", lambda e: self.standard_n9_btn("9"))


        # number add button
        self.btn_add = tkinter.Button(self.second_btn_frame, text="+", width=4, font=("Arial", 16), bg="#404040", fg="white", height=3, relief='flat', command=lambda: self.standard_addition_input("+"))
        self.btn_add.grid(row=0, column=3, padx=2, pady=2, rowspan=2)
        # simple fg and bg change when hovered over.
        self.btn_add.bind('<Enter>', lambda e: self.btn_add.config(fg='black', bg='#4D4D4D'))
        self.btn_add.bind('<Leave>', lambda e: self.btn_add.config(fg='white', bg='#404040'))
        # keyboard press events **
        self.root.bind("+", lambda e: self.standard_addition_input("+"))
        
        ##########

        # number 4 button
        self.btn_4 = tkinter.Button(self.second_btn_frame, text="4", width=4, font=("Arial", 16), bg="#404040", fg="white", relief='flat', command=lambda: self.standard_n4_btn("4"))
        self.btn_4.grid(row=1, column=0, sticky="n", padx=2, pady=2)
        # simple fg and bg change when hovered over.
        self.btn_4.bind('<Enter>', lambda e: self.btn_4.config(fg='black', bg='#4D4D4D'))
        self.btn_4.bind('<Leave>', lambda e: self.btn_4.config(fg='white', bg='#404040'))
        # keyboard press events **
        self.root.bind("4", lambda e: self.standard_n4_btn("4"))



        # number 5 button
        self.btn_5 = tkinter.Button(self.second_btn_frame, text="5", width=4, font=("Arial", 16), bg="#404040", fg="white", relief='flat', command=lambda: self.standard_n5_btn("5"))
        self.btn_5.grid(row=1, column=1, sticky="n", padx=2, pady=2)
        # simple fg and bg change when hovered over.
        self.btn_5.bind('<Enter>', lambda e: self.btn_5.config(fg='black', bg='#4D4D4D'))
        self.btn_5.bind('<Leave>', lambda e: self.btn_5.config(fg='white', bg='#404040'))
        # keyboard press events **
        self.root.bind("5", lambda e: self.standard_n5_btn("5"))


        # number 6 button
        self.btn_6 = tkinter.Button(self.second_btn_frame, text="6", width=4, font=("Arial", 16), bg="#404040", fg="white", relief='flat', command=lambda: self.standard_n6_btn("6"))
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
        self.btn_1 = tkinter.Button(self.third_btn_frame, text="1", width=4, font=("Arial", 16), bg="#404040", fg="white", relief='flat', command=lambda: self.standard_n1_btn("1"))
        self.btn_1.grid(row=0, column=0, sticky="n", padx=2, pady=2)
        # simple fg and bg change when hovered over.
        self.btn_1.bind('<Enter>', lambda e: self.btn_1.config(fg='black', bg='#4D4D4D'))
        self.btn_1.bind('<Leave>', lambda e: self.btn_1.config(fg='white', bg='#404040'))
        # keyboard press events **
        self.root.bind("1", lambda e: self.standard_n1_btn("1"))


        # number 2 button
        self.btn_2 = tkinter.Button(self.third_btn_frame, text="2", width=4, font=("Arial", 16), bg="#404040", fg="white", relief='flat', command=lambda: self.standard_n2_btn("2"))
        self.btn_2.grid(row=0, column=1, sticky="n", padx=2, pady=2)
        # simple fg and bg change when hovered over.
        self.btn_2.bind('<Enter>', lambda e: self.btn_2.config(fg='black', bg='#4D4D4D'))
        self.btn_2.bind('<Leave>', lambda e: self.btn_2.config(fg='white', bg='#404040'))
        # keyboard press events **
        self.root.bind("2", lambda e: self.standard_n2_btn("2"))


        # number 3 button
        self.btn_3 = tkinter.Button(self.third_btn_frame, text="3", width=4, font=("Arial", 16), bg="#404040", fg="white", relief='flat', command=lambda: self.standard_n3_btn("3"))
        self.btn_3.grid(row=0, column=2, sticky="n", padx=2, pady=2)
        # simple fg and bg change when hovered over.
        self.btn_3.bind('<Enter>', lambda e: self.btn_3.config(fg='black', bg='#4D4D4D'))
        self.btn_3.bind('<Leave>', lambda e: self.btn_3.config(fg='white', bg='#404040'))
        # keyboard press events **
        self.root.bind("3", lambda e: self.standard_n3_btn("3"))


        # number enter button
        self.btn_en = tkinter.Button(self.third_btn_frame, text="Enter", width=4, font=("Arial", 16), bg="#696969", fg="white", height=3, relief='flat', command=lambda: self.standard_enter_btn("0"))
        self.btn_en.grid(row=0, column=3, padx=2, pady=2, rowspan=2)
        # simple fg and bg change when hovered over.
        self.btn_en.bind('<Enter>', lambda e: self.btn_en.config(fg='black', bg='#A9A9A9'))
        self.btn_en.bind('<Leave>', lambda e: self.btn_en.config(fg='white', bg='#696969'))
        # keyboard press events **
        self.root.bind("<Return>", lambda e: self.standard_enter_btn("0"))
        
        ##########

        # number 0 button
        self.btn_0 = tkinter.Button(self.third_btn_frame, text="0", width=9, font=("Arial", 16), bg="#404040", fg="white", relief='flat', command=lambda: self.standard_n0_btn("0"))
        self.btn_0.grid(row=1, column=0, sticky="n", padx=2, pady=2, columnspan=2)
        # simple fg and bg change when hovered over.
        self.btn_0.bind('<Enter>', lambda e: self.btn_0.config(fg='black', bg='#4D4D4D'))
        self.btn_0.bind('<Leave>', lambda e: self.btn_0.config(fg='white', bg='#404040'))
        # keyboard press events **
        self.root.bind("0", lambda e: self.standard_n0_btn("0"))

        # number dot button
        self.btn_dot = tkinter.Button(self.third_btn_frame, text=".", width=4, font=("Arial", 16), bg="#404040", fg="white", relief='flat', command=lambda: self.standard_dot_btn("."))
        self.btn_dot.grid(row=1, column=2, sticky="n", padx=2, pady=2)
        # simple fg and bg change when hovered over.
        self.btn_dot.bind('<Enter>', lambda e: self.btn_dot.config(fg='black', bg='#4D4D4D'))
        self.btn_dot.bind('<Leave>', lambda e: self.btn_dot.config(fg='white', bg='#404040'))
        # keyboard press events **
        self.root.bind(".", lambda e: self.standard_dot_btn("."))

        # end of first pack standard calculations
        
        
        
        # ------------ Main Menu ------------------- #
        self.my_menu = Menu(self.root)


        # ------------- Creating Menu Items ----------------- #
        self.file_menu = Menu(self.my_menu, tearoff=0, background='#303030', fg='white')
        self.my_menu.add_cascade(label="Calculators", menu=self.file_menu)

        # ------------------ Calculator Menu Items --------------- #
        self.file_menu.add_command(label="Standard Option", state="disabled")
        self.file_menu.add_command(label="Advanced Option", command=lambda:self.execute_advanced_option("0"))
        
        
        edit_menu = Menu(self.my_menu, tearoff=0, background='#303030', fg='white')
        self.my_menu.add_cascade(label="Converters", menu=edit_menu)
        
        edit_menu.add_command(label="Currency Exchange", command=lambda:self.execute_currency_exchange_option())
        edit_menu.add_command(label="Temperature", command=lambda:self.standard_to_temp())

        self.root.config(menu=self.my_menu)

        # destorys the app if user presses escape key (convenience)
        self.root.bind("<Escape>", lambda e: self.root.destroy())
        # deleting stuff
        self.root.bind("<BackSpace>", lambda e: self.standard_backspace())


    def standard_to_temp(self):
        self.temperature_label_frame.pack_forget()
        self.main_temp_label.pack_forget()
        self.input_temp_frame.pack_forget()
        self.output_tempertaure_frame.pack_forget()
        self.temperature_frame_for_all_buttons.pack_forget()
        
        self.execute_temp_option()
    
    # ---------------------------- End Standard Switch Option Methods ------------------------------------ #
        
        
        # ------------------------------ End Standard Methods --------------------------------------- #
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
    # --------------------------------- Start of Advanced Option ------------------------------------ #
    
    def execute_advanced_option(self, e):
        self.label_pack.pack_forget()
        self.standard_zero_label_input.pack_forget()
        self.first_set_cals_frame.pack_forget()
        self.first_pack.pack_forget()
        self.root.title("Advanced")
        self.root.geometry("235x360") # L x H change back to 270 or 280?
        

        # -------------------------------- Advanced Label Frame -------------------------------- #
        self.label_pack = customtkinter.CTkFrame(self.root, fg_color='#282828')
        self.label_pack.pack(side=TOP, anchor="w", padx=(10, 0), pady=(10, 0))
        # -------------------------------- Advanced Label Label -------------------------------- #
        self.header_label = customtkinter.CTkLabel(self.label_pack, text="Advanced", bg_color="#282828", height=0, width=0, text_font=("Arial", 14, "bold"))
        self.header_label.pack() # pady=(top, bottom) padx=(left, right) in px





        # --------------------------- Advanced Label Frame For Input -------------------------------- #
        self.zero_label_input = customtkinter.CTkFrame(self.root, fg_color='#282828')
        self.zero_label_input.pack(padx=(10, 15), fill=X)
        # -------------------------------- Advanced Input Label -------------------------------- #
        self.advanced_zero_base_input = customtkinter.StringVar(value="0")
        self.zero_label_widget = customtkinter.CTkLabel(self.zero_label_input, textvariable=self.advanced_zero_base_input, text_font=("Arial", 26), width=0, height=0)
        self.zero_label_widget.pack(side=LEFT)
     
     
     
     
     
        # -------------------------------- Advanced Main Button Frame -------------------------------- #
        self.first_pack = customtkinter.CTkFrame(self.root, fg_color='#282828')
        self.first_pack.pack(side=BOTTOM, anchor="nw", padx=(0, 0), pady=(5, 0))
        # -------------------------------------------------------------------------------------------- #




       # -------------------------------- Advanced Button Frame SET 1 -------------------------------- #
        self.first_set_cals_frame = customtkinter.CTkFrame(self.first_pack, fg_color='#282828')
        self.first_set_cals_frame.pack(side=TOP, anchor='w', padx=(0, 0))
        
        

        # ************************* Advanced CLEAR Button ************************ #
        self.c_btn = tkinter.Button(self.first_set_cals_frame, text="CE", width=3, font=("Arial", 14), bg="#404040", fg="white", relief='flat', command=lambda: self.advanced_ce_btn("c"))
        self.c_btn.grid(row=0, column=0, sticky="w", padx=2, pady=2)
        # simple fg and bg change when hovered over.
        self.c_btn.bind('<Enter>', lambda e: self.c_btn.config(fg='black', bg='#4D4D4D'))
        self.c_btn.bind('<Leave>', lambda e: self.c_btn.config(fg='white', bg='#404040'))
        # keyboard press events **
        self.root.bind("c", lambda e: self.advanced_ce_btn("c"))
        # ************************* End Advanced CLEAR Button ************************ #
        


        # ************************* Advanced PI Button ************************ #
        self.btn_div = tkinter.Button(self.first_set_cals_frame, text="π", width=3, font=("Arial", 14), bg="#404040", fg="white", relief='flat', command=self.advanced_pi)
        self.btn_div.grid(row=0, column=1, sticky="w", padx=2, pady=2)
        # simple fg and bg change when hovered over.
        self.btn_div.bind('<Enter>', lambda e: self.btn_div.config(fg='black', bg='#4D4D4D'))
        self.btn_div.bind('<Leave>', lambda e: self.btn_div.config(fg='white', bg='#404040'))
        # ************************* End Advanced PI Button ************************ #



        # # ************************* Advanced IDK Button ************************ #
        self.btn_mut = tkinter.Button(self.first_set_cals_frame, text="e", width=3, font=("Arial", 14), bg="#404040", fg="white", relief='flat', command=self.e_btn)
        self.btn_mut.grid(row=0, column=2, sticky="w", padx=2, pady=2)
        # simple fg and bg change when hovered over.
        self.btn_mut.bind('<Enter>', lambda e: self.btn_mut.config(fg='black', bg='#4D4D4D'))
        self.btn_mut.bind('<Leave>', lambda e: self.btn_mut.config(fg='white', bg='#404040'))
        # ************************* End Advanced IDK Button ************************ #
        


        # ************************* Advanced Exponent Button ************************ #
        self.btn_exp = tkinter.Button(self.first_set_cals_frame, text="exp", width=3, font=("Arial", 14), bg="#404040", fg="white", relief='flat', command=self.exponent_btn)
        self.btn_exp.grid(row=0, column=3, sticky="w", padx=2, pady=2)
        # simple fg and bg change when hovered over.
        self.btn_exp.bind('<Enter>', lambda e: self.btn_exp.config(fg='black', bg='#4D4D4D'))
        self.btn_exp.bind('<Leave>', lambda e: self.btn_exp.config(fg='white', bg='#404040'))
        # ************************* End Advanced Exponent Button ************************ #

        
        
        # ************************* Advanced Modulo Button ************************ #
        self.btn_mod = tkinter.Button(self.first_set_cals_frame, text="mod", width=3, font=("Arial", 14), bg="#404040", fg="white", relief='flat', command=self.modulo_btn)
        self.btn_mod.grid(row=0, column=4, sticky="w", padx=2, pady=2)
        # simple fg and bg change when hovered over.
        self.btn_mod.bind('<Enter>', lambda e: self.btn_mod.config(fg='black', bg='#4D4D4D'))
        self.btn_mod.bind('<Leave>', lambda e: self.btn_mod.config(fg='white', bg='#404040'))
        # ************************* End Advanced Modulo Button ************************ #
        
        
        # ------------------------------ End Advanced Button Frame SET 1 -------------------------------- #






        # -------------------------------- Advanced Button Frame SET 2 -------------------------------- #

        self.advanced_second_btn_frame = customtkinter.CTkFrame(self.first_pack, fg_color='#282828')
        self.advanced_second_btn_frame.pack(side=TOP, anchor='w', padx=(0, 0))

        
        # ************************* Advanced Square Root Button *************************** #
        self.btn_sqro = tkinter.Button(self.advanced_second_btn_frame, text="√", width=3, font=("Arial", 14), bg="#404040", fg="white", relief='flat', command=lambda:self.advanced_square_root())
        self.btn_sqro.grid(row=0, column=0, sticky="n", padx=2, pady=2)
        # simple fg and bg change when hovered over.
        self.btn_sqro.bind('<Enter>', lambda e: self.btn_sqro.config(fg='black', bg='#4D4D4D'))
        self.btn_sqro.bind('<Leave>', lambda e: self.btn_sqro.config(fg='white', bg='#404040'))
        # ************************* End Advanced Square Root Button ************************ #
        


        # ************************* Advanced Left Parentheses Button *************************** #
        self.btn_leftP = tkinter.Button(self.advanced_second_btn_frame, text="(", width=3, font=("Arial", 14), bg="#404040", fg="white", relief='flat', command=self.left_parentheses)
        self.btn_leftP.grid(row=0, column=1, sticky="n", padx=2, pady=2)
        # simple fg and bg change when hovered over.
        self.btn_leftP.bind('<Enter>', lambda e: self.btn_leftP.config(fg='black', bg='#4D4D4D'))
        self.btn_leftP.bind('<Leave>', lambda e: self.btn_leftP.config(fg='white', bg='#404040'))
        # ************************* End Advanced Left Parentheses Button *************************** #



        # ************************* Advanced Right Parentheses Button *************************** #
        self.btn_rightP = tkinter.Button(self.advanced_second_btn_frame, text=")", width=3, font=("Arial", 14), bg="#404040", fg="white", relief='flat', command=self.right_parentheses)
        self.btn_rightP.grid(row=0, column=2, sticky="n", padx=2, pady=2)
        # simple fg and bg change when hovered over.
        self.btn_rightP.bind('<Enter>', lambda e: self.btn_rightP.config(fg='black', bg='#4D4D4D'))
        self.btn_rightP.bind('<Leave>', lambda e: self.btn_rightP.config(fg='white', bg='#404040'))
        # ************************* End Advanced Right Parentheses Button *************************** #



        # ************************* Advanced Natural Number Button *************************** #
        self.ad_btn_n = tkinter.Button(self.advanced_second_btn_frame, text="n", width=3, font=("Arial", 14), bg="#404040", fg="white", relief='flat')
        self.ad_btn_n.grid(row=0, column=3, padx=2, pady=2)
        # simple fg and bg change when hovered over.
        self.ad_btn_n.bind('<Enter>', lambda e: self.ad_btn_n.config(fg='black', bg='#4D4D4D'))
        self.ad_btn_n.bind('<Leave>', lambda e: self.ad_btn_n.config(fg='white', bg='#404040'))
        # ************************* End Advanced Natural Number Button *************************** #



        # ************************* Advanced Divison Button *************************** #
        self.btn_div2 = tkinter.Button(self.advanced_second_btn_frame, text="÷", width=3, font=("Arial", 14), bg="#404040", fg="white", relief='flat', command=lambda:self.advanced_divison_btn("/"))
        self.btn_div2.grid(row=0, column=4, sticky="n", padx=2, pady=2)
        # simple fg and bg change when hovered over.
        self.btn_div2.bind('<Enter>', lambda e: self.btn_div2.config(fg='black', bg='#4D4D4D'))
        self.btn_div2.bind('<Leave>', lambda e: self.btn_div2.config(fg='white', bg='#404040'))
        # keyboard press events **
        self.root.bind("/", lambda e: self.advanced_divison_btn("/"))
        # ************************* End Advanced Divison Button *************************** #
        
        
        # ------------------------------ End Advanced Button Frame SET 2 -------------------------------- #




      
        # -------------------------------- Advanced Button Frame SET 3 -------------------------------- #
        
        self.third_btn_frame = customtkinter.CTkFrame(self.first_pack, fg_color='#282828')
        self.third_btn_frame.pack(side=TOP, anchor='w', padx=(0, 0))

        
        # ************************* Advanced x2 Button *************************** #
        self.btn_x2 = tkinter.Button(self.third_btn_frame, text="x2", width=3, font=("Arial", 14), bg="#404040", fg="white", relief='flat')
        self.btn_x2.grid(row=0, column=0, sticky="n", padx=2, pady=2)
        # simple fg and bg change when hovered over.
        self.btn_x2.bind('<Enter>', lambda e: self.btn_x2.config(fg='black', bg='#4D4D4D'))
        self.btn_x2.bind('<Leave>', lambda e: self.btn_x2.config(fg='white', bg='#404040'))
        # ************************* End Advanced x2 Button *************************** #


        # ************************* Advanced Number 7 Button *************************** #
        self.btn_7 = tkinter.Button(self.third_btn_frame, text="7", width=3, font=("Arial", 14), bg="#525252", fg="white", relief='flat', command=lambda:self.advanced_n7_btn("7"))
        self.btn_7.grid(row=0, column=1, sticky="n", padx=2, pady=2)
        # simple fg and bg change when hovered over.
        self.btn_7.bind('<Enter>', lambda e: self.btn_7.config(fg='black', bg='#4D4D4D'))
        self.btn_7.bind('<Leave>', lambda e: self.btn_7.config(fg='white', bg='#525252'))
        # keyboard press events **
        self.root.bind("7", lambda e: self.advanced_n7_btn("7"))
        # ************************* End Advanced Number 7 Button *************************** #



        # ************************* Advanced Number 8 Button *************************** #
        self.btn_8 = tkinter.Button(self.third_btn_frame, text="8", width=3, font=("Arial", 14), bg="#525252", fg="white", relief='flat', command=lambda:self.advanced_n8_btn("8"))
        self.btn_8.grid(row=0, column=2, sticky="n", padx=2, pady=2)
        # simple fg and bg change when hovered over.
        self.btn_8.bind('<Enter>', lambda e: self.btn_8.config(fg='black', bg='#4D4D4D'))
        self.btn_8.bind('<Leave>', lambda e: self.btn_8.config(fg='white', bg='#525252'))
        # keyboard press events **
        self.root.bind("8", lambda e: self.advanced_n8_btn("8"))
        # ************************* End Advanced Number 8 Button *************************** #



        # ************************* Advanced Number 9 Button *************************** #
        self.btn_9 = tkinter.Button(self.third_btn_frame, text="9", width=3, font=("Arial", 14), bg="#525252", fg="white", relief='flat', command=lambda:self.advanced_n9_btn("9"))
        self.btn_9.grid(row=0, column=3, padx=2, pady=2)
        # simple fg and bg change when hovered over.
        self.btn_9.bind('<Enter>', lambda e: self.btn_9.config(fg='black', bg='#4D4D4D'))
        self.btn_9.bind('<Leave>', lambda e: self.btn_9.config(fg='white', bg='#525252'))
        # keyboard press events **
        self.root.bind("9", lambda e: self.advanced_n9_btn("9"))
        # ************************* End Advanced Number 9 Button *************************** #



        # ************************* Advanced Multiplication Button *************************** #
        self.btn_x = tkinter.Button(self.third_btn_frame, text="x", width=3, font=("Arial", 14), bg="#404040", fg="white", relief='flat', command=lambda:self.advanced_multiplication_btn("*"))
        self.btn_x.grid(row=0, column=4, sticky="n", padx=2, pady=2)
        # simple fg and bg change when hovered over.
        self.btn_x.bind('<Enter>', lambda e: self.btn_x.config(fg='black', bg='#4D4D4D'))
        self.btn_x.bind('<Leave>', lambda e: self.btn_x.config(fg='white', bg='#404040'))
        # keyboard press events **
        self.root.bind("*", lambda e: self.advanced_multiplication_btn("*"))
        # ************************* End Advanced Multiplication Button *************************** #
        
        
        # ------------------------------ End Advanced Button Frame SET 3 -------------------------------- #
        
        
        
        
        
       # -------------------------------- Advanced Button Frame SET 4 -------------------------------- #
       
        self.advanced_fourth_btn_frame = customtkinter.CTkFrame(self.first_pack, fg_color='#282828')
        self.advanced_fourth_btn_frame.pack(side=TOP, anchor='w', padx=(0, 0))
        
        
        
        # ************************* Advanced |X| Button *************************** #
        self.btn_abs = tkinter.Button(self.advanced_fourth_btn_frame, text="|x|", width=3, font=("Arial", 14), bg="#404040", fg="white", relief='flat')
        self.btn_abs.grid(row=0, column=0, sticky="n", padx=2, pady=2)
        # simple fg and bg change when hovered over.
        self.btn_abs.bind('<Enter>', lambda e: self.btn_abs.config(fg='black', bg='#4D4D4D'))
        self.btn_abs.bind('<Leave>', lambda e: self.btn_abs.config(fg='white', bg='#404040'))
        # ************************* End Advanced |X| Button *************************** #
        
        
        
        # ************************* Advanced Number 4 Button *************************** #
        self.ad_btn_4 = tkinter.Button(self.advanced_fourth_btn_frame, text="4", width=3, font=("Arial", 14), bg="#525252", fg="white", relief='flat', command=lambda:self.advanced_n4_btn("4"))
        self.ad_btn_4.grid(row=0, column=1, sticky="n", padx=2, pady=2)
        # simple fg and bg change when hovered over.
        self.ad_btn_4.bind('<Enter>', lambda e: self.ad_btn_4.config(fg='black', bg='#4D4D4D'))
        self.ad_btn_4.bind('<Leave>', lambda e: self.ad_btn_4.config(fg='white', bg='#525252'))
        # keyboard press events **
        self.root.bind("4", lambda e: self.advanced_n4_btn("4"))
        # ************************* End Advanced Number 4 Button *************************** #
        
        
        
        # ************************* Advanced Number 5 Button *************************** #
        self.ad_btn_5 = tkinter.Button(self.advanced_fourth_btn_frame, text="5", width=3, font=("Arial", 14), bg="#525252", fg="white", relief='flat', command=lambda:self.advanced_n5_btn("5"))
        self.ad_btn_5.grid(row=0, column=2, sticky="n", padx=2, pady=2)
        # simple fg and bg change when hovered over.
        self.ad_btn_5.bind('<Enter>', lambda e: self.ad_btn_5.config(fg='black', bg='#4D4D4D'))
        self.ad_btn_5.bind('<Leave>', lambda e: self.ad_btn_5.config(fg='white', bg='#525252'))
        # keyboard press events **
        self.root.bind("5", lambda e: self.advanced_n5_btn("5"))
        # ************************* End Advanced Number 5 Button *************************** #
        
        
        
        # ************************* Advanced Number 6 Button *************************** #
        self.ad_btn_6 = tkinter.Button(self.advanced_fourth_btn_frame, text="6", width=3, font=("Arial", 14), bg="#525252", fg="white", relief='flat', command=lambda:self.advanced_n6_btn("6"))
        self.ad_btn_6.grid(row=0, column=3, sticky="n", padx=2, pady=2)
        # simple fg and bg change when hovered over.
        self.ad_btn_6.bind('<Enter>', lambda e: self.ad_btn_6.config(fg='black', bg='#4D4D4D'))
        self.ad_btn_6.bind('<Leave>', lambda e: self.ad_btn_6.config(fg='white', bg='#525252'))
        # keyboard press events **
        self.root.bind("6", lambda e: self.advanced_n6_btn("6"))
        # ************************* End Advanced Number 6 Button *************************** #
        
        
        
        # ************************* Advanced Subtraction Button *************************** #
        self.ad_btn_minus = tkinter.Button(self.advanced_fourth_btn_frame, text="-", width=3, font=("Arial", 14), bg="#404040", fg="white", relief='flat', command=lambda:self.advanced_subtraction_btn("-"))
        self.ad_btn_minus.grid(row=0, column=4, sticky="n", padx=2, pady=2)
        # simple fg and bg change when hovered over.
        self.ad_btn_minus.bind('<Enter>', lambda e: self.ad_btn_minus.config(fg='black', bg='#4D4D4D'))
        self.ad_btn_minus.bind('<Leave>', lambda e: self.ad_btn_minus.config(fg='white', bg='#404040'))
        # keyboard press events **
        self.root.bind("-", lambda e: self.advanced_subtraction_btn("-"))
        # ************************* End Advanced Subtraction Button *************************** #
        
        
        # ------------------------------ End Advanced Button Frame SET 4 -------------------------------- #





        # -------------------------------- Advanced Button Frame SET 5 -------------------------------- #
        
        self.advanced_fifth_btn_frame = customtkinter.CTkFrame(self.first_pack, fg_color='#282828')
        self.advanced_fifth_btn_frame.pack(side=TOP, anchor='w', padx=(0, 0))
        
        
        # ************************* Advanced LOG Button *************************** #
        self.btn_log = tkinter.Button(self.advanced_fifth_btn_frame, text="log", width=3, font=("Arial", 14), bg="#404040", fg="white", relief='flat', command=lambda:self.log_btn("0"))
        self.btn_log.grid(row=0, column=0, sticky="n", padx=2, pady=2)
        # simple fg and bg change when hovered over.
        self.btn_log.bind('<Enter>', lambda e: self.btn_log.config(fg='black', bg='#4D4D4D'))
        self.btn_log.bind('<Leave>', lambda e: self.btn_log.config(fg='white', bg='#404040'))
        # ************************* End Advanced LOG Button *************************** #

        
        
        # ************************* Advanced Number 1 Button *************************** #
        self.ad_btn_1 = tkinter.Button(self.advanced_fifth_btn_frame, text="1", width=3, font=("Arial", 14), bg="#525252", fg="white", relief='flat', command=lambda:self.advanced_n1_btn("1"))
        self.ad_btn_1.grid(row=0, column=1, sticky="n", padx=2, pady=2)
        # simple fg and bg change when hovered over.
        self.ad_btn_1.bind('<Enter>', lambda e: self.ad_btn_1.config(fg='black', bg='#4D4D4D'))
        self.ad_btn_1.bind('<Leave>', lambda e: self.ad_btn_1.config(fg='white', bg='#525252'))
        # keyboard press events **
        self.root.bind("1", lambda e: self.advanced_n1_btn("1"))
        # ************************* End Advanced Number 1 Button *************************** #
        
        
        
        # ************************* Advanced Number 2 Button *************************** #
        self.ad_btn_2 = tkinter.Button(self.advanced_fifth_btn_frame, text="2", width=3, font=("Arial", 14), bg="#525252", fg="white", relief='flat', command=lambda:self.advanced_n2_btn("2"))
        self.ad_btn_2.grid(row=0, column=2, sticky="n", padx=2, pady=2)
        # simple fg and bg change when hovered over.
        self.ad_btn_2.bind('<Enter>', lambda e: self.ad_btn_2.config(fg='black', bg='#4D4D4D'))
        self.ad_btn_2.bind('<Leave>', lambda e: self.ad_btn_2.config(fg='white', bg='#525252'))
        # keyboard press events **
        self.root.bind("2", lambda e: self.advanced_n2_btn("2"))
        # ************************* End Advanced Number 2 Button *************************** #
        
        
        
        # ************************* Advanced Number 3 Button *************************** #
        self.ad_btn_3 = tkinter.Button(self.advanced_fifth_btn_frame, text="3", width=3, font=("Arial", 14), bg="#525252", fg="white", relief='flat', command=lambda:self.advanced_n3_btn("3"))
        self.ad_btn_3.grid(row=0, column=3, sticky="n", padx=2, pady=2)
        # simple fg and bg change when hovered over.
        self.ad_btn_3.bind('<Enter>', lambda e: self.ad_btn_3.config(fg='black', bg='#4D4D4D'))
        self.ad_btn_3.bind('<Leave>', lambda e: self.ad_btn_3.config(fg='white', bg='#525252'))
        # keyboard press events **
        self.root.bind("3", lambda e: self.advanced_n3_btn("3"))
        # ************************* End Advanced Number 3 Button *************************** #
        
        
        
        # ************************* Advanced Addition Button *************************** #
        self.ad_btn_plus = tkinter.Button(self.advanced_fifth_btn_frame, text="+", width=3, font=("Arial", 14), bg="#404040", fg="white", relief='flat', command=lambda:self.advanced_addition_btn("+"))
        self.ad_btn_plus.grid(row=0, column=4, sticky="n", padx=2, pady=2)
        # simple fg and bg change when hovered over.
        self.ad_btn_plus.bind('<Enter>', lambda e: self.ad_btn_plus.config(fg='black', bg='#4D4D4D'))
        self.ad_btn_plus.bind('<Leave>', lambda e: self.ad_btn_plus.config(fg='white', bg='#404040'))
        # keyboard press events **
        self.root.bind("+", lambda e: self.advanced_addition_btn("+"))
        # ************************* End Advanced Addition Button *************************** #
        
        
        # ------------------------------ End Advanced Button Frame SET 5 -------------------------------- #
        
        
        
        
        
        # -------------------------------- Advanced Button Frame SET 6 -------------------------------- #
        self.advanced_sixth_btn_frame = customtkinter.CTkFrame(self.first_pack, fg_color='#282828')
        self.advanced_sixth_btn_frame.pack(side=TOP, anchor='w', padx=(0, 0))
        
        
        # ************************* Advanced In Button *************************** #
        self.btn_in = tkinter.Button(self.advanced_sixth_btn_frame, text="in", width=3, font=("Arial", 14), bg="#404040", fg="white", relief='flat', command=lambda:self.in_btn())
        self.btn_in.grid(row=0, column=0, sticky="n", padx=2, pady=2)
        # simple fg and bg change when hovered over.
        self.btn_in.bind('<Enter>', lambda e: self.btn_in.config(fg='black', bg='#4D4D4D'))
        self.btn_in.bind('<Leave>', lambda e: self.btn_in.config(fg='white', bg='#404040'))
        # ************************* End Advanced In Button *************************** #

        
        
        # ************************* Advanced Percentage Button *************************** #
        self.ad_plus_minus = tkinter.Button(self.advanced_sixth_btn_frame, text="%", width=3, font=("Arial", 14), bg="#404040", fg="white", relief='flat', command=lambda:self.percentage())
        self.ad_plus_minus.grid(row=0, column=1, sticky="n", padx=2, pady=2)
        # simple fg and bg change when hovered over.
        self.ad_plus_minus.bind('<Enter>', lambda e: self.ad_plus_minus.config(fg='black', bg='#4D4D4D'))
        self.ad_plus_minus.bind('<Leave>', lambda e: self.ad_plus_minus.config(fg='white', bg='#404040'))
        # ************************* End Advanced Plus/Minus Button *************************** #
        
        
        # ************************* Advanced Number 0 Button *************************** #
        self.ad_btn_0 = tkinter.Button(self.advanced_sixth_btn_frame, text="0", width=3, font=("Arial", 14), bg="#525252", fg="white", relief='flat', command=lambda:self.advanced_n0_btn("0"))
        self.ad_btn_0.grid(row=0, column=2, sticky="n", padx=2, pady=2)
        # simple fg and bg change when hovered over.
        self.ad_btn_0.bind('<Enter>', lambda e: self.ad_btn_0.config(fg='black', bg='#4D4D4D'))
        self.ad_btn_0.bind('<Leave>', lambda e: self.ad_btn_0.config(fg='white', bg='#525252'))
        # keyboard press events **
        self.root.bind("0", lambda e: self.advanced_n0_btn("0"))
        # ************************* End Advanced Number 0 Button *************************** #
        
        
        
        # ************************* Advanced DOT Button *************************** #
        self.ad_btn_dot = tkinter.Button(self.advanced_sixth_btn_frame, text=".", width=3, font=("Arial", 14), bg="#404040", fg="white", relief='flat', command=lambda:self.advanced_dot_btn("."))
        self.ad_btn_dot.grid(row=0, column=3, sticky="n", padx=2, pady=2)
        # simple fg and bg change when hovered over.
        self.ad_btn_dot.bind('<Enter>', lambda e: self.ad_btn_dot.config(fg='black', bg='#4D4D4D'))
        self.ad_btn_dot.bind('<Leave>', lambda e: self.ad_btn_dot.config(fg='white', bg='#404040'))
        # keyboard press events **
        self.root.bind(".", lambda e: self.advanced_dot_btn("."))
        # ************************* End Advanced DOT Button *************************** #
        
        
        
        # ************************* Advanced Equals Button *************************** #
        self.ad_btn_equals = tkinter.Button(self.advanced_sixth_btn_frame, text="=", width=3, font=("Arial", 14), bg="#808A87", fg="white", relief='flat', command=lambda:self.advanced_enter_btn("0"))
        self.ad_btn_equals.grid(row=0, column=4, sticky="n", padx=2, pady=2)
        # simple fg and bg change when hovered over.
        self.ad_btn_equals.bind('<Enter>', lambda e: self.ad_btn_equals.config(fg='black', bg='#4D4D4D'))
        self.ad_btn_equals.bind('<Leave>', lambda e: self.ad_btn_equals.config(fg='white', bg='#808A87'))
        # keyboard press events **
        self.root.bind("<Return>", lambda e: self.advanced_enter_btn("0"))
        # ************************* End Advanced Equals Button *************************** #
        
        self.root.bind("<BackSpace>", lambda e: self.advanced_backspace(" "))
        
        
        
        # menu
        my_menu = Menu(self.root)


        # create menu items
        file_menu = Menu(my_menu, tearoff=0, background='#303030', fg='white')
        my_menu.add_cascade(label="Calculators", menu=file_menu)

        file_menu.add_command(label="Standard Option", command=lambda:self.return_standard_from_advanced())
        file_menu.add_command(label="Advanced Option", state="disabled")
            

        edit_menu = Menu(my_menu, tearoff=0, background='#303030', fg='white')
        my_menu.add_cascade(label="Converters", menu=edit_menu)
        
        edit_menu.add_command(label="Currency Exchange", command=lambda:self.return_exchange_from_advanced())
        edit_menu.add_command(label="Temperature", command=lambda:self.advanced_to_temp())

        self.root.config(menu=my_menu)

        # destorys the app if user presses escape key (convenience)
        self.root.bind("<Escape>", lambda e: self.root.destroy())
        # deleting stuff
        self.root.bind("<BackSpace>", lambda e: self.standard_backspace())
        # stops the user from resizing the app

        
        # ------------------------------ End Advanced Button Frame SET 6 -------------------------------- #
        
        nothing_var = None
        
        
        
            # ---------------------------- Advanced Special Methods ----------------------------- #
    
    def advanced_pi(self):
        pi_value = "3.14159"
        input_value = self.advanced_zero_base_input.get()
        
        # if value is 0 put pi value as input value
        if input_value == "0":
            self.advanced_zero_base_input.set(value=pi_value)
            
            
        # multipling pi by y amount
        elif input_value != "0" and input_value.count("*"):
            split_value = input_value.split(" ")
            number_one = split_value[0]
            if "." in number_one:
                final_value = float(number_one) * float(pi_value)
                self.advanced_zero_base_input.set(value=str(final_value))
            else:
                final_value = int(number_one) * float(pi_value)
                self.advanced_zero_base_input.set(value=str(final_value))
            
            
        # subtracting pi value by y amount
        elif input_value != "0" and input_value.count("-"):
            split_value = input_value.split(" ")
            number_one = split_value[0]
            if "." in number_one:
                final_value = float(number_one) - float(pi_value)
                self.advanced_zero_base_input.set(value=str(final_value))
            else:
                final_value = int(number_one) - float(pi_value)
                self.advanced_zero_base_input.set(value=str(final_value))
            
            
        # adding x value to pi value
        elif input_value != "0" and input_value.count("+"):
            split_value = input_value.split(" ")
            number_one = split_value[0]
            if "." in number_one:
                final_value = float(number_one) + float(pi_value)
                self.advanced_zero_base_input.set(value=str(final_value))
            else:
                final_value = int(number_one) + float(pi_value)
                self.advanced_zero_base_input.set(value=str(final_value))
            
            
        # divding y amount by pi value
        elif input_value != "0" and input_value.count("/"):
            split_value = input_value.split(" ")
            number_one = split_value[0]
            if "." in number_one:
                final_value = float(number_one) / float(pi_value)
                value_toStr = str(final_value)
                value_length = len(value_toStr) - 6
                value_cut = value_toStr[:-value_length]
                self.advanced_zero_base_input.set(value=str(value_cut))
            else:
                final_value = int(number_one) / float(pi_value)
                value_toStr = str(final_value)
                value_length = len(value_toStr) - 6
                value_cut = value_toStr[:-value_length]
                self.advanced_zero_base_input.set(value=str(value_cut))
    
    
    def advanced_square_root(self):
        self.line_check()
        input_value = self.advanced_zero_base_input.get() # gets the value
        
        if input_value == "0":
            self.zero_label_widget.configure(text_font=("Arial", 26))
            self.advanced_zero_base_input.set(value=input_value + "√=0")
            
        elif input_value != "0" and not input_value.count("√ = ") and input_value != "Value Error:" and "." not in input_value:
            value_sqaure_root = str(math.sqrt(int(input_value)))
            
            if len(value_sqaure_root) > 4:
                value_length = len(value_sqaure_root) - 3
                value_cut = value_sqaure_root[:-value_length]
                self.zero_label_widget.configure(text_font=("Arial", 26))
                self.advanced_zero_base_input.set(value=input_value + "√ = " + value_cut)
                
            elif value_sqaure_root.endswith(".0"):
                remove_dot = value_sqaure_root.replace(".0", "")
                self.zero_label_widget.configure(text_font=("Arial", 26))
                self.advanced_zero_base_input.set(value=input_value + "√ = " + remove_dot)
                
        elif "." in input_value and not input_value.count("√ = "):
            value_sqaure_root = str(math.sqrt(float(input_value)))
            print(value_sqaure_root) # 1.5873373737
            sqrt_toStr = str(value_sqaure_root)
            value_length = len(sqrt_toStr) - 6
            value_cut = sqrt_toStr[:-value_length]
            self.zero_label_widget.configure(text_font=("Arial", 14))
            self.advanced_zero_base_input.set(value=f"{input_value} √ = {value_cut}")
                
        elif input_value.count("√ = "):
                self.zero_label_widget.configure(text_font=("Arial", 14))
                self.advanced_zero_base_input.set(value="Value Error:")
        
        elif input_value == "Value Error:":
                self.zero_label_widget.configure(text_font=("Arial", 26))
                self.advanced_zero_base_input.set(value="0")
            
    
    def exponent_btn(self):
        self.line_check()
        label_value = self.advanced_zero_base_input.get()
        if label_value == "0":
            self.advanced_zero_base_input.set(value="0")
            
        elif label_value != "0" and not label_value.count("^"):
            self.advanced_zero_base_input.set(value=label_value + " ^ ")
            
        elif label_value != "0" and " ^ " in label_value:
            pow_value_split = str(label_value).split(" ")
            number_one = pow_value_split[0]
            number_two = pow_value_split[2]
            value = int(number_one) ** int(number_two)
            self.advanced_zero_base_input.set(value=str(value))
            
            
    def modulo_btn(self):
        self.line_check()
        label_value = self.advanced_zero_base_input.get()
        if label_value == "0":
            self.advanced_zero_base_input.set(value="0")
            
        elif label_value != "0" and not label_value.count("mod"):
            self.advanced_zero_base_input.set(value=label_value + " mod ")
            
        elif label_value != "0" and " mod " in label_value:
            pow_value_split = str(label_value).split(" ")
            number_one = pow_value_split[0]
            number_two = pow_value_split[2]
            value = int(number_one) % int(number_two)
            self.advanced_zero_base_input.set(value=str(value))
    
    
    def e_btn(self):
        self.line_check()
        e_value = "2.71828"
        other_value = self.advanced_zero_base_input.get() # value that is there
        
        if other_value == "0":
            self.advanced_zero_base_input.set(value=e_value)
            
        # multipling Euler's number by y amount
        elif other_value != "0" and other_value.count("*"):
            split_value = other_value.split(" ")
            number_one = split_value[0]
            if "." in number_one:
                final_value = float(number_one) * float(e_value)
                self.advanced_zero_base_input.set(value=str(final_value))
            else:
                final_value = int(number_one) * float(e_value)
                self.advanced_zero_base_input.set(value=str(final_value))
            
            
        # subtracting Euler's number by y amount
        elif other_value != "0" and other_value.count("-"):
            split_value = other_value.split(" ")
            number_one = split_value[0]
            if "." in number_one:
                final_value = float(number_one) - float(e_value)
                self.advanced_zero_base_input.set(value=str(final_value))
            else:
                final_value = int(number_one) - float(e_value)
                self.advanced_zero_base_input.set(value=str(final_value))
            
            
        # adding x value to Euler's number
        elif other_value != "0" and other_value.count("+"):
            split_value = other_value.split(" ")
            number_one = split_value[0]
            if "." in number_one:
                final_value = float(number_one) + float(e_value)
                self.advanced_zero_base_input.set(value=str(final_value))
            else:
                final_value = int(number_one) + float(e_value)
                self.advanced_zero_base_input.set(value=str(final_value))
            
            
        # divding y amount by Euler's number
        elif other_value != "0" and other_value.count("/"):
            split_value = other_value.split(" ")
            number_one = split_value[0]
            if "." in number_one:
                final_value = float(number_one) / float(e_value)
                value_toStr = str(final_value)
                value_length = len(value_toStr) - 6
                value_cut = value_toStr[:-value_length]
                self.advanced_zero_base_input.set(value=str(value_cut))
            else:
                final_value = int(number_one) / float(e_value)
                value_toStr = str(final_value)
                value_length = len(value_toStr) - 6
                value_cut = value_toStr[:-value_length]
                self.advanced_zero_base_input.set(value=str(value_cut))
        
        
    def left_parentheses(self):
        self.line_check()
        value = self.advanced_zero_base_input.get()
        
        if value == "0":
            self.advanced_zero_base_input.set(value="(")


    def right_parentheses(self):
        self.line_check()
        value = self.advanced_zero_base_input.get()
        
        if value != "0":
            self.advanced_zero_base_input.set(value=value + ")")
    
    
    def log_btn(self, o):
        """Method for the logarithm calculation, log10

        Args:
            o (str): none
        """
        value = self.advanced_zero_base_input.get()
        
        if value == "0":
            self.invaild_input()
            
        elif value != "0" and not value.count("."):
            log_value = math.log10(int(value))
            self.advanced_zero_base_input.set(value=str(log_value))
            self.line_check()
        
        elif value != "0" and value.count("."):
            try:
                log_value = math.log10(float(value))
                self.advanced_zero_base_input.set(value=str(log_value))
                self.line_check()
            except:
                self.invaild_input()
            
            
    def in_btn(self):
        value = self.advanced_zero_base_input.get()
        
        if value == "0":
            self.invaild_input()
            
        elif value != "0" and not value.count("."):
            log_value = math.log(int(value))
            self.advanced_zero_base_input.set(value=str(log_value))
            self.line_check()
        
        elif value != "0" and value.count("."):
            try:
                log_value = math.log(float(value))
                self.advanced_zero_base_input.set(value=str(log_value))
                self.line_check()
            except:
                self.invaild_input()
                
    
    def percentage(self):
        value = self.advanced_zero_base_input.get()
        
        if value == "0" and len(value) == 1:
            self.invaild_input()
        elif value != "0":
            self.advanced_zero_base_input.set(value=value + " % ")
    # ---------------------------- Advanced Special Methods ----------------------------- #
        
 
    # ------------------------- Advanced X Number Press Event Methods ----------------------------- #
    
   
    # -- Advanced Event Btn 9 -- #
    def advanced_n9_btn(self, e):
        self.line_check()
        
        # Number x that is passed in when key event pressed
        self.number_value = e
        
        # Number StrVariable that is set
        self.advanced_zero_value = self.advanced_zero_base_input.get()
        
        # Checking to see if the StrVariable is x
        if self.advanced_zero_value == "0":
            self.advanced_zero_base_input.set(value="9")
        
        elif self.advanced_zero_value == "Excessed . Value":
            self.zero_label_widget.configure(text_font=("Arial", 24))
            self.advanced_zero_base_input.set(value="9")
            
        elif self.advanced_zero_value == "Cannot Divide by 0":
            self.zero_label_widget.configure(text_font=("Arial", 24))
            self.advanced_zero_base_input.set(value="9")
            
        elif self.advanced_zero_value == "Value Error:":
            self.zero_label_widget.configure(text_font=("Arial", 24))
            self.advanced_zero_base_input.set(value="9")
            
        elif self.advanced_zero_value == "Invaild Input!":
            self.invaild_input_return()
            self.advanced_zero_base_input.set(value="9")
           
            
            
        elif self.advanced_zero_value != "0":
            self.advanced_zero_base_input.set(value=self.advanced_zero_value + "9")
    
    # -- Advanced Event Btn 8 -- #
    def advanced_n8_btn(self, e):
        self.line_check()
        
        # Number x that is passed in when key event pressed
        self.number_value = e
        
        # Number StrVariable that is set
        self.advanced_zero_value = self.advanced_zero_base_input.get()
        
        # Checking to see if the StrVariable is x
        if self.advanced_zero_value == "0":
            self.advanced_zero_base_input.set(value="8")
        
        elif self.advanced_zero_value == "Excessed . Value":
            self.zero_label_widget.configure(text_font=("Arial", 24))
            self.advanced_zero_base_input.set(value="8")
            
        elif self.advanced_zero_value == "Cannot Divide by 0":
            self.zero_label_widget.configure(text_font=("Arial", 24))
            self.advanced_zero_base_input.set(value="8")
            
        elif self.advanced_zero_value == "Value Error:":
            self.zero_label_widget.configure(text_font=("Arial", 24))
            self.advanced_zero_base_input.set(value="8")
            
            
        elif self.advanced_zero_value == "Invaild Input!":
            self.invaild_input_return()
            self.advanced_zero_base_input.set(value="8")
 
            
            
        elif self.advanced_zero_value != "0":
            self.advanced_zero_base_input.set(value=self.advanced_zero_value + "8")
    
    # -- Advanced Event Btn 7 -- #
    def advanced_n7_btn(self, e):
        self.line_check()
        
        # Number x that is passed in when key event pressed
        self.number_value = e
        
        # Number StrVariable that is set
        self.advanced_zero_value = self.advanced_zero_base_input.get()
        
        # Checking to see if the StrVariable is x
        if self.advanced_zero_value == "0":
            self.advanced_zero_base_input.set(value="7")
            
        elif self.advanced_zero_value == "Excessed . Value":
            self.zero_label_widget.configure(text_font=("Arial", 24))
            self.advanced_zero_base_input.set(value="7")
            
        elif self.advanced_zero_value == "Cannot Divide by 0":
            self.zero_label_widget.configure(text_font=("Arial", 24))
            self.advanced_zero_base_input.set(value="7")
            
        elif self.advanced_zero_value == "Value Error:":
            self.zero_label_widget.configure(text_font=("Arial", 24))
            self.advanced_zero_base_input.set(value="7")
            
        elif self.advanced_zero_value == "Invaild Input!":
            self.invaild_input_return()
            self.advanced_zero_base_input.set(value="7")

            
        elif self.advanced_zero_value != "0":
            self.advanced_zero_base_input.set(value=self.advanced_zero_value + "7")
    
    # -- Advanced Event Btn 6 -- #
    def advanced_n6_btn(self, e):
        self.line_check()
        
        # Number x that is passed in when key event pressed
        self.number_value = e
        
        # Number StrVariable that is set
        self.advanced_zero_value = self.advanced_zero_base_input.get()
        
        # Checking to see if the StrVariable is x
        if self.advanced_zero_value == "0":
            self.advanced_zero_base_input.set(value="6")
            
        elif self.advanced_zero_value == "Excessed . Value":
            self.zero_label_widget.configure(text_font=("Arial", 24))
            self.advanced_zero_base_input.set(value="6")
            
        elif self.advanced_zero_value == "Cannot Divide by 0":
            self.zero_label_widget.configure(text_font=("Arial", 24))
            self.advanced_zero_base_input.set(value="6")
            
        elif self.advanced_zero_value == "Value Error:":
            self.zero_label_widget.configure(text_font=("Arial", 24))
            self.advanced_zero_base_input.set(value="6")
            
        elif self.advanced_zero_value == "Invaild Input!":
            self.invaild_input_return()
            self.advanced_zero_base_input.set(value="6")
 
            
        elif self.advanced_zero_value != "0":
            self.advanced_zero_base_input.set(value=self.advanced_zero_value + "6")
     
    # -- Advanced Event Btn 5 -- #
    def advanced_n5_btn(self, e):
        self.line_check()
        
        # Number x that is passed in when key event pressed
        self.number_value = e
        
        # Number StrVariable that is set
        self.advanced_zero_value = self.advanced_zero_base_input.get()
        
        # Checking to see if the StrVariable is x
        if self.advanced_zero_value == "0":
            self.advanced_zero_base_input.set(value="5")
            
        elif self.advanced_zero_value == "Excessed . Value":
            self.zero_label_widget.configure(text_font=("Arial", 24))
            self.advanced_zero_base_input.set(value="5")
            
        elif self.advanced_zero_value == "Cannot Divide by 0":
            self.zero_label_widget.configure(text_font=("Arial", 24))
            self.advanced_zero_base_input.set(value="5")
            
        elif self.advanced_zero_value == "Value Error:":
            self.zero_label_widget.configure(text_font=("Arial", 24))
            self.advanced_zero_base_input.set(value="5")
    
        elif self.advanced_zero_value == "Invaild Input!":
            self.invaild_input_return()
            self.advanced_zero_base_input.set(value="5")

            
        elif self.advanced_zero_value != "0":
            self.advanced_zero_base_input.set(value=self.advanced_zero_value + "5")
    
    # -- Advanced Event Btn 4 -- #
    def advanced_n4_btn(self, e):
        self.line_check()
        
        # Number x that is passed in when key event pressed
        self.number_value = e
        
        # Number StrVariable that is set
        self.advanced_zero_value = self.advanced_zero_base_input.get()
        
        # Checking to see if the StrVariable is x
        if self.advanced_zero_value == "0":
            self.advanced_zero_base_input.set(value="4")
        elif self.advanced_zero_value == "Excessed . Value":
            self.zero_label_widget.configure(text_font=("Arial", 24))
            self.advanced_zero_base_input.set(value="4")
            
        elif self.advanced_zero_value == "Cannot Divide by 0":
            self.zero_label_widget.configure(text_font=("Arial", 24))
            self.advanced_zero_base_input.set(value="4")
            
        elif self.advanced_zero_value == "Value Error:":
            self.zero_label_widget.configure(text_font=("Arial", 24))
            self.advanced_zero_base_input.set(value="4")
    
        elif self.advanced_zero_value == "Invaild Input!":
            self.invaild_input_return()
            self.advanced_zero_base_input.set(value="4")

            
        elif self.advanced_zero_value != "0":
            self.advanced_zero_base_input.set(value=self.advanced_zero_value + "4")
     
    # -- Advanced Event Btn 3 -- #
    def advanced_n3_btn(self, e):
        self.line_check()
        
        # Number x that is passed in when key event pressed
        self.number_value = e
        
        # Number StrVariable that is set
        self.advanced_zero_value = self.advanced_zero_base_input.get()
        
        # Checking to see if the StrVariable is x
        if self.advanced_zero_value == "0":
            self.advanced_zero_base_input.set(value="3")
            
        elif self.advanced_zero_value == "Excessed . Value":
            self.zero_label_widget.configure(text_font=("Arial", 24))
            self.advanced_zero_base_input.set(value="3")
            
        elif self.advanced_zero_value == "Cannot Divide by 0":
            self.zero_label_widget.configure(text_font=("Arial", 24))
            self.advanced_zero_base_input.set(value="3")
            
        elif self.advanced_zero_value == "Value Error:":
            self.zero_label_widget.configure(text_font=("Arial", 24))
            self.advanced_zero_base_input.set(value="3")
        
        elif self.advanced_zero_value == "Invaild Input!":
            self.invaild_input_return()
            self.advanced_zero_base_input.set(value="3")
 
            
        elif self.advanced_zero_value != "0":
            self.advanced_zero_base_input.set(value=self.advanced_zero_value + "3")
      
    # -- Advanced Event Btn 2 -- #
    def advanced_n2_btn(self, e):
        self.line_check()
        
        # Number x that is passed in when key event pressed
        self.number_value = e
        
        # Number StrVariable that is set
        self.advanced_zero_value = self.advanced_zero_base_input.get()
        
        # Checking to see if the StrVariable is x
        if self.advanced_zero_value == "0":
            self.advanced_zero_base_input.set(value="2")
            
        elif self.advanced_zero_value == "Excessed . Value":
            self.zero_label_widget.configure(text_font=("Arial", 24))
            self.advanced_zero_base_input.set(value="2")
            
        elif self.advanced_zero_value == "Cannot Divide by 0":
            self.zero_label_widget.configure(text_font=("Arial", 24))
            self.advanced_zero_base_input.set(value="2")
            
        elif self.advanced_zero_value == "Value Error:":
            self.zero_label_widget.configure(text_font=("Arial", 24))
            self.advanced_zero_base_input.set(value="2")
        
        elif self.advanced_zero_value == "Invaild Input!":
            self.invaild_input_return()
            self.advanced_zero_base_input.set(value="2")
            
        elif self.advanced_zero_value != "0":
            self.advanced_zero_base_input.set(value=self.advanced_zero_value + "2")
      
    # -- Advanced Event Btn 1 -- #    
    def advanced_n1_btn(self, e):
        self.line_check()
        
        # Number x that is passed in when key event pressed
        self.number_value = e
        
        # Number StrVariable that is set
        self.advanced_zero_value = self.advanced_zero_base_input.get()
        
        # Checking to see if the StrVariable is x
        if self.advanced_zero_value == "0":
            self.advanced_zero_base_input.set(value="1")
            
        elif self.advanced_zero_value == "Excessed . Value":
            self.zero_label_widget.configure(text_font=("Arial", 24))
            self.advanced_zero_base_input.set(value="1")
            
        elif self.advanced_zero_value == "Cannot Divide by 0":
            self.zero_label_widget.configure(text_font=("Arial", 24))
            self.advanced_zero_base_input.set(value="1")
            
        elif self.advanced_zero_value == "Value Error:":
            self.zero_label_widget.configure(text_font=("Arial", 24))
            self.advanced_zero_base_input.set(value="1")
    
        elif self.advanced_zero_value == "Invaild Input!":
            self.invaild_input_return()
            self.advanced_zero_base_input.set(value="1")
 
            
        elif self.advanced_zero_value != "0":
            self.advanced_zero_base_input.set(value=self.advanced_zero_value + "1")
     
    # -- Advanced Event Btn 0 -- #    
    def advanced_n0_btn(self, e):
        self.line_check()
        
        # Number x that is passed in when key event pressed
        self.number_value = e
        
        # Number StrVariable that is set
        self.advanced_zero_value = self.advanced_zero_base_input.get()
        
        # Checking to see if the StrVariable is x
        if self.advanced_zero_value == "0":
            self.advanced_zero_base_input.set(value="0")
            
        elif self.advanced_zero_value == "Excessed . Value":
            self.zero_label_widget.configure(text_font=("Arial", 24))
            self.advanced_zero_base_input.set(value="0")
            
        elif self.advanced_zero_value == "Cannot Divide by 0":
            self.zero_label_widget.configure(text_font=("Arial", 24))
            self.advanced_zero_base_input.set(value="0")
            
        elif self.advanced_zero_value == "Value Error:":
            self.zero_label_widget.configure(text_font=("Arial", 24))
            self.advanced_zero_base_input.set(value="0")
    
        elif self.advanced_zero_value == "Invaild Input!":
            self.invaild_input_return()
            self.advanced_zero_base_input.set(value="0")
 
            
        elif self.advanced_zero_value != "0":
            self.advanced_zero_base_input.set(value=self.advanced_zero_value + "0")
    
    # ------------------------ End Advanced X Number Press Event Methods ---------------------------- #
    
    
    
    # ---------------------------- Advanced Operater Press Event Methods ------------------------------- #
    

    def advanced_addition_btn(self, operater):
        """Main method for when the user presses keyboard button '+'

        Args:
            operater (str): passes the '+' to method
        """
        self.set_value = self.advanced_zero_base_input.get() # value that is there
        
        measured = len(self.set_value) # length of value
        
        last_digits = re.search(r'\d+$', self.set_value) # checking to see if the string has a digit in last index
        
        toBeCal = self.set_value.split(" ") # spliting the value into list 


        # if + is pressed and the user hasn't entered values other than pressing + key
        if self.set_value == "0" and not self.set_value.count("."):
            self.invaild_input()
            
            
        # example (2 * 2 +), if the user presses + at the end like example, this elif below will calculate the two values
        # and do something like this, example (4 +)
        elif self.set_value.count("*"):
            
            # checking if '.' in any of the values 
            if "." in self.set_value:
                
                dot_split_values = self.set_value.split(" ")
                num_one = dot_split_values[0]
                num_two = dot_split_values[2]
                
                if "." in num_one and num_two:
                    final_calculation = float(num_one) * float(num_two)
                    self.advanced_zero_base_input.set(value=str(final_calculation) + " + ")
                elif "." in num_one:
                    final_calculation = float(num_one) * int(num_two)
                    self.advanced_zero_base_input.set(value=str(final_calculation) + " + ")
                elif "." in num_two:
                    final_calculation = int(num_one) * float(num_two)
                    self.advanced_zero_base_input.set(value=str(final_calculation) + " + ")
            else:
                first_num = toBeCal[0]
                second_num = toBeCal[2]
                result = int(first_num) * int(second_num)
                self.advanced_zero_base_input.set(value=str(result) + " + ")
        
        
        # same thing as above comment but with (2 / 2 +)
        elif self.set_value.count("/"):
            if "." in self.set_value:
                dot_split_values = self.set_value.split(" ")
                num_one = dot_split_values[0]
                num_two = dot_split_values[2]
                
                if "." in num_one and num_two:
                    
                    if num_one or num_two == "0.0":
                        self.zero_label_widget.configure(text_font=("Arial", 14))
                        self.advanced_zero_base_input.set(value="Cannot Divide by 0")
                        
                    else:
                        final_calculation = float(num_one) // float(num_two)
                        self.advanced_zero_base_input.set(value=str(final_calculation) + " + ")
                    
                    
                elif "." in num_one:
                    if num_one == "0.0":
                        self.zero_label_widget.configure(text_font=("Arial", 14))
                        self.advanced_zero_base_input.set(value="Cannot Divide by 0")
                    else:
                        final_calculation = float(num_one) // int(num_two)
                        self.advanced_zero_base_input.set(value=str(final_calculation) + " + ")
                        
                        
                elif "." in num_two:
                    if num_two == "0.0":
                        self.zero_label_widget.configure(text_font=("Arial", 14))
                        self.advanced_zero_base_input.set(value="Cannot Divide by 0")
                    
                    else:
                        final_calculation = int(num_one) // float(num_two)
                        self.advanced_zero_base_input.set(value=str(final_calculation) + " + ")
                        
                else:
                    self.zero_label_widget.configure(text_font=("Arial", 14))
                    self.advanced_zero_base_input.set(value="Cannot Divide by 0")
            
            else:
                first_num = toBeCal[0]
                second_num = toBeCal[2]
                if second_num == "0":
                    self.zero_label_widget.configure(text_font=("Arial", 14))
                    self.advanced_zero_base_input.set(value="Cannot Divide by Zero")
                else:
                    result = int(first_num) // int(second_num)
                    self.advanced_zero_base_input.set(value=str(result) + " + ")
               
               
        # same thing as above comment but with (2 - 2 +) 
        elif self.set_value.count("-"):
            if "." in self.set_value:
                dot_split_values = self.set_value.split(" ")
                num_one = dot_split_values[0]
                num_two = dot_split_values[2]
                
                if "." in num_one and num_two:
                    final_calculation = float(num_one) - float(num_two)
                    self.advanced_zero_base_input.set(value=str(final_calculation) + " + ")
                elif "." in num_one:
                    final_calculation = float(num_one) - int(num_two)
                    self.advanced_zero_base_input.set(value=str(final_calculation) + " + ")
                elif "." in num_two:
                    final_calculation = int(num_one) - float(num_two)
                    self.advanced_zero_base_input.set(value=str(final_calculation) + " + ")
                    
            else:
                first_num = toBeCal[0]
                second_num = toBeCal[2]
                result = int(first_num) - int(second_num)
                self.advanced_zero_base_input.set(value=str(result) + " + ")
            
            
        # if + is pressed again while "Invaild Input!" is the value    
        elif self.set_value == "Invaild Input!":
            self.zero_label_widget.configure(text_font=("Arial", 26))
            self.advanced_zero_base_input.set(value="0")
            self.btn_div.configure(state="normal")
            self.btn_mut.configure(state="normal")
            self.btn_exp.configure(state="normal")
            self.btn_mod.configure(state="normal")
            self.btn_sqro.configure(state="normal")
            self.btn_leftP.configure(state="normal")
            self.btn_rightP.configure(state="normal")
            self.ad_btn_n.configure(state="normal")
            self.btn_div2.configure(state="normal")
            self.btn_x2.configure(state="normal")
            self.btn_x.configure(state="normal")
            self.btn_abs.configure(state="normal")
            self.ad_btn_minus.configure(state="normal")
            self.btn_log.configure(state="normal")
            self.ad_btn_plus.configure(state="normal")
            self.btn_in.configure(state="normal")
            self.ad_plus_minus.configure(state="normal")
            self.ad_btn_equals.configure(state="normal")
            
            
        # if + is pressed and value isn't 0 and there isn't a '+' already
        elif self.set_value != "0" and not self.set_value.count("+") and not self.set_value.count("."):
            self.advanced_zero_base_input.set(value=self.set_value + " " + operater + " ")
        
        
        # if there is a '+' and length is > 3 and value ends with a int and the values aren't floats
        elif self.set_value.count("+") and measured >= 3 and last_digits != None:
            # checking if there is a '.' in set_value
            if "." in self.set_value:
                float_split = self.set_value.split(" ")
                number_one = float_split[0]
                number_two = float_split[2]
                
                if "." in number_one and number_two:
                    calculated_value = float(number_one) + float(number_two)
                    self.advanced_zero_base_input.set(value=str(calculated_value))
                    
                elif "." in number_two:
                    calculated_value = int(number_one) + float(number_two)
                    self.advanced_zero_base_input.set(value=str(calculated_value))
                    
                elif "." in number_one:
                    calculated_value = float(number_one) + int(number_two)
                    self.advanced_zero_base_input.set(value=str(calculated_value))
                    
            else:
                first_num = toBeCal[0]
                second_num = toBeCal[2]
                result = int(first_num) + int(second_num)
                self.advanced_zero_base_input.set(value=str(result) + " + ")
        
        
        # If there is a '0.5' as value input
        elif self.set_value.count("."):
            float_split = self.set_value.split(" ")
            if len(self.set_value) >= 3:
                self.advanced_zero_base_input.set(value=self.set_value + " " + operater + " ")
                

    def advanced_subtraction_btn(self, operater):
        """Main method for when the user presses keyboard button '-'

        Args:
            operater (str): passes the '-' to method
        """
        
        self.set_value = self.advanced_zero_base_input.get() # value that is there
        
        measured = len(self.set_value) # length of value
        
        last_digits = re.search(r'\d+$', self.set_value) # checking to see if the string has a digit in last index
        
        toBeCal = self.set_value.split(" ") # spliting the value into list 


        # if + is pressed and the user hasn't entered values other than pressing + key
        if self.set_value == "0" and not self.set_value.count("."):
            self.invaild_input()
            
        # example (2 * 2 -), if the user presses + at the end like example, this elif below will calculate the two values
        # and do something like this, example (4 +)
        elif self.set_value.count("*"):
            
            # checking if '.' in any of the values 
            if "." in self.set_value:
                
                dot_split_values = self.set_value.split(" ")
                num_one = dot_split_values[0]
                num_two = dot_split_values[2]
                
                if "." in num_one and num_two:
                    final_calculation = float(num_one) * float(num_two)
                    self.advanced_zero_base_input.set(value=str(final_calculation) + " - ")
                elif "." in num_one:
                    final_calculation = float(num_one) * int(num_two)
                    self.advanced_zero_base_input.set(value=str(final_calculation) + " - ")
                elif "." in num_two:
                    final_calculation = int(num_one) * float(num_two)
                    self.advanced_zero_base_input.set(value=str(final_calculation) + " - ")
            else:
                first_num = toBeCal[0]
                second_num = toBeCal[2]
                result = int(first_num) * int(second_num)
                self.advanced_zero_base_input.set(value=str(result) + " - ")
        
        
        # same thing as above comment but with (2 / 2 -)
        elif self.set_value.count("/"):
            if "." in self.set_value:
                dot_split_values = self.set_value.split(" ")
                num_one = dot_split_values[0]
                num_two = dot_split_values[2]
                
                if "." in num_one and num_two:
                    
                    if num_one or num_two == "0.0":
                        self.zero_label_widget.configure(text_font=("Arial", 14))
                        self.advanced_zero_base_input.set(value="Cannot Divide by 0")
                        
                    else:
                        final_calculation = float(num_one) // float(num_two)
                        self.advanced_zero_base_input.set(value=str(final_calculation) + " - ")
                    
                    
                elif "." in num_one:
                    if num_one == "0.0":
                        self.zero_label_widget.configure(text_font=("Arial", 14))
                        self.advanced_zero_base_input.set(value="Cannot Divide by 0")
                    else:
                        final_calculation = float(num_one) // int(num_two)
                        self.advanced_zero_base_input.set(value=str(final_calculation) + " - ")
                        
                        
                elif "." in num_two:
                    if num_two == "0.0":
                        self.zero_label_widget.configure(text_font=("Arial", 14))
                        self.advanced_zero_base_input.set(value="Cannot Divide by 0")
                    
                    else:
                        final_calculation = int(num_one) // float(num_two)
                        self.advanced_zero_base_input.set(value=str(final_calculation) + " - ")
                        
                else:
                    self.zero_label_widget.configure(text_font=("Arial", 14))
                    self.advanced_zero_base_input.set(value="Cannot Divide by 0")
            
            else:
                first_num = toBeCal[0]
                second_num = toBeCal[2]
                if second_num == "0":
                    self.zero_label_widget.configure(text_font=("Arial", 14))
                    self.advanced_zero_base_input.set(value="Cannot Divide by Zero")
                else:
                    result = int(first_num) // int(second_num)
                    self.advanced_zero_base_input.set(value=str(result) + " - ")
               
               
        # same thing as above comment but with (2 - 2 +) 
        elif self.set_value.count("+"):
            if "." in self.set_value:
                dot_split_values = self.set_value.split(" ")
                num_one = dot_split_values[0]
                num_two = dot_split_values[2]
                
                if "." in num_one and num_two:
                    final_calculation = float(num_one) + float(num_two)
                    self.advanced_zero_base_input.set(value=str(final_calculation) + " - ")
                elif "." in num_one:
                    final_calculation = float(num_one) + int(num_two)
                    self.advanced_zero_base_input.set(value=str(final_calculation) + " - ")
                elif "." in num_two:
                    final_calculation = int(num_one) + float(num_two)
                    self.advanced_zero_base_input.set(value=str(final_calculation) + " - ")
                    
            else:
                first_num = toBeCal[0]
                second_num = toBeCal[2]
                result = int(first_num) - int(second_num)
                self.advanced_zero_base_input.set(value=str(result) + " - ")
            
            
        # if + is pressed again while "Invaild Input!" is the value    
        elif self.set_value == "Invaild Input!":
            self.zero_label_widget.configure(text_font=("Arial", 26))
            self.advanced_zero_base_input.set(value="0")
            
            
        # if - is pressed and value isn't 0 and there isn't a '+' already
        elif self.set_value != "0" and not self.set_value.count("-") and not self.set_value.count("."):
            self.advanced_zero_base_input.set(value=self.set_value + " " + operater + " ")
        
        
        # if there is a '-' and length is > 3 and value ends with a int and the values aren't floats
        elif self.set_value.count("-") and measured >= 3 and last_digits != None:
            # checking if there is a '.' in set_value
            if "." in self.set_value:
                float_split = self.set_value.split(" ")
                number_one = float_split[0]
                number_two = float_split[2]
                
                if "." in number_one and number_two:
                    calculated_value = float(number_one) - float(number_two)
                    self.advanced_zero_base_input.set(value=str(calculated_value))
                    
                elif "." in number_two:
                    calculated_value = int(number_one) - float(number_two)
                    self.advanced_zero_base_input.set(value=str(calculated_value))
                    
                elif "." in number_one:
                    calculated_value = float(number_one) - int(number_two)
                    self.advanced_zero_base_input.set(value=str(calculated_value))
                    
            else:
                first_num = toBeCal[0]
                second_num = toBeCal[2]
                result = int(first_num) + int(second_num)
                self.advanced_zero_base_input.set(value=str(result) + " - ")
        
        
        # If there is a '0.5' as value input
        elif self.set_value.count("."):
            float_split = self.set_value.split(" ")
            if len(self.set_value) >= 3:
                self.advanced_zero_base_input.set(value=self.set_value + " " + operater + " ")

    
    def advanced_multiplication_btn(self, operater):
        """Main method for when the user presses keyboard button '*'

        Args:
            operater (str): passes the '*' to method
        """
        self.set_value = self.advanced_zero_base_input.get() # value that is there
        
        measured = len(self.set_value) # length of value
        
        last_digits = re.search(r'\d+$', self.set_value) # checking to see if the string has a digit in last index
        
        toBeCal = self.set_value.split(" ") # spliting the value into list 


        # if + is pressed and the user hasn't entered values other than pressing + key
        if self.set_value == "0" and not self.set_value.count("."):
            self.invaild_input()
            
        # example (2 + 2 *), if the user presses + at the end like example, this elif below will calculate the two values
        # and do something like this, example (4 +)
        elif self.set_value.count("+"):
            
            # checking if '.' in any of the values 
            if "." in self.set_value:
                
                dot_split_values = self.set_value.split(" ")
                num_one = dot_split_values[0]
                num_two = dot_split_values[2]
                
                if "." in num_one and num_two:
                    final_calculation = float(num_one) + float(num_two)
                    self.advanced_zero_base_input.set(value=str(final_calculation) + " * ")
                elif "." in num_one:
                    final_calculation = float(num_one) + int(num_two)
                    self.advanced_zero_base_input.set(value=str(final_calculation) + " * ")
                elif "." in num_two:
                    final_calculation = int(num_one) + float(num_two)
                    self.advanced_zero_base_input.set(value=str(final_calculation) + " * ")
            else:
                first_num = toBeCal[0]
                second_num = toBeCal[2]
                result = int(first_num) * int(second_num)
                self.advanced_zero_base_input.set(value=str(result) + " + ")
        
        
        # same thing as above comment but with (2 / 2 *)
        elif self.set_value.count("/"):
            if "." in self.set_value:
                dot_split_values = self.set_value.split(" ")
                num_one = dot_split_values[0]
                num_two = dot_split_values[2]
                
                if "." in num_one and num_two:
                    
                    if num_one or num_two == "0.0":
                        self.zero_label_widget.configure(text_font=("Arial", 14))
                        self.advanced_zero_base_input.set(value="Cannot Divide by 0")
                        
                    else:
                        final_calculation = float(num_one) // float(num_two)
                        self.advanced_zero_base_input.set(value=str(final_calculation) + " * ")
                    
                    
                elif "." in num_one:
                    if num_one == "0.0":
                        self.zero_label_widget.configure(text_font=("Arial", 14))
                        self.advanced_zero_base_input.set(value="Cannot Divide by 0")
                    else:
                        final_calculation = float(num_one) // int(num_two)
                        self.advanced_zero_base_input.set(value=str(final_calculation) + " * ")
                        
                        
                elif "." in num_two:
                    if num_two == "0.0":
                        self.zero_label_widget.configure(text_font=("Arial", 14))
                        self.advanced_zero_base_input.set(value="Cannot Divide by 0")
                    
                    else:
                        final_calculation = int(num_one) // float(num_two)
                        self.advanced_zero_base_input.set(value=str(final_calculation) + " * ")
                        
                else:
                    self.zero_label_widget.configure(text_font=("Arial", 14))
                    self.advanced_zero_base_input.set(value="Cannot Divide by 0")
            
            else:
                first_num = toBeCal[0]
                second_num = toBeCal[2]
                if second_num == "0":
                    self.zero_label_widget.configure(text_font=("Arial", 14))
                    self.advanced_zero_base_input.set(value="Cannot Divide by Zero")
                else:
                    result = int(first_num) // int(second_num)
                    self.advanced_zero_base_input.set(value=str(result) + " * ")
               
               
        # same thing as above comment but with (2 - 2 *) 
        elif self.set_value.count("-"):
            if "." in self.set_value:
                dot_split_values = self.set_value.split(" ")
                num_one = dot_split_values[0]
                num_two = dot_split_values[2]
                
                if "." in num_one and num_two:
                    final_calculation = float(num_one) - float(num_two)
                    self.advanced_zero_base_input.set(value=str(final_calculation) + " * ")
                elif "." in num_one:
                    final_calculation = float(num_one) - int(num_two)
                    self.advanced_zero_base_input.set(value=str(final_calculation) + " * ")
                elif "." in num_two:
                    final_calculation = int(num_one) - float(num_two)
                    self.advanced_zero_base_input.set(value=str(final_calculation) + " * ")
                    
            else:
                first_num = toBeCal[0]
                second_num = toBeCal[2]
                result = int(first_num) - int(second_num)
                self.advanced_zero_base_input.set(value=str(result) + " * ")
            
            
        # if + is pressed again while "Invaild Input!" is the value    
        elif self.set_value == "Invaild Input!":
            self.zero_label_widget.configure(text_font=("Arial", 26))
            self.advanced_zero_base_input.set(value="0")
            
            
        # if * is pressed and value isn't 0 and there isn't a '*' already
        elif self.set_value != "0" and not self.set_value.count("*") and not self.set_value.count("."):
            self.advanced_zero_base_input.set(value=self.set_value + " " + operater + " ")
        
        
        # if there is a '*' and length is > 3 and value ends with a int and the values aren't floats
        elif self.set_value.count("*") and measured >= 3 and last_digits != None:
            # checking if there is a '.' in set_value
            if "." in self.set_value:
                float_split = self.set_value.split(" ")
                number_one = float_split[0]
                number_two = float_split[2]
                
                if "." in number_one and number_two:
                    calculated_value = float(number_one) * float(number_two)
                    self.advanced_zero_base_input.set(value=str(calculated_value))
                    
                elif "." in number_two:
                    calculated_value = int(number_one) * float(number_two)
                    self.advanced_zero_base_input.set(value=str(calculated_value))
                    
                elif "." in number_one:
                    calculated_value = float(number_one) * int(number_two)
                    self.advanced_zero_base_input.set(value=str(calculated_value))
                    
            else:
                first_num = toBeCal[0]
                second_num = toBeCal[2]
                result = int(first_num) + int(second_num)
                self.advanced_zero_base_input.set(value=str(result) + " * ")
        
        
        # If there is a '0.5' as value input
        elif self.set_value.count("."):
            float_split = self.set_value.split(" ")
            if len(self.set_value) >= 3:
                self.advanced_zero_base_input.set(value=self.set_value + " " + operater + " ")
    
    
    def advanced_divison_btn(self, operater):
        """Main method for when the user presses keyboard button '/'

        Args:
            operater (str): passes the '/' to method
        """
        
        self.set_value = self.advanced_zero_base_input.get() # value that is there
        
        measured = len(self.set_value) # length of value
        
        last_digits = re.search(r'\d+$', self.set_value) # checking to see if the string has a digit in last index
        
        toBeCal = self.set_value.split(" ") # spliting the value into list 


        # if + is pressed and the user hasn't entered values other than pressing + key
        if self.set_value == "0" and not self.set_value.count("."):
            self.invaild_input()
            
        # example (2 * 2 /), if the user presses / at the end like example, this elif below will calculate the two values
        # and do something like this, example (4 /)
        elif self.set_value.count("*"):
            
            # checking if '.' in any of the values 
            if "." in self.set_value:
                
                dot_split_values = self.set_value.split(" ")
                num_one = dot_split_values[0]
                num_two = dot_split_values[2]
                
                if "." in num_one and num_two:
                    final_calculation = float(num_one) * float(num_two)
                    self.advanced_zero_base_input.set(value=str(final_calculation) + " / ")
                elif "." in num_one:
                    final_calculation = float(num_one) * int(num_two)
                    self.advanced_zero_base_input.set(value=str(final_calculation) + " / ")
                elif "." in num_two:
                    final_calculation = int(num_one) * float(num_two)
                    self.advanced_zero_base_input.set(value=str(final_calculation) + " / ")
            else:
                first_num = toBeCal[0]
                second_num = toBeCal[2]
                result = int(first_num) * int(second_num)
                self.advanced_zero_base_input.set(value=str(result) + " / ")
        
        
        # same thing as above comment but with (2 + 2 /)
        elif self.set_value.count("+"):
            if "." in self.set_value:
                dot_split_values = self.set_value.split(" ")
                num_one = dot_split_values[0]
                num_two = dot_split_values[2]
                
                if "." in num_one and num_two:
                    
                    if num_one or num_two == "0.0":
                        self.zero_label_widget.configure(text_font=("Arial", 14))
                        self.advanced_zero_base_input.set(value="Cannot Divide by 0")
                        
                    else:
                        final_calculation = float(num_one) + float(num_two)
                        self.advanced_zero_base_input.set(value=str(final_calculation) + " / ")
                    
                    
                elif "." in num_one:
                    if num_one == "0.0":
                        self.zero_label_widget.configure(text_font=("Arial", 14))
                        self.advanced_zero_base_input.set(value="Cannot Divide by 0")
                    else:
                        final_calculation = float(num_one) + int(num_two)
                        self.advanced_zero_base_input.set(value=str(final_calculation) + " / ")
                        
                        
                elif "." in num_two:
                    if num_two == "0.0":
                        self.zero_label_widget.configure(text_font=("Arial", 14))
                        self.advanced_zero_base_input.set(value="Cannot Divide by 0")
                    
                    else:
                        final_calculation = int(num_one) + float(num_two)
                        self.advanced_zero_base_input.set(value=str(final_calculation) + " / ")
                        
                else:
                    self.zero_label_widget.configure(text_font=("Arial", 14))
                    self.advanced_zero_base_input.set(value="Cannot Divide by 0")
            
            else:
                first_num = toBeCal[0]
                second_num = toBeCal[2]
                if second_num == "0":
                    self.zero_label_widget.configure(text_font=("Arial", 14))
                    self.advanced_zero_base_input.set(value="Cannot Divide by Zero")
                else:
                    result = int(first_num) // int(second_num)
                    self.advanced_zero_base_input.set(value=str(result) + " / ")
               
               
        # same thing as above comment but with (2 - 2 +) 
        elif self.set_value.count("-"):
            if "." in self.set_value:
                dot_split_values = self.set_value.split(" ")
                num_one = dot_split_values[0]
                num_two = dot_split_values[2]
                
                if "." in num_one and num_two:
                    final_calculation = float(num_one) - float(num_two)
                    self.advanced_zero_base_input.set(value=str(final_calculation) + " / ")
                elif "." in num_one:
                    final_calculation = float(num_one) - int(num_two)
                    self.advanced_zero_base_input.set(value=str(final_calculation) + " / ")
                elif "." in num_two:
                    final_calculation = int(num_one) - float(num_two)
                    self.advanced_zero_base_input.set(value=str(final_calculation) + " / ")
                    
            else:
                first_num = toBeCal[0]
                second_num = toBeCal[2]
                result = int(first_num) - int(second_num)
                self.advanced_zero_base_input.set(value=str(result) + " / ")
            
            
        # if + is pressed again while "Invaild Input!" is the value    
        elif self.set_value == "Invaild Input!":
            self.zero_label_widget.configure(text_font=("Arial", 26))
            self.advanced_zero_base_input.set(value="0")
            
            
        # if / is pressed and value isn't 0 and there isn't a '/' already
        elif self.set_value != "0" and not self.set_value.count("/") and not self.set_value.count("."):
            self.advanced_zero_base_input.set(value=self.set_value + " " + operater + " ")
        
        
        # if there is a '/' and length is > 3 and value ends with a int and the values aren't floats
        elif self.set_value.count("/") and measured >= 3 and last_digits != None:
            # checking if there is a '.' in set_value
            if "." in self.set_value:
                float_split = self.set_value.split(" ")
                number_one = float_split[0]
                number_two = float_split[2]
                
                if "." in number_one and number_two:
                    calculated_value = float(number_one) // float(number_two)
                    self.advanced_zero_base_input.set(value=str(calculated_value))
                    
                elif "." in number_two:
                    calculated_value = int(number_one) // float(number_two)
                    self.advanced_zero_base_input.set(value=str(calculated_value))
                    
                elif "." in number_one:
                    calculated_value = float(number_one) // int(number_two)
                    self.advanced_zero_base_input.set(value=str(calculated_value))
                    
            else:
                first_num = toBeCal[0]
                second_num = toBeCal[2]
                result = int(first_num) // int(second_num)
                self.advanced_zero_base_input.set(value=str(result) + " / ")
        
        
        # If there is a '0.5' as value input
        elif self.set_value.count("."):
            float_split = self.set_value.split(" ")
            if len(self.set_value) >= 3:
                self.advanced_zero_base_input.set(value=self.set_value + " " + operater + " ")
    
    
    
    # ------------------------- End Advanced Operater Press Event Methods ------------------------------- #
    
    
    
    
    # ---------------------------- Misc Advanced Press Event Methods ------------------------------------ #
    
    def advanced_enter_btn(self, e):
        value_to_calculate = self.advanced_zero_base_input.get()
        toBeCal = value_to_calculate.split(" ")
        measured = len(toBeCal)
        last_digit = re.search(r'\d+$', value_to_calculate)
        self.line_check()


        # ------------ Checks Addition Operator ------------ #
        
        if toBeCal.count("+") and measured == 3 and last_digit != None:
                if "." in value_to_calculate:
                    float_split = value_to_calculate.split(" ")
                    number_one = float_split[0]
                    number_two = float_split[2]
                
                    if "." in number_one and number_two:
                        calculated_value = float(number_one) + float(number_two)
                        self.advanced_zero_base_input.set(value=str(calculated_value))
                    
                    elif "." in number_two:
                        calculated_value = int(number_one) + float(number_two)
                        self.advanced_zero_base_input.set(value=str(calculated_value))
                    
                    elif "." in number_one:
                        calculated_value = float(number_one) + int(number_two)
                        self.advanced_zero_base_input.set(value=str(calculated_value))
                else:
                    first_num = toBeCal[0]
                    second_num = toBeCal[2]
                    result = int(first_num) + int(second_num)
                    self.advanced_zero_base_input.set(value=str(result))
            
            
        # ------------ Ends Addition Operator ------------ #
            
            
            
        # ------------ Checks Subtraction Operator ------------ #
        
        elif toBeCal.count("-") and measured == 3 and last_digit != None:
            if "." in value_to_calculate:
                float_split = value_to_calculate.split(" ")
                number_one = float_split[0]
                number_two = float_split[2]
                
                if "." in number_one and number_two:
                    calculated_value = float(number_one) - float(number_two)
                    self.advanced_zero_base_input.set(value=str(calculated_value))
                    
                elif "." in number_two:
                    calculated_value = int(number_one) - float(number_two)
                    self.advanced_zero_base_input.set(value=str(calculated_value))
                    
                elif "." in number_one:
                    calculated_value = float(number_one) - int(number_two)
                    self.advanced_zero_base_input.set(value=str(calculated_value))
            else:
                first_num = toBeCal[0]
                second_num = toBeCal[2]
                result = int(first_num) - int(second_num)
                self.advanced_zero_base_input.set(value=str(result))
        
        # ------------ Ends Subtraction Operator ------------ #
            
            
            
        # ------------ Checks Divison Operator ------------ #
        
        elif toBeCal.count("/") and measured == 3 and last_digit != None:
            if "." in value_to_calculate:
                float_split = value_to_calculate.split(" ")
                number_one = float_split[0]
                number_two = float_split[2]
                
                if "." in number_one and number_two:
                    calculated_value = float(number_one) // float(number_two)
                    self.advanced_zero_base_input.set(value=str(calculated_value))
                    
                elif "." in number_two:
                    calculated_value = int(number_one) // float(number_two)
                    self.advanced_zero_base_input.set(value=str(calculated_value))
                    
                elif "." in number_one:
                    calculated_value = float(number_one) // int(number_two)
                    self.advanced_zero_base_input.set(value=str(calculated_value))
            else:
                first_num = toBeCal[0]
                second_num = toBeCal[2]
                if second_num == "0":
                    self.zero_label_widget.configure(text_font=("Arial", 16))
                    self.advanced_zero_base_input.set(value="Cannot Divide by 0")
                else:
                    result = int(first_num) // int(second_num)
                    self.advanced_zero_base_input.set(value=str(result))
        
        # ------------ Ends Divison Operator ------------ #
        
        
        
                
        # ------------ Checks Multiplication Operator ------------ #
        
        elif toBeCal.count("*") and measured == 3 and last_digit != None:
            if "." in value_to_calculate:
                float_split = value_to_calculate.split(" ")
                number_one = float_split[0]
                number_two = float_split[2]
                
                if "." in number_one and number_two:
                    calculated_value = float(number_one) * float(number_two)
                    self.advanced_zero_base_input.set(value=str(calculated_value))
                    
                elif "." in number_two:
                    calculated_value = int(number_one) * float(number_two)
                    self.advanced_zero_base_input.set(value=str(calculated_value))
                    
                elif "." in number_one:
                    calculated_value = float(number_one) * int(number_two)
                    self.advanced_zero_base_input.set(value=str(calculated_value))
            else:
                first_num = toBeCal[0]
                second_num = toBeCal[2]
                result = int(first_num) * int(second_num)
                self.advanced_zero_base_input.set(value=str(result))
        # ------------ Ends Multiplication Operator ------------ #
        
        
        # ------------ Exponent Operator ------------ #
        elif toBeCal.count("^") and measured == 3 and last_digit != None:
            if "." in value_to_calculate:
                float_split = value_to_calculate.split(" ")
                number_one = float_split[0]
                number_two = float_split[2]
                
                if "." in number_one and number_two:
                    calculated_value = float(number_one) ** float(number_two)
                    self.advanced_zero_base_input.set(value=str(calculated_value))
                    
                elif "." in number_two:
                    calculated_value = int(number_one) ** float(number_two)
                    self.advanced_zero_base_input.set(value=str(calculated_value))
                    
                elif "." in number_one:
                    calculated_value = float(number_one) ** int(number_two)
                    self.advanced_zero_base_input.set(value=str(calculated_value))
            else:
                first_num = toBeCal[0]
                second_num = toBeCal[2]
                result = int(first_num) ** int(second_num)
                self.advanced_zero_base_input.set(value=str(result))
            # ------------ End Exponent Operator ------------ #
            
            
            # ------------ Modulo Operator ------------ #
        elif toBeCal.count("mod") and measured == 3 and last_digit != None:
            if "." in value_to_calculate:
                float_split = value_to_calculate.split(" ")
                number_one = float_split[0]
                number_two = float_split[2]
                
                if "." in number_one and number_two:
                    calculated_value = float(number_one) % float(number_two)
                    self.advanced_zero_base_input.set(value=str(calculated_value))
                    
                elif "." in number_two:
                    calculated_value = int(number_one) % float(number_two)
                    self.advanced_zero_base_input.set(value=str(calculated_value))
                    
                elif "." in number_one:
                    calculated_value = float(number_one) % int(number_two)
                    self.advanced_zero_base_input.set(value=str(calculated_value))
            else:
                first_num = toBeCal[0]
                second_num = toBeCal[2]
                result = int(first_num) % int(second_num)
                self.advanced_zero_base_input.set(value=str(result))
            # ------------ End Modulo Operator ------------ #
            
            # -------------- Percentage Cal ---------------- # 
        elif toBeCal.count("%") and measured == 3 and last_digit != None:
            if "." in value_to_calculate:
                float_split = value_to_calculate.split(" ")
                number_one = float_split[0]
                number_two = float_split[2]
                
                if "." in number_one and number_two:
                    calculated_value = float(number_one) / 100 * float(number_two)
                    self.advanced_zero_base_input.set(value=str(calculated_value))
                    
                elif "." in number_two:
                    calculated_value = int(number_one) / 100 * float(number_two)
                    self.advanced_zero_base_input.set(value=str(calculated_value))
                    
                elif "." in number_one:
                    calculated_value = float(number_one) / 100 * int(number_two)
                    self.advanced_zero_base_input.set(value=str(calculated_value))
            else:
                first_num = toBeCal[0]
                second_num = toBeCal[2]
                result = int(first_num) / 100 * int(second_num)
                end_result = str(result).replace(".0", "")
                self.advanced_zero_base_input.set(value=f"{end_result}")
            # ------------ End Percentage ------------ #
        
        
        # Checks if value is "Cannot Divide by 0" and enter is pressed again, value returns to 0
        elif value_to_calculate == "Cannot Divide by 0":
            self.zero_label_widget.configure(text_font=("Arial", 26))
            self.advanced_zero_base_input.set(value="0")
        
        # calculating if parenthesis in value
        elif toBeCal.count("(") and toBeCal.count(")"):
            pass
            
    
    def advanced_dot_btn(self, dot):
        input_value = self.advanced_zero_base_input.get()
        
        if input_value == "0":
            self.advanced_zero_base_input.set(value="0" + dot)
            
            
        elif input_value == "0.":
            self.zero_label_widget.configure(text_font=("Arial", 14))
            self.advanced_zero_base_input.set(value="Excessed . Value")
            
            
        elif input_value != "0" and input_value != "Excessed . Value":
            self.advanced_zero_base_input.set(value=input_value + dot)
            
            
        elif input_value == "Excessed . Value":
            self.zero_label_widget.configure(text_font=("Arial", 26))
            self.advanced_zero_base_input.set(value="0" + dot)
            
        else:
            self.zero_label_widget.configure(text_font=("Arial", 14))
            self.advanced_zero_base_input.set(value="Excessed . Value")
        
    
    def advanced_ce_btn(self, e):
        value = self.advanced_zero_base_input.get()
        
        if value == "0":
            pass
        else:
            self.zero_label_widget.configure(text_font=("Arial", 26))
            self.advanced_zero_base_input.set(value="0")
        
        
    def line_check(self):
        input_value = self.advanced_zero_base_input.get() # gets the value
        value_length = len(input_value) # length of input
        
        if input_value != "0" and value_length in range(11, 16):
            self.zero_label_widget.configure(text_font=("Arial", 18))
            
        elif input_value != "0" and value_length in range(16, 20):
            self.zero_label_widget.configure(text_font=("Arial", 14))
        
        elif input_value != "0" and value_length in range(20, 25):
            self.zero_label_widget.configure(text_font=("Arial", 10))
            

    def invaild_input(self):
        self.zero_label_widget.configure(text_font=("Arial", 24))
        self.advanced_zero_base_input.set(value="Invaild Input!")
        self.btn_div.configure(state="disable")
        self.btn_mut.configure(state="disable")
        self.btn_exp.configure(state="disable")
        self.btn_mod.configure(state="disable")
        self.btn_sqro.configure(state="disable")
        self.btn_leftP.configure(state="disable")
        self.btn_rightP.configure(state="disable")
        self.ad_btn_n.configure(state="disable")
        self.btn_div2.configure(state="disable")
        self.btn_x2.configure(state="disable")
        self.btn_x.configure(state="disable")
        self.btn_abs.configure(state="disable")
        self.ad_btn_minus.configure(state="disable")
        self.btn_log.configure(state="disable")
        self.ad_btn_plus.configure(state="disable")
        self.btn_in.configure(state="disable")
        self.ad_plus_minus.configure(state="disable")
        self.ad_btn_equals.configure(state="disable")
            
    
    def invaild_input_return(self):
        self.zero_label_widget.configure(text_font=("Arial", 24))
        self.advanced_zero_base_input.set(value="0")
        self.btn_div.configure(state="normal")
        self.btn_mut.configure(state="normal")
        self.btn_exp.configure(state="normal")
        self.btn_mod.configure(state="normal")
        self.btn_sqro.configure(state="normal")
        self.btn_leftP.configure(state="normal")
        self.btn_rightP.configure(state="normal")
        self.ad_btn_n.configure(state="normal")
        self.btn_div2.configure(state="normal")
        self.btn_x2.configure(state="normal")
        self.btn_x.configure(state="normal")
        self.btn_abs.configure(state="normal")
        self.ad_btn_minus.configure(state="normal")
        self.btn_log.configure(state="normal")
        self.ad_btn_plus.configure(state="normal")
        self.btn_in.configure(state="normal")
        self.ad_plus_minus.configure(state="normal")
        self.ad_btn_equals.configure(state="normal")   
        
            
    def advanced_backspace(self, e):
        """Method used for when the user presses the backspace key

        Args:
            e (None): Needed something to pass into lambda
        """
        value_to_del = self.advanced_zero_base_input.get()
        
        if value_to_del == "0" and len(value_to_del) == 1:
            self.advanced_zero_base_input.set(value="0")
            
        elif value_to_del != "0" and len(value_to_del) == 1:
            self.advanced_zero_base_input.set(value="0")
            
        elif value_to_del != "0" and len(value_to_del) > 1:
            self.advanced_zero_base_input.set(value=value_to_del[:-1])
        

    # ---------------------------- End Misc Advanced Press Event Methods ------------------------------------ #
    
    
    # ---------------------------- Start Advanced Switch Option Methods ------------------------------------ #
    
    

    # Method to return to advanced from currency exchange option
    def return_advcanced_from_exchange(self):
        self.currency_label_frame.pack_forget()
        self.currency_label.pack_forget()
        self.input_convert_frame.pack_forget()
        self.output_convert_frame.pack_forget()
        self.conversion_rates_frame.pack_forget()
        self.currency_exchange_buttons_frame.pack_forget()
        self.last_exchange_frame.pack_forget()
        self.powered_by_api.pack_forget()
    
        self.execute_advanced_option("0")
    


    # ---------------------------- End Standard Switch Option Methods ------------------------------------ #
        
        
    # ------------------------------ End Advanced Method ---------------------------------------
        
    
    # ---------------------------------- End of Advanced Option ------------------------------------------ #
    





















    
    def execute_currency_exchange_option(self):
        self.label_pack.pack_forget()
        self.standard_zero_label_input.pack_forget()
        self.first_set_cals_frame.pack_forget()
        self.first_pack.pack_forget()
        self.root.title("Currency Exchange")
        self.root.geometry("280x560")
        # self.entry.delete(0, END)
        
        
        # ------------------------------- Currency Exhchange Label Frame ----------------------------------- #
        self.currency_label_frame = customtkinter.CTkFrame(self.root)
        self.currency_label_frame.pack(side=TOP, anchor="w", padx=(15, 0), pady=(10, 0))
        
        # ------------------------------- Currency Exchange Label ----------------------------------- #
        self.currency_label = customtkinter.CTkLabel(self.currency_label_frame, text="Currency Exchange", bg_color="#282828", height=0, width=0, text_font=("Arial", 14, "bold"))
        self.currency_label.pack()
        

      
        # ------------------------------- Convert Input Frame ----------------------------------- #
        self.input_convert_frame = customtkinter.CTkFrame(self.root, fg_color='#282828')
        self.input_convert_frame.pack(side=TOP, anchor="w", padx=(15, 0), pady=(10, 0))
        

        # ------------------------------- Currnecy Symbol Label ----------------------------------- #
        self.input_currency_symbol = customtkinter.CTkLabel(self.input_convert_frame, text="$", bg_color="#282828", height=0, width=0, text_font=("Arial", 16, "bold"))
        self.input_currency_symbol.grid(row=0, column=0, sticky='w')
        
        
        # ------------------------------- Input Currency Label ----------------------------------- #
        self.input_zero_base = customtkinter.StringVar(value="0")
        self.input_currency_input = customtkinter.CTkLabel(self.input_convert_frame, textvariable=self.input_zero_base, bg_color="#282828", height=0, width=0, text_font=("Arial", 30))
        self.input_currency_input.grid(row=0, column=1, sticky='we', padx=(0, 200), columnspan=3)


        # ------------------------------- Currency ComboBox Selectlor One ----------------------------------- #
        self.currency_selector = customtkinter.CTkComboBox(self.input_convert_frame, values=sorted(list(exchanges.keys())), width=170, command=self.first_currency_selector_function)
        self.currency_selector.set(list(exchanges.keys())[0])
        self.currency_selector.grid(row=1, column=0, columnspan=2, sticky='e', pady=(3, 0))

        # ------------------------------- End of Input Section ----------------------------------- #
      
      

        # ------------------------------- Start of Output Section ----------------------------------- #
      
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



        # ------------------------------- Update Time Stuff ----------------------------------- #
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



        # ------------------------------- Conversion Rates ----------------------------------- #

        # Frame for the conversion rates labels and stuff
        self.conversion_rates_frame = customtkinter.CTkFrame(self.root, fg_color='#282828')
        self.conversion_rates_frame.pack(side=TOP, anchor="w", padx=(15, 0), pady=(10, 0))
        
        # The conversion rates label
        self.conversion_rates_conversion_label = customtkinter.CTkLabel(self.conversion_rates_frame, text=f"1 USD = 1.0005 EUR\nUpdated: {self.month}/{self.day}/{self.year} {self.hour}:{self.minute} {self.pm_am}", text_font=("Arial", 10))
        self.conversion_rates_conversion_label.grid(row=0, column=0, sticky='w')
        
        # The update rates button
        self.update_rates_button = customtkinter.CTkButton(self.conversion_rates_frame, text="Update Rates", height=0, width=0, bg_color='#282828', command=self.update_rates_btn)
        self.update_rates_button.grid(row=1, column=0, pady=(2, 0), sticky='w')

        # ------------------------------- End of Conversion Rates ----------------------------------- #




        # ------------------------------- Main Button Frame ----------------------------------- #
        
        self.currency_exchange_buttons_frame = customtkinter.CTkFrame(self.root, fg_color="#282828")
        self.currency_exchange_buttons_frame.pack(side=TOP, anchor="n", padx=(0, 0), pady=(15, 0))



        # ------------------------------- First Button Frame ----------------------------------- #
        
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
        
        # ------------------------------- End First Button Frame ----------------------------------- #



        # ------------------------------- Second Button Frame ----------------------------------- #

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
        
        # ------------------------------- Second Button Frame ----------------------------------- #



        # ------------------------------- Third Button Frame ----------------------------------- #
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
        
        # ------------------------------- End Third Button Frame ----------------------------------- #



        # ------------------------------- Fourth Button Frame ----------------------------------- #
        
        self.fourth_exchange_set = customtkinter.CTkFrame(self.currency_exchange_buttons_frame)
        self.fourth_exchange_set.grid(row=3, column=0, sticky='e')
        

        # number 1 button
        self.btn_1 = tkinter.Button(self.fourth_exchange_set, text="1", width=6, font=("Arial", 16), bg="#404040", fg="white", relief='flat', command=lambda:self.exchange_1_btn("1"))
        self.btn_1.grid(row=0, column=0, sticky="n", padx=2, pady=2)
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
        
        # ------------------------------- End Fourth Button Frame ----------------------------------- #



        # ------------------------------- Fifth Button Frame ----------------------------------- #
        
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
        
        # ------------------------------- End Fifth Button Frame ----------------------------------- #



        # ------------------------------- Last Bottom Frame ----------------------------------- #
        self.last_exchange_frame = customtkinter.CTkFrame(self.root)
        self.last_exchange_frame.pack(side=BOTTOM)
        self.powered_by_api = customtkinter.CTkLabel(self.last_exchange_frame, text="Powered by ExchangeRate API", text_font=("Arial", 7), width=0, height=0, fg_color="#282828")
        self.powered_by_api.pack()
        # ------------------------------- End Last Bottom Frame ----------------------------------- #
        
        
                # menu
        my_menu = Menu(self.root)


        # create menu items
        file_menu = Menu(my_menu, tearoff=0, background='#303030', fg='white')
        my_menu.add_cascade(label="Calculators", menu=file_menu)


        file_menu.add_command(label="Standard Option",  command=lambda:self.return_standard_from_exchange())
        file_menu.add_command(label="Advanced Option",  command=lambda:self.return_advcanced_from_exchange())
            


        edit_menu = Menu(my_menu, tearoff=0, background='#303030', fg='white')
        my_menu.add_cascade(label="Converters", menu=edit_menu)
        
        edit_menu.add_command(label="Currency Exchange", state="disabled")
        edit_menu.add_command(label="Temperature", command=lambda:self.currency_to_temp())
        
        
        self.root.config(menu=my_menu)



    # ----------------------------------- Currency Exchange Methods ----------------------------------------- #
    
    
    
    # ----------------------------------- Numbered Event Methods --------------------------------------------- #
    
    # Exchange Button Event for Number 1:
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

    # --------------------------------- End Numbered Event Methods ------------------------------------------- #
    
    
    
    
    # --------------------------------- Currnecy Exchange Methods ------------------------------------------- #



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



    # Exchange Button All Clear
    def exchange_ac_btn(self, e):
        self.get_value = self.input_zero_base.get()
        if self.get_value == "0":
            pass
        elif self.get_value != "0":
            self.input_zero_base.set(value="0")
            self.output_zero_base.set(value="0")
        

    # Method for getting the output of input
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


    # Exchange Command for Backspace Key Event
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



    # ------------------------------ End of Currnecy Exchange Methods ----------------------------------------- #
    
    
    
    # ---------------------------- Start Advanced Switch Option Methods ------------------------------------ #
    
    

    # Method to return to advanced from currency exchange option
    def return_exchange_from_advanced(self):
        self.label_pack.pack_forget()
        self.header_label.pack_forget()
        self.zero_label_input.pack_forget()
        self.zero_label_widget.pack_forget()
        self.first_pack.pack_forget()
        self.first_set_cals_frame.pack_forget()
        self.advanced_second_btn_frame.pack_forget()
        self.third_btn_frame.pack_forget()
        self.advanced_fourth_btn_frame.pack_forget()
        self.advanced_fifth_btn_frame.pack_forget()
        self.advanced_sixth_btn_frame.pack_forget()
        
        self.execute_currency_exchange_option()
    
    # Method to return to advanced from tempertaure converter option
    def return_exchange_from_temp(self):
        self.temperature_label_frame.pack_forget()
        self.main_temp_label.pack_forget()
        self.input_temp_frame.pack_forget()
        self.output_tempertaure_frame.pack_forget()
        self.temperature_frame_for_all_buttons.pack_forget()

        
        
        self.execute_advanced_option("0")
    
    
    def advanced_to_temp(self):
        self.label_pack.pack_forget()
        self.header_label.pack_forget()
        self.zero_label_input.pack_forget()
        self.first_pack.pack_forget()
        self.zero_label_widget.pack_forget()
        self.first_set_cals_frame.pack_forget()
        self.advanced_second_btn_frame.pack_forget()
        self.third_btn_frame.pack_forget()
        self.advanced_fourth_btn_frame.pack_forget()
        self.advanced_fifth_btn_frame.pack_forget()
        self.advanced_sixth_btn_frame.pack_forget()
        
        self.execute_temp_option()
    # ---------------------------- End Standard Switch Option Methods ------------------------------------ #
        
    def currency_to_temp(self):
        self.currency_label_frame.pack_forget()
        self.currency_label.pack_forget()
        self.input_convert_frame.pack_forget()
        self.output_convert_frame.pack_forget()
        self.conversion_rates_frame.pack_forget()
        self.currency_exchange_buttons_frame.pack_forget()
        self.last_exchange_frame.pack_forget()
        self.powered_by_api.pack_forget()
        
        self.execute_temp_option()




    # ------------------------------- End of Currency Exchange Option --------------------------------------- #
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
     # ------------------------------------- Start of Temp Option  ------------------------------------- #
   
    def execute_temp_option(self):
        self.label_pack.pack_forget()
        self.standard_zero_label_input.pack_forget()
        self.first_set_cals_frame.pack_forget()
        self.first_pack.pack_forget()
        
        
        self.root.title("Temperature")
        self.root.geometry("280x480")
        
        # ------------------------------- Currency Exhchange Label Frame ----------------------------------- #
        self.temperature_label_frame = customtkinter.CTkFrame(self.root)
        self.temperature_label_frame.pack(side=TOP, anchor="w", padx=(15, 0), pady=(10, 0))
        
        # ------------------------------- Currency Exchange Label ----------------------------------- #
        self.main_temp_label = customtkinter.CTkLabel(self.temperature_label_frame, text="Temperature Converter", bg_color="#282828", height=0, width=0, text_font=("Arial", 14, "bold"))
        self.main_temp_label.pack()
        
      
        # ------------------------------- Convert Input Frame ----------------------------------- #
        self.input_temp_frame = customtkinter.CTkFrame(self.root, fg_color='#282828')
        self.input_temp_frame.pack(side=TOP, anchor="w", padx=(15, 0), pady=(10, 0))
        

        # ------------------------------- Input Currency Label ----------------------------------- #
        self.input_temp_string_var = customtkinter.StringVar(value="0")
        self.temperature_input_label = customtkinter.CTkLabel(self.input_temp_frame, textvariable=self.input_temp_string_var, bg_color="#282828", height=0, width=0, text_font=("Arial", 30))
        self.temperature_input_label.grid(row=0, column=1, sticky='we', padx=(0, 200), columnspan=3)


        # ------------------------------- Currency ComboBox Selectlor One ----------------------------------- #
        self.input_temp_first_selector = customtkinter.CTkComboBox(self.input_temp_frame, values=sorted(temps), width=170, command=self.first_temperature_selector)
        self.input_temp_first_selector.set(temps[0])
        self.input_temp_first_selector.grid(row=1, column=0, columnspan=2, sticky='e', pady=(3, 0))

        # ------------------------------- End of Input Section ----------------------------------- #
      
      

        # ------------------------------- Start of Output Section ----------------------------------- #
      
        # Frame for the out stuff
        self.output_tempertaure_frame = customtkinter.CTkFrame(self.root, fg_color="#282828")
        self.output_tempertaure_frame.pack(side=TOP, anchor="w", padx=(15, 0), pady=(10, 0))
        # The output label
        self.output_temp_string_var = customtkinter.StringVar(value="0")
        self.output_temp_label = customtkinter.CTkLabel(self.output_tempertaure_frame, textvariable=self.output_temp_string_var, bg_color="#282828", height=0, width=0, text_font=("Arial", 30), text_color='#BABABA')
        self.output_temp_label.grid(row=0, column=1, padx=(0, 200), columnspan=3, sticky='we')
        # The output currency selector (comboBox)
        self.output_temp_second_selector = customtkinter.CTkComboBox(self.output_tempertaure_frame, values=sorted(temps), width=170, command=self.second_temperature_selector)
        self.output_temp_second_selector.set(temps[2])
        self.output_temp_second_selector.grid(row=1, column=0, columnspan=2, sticky='e', pady=(3, 0))

        # end of output section

        # **************************************************************








        # ------------------------------- Main Button Frame ----------------------------------- #
        
        self.temperature_frame_for_all_buttons = customtkinter.CTkFrame(self.root, fg_color="#282828")
        self.temperature_frame_for_all_buttons.pack(side=TOP, anchor="n", padx=(0, 0), pady=(15, 0))



        # ------------------------------- First Button Frame ----------------------------------- #
        
        self.first_temp_set_btns = customtkinter.CTkFrame(self.temperature_frame_for_all_buttons, fg_color="#282828")
        self.first_temp_set_btns.grid(row=0, column=0, sticky='e')

        # number AC button
        self.btn_mut = tkinter.Button(self.first_temp_set_btns, text="AC", width=6, font=("Arial", 16), bg="#404040", fg="white", relief='flat', command=lambda: self.temp_ac_clear("0"))
        self.btn_mut.grid(row=0, column=2, sticky="w", padx=2, pady=2)
        # simple fg and bg change when hovered over.
        self.btn_mut.bind('<Enter>', lambda e: self.btn_mut.config(fg='black', bg='#4D4D4D'))
        self.btn_mut.bind('<Leave>', lambda e: self.btn_mut.config(fg='white', bg='#404040'))
        # keyboard press events **
        self.root.bind("c", lambda e: self.temp_ac_clear("c"))


        # number Backspace button 
        self.btn_sub = tkinter.Button(self.first_temp_set_btns, text="⌫", width=6, font=("Arial", 16), bg="#404040", fg="white", relief='flat', command=lambda:self.temp_backspace("0"))
        self.btn_sub.grid(row=0, column=3, sticky="w", padx=2, pady=2)
        # simple fg and bg change when hovered over.
        self.btn_sub.bind('<Enter>', lambda e: self.btn_sub.config(fg='black', bg='#4D4D4D'))
        self.btn_sub.bind('<Leave>', lambda e: self.btn_sub.config(fg='white', bg='#404040'))
        # keyboard press events **
        self.root.bind("<BackSpace>", lambda e: self.temp_backspace(" "))
        
        # ------------------------------- End First Button Frame ----------------------------------- #



        # ------------------------------- Second Button Frame ----------------------------------- #

        self.second_temp_set_btns = customtkinter.CTkFrame(self.temperature_frame_for_all_buttons)
        self.second_temp_set_btns.grid(row=1, column=0, sticky='e')
        
        # number 7 button
        self.btn_7 = tkinter.Button(self.second_temp_set_btns, text="7", width=6, font=("Arial", 16), bg="#404040", fg="white", relief='flat', command=lambda: self.temp_number_7("7"))
        self.btn_7.grid(row=0, column=0, sticky="n", padx=2, pady=2)
        # simple fg and bg change when hovered over.
        self.btn_7.bind('<Enter>', lambda e: self.btn_7.config(fg='black', bg='#4D4D4D'))
        self.btn_7.bind('<Leave>', lambda e: self.btn_7.config(fg='white', bg='#404040'))
        # keyboard press events **
        self.root.bind("7", lambda e: self.temp_number_7("7"))


        # number 8 button
        self.btn_8 = tkinter.Button(self.second_temp_set_btns, text="8", width=6, font=("Arial", 16), bg="#404040", fg="white", relief='flat', command=lambda: self.temp_number_8("8"))
        self.btn_8.grid(row=0, column=1, sticky="n", padx=2, pady=2)
        # simple fg and bg change when hovered over.
        self.btn_8.bind('<Enter>', lambda e: self.btn_8.config(fg='black', bg='#4D4D4D'))
        self.btn_8.bind('<Leave>', lambda e: self.btn_8.config(fg='white', bg='#404040'))
        # keyboard press events **
        self.root.bind("8", lambda e: self.temp_number_8("8"))


        # number 9 button
        self.btn_9 = tkinter.Button(self.second_temp_set_btns, text="9", width=6, font=("Arial", 16), bg="#404040", fg="white", relief='flat', command=lambda: self.temp_number_9("9"))
        self.btn_9.grid(row=0, column=2, sticky="n", padx=2, pady=2)
        # simple fg and bg change when hovered over.
        self.btn_9.bind('<Enter>', lambda e: self.btn_9.config(fg='black', bg='#4D4D4D'))
        self.btn_9.bind('<Leave>', lambda e: self.btn_9.config(fg='white', bg='#404040'))
        # keyboard press events **
        self.root.bind("9", lambda e: self.temp_number_9("9"))  
        
        # ------------------------------- Second Button Frame ----------------------------------- #



        # ------------------------------- Third Button Frame ----------------------------------- #
        self.third_temp_set_btns = customtkinter.CTkFrame(self.temperature_frame_for_all_buttons)
        self.third_temp_set_btns.grid(row=2, column=0, sticky='e')
        
        # number 4 button
        self.btn_4 = tkinter.Button(self.third_temp_set_btns, text="4", width=6, font=("Arial", 16), bg="#404040", fg="white", relief='flat', command=lambda:self.temp_number_4("4"))
        self.btn_4.grid(row=1, column=0, sticky="n", padx=2, pady=2)
        # simple fg and bg change when hovered over.
        self.btn_4.bind('<Enter>', lambda e: self.btn_4.config(fg='black', bg='#4D4D4D'))
        self.btn_4.bind('<Leave>', lambda e: self.btn_4.config(fg='white', bg='#404040'))
        # keyboard press events **
        self.root.bind("4", lambda e: self.temp_number_4("4"))


        # number 5 button
        self.btn_5 = tkinter.Button(self.third_temp_set_btns, text="5", width=6, font=("Arial", 16), bg="#404040", fg="white", relief='flat', command=lambda:self.temp_number_5("5"))
        self.btn_5.grid(row=1, column=1, sticky="n", padx=2, pady=2)
        # simple fg and bg change when hovered over.
        self.btn_5.bind('<Enter>', lambda e: self.btn_5.config(fg='black', bg='#4D4D4D'))
        self.btn_5.bind('<Leave>', lambda e: self.btn_5.config(fg='white', bg='#404040'))
        # keyboard press events **
        self.root.bind("5", lambda e: self.temp_number_5("5"))


        # number 6 button
        self.btn_6 = tkinter.Button(self.third_temp_set_btns, text="6", width=6, font=("Arial", 16), bg="#404040", fg="white", relief='flat', command=lambda:self.temp_number_6("6"))
        self.btn_6.grid(row=1, column=2, sticky="n", padx=2, pady=2)
        # simple fg and bg change when hovered over.
        self.btn_6.bind('<Enter>', lambda e: self.btn_6.config(fg='black', bg='#4D4D4D'))
        self.btn_6.bind('<Leave>', lambda e: self.btn_6.config(fg='white', bg='#404040'))
        # keyboard press events **
        self.root.bind("6", lambda e: self.temp_number_6("6"))
        
        # ------------------------------- End Third Button Frame ----------------------------------- #



        # ------------------------------- Fourth Button Frame ----------------------------------- #
        
        self.fourth_temp_set_btns = customtkinter.CTkFrame(self.temperature_frame_for_all_buttons)
        self.fourth_temp_set_btns.grid(row=3, column=0, sticky='e')
        

        # number 1 button
        self.btn_1 = tkinter.Button(self.fourth_temp_set_btns, text="1", width=6, font=("Arial", 16), bg="#404040", fg="white", relief='flat', command=lambda:self.temp_number_1("1"))
        self.btn_1.grid(row=0, column=0, sticky="n", padx=2, pady=2)
        # simple fg and bg change when hovered over.
        self.btn_1.bind('<Enter>', lambda e: self.btn_1.config(fg='black', bg='#4D4D4D'))
        self.btn_1.bind('<Leave>', lambda e: self.btn_1.config(fg='white', bg='#404040'))
        # keyboard press events **
        self.root.bind("1", lambda e: self.temp_number_1("1"))


        # number 2 button
        self.btn_2 = tkinter.Button(self.fourth_temp_set_btns, text="2", width=6, font=("Arial", 16), bg="#404040", fg="white", relief='flat', command=lambda:self.temp_number_2("2"))
        self.btn_2.grid(row=0, column=1, sticky="n", padx=2, pady=2)
        # simple fg and bg change when hovered over.
        self.btn_2.bind('<Enter>', lambda e: self.btn_2.config(fg='black', bg='#4D4D4D'))
        self.btn_2.bind('<Leave>', lambda e: self.btn_2.config(fg='white', bg='#404040'))
        # keyboard press events **
        self.root.bind("2", lambda e: self.temp_number_2("2"))


        # number 3 button
        self.btn_3 = tkinter.Button(self.fourth_temp_set_btns, text="3", width=6, font=("Arial", 16), bg="#404040", fg="white", relief='flat', command=lambda:self.temp_number_3("3"))
        self.btn_3.grid(row=0, column=2, sticky="n", padx=2, pady=2)
        # simple fg and bg change when hovered over.
        self.btn_3.bind('<Enter>', lambda e: self.btn_3.config(fg='black', bg='#4D4D4D'))
        self.btn_3.bind('<Leave>', lambda e: self.btn_3.config(fg='white', bg='#404040'))
        # keyboard press events **
        self.root.bind("3", lambda e: self.temp_number_3("3"))
        
        # ------------------------------- End Fourth Button Frame ----------------------------------- #



        # ------------------------------- Fifth Button Frame ----------------------------------- #
        
        self.fifth_temp_set_btns = customtkinter.CTkFrame(self.temperature_frame_for_all_buttons)
        self.fifth_temp_set_btns.grid(row=4, column=0, sticky='e')

        # number 0 button
        self.btn_plus_min = tkinter.Button(self.fifth_temp_set_btns, text="+/-", width=6, font=("Arial", 16), bg="#404040", fg="white", relief='flat', command=lambda: self.plus_minus_btn("0"))
        self.btn_plus_min.grid(row=1, column=0, sticky="n", padx=2, pady=2)
        # simple fg and bg change when hovered over.
        self.btn_plus_min.bind('<Enter>', lambda e: self.btn_plus_min.config(fg='black', bg='#4D4D4D'))
        self.btn_plus_min.bind('<Leave>', lambda e: self.btn_plus_min.config(fg='white', bg='#404040'))
        # keyboard press events **
        self.root.bind("0", lambda e: self.plus_minus_btn("0"))

        
        # number 0 button
        self.temp_btn_0 = tkinter.Button(self.fifth_temp_set_btns, text="0", width=6, font=("Arial", 16), bg="#404040", fg="white", relief='flat', command=lambda: self.temp_number_0("0"))
        self.temp_btn_0.grid(row=1, column=1, sticky="n", padx=2, pady=2)
        # simple fg and bg change when hovered over.
        self.temp_btn_0.bind('<Enter>', lambda e: self.temp_btn_0.config(fg='black', bg='#4D4D4D'))
        self.temp_btn_0.bind('<Leave>', lambda e: self.temp_btn_0.config(fg='white', bg='#404040'))
        # keyboard press events **
        self.root.bind("0", lambda e: self.temp_number_0("0"))
        
        
        # number dot button
        self.btn_dot = tkinter.Button(self.fifth_temp_set_btns, text=".", width=6, font=("Arial", 16), bg="#404040", fg="white", relief='flat', state='disabled')
        self.btn_dot.grid(row=1, column=2, sticky="n", padx=2, pady=2)
        
        # ------------------------------- End Fifth Button Frame ----------------------------------- #
        
        
        # menu
        my_menu = Menu(self.root)


        # create menu items
        file_menu = Menu(my_menu, tearoff=0, background='#303030', fg='white')
        my_menu.add_cascade(label="Calculators", menu=file_menu)
        
        file_menu.add_command(label="Standard Option", command=lambda:self.temp_to_standard())
        file_menu.add_command(label="Advanced Option", command=lambda:self.temp_to_advanced())
            


        edit_menu = Menu(my_menu, tearoff=0, background='#303030', fg='white')
        my_menu.add_cascade(label="Converters", menu=edit_menu)
        
        edit_menu.add_command(label="Currency Exchange", command=lambda:self.temp_to_currency())
        edit_menu.add_command(label="Temperature", state="disabled")
        
        self.root.config(menu=my_menu)

        # destorys the app if user presses escape key (convenience)
        self.root.bind("<Escape>", lambda e: self.root.destroy())
        # deleting stuff
        self.root.bind("<BackSpace>", lambda e: self.temp_backspace())
        # stops the user from resizing the app
        nothing = None
        
    # ---------------------------- Start of Temp Methods ---------------------------- #
    
    
    
    # ---------------------------- Temp Converter Methods ---------------------------- #
    
    def kelvin_to_fahrenhit(self):
        """Method for converting kelvin to fahrenhit"""
        K_VALUE = int(self.input_temp_string_var.get())
        K = (K_VALUE - 273.15) * 1.8 + 32
        final_value = str(K).split(".")[0] + "°F"
        return final_value
    
    
    def kelvin_to_celsius(self):
        K_VALUE = int(self.input_temp_string_var.get())
        K = (K_VALUE - 273.15)
        final_value = str(K).split(".")[0] + "°C"
        return final_value
    
    
    def fahrenheit_to_celsius(self):
        F_VALUE = int(self.input_temp_string_var.get())
        F = (F_VALUE - 32) * 5/9
        str_value = str(F).split(".")[0] + "°C"
        return str_value
    
    
    def fahrenheit_to_kelvin(self):
        F_VALUE = int(self.input_temp_string_var.get())
        F = (F_VALUE - 32) * 5/9 + 273.15
        split_value = str(F).split(".")[0]
        return split_value

    
    def celsius_to_fahrenhit(self):
        C_VALUE = int(self.input_temp_string_var.get())
        C = (C_VALUE * 9/5) + 32
        str_value = str(C).split(".")[0] + "°F"
        return str_value
    
    
    def celsius_to_kelvin(self):
        C_VALUE = int(self.input_temp_string_var.get())
        C = C_VALUE + 273.15
        str_value = str(C).split(".")[0]
        return str_value

    # ---------------------------- End Temp Converter Methods ---------------------------- #
    
    
    
    # ------------------------------ Numbers for Temperature Option ------------------------------- #
    
    def temp_number_9(self, e):
        value = self.input_temp_string_var.get()
        first_temp_selector = self.input_temp_first_selector.get()
        second_temp_selector = self.output_temp_second_selector.get()
        
        
        if value == "0":
            self.input_temp_string_var.set(value="9")
            
            # -- Checking Kelvin is first selected and Fahrenhit is second selected -- #
            if first_temp_selector == "Kelvin" and second_temp_selector == "Fahrenheit":
                self.output_temp_string_var.set(value=self.kelvin_to_fahrenhit())
                
            
            elif first_temp_selector == "Kelvin" and second_temp_selector == "Celsius":
                self.output_temp_string_var.set(value=self.kelvin_to_celsius())
            
            
            elif first_temp_selector == "Kelvin" and second_temp_selector == "Kelvin":
                K_VALUE = int(self.input_temp_string_var.get())
                self.output_temp_string_var.set(value=str(K_VALUE))
            
            
            
            # Checking Fahrenheit is first
            elif first_temp_selector == "Fahrenheit" and second_temp_selector == "Celsius":
                self.output_temp_string_var.set(value=self.fahrenheit_to_celsius())
            
            
            elif first_temp_selector == "Fahrenheit" and second_temp_selector == "Kelvin":
                self.output_temp_string_var.set(value=self.fahrenheit_to_kelvin())
            
            
            elif first_temp_selector == "Fahrenheit" and second_temp_selector == "Fahrenheit":
                F_VALUE = int(self.input_temp_string_var.get())
                self.output_temp_string_var.set(value=str(F_VALUE) + "°F")
            
            
            
            # Checking Celsius is first
            elif first_temp_selector == "Celsius" and second_temp_selector == "Kelvin":
                self.output_temp_string_var.set(value=self.celsius_to_kelvin())
                
                
            
            elif first_temp_selector == "Celsius" and second_temp_selector == "Fahrenheit":
                self.output_temp_string_var.set(value=self.celsius_to_fahrenhit())
                
                
            
            elif first_temp_selector == "Celsius" and second_temp_selector == "Celsius":
                C_VALUE = int(self.input_temp_string_var.get())
                self.output_temp_string_var.set(value=str(C_VALUE))
            
            
            
            
        elif value != "0":
            self.input_temp_string_var.set(value=value + "9")
            
            # Checking Kelvin is first
            if first_temp_selector == "Kelvin" and second_temp_selector == "Fahrenheit":
                self.output_temp_string_var.set(value=self.kelvin_to_fahrenhit())
                
        
            elif first_temp_selector == "Kelvin" and second_temp_selector == "Celsius":
                self.output_temp_string_var.set(value=self.kelvin_to_celsius())
            
            
            elif first_temp_selector == "Kelvin" and second_temp_selector == "Kelvin":
                K_VALUE = int(self.input_temp_string_var.get())
                self.output_temp_string_var.set(value=str(K_VALUE))
            
            
            
            # Checking Fahrenheit is first
            elif first_temp_selector == "Fahrenheit" and second_temp_selector == "Celsius":
                self.output_temp_string_var.set(value=self.fahrenheit_to_celsius())
            
            
            elif first_temp_selector == "Fahrenheit" and second_temp_selector == "Kelvin":
                self.output_temp_string_var.set(value=self.fahrenheit_to_kelvin())
            
            
            elif first_temp_selector == "Fahrenheit" and second_temp_selector == "Fahrenheit":
                F_VALUE = int(self.input_temp_string_var.get())
                self.output_temp_string_var.set(value=str(F_VALUE) + "°F")
            
            
            
            # Checking Celsius is first
            elif first_temp_selector == "Celsius" and second_temp_selector == "Kelvin":
                self.output_temp_string_var.set(value=self.celsius_to_kelvin())
                
                
            
            elif first_temp_selector == "Celsius" and second_temp_selector == "Fahrenheit":
                self.output_temp_string_var.set(value=self.celsius_to_fahrenhit())
                
                
            
            elif first_temp_selector == "Celsius" and second_temp_selector == "Celsius":
                C_VALUE = int(self.input_temp_string_var.get())
                self.output_temp_string_var.set(value=str(C_VALUE))
            
            
    def temp_number_8(self, e):
        value = self.input_temp_string_var.get()
        first_temp_selector = self.input_temp_first_selector.get()
        second_temp_selector = self.output_temp_second_selector.get()
        
        
        if value == "0":
            self.input_temp_string_var.set(value="8")
            
            # -- Checking Kelvin is first selected and Fahrenhit is second selected -- #
            if first_temp_selector == "Kelvin" and second_temp_selector == "Fahrenheit":
                self.output_temp_string_var.set(value=self.kelvin_to_fahrenhit())
                
            
            elif first_temp_selector == "Kelvin" and second_temp_selector == "Celsius":
                self.output_temp_string_var.set(value=self.kelvin_to_celsius())
            
            
            elif first_temp_selector == "Kelvin" and second_temp_selector == "Kelvin":
                K_VALUE = int(self.input_temp_string_var.get())
                self.output_temp_string_var.set(value=str(K_VALUE))
            
            
            
            # Checking Fahrenheit is first
            elif first_temp_selector == "Fahrenheit" and second_temp_selector == "Celsius":
                self.output_temp_string_var.set(value=self.fahrenheit_to_celsius())
            
            
            elif first_temp_selector == "Fahrenheit" and second_temp_selector == "Kelvin":
                self.output_temp_string_var.set(value=self.fahrenheit_to_kelvin())
            
            
            elif first_temp_selector == "Fahrenheit" and second_temp_selector == "Fahrenheit":
                F_VALUE = int(self.input_temp_string_var.get())
                self.output_temp_string_var.set(value=str(F_VALUE) + "°F")
            
            
            
            # Checking Celsius is first
            elif first_temp_selector == "Celsius" and second_temp_selector == "Kelvin":
                self.output_temp_string_var.set(value=self.celsius_to_kelvin())
                
                
            
            elif first_temp_selector == "Celsius" and second_temp_selector == "Fahrenheit":
                self.output_temp_string_var.set(value=self.celsius_to_fahrenhit())
                
                
            
            elif first_temp_selector == "Celsius" and second_temp_selector == "Celsius":
                C_VALUE = int(self.input_temp_string_var.get())
                self.output_temp_string_var.set(value=str(C_VALUE))
            
            
            
            
        elif value != "0":
            self.input_temp_string_var.set(value=value + "8")
            
            # Checking Kelvin is first
            if first_temp_selector == "Kelvin" and second_temp_selector == "Fahrenheit":
                self.output_temp_string_var.set(value=self.kelvin_to_fahrenhit())
                
        
            elif first_temp_selector == "Kelvin" and second_temp_selector == "Celsius":
                self.output_temp_string_var.set(value=self.kelvin_to_celsius())
            
            
            elif first_temp_selector == "Kelvin" and second_temp_selector == "Kelvin":
                K_VALUE = int(self.input_temp_string_var.get())
                self.output_temp_string_var.set(value=str(K_VALUE))
            
            
            
            # Checking Fahrenheit is first
            elif first_temp_selector == "Fahrenheit" and second_temp_selector == "Celsius":
                self.output_temp_string_var.set(value=self.fahrenheit_to_celsius())
            
            
            elif first_temp_selector == "Fahrenheit" and second_temp_selector == "Kelvin":
                self.output_temp_string_var.set(value=self.fahrenheit_to_kelvin())
            
            
            elif first_temp_selector == "Fahrenheit" and second_temp_selector == "Fahrenheit":
                F_VALUE = int(self.input_temp_string_var.get())
                self.output_temp_string_var.set(value=str(F_VALUE) + "°F")
            
            
            
            # Checking Celsius is first
            elif first_temp_selector == "Celsius" and second_temp_selector == "Kelvin":
                self.output_temp_string_var.set(value=self.celsius_to_kelvin())
                
                
            
            elif first_temp_selector == "Celsius" and second_temp_selector == "Fahrenheit":
                self.output_temp_string_var.set(value=self.celsius_to_fahrenhit())
                
                
            
            elif first_temp_selector == "Celsius" and second_temp_selector == "Celsius":
                C_VALUE = int(self.input_temp_string_var.get())
                self.output_temp_string_var.set(value=str(C_VALUE))
            
            
    def temp_number_7(self, e):
        value = self.input_temp_string_var.get()
        first_temp_selector = self.input_temp_first_selector.get()
        second_temp_selector = self.output_temp_second_selector.get()
        
        
        if value == "0":
            self.input_temp_string_var.set(value="7")
            
            # -- Checking Kelvin is first selected and Fahrenhit is second selected -- #
            if first_temp_selector == "Kelvin" and second_temp_selector == "Fahrenheit":
                self.output_temp_string_var.set(value=self.kelvin_to_fahrenhit())
                
            
            elif first_temp_selector == "Kelvin" and second_temp_selector == "Celsius":
                self.output_temp_string_var.set(value=self.kelvin_to_celsius())
            
            
            elif first_temp_selector == "Kelvin" and second_temp_selector == "Kelvin":
                K_VALUE = int(self.input_temp_string_var.get())
                self.output_temp_string_var.set(value=str(K_VALUE))
            
            
            
            # Checking Fahrenheit is first
            elif first_temp_selector == "Fahrenheit" and second_temp_selector == "Celsius":
                self.output_temp_string_var.set(value=self.fahrenheit_to_celsius())
            
            
            elif first_temp_selector == "Fahrenheit" and second_temp_selector == "Kelvin":
                self.output_temp_string_var.set(value=self.fahrenheit_to_kelvin())
            
            
            elif first_temp_selector == "Fahrenheit" and second_temp_selector == "Fahrenheit":
                F_VALUE = int(self.input_temp_string_var.get())
                self.output_temp_string_var.set(value=str(F_VALUE) + "°F")
            
            
            
            # Checking Celsius is first
            elif first_temp_selector == "Celsius" and second_temp_selector == "Kelvin":
                self.output_temp_string_var.set(value=self.celsius_to_kelvin())
                
                
            
            elif first_temp_selector == "Celsius" and second_temp_selector == "Fahrenheit":
                self.output_temp_string_var.set(value=self.celsius_to_fahrenhit())
                
                
            
            elif first_temp_selector == "Celsius" and second_temp_selector == "Celsius":
                C_VALUE = int(self.input_temp_string_var.get())
                self.output_temp_string_var.set(value=str(C_VALUE))
            
            
            
            
        elif value != "0":
            self.input_temp_string_var.set(value=value + "7")
            
            # Checking Kelvin is first
            if first_temp_selector == "Kelvin" and second_temp_selector == "Fahrenheit":
                self.output_temp_string_var.set(value=self.kelvin_to_fahrenhit())
                
        
            elif first_temp_selector == "Kelvin" and second_temp_selector == "Celsius":
                self.output_temp_string_var.set(value=self.kelvin_to_celsius())
            
            
            elif first_temp_selector == "Kelvin" and second_temp_selector == "Kelvin":
                K_VALUE = int(self.input_temp_string_var.get())
                self.output_temp_string_var.set(value=str(K_VALUE))
            
            
            
            # Checking Fahrenheit is first
            elif first_temp_selector == "Fahrenheit" and second_temp_selector == "Celsius":
                self.output_temp_string_var.set(value=self.fahrenheit_to_celsius())
            
            
            elif first_temp_selector == "Fahrenheit" and second_temp_selector == "Kelvin":
                self.output_temp_string_var.set(value=self.fahrenheit_to_kelvin())
            
            
            elif first_temp_selector == "Fahrenheit" and second_temp_selector == "Fahrenheit":
                F_VALUE = int(self.input_temp_string_var.get())
                self.output_temp_string_var.set(value=str(F_VALUE) + "°F")
            
            
            
            # Checking Celsius is first
            elif first_temp_selector == "Celsius" and second_temp_selector == "Kelvin":
                self.output_temp_string_var.set(value=self.celsius_to_kelvin())
                
                
            
            elif first_temp_selector == "Celsius" and second_temp_selector == "Fahrenheit":
                self.output_temp_string_var.set(value=self.celsius_to_fahrenhit())
                
                
            
            elif first_temp_selector == "Celsius" and second_temp_selector == "Celsius":
                C_VALUE = int(self.input_temp_string_var.get())
                self.output_temp_string_var.set(value=str(C_VALUE))
            
            
    def temp_number_6(self, e):
        value = self.input_temp_string_var.get()
        first_temp_selector = self.input_temp_first_selector.get()
        second_temp_selector = self.output_temp_second_selector.get()
        
        
        if value == "0":
            self.input_temp_string_var.set(value="6")
            
            # -- Checking Kelvin is first selected and Fahrenhit is second selected -- #
            if first_temp_selector == "Kelvin" and second_temp_selector == "Fahrenheit":
                self.output_temp_string_var.set(value=self.kelvin_to_fahrenhit())
                
            
            elif first_temp_selector == "Kelvin" and second_temp_selector == "Celsius":
                self.output_temp_string_var.set(value=self.kelvin_to_celsius())
            
            
            elif first_temp_selector == "Kelvin" and second_temp_selector == "Kelvin":
                K_VALUE = int(self.input_temp_string_var.get())
                self.output_temp_string_var.set(value=str(K_VALUE))
            
            
            
            # Checking Fahrenheit is first
            elif first_temp_selector == "Fahrenheit" and second_temp_selector == "Celsius":
                self.output_temp_string_var.set(value=self.fahrenheit_to_celsius())
            
            
            elif first_temp_selector == "Fahrenheit" and second_temp_selector == "Kelvin":
                self.output_temp_string_var.set(value=self.fahrenheit_to_kelvin())
            
            
            elif first_temp_selector == "Fahrenheit" and second_temp_selector == "Fahrenheit":
                F_VALUE = int(self.input_temp_string_var.get())
                self.output_temp_string_var.set(value=str(F_VALUE) + "°F")
            
            
            
            # Checking Celsius is first
            elif first_temp_selector == "Celsius" and second_temp_selector == "Kelvin":
                self.output_temp_string_var.set(value=self.celsius_to_kelvin())
                
                
            
            elif first_temp_selector == "Celsius" and second_temp_selector == "Fahrenheit":
                self.output_temp_string_var.set(value=self.celsius_to_fahrenhit())
                
                
            
            elif first_temp_selector == "Celsius" and second_temp_selector == "Celsius":
                C_VALUE = int(self.input_temp_string_var.get())
                self.output_temp_string_var.set(value=str(C_VALUE))
            
            
            
            
        elif value != "0":
            self.input_temp_string_var.set(value=value + "6")
            
            # Checking Kelvin is first
            if first_temp_selector == "Kelvin" and second_temp_selector == "Fahrenheit":
                self.output_temp_string_var.set(value=self.kelvin_to_fahrenhit())
                
        
            elif first_temp_selector == "Kelvin" and second_temp_selector == "Celsius":
                self.output_temp_string_var.set(value=self.kelvin_to_celsius())
            
            
            elif first_temp_selector == "Kelvin" and second_temp_selector == "Kelvin":
                K_VALUE = int(self.input_temp_string_var.get())
                self.output_temp_string_var.set(value=str(K_VALUE))
            
            
            
            # Checking Fahrenheit is first
            elif first_temp_selector == "Fahrenheit" and second_temp_selector == "Celsius":
                self.output_temp_string_var.set(value=self.fahrenheit_to_celsius())
            
            
            elif first_temp_selector == "Fahrenheit" and second_temp_selector == "Kelvin":
                self.output_temp_string_var.set(value=self.fahrenheit_to_kelvin())
            
            
            elif first_temp_selector == "Fahrenheit" and second_temp_selector == "Fahrenheit":
                F_VALUE = int(self.input_temp_string_var.get())
                self.output_temp_string_var.set(value=str(F_VALUE) + "°F")
            
            
            
            # Checking Celsius is first
            elif first_temp_selector == "Celsius" and second_temp_selector == "Kelvin":
                self.output_temp_string_var.set(value=self.celsius_to_kelvin())
                
                
            
            elif first_temp_selector == "Celsius" and second_temp_selector == "Fahrenheit":
                self.output_temp_string_var.set(value=self.celsius_to_fahrenhit())
                
                
            
            elif first_temp_selector == "Celsius" and second_temp_selector == "Celsius":
                C_VALUE = int(self.input_temp_string_var.get())
                self.output_temp_string_var.set(value=str(C_VALUE))
            
          
    def temp_number_5(self, e):
        value = self.input_temp_string_var.get()
        first_temp_selector = self.input_temp_first_selector.get()
        second_temp_selector = self.output_temp_second_selector.get()
        
        
        if value == "0":
            self.input_temp_string_var.set(value="5")
            
            # -- Checking Kelvin is first selected and Fahrenhit is second selected -- #
            if first_temp_selector == "Kelvin" and second_temp_selector == "Fahrenheit":
                self.output_temp_string_var.set(value=self.kelvin_to_fahrenhit())
                
            
            elif first_temp_selector == "Kelvin" and second_temp_selector == "Celsius":
                self.output_temp_string_var.set(value=self.kelvin_to_celsius())
            
            
            elif first_temp_selector == "Kelvin" and second_temp_selector == "Kelvin":
                K_VALUE = int(self.input_temp_string_var.get())
                self.output_temp_string_var.set(value=str(K_VALUE))
            
            
            
            # Checking Fahrenheit is first
            elif first_temp_selector == "Fahrenheit" and second_temp_selector == "Celsius":
                self.output_temp_string_var.set(value=self.fahrenheit_to_celsius())
            
            
            elif first_temp_selector == "Fahrenheit" and second_temp_selector == "Kelvin":
                self.output_temp_string_var.set(value=self.fahrenheit_to_kelvin())
            
            
            elif first_temp_selector == "Fahrenheit" and second_temp_selector == "Fahrenheit":
                F_VALUE = int(self.input_temp_string_var.get())
                self.output_temp_string_var.set(value=str(F_VALUE) + "°F")
            
            
            
            # Checking Celsius is first
            elif first_temp_selector == "Celsius" and second_temp_selector == "Kelvin":
                self.output_temp_string_var.set(value=self.celsius_to_kelvin())
                
                
            
            elif first_temp_selector == "Celsius" and second_temp_selector == "Fahrenheit":
                self.output_temp_string_var.set(value=self.celsius_to_fahrenhit())
                
                
            
            elif first_temp_selector == "Celsius" and second_temp_selector == "Celsius":
                C_VALUE = int(self.input_temp_string_var.get())
                self.output_temp_string_var.set(value=str(C_VALUE))
            
            
            
            
        elif value != "0":
            self.input_temp_string_var.set(value=value + "5")
            
            # Checking Kelvin is first
            if first_temp_selector == "Kelvin" and second_temp_selector == "Fahrenheit":
                self.output_temp_string_var.set(value=self.kelvin_to_fahrenhit())
                
        
            elif first_temp_selector == "Kelvin" and second_temp_selector == "Celsius":
                self.output_temp_string_var.set(value=self.kelvin_to_celsius())
            
            
            elif first_temp_selector == "Kelvin" and second_temp_selector == "Kelvin":
                K_VALUE = int(self.input_temp_string_var.get())
                self.output_temp_string_var.set(value=str(K_VALUE))
            
            
            
            # Checking Fahrenheit is first
            elif first_temp_selector == "Fahrenheit" and second_temp_selector == "Celsius":
                self.output_temp_string_var.set(value=self.fahrenheit_to_celsius())
            
            
            elif first_temp_selector == "Fahrenheit" and second_temp_selector == "Kelvin":
                self.output_temp_string_var.set(value=self.fahrenheit_to_kelvin())
            
            
            elif first_temp_selector == "Fahrenheit" and second_temp_selector == "Fahrenheit":
                F_VALUE = int(self.input_temp_string_var.get())
                self.output_temp_string_var.set(value=str(F_VALUE) + "°F")
            
            
            
            # Checking Celsius is first
            elif first_temp_selector == "Celsius" and second_temp_selector == "Kelvin":
                self.output_temp_string_var.set(value=self.celsius_to_kelvin())
                
                
            
            elif first_temp_selector == "Celsius" and second_temp_selector == "Fahrenheit":
                self.output_temp_string_var.set(value=self.celsius_to_fahrenhit())
                
                
            
            elif first_temp_selector == "Celsius" and second_temp_selector == "Celsius":
                C_VALUE = int(self.input_temp_string_var.get())
                self.output_temp_string_var.set(value=str(C_VALUE))
            
            
    def temp_number_4(self, e):
        value = self.input_temp_string_var.get()
        first_temp_selector = self.input_temp_first_selector.get()
        second_temp_selector = self.output_temp_second_selector.get()
        
        
        if value == "0":
            self.input_temp_string_var.set(value="4")
            
            # -- Checking Kelvin is first selected and Fahrenhit is second selected -- #
            if first_temp_selector == "Kelvin" and second_temp_selector == "Fahrenheit":
                self.output_temp_string_var.set(value=self.kelvin_to_fahrenhit())
                
            
            elif first_temp_selector == "Kelvin" and second_temp_selector == "Celsius":
                self.output_temp_string_var.set(value=self.kelvin_to_celsius())
            
            
            elif first_temp_selector == "Kelvin" and second_temp_selector == "Kelvin":
                K_VALUE = int(self.input_temp_string_var.get())
                self.output_temp_string_var.set(value=str(K_VALUE))
            
            
            
            # Checking Fahrenheit is first
            elif first_temp_selector == "Fahrenheit" and second_temp_selector == "Celsius":
                self.output_temp_string_var.set(value=self.fahrenheit_to_celsius())
            
            
            elif first_temp_selector == "Fahrenheit" and second_temp_selector == "Kelvin":
                self.output_temp_string_var.set(value=self.fahrenheit_to_kelvin())
            
            
            elif first_temp_selector == "Fahrenheit" and second_temp_selector == "Fahrenheit":
                F_VALUE = int(self.input_temp_string_var.get())
                self.output_temp_string_var.set(value=str(F_VALUE) + "°F")
            
            
            
            # Checking Celsius is first
            elif first_temp_selector == "Celsius" and second_temp_selector == "Kelvin":
                self.output_temp_string_var.set(value=self.celsius_to_kelvin())
                
                
            
            elif first_temp_selector == "Celsius" and second_temp_selector == "Fahrenheit":
                self.output_temp_string_var.set(value=self.celsius_to_fahrenhit())
                
                
            
            elif first_temp_selector == "Celsius" and second_temp_selector == "Celsius":
                C_VALUE = int(self.input_temp_string_var.get())
                self.output_temp_string_var.set(value=str(C_VALUE))
            
            
            
            
        elif value != "0":
            self.input_temp_string_var.set(value=value + "4")
            
            # Checking Kelvin is first
            if first_temp_selector == "Kelvin" and second_temp_selector == "Fahrenheit":
                self.output_temp_string_var.set(value=self.kelvin_to_fahrenhit())
                
        
            elif first_temp_selector == "Kelvin" and second_temp_selector == "Celsius":
                self.output_temp_string_var.set(value=self.kelvin_to_celsius())
            
            
            elif first_temp_selector == "Kelvin" and second_temp_selector == "Kelvin":
                K_VALUE = int(self.input_temp_string_var.get())
                self.output_temp_string_var.set(value=str(K_VALUE))
            
            
            
            # Checking Fahrenheit is first
            elif first_temp_selector == "Fahrenheit" and second_temp_selector == "Celsius":
                self.output_temp_string_var.set(value=self.fahrenheit_to_celsius())
            
            
            elif first_temp_selector == "Fahrenheit" and second_temp_selector == "Kelvin":
                self.output_temp_string_var.set(value=self.fahrenheit_to_kelvin())
            
            
            elif first_temp_selector == "Fahrenheit" and second_temp_selector == "Fahrenheit":
                F_VALUE = int(self.input_temp_string_var.get())
                self.output_temp_string_var.set(value=str(F_VALUE) + "°F")
            
            
            
            # Checking Celsius is first
            elif first_temp_selector == "Celsius" and second_temp_selector == "Kelvin":
                self.output_temp_string_var.set(value=self.celsius_to_kelvin())
                
                
            
            elif first_temp_selector == "Celsius" and second_temp_selector == "Fahrenheit":
                self.output_temp_string_var.set(value=self.celsius_to_fahrenhit())
                
                
            
            elif first_temp_selector == "Celsius" and second_temp_selector == "Celsius":
                C_VALUE = int(self.input_temp_string_var.get())
                self.output_temp_string_var.set(value=str(C_VALUE))
            
            
    def temp_number_3(self, e):
        value = self.input_temp_string_var.get()
        first_temp_selector = self.input_temp_first_selector.get()
        second_temp_selector = self.output_temp_second_selector.get()
        
        
        if value == "0":
            self.input_temp_string_var.set(value="3")
            
            # -- Checking Kelvin is first selected and Fahrenhit is second selected -- #
            if first_temp_selector == "Kelvin" and second_temp_selector == "Fahrenheit":
                self.output_temp_string_var.set(value=self.kelvin_to_fahrenhit())
                
            
            elif first_temp_selector == "Kelvin" and second_temp_selector == "Celsius":
                self.output_temp_string_var.set(value=self.kelvin_to_celsius())
            
            
            elif first_temp_selector == "Kelvin" and second_temp_selector == "Kelvin":
                K_VALUE = int(self.input_temp_string_var.get())
                self.output_temp_string_var.set(value=str(K_VALUE))
            
            
            
            # Checking Fahrenheit is first
            elif first_temp_selector == "Fahrenheit" and second_temp_selector == "Celsius":
                self.output_temp_string_var.set(value=self.fahrenheit_to_celsius())
            
            
            elif first_temp_selector == "Fahrenheit" and second_temp_selector == "Kelvin":
                self.output_temp_string_var.set(value=self.fahrenheit_to_kelvin())
            
            
            elif first_temp_selector == "Fahrenheit" and second_temp_selector == "Fahrenheit":
                F_VALUE = int(self.input_temp_string_var.get())
                self.output_temp_string_var.set(value=str(F_VALUE) + "°F")
            
            
            
            # Checking Celsius is first
            elif first_temp_selector == "Celsius" and second_temp_selector == "Kelvin":
                self.output_temp_string_var.set(value=self.celsius_to_kelvin())
                
                
            
            elif first_temp_selector == "Celsius" and second_temp_selector == "Fahrenheit":
                self.output_temp_string_var.set(value=self.celsius_to_fahrenhit())
                
                
            
            elif first_temp_selector == "Celsius" and second_temp_selector == "Celsius":
                C_VALUE = int(self.input_temp_string_var.get())
                self.output_temp_string_var.set(value=str(C_VALUE))
            
            
            
            
        elif value != "0":
            self.input_temp_string_var.set(value=value + "3")
            
            # Checking Kelvin is first
            if first_temp_selector == "Kelvin" and second_temp_selector == "Fahrenheit":
                self.output_temp_string_var.set(value=self.kelvin_to_fahrenhit())
                
        
            elif first_temp_selector == "Kelvin" and second_temp_selector == "Celsius":
                self.output_temp_string_var.set(value=self.kelvin_to_celsius())
            
            
            elif first_temp_selector == "Kelvin" and second_temp_selector == "Kelvin":
                K_VALUE = int(self.input_temp_string_var.get())
                self.output_temp_string_var.set(value=str(K_VALUE))
            
            
            
            # Checking Fahrenheit is first
            elif first_temp_selector == "Fahrenheit" and second_temp_selector == "Celsius":
                self.output_temp_string_var.set(value=self.fahrenheit_to_celsius())
            
            
            elif first_temp_selector == "Fahrenheit" and second_temp_selector == "Kelvin":
                self.output_temp_string_var.set(value=self.fahrenheit_to_kelvin())
            
            
            elif first_temp_selector == "Fahrenheit" and second_temp_selector == "Fahrenheit":
                F_VALUE = int(self.input_temp_string_var.get())
                self.output_temp_string_var.set(value=str(F_VALUE) + "°F")
            
            
            
            # Checking Celsius is first
            elif first_temp_selector == "Celsius" and second_temp_selector == "Kelvin":
                self.output_temp_string_var.set(value=self.celsius_to_kelvin())
                
                
            
            elif first_temp_selector == "Celsius" and second_temp_selector == "Fahrenheit":
                self.output_temp_string_var.set(value=self.celsius_to_fahrenhit())
                
                
            
            elif first_temp_selector == "Celsius" and second_temp_selector == "Celsius":
                C_VALUE = int(self.input_temp_string_var.get())
                self.output_temp_string_var.set(value=str(C_VALUE))
            
            
    def temp_number_2(self, e):
        value = self.input_temp_string_var.get()
        first_temp_selector = self.input_temp_first_selector.get()
        second_temp_selector = self.output_temp_second_selector.get()
        
        
        if value == "0":
            self.input_temp_string_var.set(value="2")
            
            # -- Checking Kelvin is first selected and Fahrenhit is second selected -- #
            if first_temp_selector == "Kelvin" and second_temp_selector == "Fahrenheit":
                self.output_temp_string_var.set(value=self.kelvin_to_fahrenhit())
                
            
            elif first_temp_selector == "Kelvin" and second_temp_selector == "Celsius":
                self.output_temp_string_var.set(value=self.kelvin_to_celsius())
            
            
            elif first_temp_selector == "Kelvin" and second_temp_selector == "Kelvin":
                K_VALUE = int(self.input_temp_string_var.get())
                self.output_temp_string_var.set(value=str(K_VALUE))
            
            
            
            # Checking Fahrenheit is first
            elif first_temp_selector == "Fahrenheit" and second_temp_selector == "Celsius":
                self.output_temp_string_var.set(value=self.fahrenheit_to_celsius())
            
            
            elif first_temp_selector == "Fahrenheit" and second_temp_selector == "Kelvin":
                self.output_temp_string_var.set(value=self.fahrenheit_to_kelvin())
            
            
            elif first_temp_selector == "Fahrenheit" and second_temp_selector == "Fahrenheit":
                F_VALUE = int(self.input_temp_string_var.get())
                self.output_temp_string_var.set(value=str(F_VALUE) + "°F")
            
            
            
            # Checking Celsius is first
            elif first_temp_selector == "Celsius" and second_temp_selector == "Kelvin":
                self.output_temp_string_var.set(value=self.celsius_to_kelvin())
                
                
            
            elif first_temp_selector == "Celsius" and second_temp_selector == "Fahrenheit":
                self.output_temp_string_var.set(value=self.celsius_to_fahrenhit())
                
                
            
            elif first_temp_selector == "Celsius" and second_temp_selector == "Celsius":
                C_VALUE = int(self.input_temp_string_var.get())
                self.output_temp_string_var.set(value=str(C_VALUE))
            
            
            
            
        elif value != "0":
            self.input_temp_string_var.set(value=value + "2")
            
            # Checking Kelvin is first
            if first_temp_selector == "Kelvin" and second_temp_selector == "Fahrenheit":
                self.output_temp_string_var.set(value=self.kelvin_to_fahrenhit())
                
        
            elif first_temp_selector == "Kelvin" and second_temp_selector == "Celsius":
                self.output_temp_string_var.set(value=self.kelvin_to_celsius())
            
            
            elif first_temp_selector == "Kelvin" and second_temp_selector == "Kelvin":
                K_VALUE = int(self.input_temp_string_var.get())
                self.output_temp_string_var.set(value=str(K_VALUE))
            
            
            
            # Checking Fahrenheit is first
            elif first_temp_selector == "Fahrenheit" and second_temp_selector == "Celsius":
                self.output_temp_string_var.set(value=self.fahrenheit_to_celsius())
            
            
            elif first_temp_selector == "Fahrenheit" and second_temp_selector == "Kelvin":
                self.output_temp_string_var.set(value=self.fahrenheit_to_kelvin())
            
            
            elif first_temp_selector == "Fahrenheit" and second_temp_selector == "Fahrenheit":
                F_VALUE = int(self.input_temp_string_var.get())
                self.output_temp_string_var.set(value=str(F_VALUE) + "°F")
            
            
            
            # Checking Celsius is first
            elif first_temp_selector == "Celsius" and second_temp_selector == "Kelvin":
                self.output_temp_string_var.set(value=self.celsius_to_kelvin())
                
                
            
            elif first_temp_selector == "Celsius" and second_temp_selector == "Fahrenheit":
                self.output_temp_string_var.set(value=self.celsius_to_fahrenhit())
                
                
            
            elif first_temp_selector == "Celsius" and second_temp_selector == "Celsius":
                C_VALUE = int(self.input_temp_string_var.get())
                self.output_temp_string_var.set(value=str(C_VALUE))
            

    def temp_number_1(self, e):
        value = self.input_temp_string_var.get()
        first_temp_selector = self.input_temp_first_selector.get()
        second_temp_selector = self.output_temp_second_selector.get()
        
        
        if value == "0":
            self.input_temp_string_var.set(value="1")
            
            # -- Checking Kelvin is first selected and Fahrenhit is second selected -- #
            if first_temp_selector == "Kelvin" and second_temp_selector == "Fahrenheit":
                self.output_temp_string_var.set(value=self.kelvin_to_fahrenhit())
                
            
            elif first_temp_selector == "Kelvin" and second_temp_selector == "Celsius":
                self.output_temp_string_var.set(value=self.kelvin_to_celsius())
            
            
            elif first_temp_selector == "Kelvin" and second_temp_selector == "Kelvin":
                K_VALUE = int(self.input_temp_string_var.get())
                self.output_temp_string_var.set(value=str(K_VALUE))
            
            
            
            # Checking Fahrenheit is first
            elif first_temp_selector == "Fahrenheit" and second_temp_selector == "Celsius":
                self.output_temp_string_var.set(value=self.fahrenheit_to_celsius())
            
            
            elif first_temp_selector == "Fahrenheit" and second_temp_selector == "Kelvin":
                self.output_temp_string_var.set(value=self.fahrenheit_to_kelvin())
            
            
            elif first_temp_selector == "Fahrenheit" and second_temp_selector == "Fahrenheit":
                F_VALUE = int(self.input_temp_string_var.get())
                self.output_temp_string_var.set(value=str(F_VALUE) + "°F")
            
            
            
            # Checking Celsius is first
            elif first_temp_selector == "Celsius" and second_temp_selector == "Kelvin":
                self.output_temp_string_var.set(value=self.celsius_to_kelvin())
                
                
            
            elif first_temp_selector == "Celsius" and second_temp_selector == "Fahrenheit":
                self.output_temp_string_var.set(value=self.celsius_to_fahrenhit())
                
                
            
            elif first_temp_selector == "Celsius" and second_temp_selector == "Celsius":
                C_VALUE = int(self.input_temp_string_var.get())
                self.output_temp_string_var.set(value=str(C_VALUE))
            
            
            
            
        elif value != "0":
            self.input_temp_string_var.set(value=value + "1")
            
            # Checking Kelvin is first
            if first_temp_selector == "Kelvin" and second_temp_selector == "Fahrenheit":
                self.output_temp_string_var.set(value=self.kelvin_to_fahrenhit())
                
        
            elif first_temp_selector == "Kelvin" and second_temp_selector == "Celsius":
                self.output_temp_string_var.set(value=self.kelvin_to_celsius())
            
            
            elif first_temp_selector == "Kelvin" and second_temp_selector == "Kelvin":
                K_VALUE = int(self.input_temp_string_var.get())
                self.output_temp_string_var.set(value=str(K_VALUE))
            
            
            
            # Checking Fahrenheit is first
            elif first_temp_selector == "Fahrenheit" and second_temp_selector == "Celsius":
                self.output_temp_string_var.set(value=self.fahrenheit_to_celsius())
            
            
            elif first_temp_selector == "Fahrenheit" and second_temp_selector == "Kelvin":
                self.output_temp_string_var.set(value=self.fahrenheit_to_kelvin())
            
            
            elif first_temp_selector == "Fahrenheit" and second_temp_selector == "Fahrenheit":
                F_VALUE = int(self.input_temp_string_var.get())
                self.output_temp_string_var.set(value=str(F_VALUE) + "°F")
            
            
            
            # Checking Celsius is first
            elif first_temp_selector == "Celsius" and second_temp_selector == "Kelvin":
                self.output_temp_string_var.set(value=self.celsius_to_kelvin())
                
                
            
            elif first_temp_selector == "Celsius" and second_temp_selector == "Fahrenheit":
                self.output_temp_string_var.set(value=self.celsius_to_fahrenhit())
                
                
            
            elif first_temp_selector == "Celsius" and second_temp_selector == "Celsius":
                C_VALUE = int(self.input_temp_string_var.get())
                self.output_temp_string_var.set(value=str(C_VALUE))
            
            
    def temp_number_0(self, e):
        value = self.input_temp_string_var.get()
        first_temp_selector = self.input_temp_first_selector.get()
        second_temp_selector = self.output_temp_second_selector.get()
        
        
        if value == "0":
            pass
            
        elif value != "0":
            self.input_temp_string_var.set(value=value + "0")
            
            # Checking Kelvin is first
            if first_temp_selector == "Kelvin" and second_temp_selector == "Fahrenheit":
                self.output_temp_string_var.set(value=self.kelvin_to_fahrenhit())
                
        
            elif first_temp_selector == "Kelvin" and second_temp_selector == "Celsius":
                self.output_temp_string_var.set(value=self.kelvin_to_celsius())
            
            
            elif first_temp_selector == "Kelvin" and second_temp_selector == "Kelvin":
                K_VALUE = int(self.input_temp_string_var.get())
                self.output_temp_string_var.set(value=str(K_VALUE))
            
            
            
            # Checking Fahrenheit is first
            elif first_temp_selector == "Fahrenheit" and second_temp_selector == "Celsius":
                self.output_temp_string_var.set(value=self.fahrenheit_to_celsius())
            
            
            elif first_temp_selector == "Fahrenheit" and second_temp_selector == "Kelvin":
                self.output_temp_string_var.set(value=self.fahrenheit_to_kelvin())
            
            
            elif first_temp_selector == "Fahrenheit" and second_temp_selector == "Fahrenheit":
                F_VALUE = int(self.input_temp_string_var.get())
                self.output_temp_string_var.set(value=str(F_VALUE) + "°F")
            
            
            
            # Checking Celsius is first
            elif first_temp_selector == "Celsius" and second_temp_selector == "Kelvin":
                self.output_temp_string_var.set(value=self.celsius_to_kelvin())
                
                
            
            elif first_temp_selector == "Celsius" and second_temp_selector == "Fahrenheit":
                self.output_temp_string_var.set(value=self.celsius_to_fahrenhit())
                
                
            
            elif first_temp_selector == "Celsius" and second_temp_selector == "Celsius":
                C_VALUE = int(self.input_temp_string_var.get())
                self.output_temp_string_var.set(value=str(C_VALUE))
            
    # ------------------------------ End Numbers for Temperature Option ------------------------------- #
        
        
        
    # ----------------------------------- Temperature Selectors ------------------------------------- #
    
    def first_temperature_selector(self, e):
        temp_degree_input = self.input_temp_first_selector.get()
        temp_degree_output = self.output_temp_second_selector.get()
        value = self.input_temp_string_var.get()
            
            
        if value != "0":
            # Checking Kelvin is first
            if temp_degree_input == "Kelvin" and temp_degree_output == "Fahrenheit":
                self.output_temp_string_var.set(value=self.kelvin_to_fahrenhit())
                
        
            elif temp_degree_input == "Kelvin" and temp_degree_output == "Celsius":
                self.output_temp_string_var.set(value=self.kelvin_to_celsius())
            
            
            elif temp_degree_input == "Kelvin" and temp_degree_output == "Kelvin":
                K_VALUE = int(self.input_temp_string_var.get())
                self.output_temp_string_var.set(value=str(K_VALUE))
            
            
            
            # Checking Fahrenheit is first
            elif temp_degree_input == "Fahrenheit" and temp_degree_output == "Celsius":
                self.output_temp_string_var.set(value=self.fahrenheit_to_celsius())
            
            
            elif temp_degree_input == "Fahrenheit" and temp_degree_output == "Kelvin":
                self.output_temp_string_var.set(value=self.fahrenheit_to_kelvin())
            
            
            elif temp_degree_input == "Fahrenheit" and temp_degree_output == "Fahrenheit":
                F_VALUE = int(self.input_temp_string_var.get())
                self.output_temp_string_var.set(value=str(F_VALUE) + "°F")
            
            
            
            # Checking Celsius is first
            elif temp_degree_input == "Celsius" and temp_degree_output == "Kelvin":
                self.output_temp_string_var.set(value=self.celsius_to_kelvin())
                
                
            
            elif temp_degree_input == "Celsius" and temp_degree_output == "Fahrenheit":
                self.output_temp_string_var.set(value=self.celsius_to_fahrenhit())
                
                
            
            elif temp_degree_input == "Celsius" and temp_degree_output == "Celsius":
                C_VALUE = int(self.input_temp_string_var.get())
                self.output_temp_string_var.set(value=str(C_VALUE))
 
 
    def second_temperature_selector(self, e):
        temp_degree_input = self.input_temp_first_selector.get()
        temp_degree_output = self.output_temp_second_selector.get()
        value = self.input_temp_string_var.get()
            
            
        if value != "0":
            # Checking Kelvin is first
            if temp_degree_input == "Kelvin" and temp_degree_output == "Fahrenheit":
                self.output_temp_string_var.set(value=self.kelvin_to_fahrenhit())
                
        
            elif temp_degree_input == "Kelvin" and temp_degree_output == "Celsius":
                self.output_temp_string_var.set(value=self.kelvin_to_celsius())
            
            
            elif temp_degree_input == "Kelvin" and temp_degree_output == "Kelvin":
                K_VALUE = int(self.input_temp_string_var.get())
                self.output_temp_string_var.set(value=str(K_VALUE))
            
            
            
            # Checking Fahrenheit is first
            elif temp_degree_input == "Fahrenheit" and temp_degree_output == "Celsius":
                self.output_temp_string_var.set(value=self.fahrenheit_to_celsius())
            
            
            elif temp_degree_input == "Fahrenheit" and temp_degree_output == "Kelvin":
                self.output_temp_string_var.set(value=self.fahrenheit_to_kelvin())
            
            
            elif temp_degree_input == "Fahrenheit" and temp_degree_output == "Fahrenheit":
                F_VALUE = int(self.input_temp_string_var.get())
                self.output_temp_string_var.set(value=str(F_VALUE) + "°F")
            
            
            
            # Checking Celsius is first
            elif temp_degree_input == "Celsius" and temp_degree_output == "Kelvin":
                self.output_temp_string_var.set(value=self.celsius_to_kelvin())
                
                
            
            elif temp_degree_input == "Celsius" and temp_degree_output == "Fahrenheit":
                self.output_temp_string_var.set(value=self.celsius_to_fahrenhit())
                
                
            
            elif temp_degree_input == "Celsius" and temp_degree_output == "Celsius":
                C_VALUE = int(self.input_temp_string_var.get())
                self.output_temp_string_var.set(value=str(C_VALUE))
 
    # ----------------------------------- End Temperature Selectors ------------------------------------- #
    
    
    
    # ----------------------------------- Start of Misc Temp Methods ------------------------------------- #
    
    def temp_ac_clear(self, e):
        value = self.input_temp_string_var.get()
        value2 = self.output_temp_string_var.get()
        
        if value == "0" and value2 == "0":
            pass
        
        elif value != "0" and value2 != "0":
            self.input_temp_string_var.set(value="0")
            self.output_temp_string_var.set(value="0")
    
    
    def temp_backspace(self, e):
        value = self.input_temp_string_var.get()
        first_temp_selector = self.input_temp_first_selector.get()
        second_temp_selector = self.output_temp_second_selector.get()
        
        if value == "0":
            pass
        
        elif value != "0" and len(value) == 1:
            self.input_temp_string_var.set(value="0")
            self.output_temp_string_var.set(value="0")
            
        elif value != "0" and len(value) > 1:
            cutting_value = self.input_temp_string_var.get()[:-1]
            self.input_temp_string_var.set(value=cutting_value)
            new_value = self.input_temp_string_var.get()
            
            if new_value != "0":
                
                if first_temp_selector == "Fahrenheit" and second_temp_selector == "Celsius":
                    self.output_temp_string_var.set(value=self.fahrenheit_to_celsius())
                
                elif first_temp_selector == "Fahrenheit" and second_temp_selector == "Kelvin":
                    self.output_temp_string_var.set(value=self.fahrenheit_to_kelvin())
                
                elif first_temp_selector == "Fahrenheit" and second_temp_selector == "Fahrenheit":
                    F_VALUE = int(self.input_temp_string_var.get())
                    self.output_temp_string_var.set(value=str(F_VALUE) + "°F")
                
                
                
                elif first_temp_selector == "Celsius" and second_temp_selector == "Kelvin":
                    self.output_temp_string_var.set(value=self.celsius_to_kelvin())
                
                elif first_temp_selector == "Celsius" and second_temp_selector == "Fahrenheit":
                    self.output_temp_string_var.set(value=self.celsius_to_fahrenhit())
            
                elif first_temp_selector == "Celsius" and second_temp_selector == "Celsius":
                    C_VALUE = int(self.input_temp_string_var.get())
                    self.output_temp_string_var.set(value=str(C_VALUE))
                
                
                
                elif first_temp_selector == "Kelvin" and second_temp_selector == "Fahrenheit":
                    self.output_temp_string_var.set(value=self.kelvin_to_fahrenhit())
                
                elif first_temp_selector == "Kelvin" and second_temp_selector == "Celsius":
                    self.output_temp_string_var.set(value=self.kelvin_to_celsius())
            
                elif first_temp_selector == "Kelvin" and second_temp_selector == "Kelvin":
                    K_VALUE = int(self.input_temp_string_var.get())
                    self.output_temp_string_var.set(value=str(K_VALUE))
                
                
            
        
            elif value != "0" and value.count("-"):
                new_value = value.replace("-", "")
                self.input_temp_string_var.set(value=new_value)
            
                if first_temp_selector == "Fahrenheit" and second_temp_selector == "Celsius":
                    self.output_temp_string_var.set(value=self.fahrenheit_to_celsius())
                
                elif first_temp_selector == "Fahrenheit" and second_temp_selector == "Kelvin":
                    self.output_temp_string_var.set(value=self.fahrenheit_to_kelvin())
                
                elif first_temp_selector == "Fahrenheit" and second_temp_selector == "Fahrenheit":
                    F_VALUE = int(self.input_temp_string_var.get())
                    self.output_temp_string_var.set(value=str(F_VALUE) + "°F")
                

                elif first_temp_selector == "Celsius" and second_temp_selector == "Kelvin":
                    self.output_temp_string_var.set(value=self.celsius_to_kelvin())
                
                elif first_temp_selector == "Celsius" and second_temp_selector == "Fahrenheit":
                    self.output_temp_string_var.set(value=self.celsius_to_fahrenhit())
            
                elif first_temp_selector == "Celsius" and second_temp_selector == "Celsius":
                    C_VALUE = int(self.input_temp_string_var.get())
                    self.output_temp_string_var.set(value=str(C_VALUE))
                
                
                
                elif first_temp_selector == "Kelvin" and second_temp_selector == "Fahrenheit":
                    self.output_temp_string_var.set(value=self.kelvin_to_fahrenhit())
                
                elif first_temp_selector == "Kelvin" and second_temp_selector == "Celsius":
                    self.output_temp_string_var.set(value=self.kelvin_to_celsius())
            
                elif first_temp_selector == "Kelvin" and second_temp_selector == "Kelvin":
                    K_VALUE = int(self.input_temp_string_var.get())
                    self.output_temp_string_var.set(value=str(K_VALUE))
                
                
    def plus_minus_btn(self, e):
        value = self.input_temp_string_var.get()
        first_temp_selector = self.input_temp_first_selector.get()
        second_temp_selector = self.output_temp_second_selector.get()
        
        if value == "0":
            pass
        
        elif value != "0" and not value.count("-"):
            self.input_temp_string_var.set(value="-" + value)
            new_value = self.input_temp_string_var.get()
            
            if first_temp_selector == "Fahrenheit" and second_temp_selector == "Celsius":
                self.output_temp_string_var.set(value=self.fahrenheit_to_celsius())
                
            elif first_temp_selector == "Fahrenheit" and second_temp_selector == "Kelvin":
                self.output_temp_string_var.set(value=self.fahrenheit_to_kelvin())
                
            elif first_temp_selector == "Fahrenheit" and second_temp_selector == "Fahrenheit":
                F_VALUE = int(self.input_temp_string_var.get())
                self.output_temp_string_var.set(value=str(F_VALUE) + "°F")
                
                
                
            elif first_temp_selector == "Celsius" and second_temp_selector == "Kelvin":
                self.output_temp_string_var.set(value=self.celsius_to_kelvin())
                
            elif first_temp_selector == "Celsius" and second_temp_selector == "Fahrenheit":
                self.output_temp_string_var.set(value=self.celsius_to_fahrenhit())
            
            elif first_temp_selector == "Celsius" and second_temp_selector == "Celsius":
                C_VALUE = int(self.input_temp_string_var.get())
                self.output_temp_string_var.set(value=str(C_VALUE))
                
                
                
            elif first_temp_selector == "Kelvin" and second_temp_selector == "Fahrenheit":
                self.output_temp_string_var.set(value=self.kelvin_to_fahrenhit())
                
            elif first_temp_selector == "Kelvin" and second_temp_selector == "Celsius":
                self.output_temp_string_var.set(value=self.kelvin_to_celsius())
            
            elif first_temp_selector == "Kelvin" and second_temp_selector == "Kelvin":
                K_VALUE = int(self.input_temp_string_var.get())
                self.output_temp_string_var.set(value=str(K_VALUE))
                
                
            
        
        elif value != "0" and value.count("-"):
            new_value = value.replace("-", "")
            self.input_temp_string_var.set(value=new_value)
            
            if first_temp_selector == "Fahrenheit" and second_temp_selector == "Celsius":
                self.output_temp_string_var.set(value=self.fahrenheit_to_celsius())
                
            elif first_temp_selector == "Fahrenheit" and second_temp_selector == "Kelvin":
                self.output_temp_string_var.set(value=self.fahrenheit_to_kelvin())
                
            elif first_temp_selector == "Fahrenheit" and second_temp_selector == "Fahrenheit":
                F_VALUE = int(self.input_temp_string_var.get())
                self.output_temp_string_var.set(value=str(F_VALUE) + "°F")
                
                
                
            elif first_temp_selector == "Celsius" and second_temp_selector == "Kelvin":
                self.output_temp_string_var.set(value=self.celsius_to_kelvin())
                
            elif first_temp_selector == "Celsius" and second_temp_selector == "Fahrenheit":
                self.output_temp_string_var.set(value=self.celsius_to_fahrenhit())
            
            elif first_temp_selector == "Celsius" and second_temp_selector == "Celsius":
                C_VALUE = int(self.input_temp_string_var.get())
                self.output_temp_string_var.set(value=str(C_VALUE))
                
                
                
            elif first_temp_selector == "Kelvin" and second_temp_selector == "Fahrenheit":
                self.output_temp_string_var.set(value=self.kelvin_to_fahrenhit())
                
            elif first_temp_selector == "Kelvin" and second_temp_selector == "Celsius":
                self.output_temp_string_var.set(value=self.kelvin_to_celsius())
            
            elif first_temp_selector == "Kelvin" and second_temp_selector == "Kelvin":
                K_VALUE = int(self.input_temp_string_var.get())
                self.output_temp_string_var.set(value=str(K_VALUE))
    
    # ----------------------------------- End of Misc Temp Methods ------------------------------------- #
    
    
    
    def temp_to_standard(self):
        self.temperature_label_frame.pack_forget()
        self.main_temp_label.pack_forget()
        self.input_temp_frame.pack_forget()
        self.output_tempertaure_frame.pack_forget()
        self.temperature_frame_for_all_buttons.pack_forget()

        
        self.standard_look()

    
    def temp_to_advanced(self):
        self.temperature_label_frame.pack_forget()
        self.main_temp_label.pack_forget()
        self.input_temp_frame.pack_forget()
        self.output_tempertaure_frame.pack_forget()
        self.temperature_frame_for_all_buttons.pack_forget()
        
        self.execute_advanced_option("0")
    
    
    def temp_to_currency(self):
        self.temperature_label_frame.pack_forget()
        self.main_temp_label.pack_forget()
        self.input_temp_frame.pack_forget()
        self.output_tempertaure_frame.pack_forget()
        self.temperature_frame_for_all_buttons.pack_forget()
        
        self.execute_currency_exchange_option()
        
        
        
        
app = App()