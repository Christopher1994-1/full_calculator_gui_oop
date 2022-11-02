import customtkinter
import tkinter
from tkinter import *
import requests
from datetime import datetime
import tkinter as tk
import tkinter.ttk as ttk
import math
import os
from currency_exchanges import currency_symbols, exchanges




class Windows:
    def __init__(self):
        # main frame -------------------------------------------------------------
        self.root = customtkinter.CTk()
        self.root.title("Advanced")
        self.root.iconbitmap("darkModeV.ico")
        self.root.geometry("285x340") # L x H change back to 270 or 280?
        self.root.config(background="#282828")

        
        
        # copy everything from below ---------------------------------------------
        
    
        # label here
        self.label_pack = customtkinter.CTkFrame(self.root, fg_color='#282828')
        self.label_pack.pack(side=TOP, anchor="w", padx=(20, 0), pady=(10, 0))

        self.header_label = customtkinter.CTkLabel(self.label_pack, text="Advanced", bg_color="#282828", height=0, width=0, text_font=("Arial", 14, "bold"))
        self.header_label.pack() # pady=(top, bottom) padx=(left, right) in px


        # entry box here
        self.entry_pack = customtkinter.CTkFrame(self.root, fg_color='#282828')
        self.entry_pack.pack(padx=(22, 15), fill=X)

        # entry box widget
        
        self.entry_label = customtkinter.CTkLabel(self.entry_pack, text='0', text_font=("Arial", 26), width=0, height=0)
        self.entry_label.pack(side=LEFT)
     
        # first set of standard calculator buttons
        self.first_pack = customtkinter.CTkFrame(self.root, fg_color='#282828')
        self.first_pack.pack(side=LEFT, anchor="nw", padx=(15, 0), pady=(5, 0))


        #########################################
        # button frame
        self.first_set_cals_frame = customtkinter.CTkFrame(self.first_pack, fg_color='#282828')
        self.first_set_cals_frame.pack(side=TOP, anchor='w', padx=(5, 0))
        
        

        # key press CE button 
        self.c_btn = tkinter.Button(self.first_set_cals_frame, text="CE", width=4, font=("Arial", 16), bg="#404040", fg="white", relief='flat') # command=self.c_key2
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
        
        
        self.root.mainloop()
        # copy everything from above -----------------------------------------------

app = Windows()



