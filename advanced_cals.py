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
        self.btn_div = tkinter.Button(self.first_set_cals_frame, text="π", width=3, font=("Arial", 14), bg="#404040", fg="white", relief='flat', command=self.advanced_pi) # command=lambda:self.div_func2("/")
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
        self.ad_btn_n = tkinter.Button(self.advanced_second_btn_frame, text="n", width=3, font=("Arial", 14), bg="#404040", fg="white", relief='flat') # command=lambda:self.add_func2("+")
        self.ad_btn_n.grid(row=0, column=3, padx=2, pady=2)
        # simple fg and bg change when hovered over.
        self.ad_btn_n.bind('<Enter>', lambda e: self.ad_btn_n.config(fg='black', bg='#4D4D4D'))
        self.ad_btn_n.bind('<Leave>', lambda e: self.ad_btn_n.config(fg='white', bg='#404040'))
        # ************************* End Advanced Natural Number Button *************************** #



        # ************************* Advanced Divison Button *************************** #
        self.btn_div2 = tkinter.Button(self.advanced_second_btn_frame, text="÷", width=3, font=("Arial", 14), bg="#404040", fg="white", relief='flat', command=lambda:self.advanced_divison_btn("/")) # command=lambda:self.key_4("4")
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
        self.btn_x2 = tkinter.Button(self.third_btn_frame, text="x2", width=3, font=("Arial", 14), bg="#404040", fg="white", relief='flat') # command=lambda:self.key_1("1")
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
        self.btn_abs = tkinter.Button(self.advanced_fourth_btn_frame, text="|x|", width=3, font=("Arial", 14), bg="#404040", fg="white", relief='flat', command=lambda:self.key_0("0"))
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
        
        # ------------------------------ End Advanced Button Frame SET 6 -------------------------------- #


        
        self.root.mainloop()
        
        
        
        # ------------------------------ Advanced Option Methods ---------------------------------- #
        
        
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
        pass
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
        
        
        # ------------------------------ End Advanced Method ---------------------------------------
        
        
        # copy everything from above -----------------------------------------------

app = Windows()



