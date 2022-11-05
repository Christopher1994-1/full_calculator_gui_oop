import customtkinter
import tkinter
import re
from tkinter import *
import requests
from datetime import datetime
import tkinter as tk
import keyboard
import tkinter.ttk as ttk
import math
import os
from currency_exchanges import currency_symbols, exchanges




class Windows:
    def __init__(self):
        # main frame -------------------------------------------------------------
        self.root = customtkinter.CTk()
        # self.root.title("Advanced")
        self.root.iconbitmap("darkModeV.ico")
        self.root.config(background="#282828")
        # self.root.geometry("280x350") # L x H change back to 270 or 280?

        
        
        # copy everything from below ---------------------------------------------
        
        
        # --------------------- Advancned Method -------------------------------- #
        
        self.root.geometry("235x340") # L x H change back to 270 or 280?
        self.root.title("Advanced")
        
    
        # label here
        self.label_pack = customtkinter.CTkFrame(self.root, fg_color='#282828')
        self.label_pack.pack(side=TOP, anchor="w", padx=(10, 0), pady=(10, 0))

        self.header_label = customtkinter.CTkLabel(self.label_pack, text="Advanced", bg_color="#282828", height=0, width=0, text_font=("Arial", 14, "bold"))
        self.header_label.pack() # pady=(top, bottom) padx=(left, right) in px


        # Main Label Zero Input
        self.zero_label_input = customtkinter.CTkFrame(self.root, fg_color='#282828')
        self.zero_label_input.pack(padx=(10, 15), fill=X)

        # Label widget
        self.advanced_zero_base_input = customtkinter.StringVar(value="0")
        self.zero_label_widget = customtkinter.CTkLabel(self.zero_label_input, textvariable=self.advanced_zero_base_input, text_font=("Arial", 26), width=0, height=0)
        self.zero_label_widget.pack(side=LEFT)
     
     
     
     
        # first set of standard calculator buttons
        self.first_pack = customtkinter.CTkFrame(self.root, fg_color='#282828')
        self.first_pack.pack(side=BOTTOM, anchor="nw", padx=(0, 0), pady=(5, 0))


        #########################################
        # button frame
        self.first_set_cals_frame = customtkinter.CTkFrame(self.first_pack, fg_color='#282828')
        self.first_set_cals_frame.pack(side=TOP, anchor='w', padx=(0, 0))
        
        

        # key press CE button 
        self.c_btn = tkinter.Button(self.first_set_cals_frame, text="CE", width=3, font=("Arial", 14), bg="#404040", fg="white", relief='flat', command=lambda: self.advanced_ce_btn("c"))
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
        self.root.bind("/", lambda e: self.advanced_divison_btn("/"))



      
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
        self.btn_7 = tkinter.Button(self.third_btn_frame, text="7", width=3, font=("Arial", 14), bg="#525252", fg="white", relief='flat', command=lambda:self.advanced_n7_btn("7"))
        self.btn_7.grid(row=0, column=1, sticky="n", padx=2, pady=2)
        # simple fg and bg change when hovered over.
        self.btn_7.bind('<Enter>', lambda e: self.btn_7.config(fg='black', bg='#4D4D4D'))
        self.btn_7.bind('<Leave>', lambda e: self.btn_7.config(fg='white', bg='#525252'))
        # keyboard press events **
        self.root.bind("7", lambda e: self.advanced_n7_btn("7"))


        # Number 8 Button
        self.btn_8 = tkinter.Button(self.third_btn_frame, text="8", width=3, font=("Arial", 14), bg="#525252", fg="white", relief='flat', command=lambda:self.advanced_n8_btn("8"))
        self.btn_8.grid(row=0, column=2, sticky="n", padx=2, pady=2)
        # simple fg and bg change when hovered over.
        self.btn_8.bind('<Enter>', lambda e: self.btn_8.config(fg='black', bg='#4D4D4D'))
        self.btn_8.bind('<Leave>', lambda e: self.btn_8.config(fg='white', bg='#525252'))
        # keyboard press events **
        self.root.bind("8", lambda e: self.advanced_n8_btn("8"))


        # Number 9 Button
        self.btn_9 = tkinter.Button(self.third_btn_frame, text="9", width=3, font=("Arial", 14), bg="#525252", fg="white", relief='flat', command=lambda:self.advanced_n9_btn("9"))
        self.btn_9.grid(row=0, column=3, padx=2, pady=2)
        # simple fg and bg change when hovered over.
        self.btn_9.bind('<Enter>', lambda e: self.btn_9.config(fg='black', bg='#4D4D4D'))
        self.btn_9.bind('<Leave>', lambda e: self.btn_9.config(fg='white', bg='#525252'))
        # keyboard press events **
        self.root.bind("9", lambda e: self.advanced_n9_btn("9"))


        # Multiplication Button
        self.btn_x = tkinter.Button(self.third_btn_frame, text="X", width=3, font=("Arial", 14), bg="#404040", fg="white", relief='flat', command=lambda:self.advanced_multiplication_btn("*"))
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
        self.ad_btn_4 = tkinter.Button(self.advanced_fourth_btn_frame, text="4", width=3, font=("Arial", 14), bg="#525252", fg="white", relief='flat', command=lambda:self.advanced_n4_btn("4"))
        self.ad_btn_4.grid(row=0, column=1, sticky="n", padx=2, pady=2)
        # simple fg and bg change when hovered over.
        self.ad_btn_4.bind('<Enter>', lambda e: self.ad_btn_4.config(fg='black', bg='#4D4D4D'))
        self.ad_btn_4.bind('<Leave>', lambda e: self.ad_btn_4.config(fg='white', bg='#525252'))
        # keyboard press events **
        self.root.bind("4", lambda e: self.advanced_n4_btn("4"))
        
        
        # Number 5 Button
        self.ad_btn_5 = tkinter.Button(self.advanced_fourth_btn_frame, text="5", width=3, font=("Arial", 14), bg="#525252", fg="white", relief='flat', command=lambda:self.advanced_n5_btn("5"))
        self.ad_btn_5.grid(row=0, column=2, sticky="n", padx=2, pady=2)
        # simple fg and bg change when hovered over.
        self.ad_btn_5.bind('<Enter>', lambda e: self.ad_btn_5.config(fg='black', bg='#4D4D4D'))
        self.ad_btn_5.bind('<Leave>', lambda e: self.ad_btn_5.config(fg='white', bg='#525252'))
        # keyboard press events **
        self.root.bind("5", lambda e: self.advanced_n5_btn("5"))
        
        
        # Number 6 Button
        self.ad_btn_6 = tkinter.Button(self.advanced_fourth_btn_frame, text="6", width=3, font=("Arial", 14), bg="#525252", fg="white", relief='flat', command=lambda:self.advanced_n6_btn("6"))
        self.ad_btn_6.grid(row=0, column=3, sticky="n", padx=2, pady=2)
        # simple fg and bg change when hovered over.
        self.ad_btn_6.bind('<Enter>', lambda e: self.ad_btn_6.config(fg='black', bg='#4D4D4D'))
        self.ad_btn_6.bind('<Leave>', lambda e: self.ad_btn_6.config(fg='white', bg='#525252'))
        # keyboard press events **
        self.root.bind("6", lambda e: self.advanced_n6_btn("6"))
        
        
        # Advanced Subtraction Button
        self.ad_btn_minus = tkinter.Button(self.advanced_fourth_btn_frame, text="-", width=3, font=("Arial", 14), bg="#404040", fg="white", relief='flat', command=lambda:self.advanced_subtraction_btn("-"))
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
        self.ad_btn_1 = tkinter.Button(self.advanced_fifth_btn_frame, text="1", width=3, font=("Arial", 14), bg="#525252", fg="white", relief='flat', command=lambda:self.advanced_n1_btn("1"))
        self.ad_btn_1.grid(row=0, column=1, sticky="n", padx=2, pady=2)
        # simple fg and bg change when hovered over.
        self.ad_btn_1.bind('<Enter>', lambda e: self.ad_btn_1.config(fg='black', bg='#4D4D4D'))
        self.ad_btn_1.bind('<Leave>', lambda e: self.ad_btn_1.config(fg='white', bg='#525252'))
        # keyboard press events **
        self.root.bind("1", lambda e: self.advanced_n1_btn("1"))
        
        
        # Number 2 Button
        self.ad_btn_2 = tkinter.Button(self.advanced_fifth_btn_frame, text="2", width=3, font=("Arial", 14), bg="#525252", fg="white", relief='flat', command=lambda:self.advanced_n2_btn("2"))
        self.ad_btn_2.grid(row=0, column=2, sticky="n", padx=2, pady=2)
        # simple fg and bg change when hovered over.
        self.ad_btn_2.bind('<Enter>', lambda e: self.ad_btn_2.config(fg='black', bg='#4D4D4D'))
        self.ad_btn_2.bind('<Leave>', lambda e: self.ad_btn_2.config(fg='white', bg='#525252'))
        # keyboard press events **
        self.root.bind("2", lambda e: self.advanced_n2_btn("2"))
        
        
        # Number 3 Button
        self.ad_btn_3 = tkinter.Button(self.advanced_fifth_btn_frame, text="3", width=3, font=("Arial", 14), bg="#525252", fg="white", relief='flat', command=lambda:self.advanced_n3_btn("3"))
        self.ad_btn_3.grid(row=0, column=3, sticky="n", padx=2, pady=2)
        # simple fg and bg change when hovered over.
        self.ad_btn_3.bind('<Enter>', lambda e: self.ad_btn_3.config(fg='black', bg='#4D4D4D'))
        self.ad_btn_3.bind('<Leave>', lambda e: self.ad_btn_3.config(fg='white', bg='#525252'))
        # keyboard press events **
        self.root.bind("3", lambda e: self.advanced_n3_btn("3"))
        
        
        # Advanced Addition Button
        self.ad_btn_plus = tkinter.Button(self.advanced_fifth_btn_frame, text="+", width=3, font=("Arial", 14), bg="#404040", fg="white", relief='flat', command=lambda:self.advanced_addition_btn("+"))
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
        self.ad_btn_0 = tkinter.Button(self.advanced_sixth_btn_frame, text="0", width=3, font=("Arial", 14), bg="#525252", fg="white", relief='flat', command=lambda:self.advanced_n0_btn("0"))
        self.ad_btn_0.grid(row=0, column=2, sticky="n", padx=2, pady=2)
        # simple fg and bg change when hovered over.
        self.ad_btn_0.bind('<Enter>', lambda e: self.ad_btn_0.config(fg='black', bg='#4D4D4D'))
        self.ad_btn_0.bind('<Leave>', lambda e: self.ad_btn_0.config(fg='white', bg='#525252'))
        # keyboard press events **
        self.root.bind("0", lambda e: self.advanced_n0_btn("0"))
        
        
        # Number Dot Button
        self.ad_btn_dot = tkinter.Button(self.advanced_sixth_btn_frame, text=".", width=3, font=("Arial", 14), bg="#404040", fg="white", relief='flat', command=lambda:self.advanced_dot_btn("."))
        self.ad_btn_dot.grid(row=0, column=3, sticky="n", padx=2, pady=2)
        # simple fg and bg change when hovered over.
        self.ad_btn_dot.bind('<Enter>', lambda e: self.ad_btn_dot.config(fg='black', bg='#4D4D4D'))
        self.ad_btn_dot.bind('<Leave>', lambda e: self.ad_btn_dot.config(fg='white', bg='#404040'))
        # keyboard press events **
        self.root.bind(".", lambda e: self.advanced_dot_btn("0"))
        
        
        # Advanced Equals Button
        self.ad_btn_equals = tkinter.Button(self.advanced_sixth_btn_frame, text="=", width=3, font=("Arial", 14), bg="#808A87", fg="white", relief='flat', command=lambda:self.advanced_enter_btn("0"))
        self.ad_btn_equals.grid(row=0, column=4, sticky="n", padx=2, pady=2)
        # simple fg and bg change when hovered over.
        self.ad_btn_equals.bind('<Enter>', lambda e: self.ad_btn_equals.config(fg='black', bg='#4D4D4D'))
        self.ad_btn_equals.bind('<Leave>', lambda e: self.ad_btn_equals.config(fg='white', bg='#808A87'))
        # keyboard press events **
        self.root.bind("<Return>", lambda e: self.advanced_enter_btn("0"))


        
        self.root.mainloop()
        
        
        
        # ------------------------------ Advanced Option Methods ---------------------------------- #
        
        
        
    # ------------------------- Advanced X Number Press Event Methods ----------------------------- #
    
    # -- Advanced Event Btn 9 -- #
    def advanced_n9_btn(self, e):
        
        # Number x that is passed in when key event pressed
        self.number_value = e
        
        # Number StrVariable that is set
        self.advanced_zero_value = self.advanced_zero_base_input.get()
        
        # Checking to see if the StrVariable is x
        if self.advanced_zero_value == "0":
            self.advanced_zero_base_input.set(value="9")
        elif self.advanced_zero_value != "0":
            self.advanced_zero_base_input.set(value=self.advanced_zero_value + "9")


    # -- Advanced Event Btn 8 -- #
    def advanced_n8_btn(self, e):
        
        # Number x that is passed in when key event pressed
        self.number_value = e
        
        # Number StrVariable that is set
        self.advanced_zero_value = self.advanced_zero_base_input.get()
        
        # Checking to see if the StrVariable is x
        if self.advanced_zero_value == "0":
            self.advanced_zero_base_input.set(value="8")
        elif self.advanced_zero_value != "0":
            self.advanced_zero_base_input.set(value=self.advanced_zero_value + "8")
    
    
    # -- Advanced Event Btn 7 -- #
    def advanced_n7_btn(self, e):
        
        # Number x that is passed in when key event pressed
        self.number_value = e
        
        # Number StrVariable that is set
        self.advanced_zero_value = self.advanced_zero_base_input.get()
        
        # Checking to see if the StrVariable is x
        if self.advanced_zero_value == "0":
            self.advanced_zero_base_input.set(value="7")
        elif self.advanced_zero_value != "0":
            self.advanced_zero_base_input.set(value=self.advanced_zero_value + "7")
    
    
    # -- Advanced Event Btn 6 -- #
    def advanced_n6_btn(self, e):
        
        # Number x that is passed in when key event pressed
        self.number_value = e
        
        # Number StrVariable that is set
        self.advanced_zero_value = self.advanced_zero_base_input.get()
        
        # Checking to see if the StrVariable is x
        if self.advanced_zero_value == "0":
            self.advanced_zero_base_input.set(value="6")
        elif self.advanced_zero_value != "0":
            self.advanced_zero_base_input.set(value=self.advanced_zero_value + "6")
     
     
    # -- Advanced Event Btn 5 -- #
    def advanced_n5_btn(self, e):
        
        # Number x that is passed in when key event pressed
        self.number_value = e
        
        # Number StrVariable that is set
        self.advanced_zero_value = self.advanced_zero_base_input.get()
        
        # Checking to see if the StrVariable is x
        if self.advanced_zero_value == "0":
            self.advanced_zero_base_input.set(value="5")
        elif self.advanced_zero_value != "0":
            self.advanced_zero_base_input.set(value=self.advanced_zero_value + "5")
    
    
    # -- Advanced Event Btn 4 -- #
    def advanced_n4_btn(self, e):
        
        # Number x that is passed in when key event pressed
        self.number_value = e
        
        # Number StrVariable that is set
        self.advanced_zero_value = self.advanced_zero_base_input.get()
        
        # Checking to see if the StrVariable is x
        if self.advanced_zero_value == "0":
            self.advanced_zero_base_input.set(value="4")
        elif self.advanced_zero_value != "0":
            self.advanced_zero_base_input.set(value=self.advanced_zero_value + "4")
    
    
    # -- Advanced Event Btn 3 -- #
    def advanced_n3_btn(self, e):
        
        # Number x that is passed in when key event pressed
        self.number_value = e
        
        # Number StrVariable that is set
        self.advanced_zero_value = self.advanced_zero_base_input.get()
        
        # Checking to see if the StrVariable is x
        if self.advanced_zero_value == "0":
            self.advanced_zero_base_input.set(value="3")
        elif self.advanced_zero_value != "0":
            self.advanced_zero_base_input.set(value=self.advanced_zero_value + "3")
    
    
    # -- Advanced Event Btn 2 -- #
    def advanced_n2_btn(self, e):
        
        # Number x that is passed in when key event pressed
        self.number_value = e
        
        # Number StrVariable that is set
        self.advanced_zero_value = self.advanced_zero_base_input.get()
        
        # Checking to see if the StrVariable is x
        if self.advanced_zero_value == "0":
            self.advanced_zero_base_input.set(value="2")
        elif self.advanced_zero_value != "0":
            self.advanced_zero_base_input.set(value=self.advanced_zero_value + "2")
    
    
    # -- Advanced Event Btn 1 -- #    
    def advanced_n1_btn(self, e):
        
        # Number x that is passed in when key event pressed
        self.number_value = e
        
        # Number StrVariable that is set
        self.advanced_zero_value = self.advanced_zero_base_input.get()
        
        # Checking to see if the StrVariable is x
        if self.advanced_zero_value == "0":
            self.advanced_zero_base_input.set(value="1")
        elif self.advanced_zero_value != "0":
            self.advanced_zero_base_input.set(value=self.advanced_zero_value + "1")
    
    
    # -- Advanced Event Btn 0 -- #    
    def advanced_n0_btn(self, e):
        
        # Number x that is passed in when key event pressed
        self.number_value = e
        
        # Number StrVariable that is set
        self.advanced_zero_value = self.advanced_zero_base_input.get()
        
        # Checking to see if the StrVariable is x
        if self.advanced_zero_value == "0":
            self.advanced_zero_base_input.set(value="0")
        elif self.advanced_zero_value != "0":
            self.advanced_zero_base_input.set(value=self.advanced_zero_value + "0")
    
    # ------------------------ End Advanced X Number Press Event Methods ---------------------------- #
    
    
    
    # ---------------------------- Advanced Operater Press Event Methods ------------------------------- #
    
    # TODO copy below method and paste to other three
    def advanced_addition_btn(self, operater):
        self.set_value = self.advanced_zero_base_input.get() # value that is there
        
        measured = len(self.set_value) # length of value
        
        last_digits = re.search(r'\d+$', self.set_value) # checking to see if the string has a digit in last index
        
        toBeCal = self.set_value.split(" ") # spliting the value into list 


        # if + is pressed and value is == 0
        if self.set_value == "0":
            self.zero_label_widget.configure(text_font=("Arial", 18))
            self.advanced_zero_base_input.set(value="Invaild Input!")
            
        elif self.set_value.count("*"):
            first_num = toBeCal[0]
            second_num = toBeCal[2]
            result = int(first_num) * int(second_num)
            self.advanced_zero_base_input.set(value=str(result) + " + ")
        
        elif self.set_value.count("/"):
            first_num = toBeCal[0]
            second_num = toBeCal[2]
            if second_num == "0":
                self.zero_label_widget.configure(text_font=("Arial", 14))
                self.advanced_zero_base_input.set(value="Cannot Divide by Zero")
            else:
                result = int(first_num) // int(second_num)
                self.advanced_zero_base_input.set(value=str(result) + " + ")
                
        elif self.set_value.count("-"):
            first_num = toBeCal[0]
            second_num = toBeCal[2]
            result = int(first_num) - int(second_num)
            self.advanced_zero_base_input.set(value=str(result) + " + ")
            
            
        # if + is pressed again while "Invaild Input!" is the value    
        elif self.set_value == "Invaild Input!":
            self.zero_label_widget.configure(text_font=("Arial", 26))
            self.advanced_zero_base_input.set(value="0")
            
        # if + is pressed and value isn't 0 and there isn't a + already
        elif self.set_value != "0" and not self.set_value.count("+"):
            self.advanced_zero_base_input.set(value=self.set_value + " " + operater + " ")
        
        # if there is a + and length is > 3 and value ends with a int
        elif self.set_value.count("+") and measured >= 3 and last_digits != None:
            first_num = toBeCal[0]
            second_num = toBeCal[2]
            result = int(first_num) + int(second_num)
            self.advanced_zero_base_input.set(value=str(result))
        

    
    
    def advanced_subtraction_btn(self, operater):
        self.set_value = self.advanced_zero_base_input.get()
        
        measured = len(self.set_value)
        last_digits = re.search(r'\d+$', self.set_value)
        toBeCal = self.set_value.split(" ")


        
        if self.set_value == "0":
            self.zero_label_widget.configure(text_font=("Arial", 18))
            self.advanced_zero_base_input.set(value="Invaild Input!")
            
        elif self.set_value == "Invaild Input!":
            self.zero_label_widget.configure(text_font=("Arial", 26))
            self.advanced_zero_base_input.set(value="0")
            
        elif self.set_value != "0" and not self.set_value.count("-"):
            self.advanced_zero_base_input.set(value=self.set_value + " " + operater + " ")
        
        elif self.set_value.count("-") and measured >= 3 and last_digits != None:
            first_num = toBeCal[0]
            second_num = toBeCal[2]
            result = int(first_num) + int(second_num)
            self.advanced_zero_base_input.set(value=str(result))
            
    
    
    def advanced_multiplication_btn(self, operater):
        self.set_value = self.advanced_zero_base_input.get()
        
        measured = len(self.set_value)
        last_digits = re.search(r'\d+$', self.set_value)
        toBeCal = self.set_value.split(" ")


        
        if self.set_value == "0":
            self.zero_label_widget.configure(text_font=("Arial", 18))
            self.advanced_zero_base_input.set(value="Invaild Input!")
            
        elif self.set_value == "Invaild Input!":
            self.zero_label_widget.configure(text_font=("Arial", 26))
            self.advanced_zero_base_input.set(value="0")
            
        elif self.set_value != "0" and not self.set_value.count("*"):
            self.advanced_zero_base_input.set(value=self.set_value + " " + operater + " ")
        
        elif self.set_value.count("*") and measured >= 3 and last_digits != None:
            first_num = toBeCal[0]
            second_num = toBeCal[2]
            result = int(first_num) + int(second_num)
            self.advanced_zero_base_input.set(value=str(result))
            
    
    
    def advanced_divison_btn(self, operater):
        self.set_value = self.advanced_zero_base_input.get()
        
        measured = len(self.set_value)
        last_digits = re.search(r'\d+$', self.set_value)
        toBeCal = self.set_value.split(" ")


        
        if self.set_value == "0":
            self.zero_label_widget.configure(text_font=("Arial", 18))
            self.advanced_zero_base_input.set(value="Invaild Input!")
            
        elif self.set_value == "Invaild Input!":
            self.zero_label_widget.configure(text_font=("Arial", 26))
            self.advanced_zero_base_input.set(value="0")
            
        elif self.set_value != "0" and not self.set_value.count("/"):
            self.advanced_zero_base_input.set(value=self.set_value + " " + operater + " ")
        
        elif self.set_value.count("/") and measured >= 3 and last_digits != None:
            
            second_num = toBeCal[2]
            if second_num == "0":
                self.zero_label_widget.configure(text_font=("Arial", 18))
                self.advanced_zero_base_input.set(value="Cannot Divide by Zero")
            else:
                first_num = toBeCal[0]
                second_num = toBeCal[2]
                result = int(first_num) // int(second_num)
                self.advanced_zero_base_input.set(value=str(result))
            
    
    
    # ------------------------- End Advanced Operater Press Event Methods ------------------------------- #
    
    
    
    
    # ---------------------------- Misc Advanced Press Event Methods ------------------------------------ #
    
    def advanced_enter_btn(self, e):
        value_to_calculate = self.advanced_zero_base_input.get()
        toBeCal = value_to_calculate.split(" ")
        measured = len(toBeCal)
        last_digit = re.search(r'\d+$', value_to_calculate)


        # ------------ Checks Addition Operator ------------ #
        
        if toBeCal.count("+") and measured == 3 and last_digit != None:
            first_num = toBeCal[0]
            second_num = toBeCal[2]
            result = int(first_num) + int(second_num)
            self.advanced_zero_base_input.set(value=str(result))
            
            
        # ------------ Ends Addition Operator ------------ #
            
            
            
        # ------------ Checks Subtraction Operator ------------ #
        
        elif toBeCal.count("-") and measured == 3 and last_digit != None:
            first_num = toBeCal[0]
            second_num = toBeCal[2]
            result = int(first_num) - int(second_num)
            self.advanced_zero_base_input.set(value=str(result))
        
        # ------------ Ends Subtraction Operator ------------ #
            
            
            
        # ------------ Checks Divison Operator ------------ #
        
        elif toBeCal.count("/") and measured == 3 and last_digit != None:
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
            first_num = toBeCal[0]
            second_num = toBeCal[2]
            result = int(first_num) * int(second_num)
            self.advanced_zero_base_input.set(value=str(result))
        # ------------ Ends Multiplication Operator ------------ #
   

    
    def advanced_dot_btn(self, e):
        pass
    
    def advanced_ce_btn(self, e):
        value = self.advanced_zero_base_input.get()
        
        if value == "0":
            pass
        else:
            self.advanced_zero_base_input.set(value="0")
        
        
    # ---------------------------- End Misc Advanced Press Event Methods ------------------------------------ #
        
        
        # ------------------------------ End Advanced Method ---------------------------------------
        
        
        # copy everything from above -----------------------------------------------

app = Windows()



