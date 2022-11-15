import customtkinter
from tkinter import *
from currency_exchanges import temps
import customtkinter
import tkinter

from currency_exchanges import exchanges, currency_symbols
import os
import tkinter.ttk as ttk
import datetime
from datetime import datetime
import requests


class App:
    def __init__(self):
        self.root = customtkinter.CTk()
        self.root.config(background="#282828")
        self.root.iconbitmap("darkModeV.ico")
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
        self.output_temp_second_selector = customtkinter.CTkComboBox(self.output_tempertaure_frame, values=sorted(temps), width=170)
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
        self.btn_mut = tkinter.Button(self.first_temp_set_btns, text="AC", width=6, font=("Arial", 16), bg="#404040", fg="white", relief='flat')
        self.btn_mut.grid(row=0, column=2, sticky="w", padx=2, pady=2)
        # simple fg and bg change when hovered over.
        self.btn_mut.bind('<Enter>', lambda e: self.btn_mut.config(fg='black', bg='#4D4D4D'))
        self.btn_mut.bind('<Leave>', lambda e: self.btn_mut.config(fg='white', bg='#404040'))
        # keyboard press events **
        self.root.bind("c", lambda e: self.exchange_ac_btn("c"))


        # number Backspace button 
        self.btn_sub = tkinter.Button(self.first_temp_set_btns, text="⌫", width=6, font=("Arial", 16), bg="#404040", fg="white", relief='flat') # command=lambda:self.sub_key2("-")
        self.btn_sub.grid(row=0, column=3, sticky="w", padx=2, pady=2)
        # simple fg and bg change when hovered over.
        self.btn_sub.bind('<Enter>', lambda e: self.btn_sub.config(fg='black', bg='#4D4D4D'))
        self.btn_sub.bind('<Leave>', lambda e: self.btn_sub.config(fg='white', bg='#404040'))
        # keyboard press events **
        self.root.bind("<BackSpace>", lambda e: self.exchange_backspace(" "))
        
        # ------------------------------- End First Button Frame ----------------------------------- #



        # ------------------------------- Second Button Frame ----------------------------------- #

        self.second_temp_set_btns = customtkinter.CTkFrame(self.temperature_frame_for_all_buttons)
        self.second_temp_set_btns.grid(row=1, column=0, sticky='e')
        
        # number 7 button
        self.btn_7 = tkinter.Button(self.second_temp_set_btns, text="7", width=6, font=("Arial", 16), bg="#404040", fg="white", relief='flat', command=lambda: self.exchange_7_btn("7"))
        self.btn_7.grid(row=0, column=0, sticky="n", padx=2, pady=2)
        # simple fg and bg change when hovered over.
        self.btn_7.bind('<Enter>', lambda e: self.btn_7.config(fg='black', bg='#4D4D4D'))
        self.btn_7.bind('<Leave>', lambda e: self.btn_7.config(fg='white', bg='#404040'))
        # keyboard press events **
        self.root.bind("7", lambda e: self.exchange_7_btn("7"))


        # number 8 button
        self.btn_8 = tkinter.Button(self.second_temp_set_btns, text="8", width=6, font=("Arial", 16), bg="#404040", fg="white", relief='flat', command=lambda: self.exchange_8_btn("8"))
        self.btn_8.grid(row=0, column=1, sticky="n", padx=2, pady=2)
        # simple fg and bg change when hovered over.
        self.btn_8.bind('<Enter>', lambda e: self.btn_8.config(fg='black', bg='#4D4D4D'))
        self.btn_8.bind('<Leave>', lambda e: self.btn_8.config(fg='white', bg='#404040'))
        # keyboard press events **
        self.root.bind("8", lambda e: self.exchange_8_btn("8"))


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
        self.btn_4 = tkinter.Button(self.third_temp_set_btns, text="4", width=6, font=("Arial", 16), bg="#404040", fg="white", relief='flat', command=lambda:self.exchange_4_btn("4"))
        self.btn_4.grid(row=1, column=0, sticky="n", padx=2, pady=2)
        # simple fg and bg change when hovered over.
        self.btn_4.bind('<Enter>', lambda e: self.btn_4.config(fg='black', bg='#4D4D4D'))
        self.btn_4.bind('<Leave>', lambda e: self.btn_4.config(fg='white', bg='#404040'))
        # keyboard press events **
        self.root.bind("4", lambda e: self.exchange_4_btn("4"))


        # number 5 button
        self.btn_5 = tkinter.Button(self.third_temp_set_btns, text="5", width=6, font=("Arial", 16), bg="#404040", fg="white", relief='flat', command=lambda:self.exchange_5_btn("5"))
        self.btn_5.grid(row=1, column=1, sticky="n", padx=2, pady=2)
        # simple fg and bg change when hovered over.
        self.btn_5.bind('<Enter>', lambda e: self.btn_5.config(fg='black', bg='#4D4D4D'))
        self.btn_5.bind('<Leave>', lambda e: self.btn_5.config(fg='white', bg='#404040'))
        # keyboard press events **
        self.root.bind("5", lambda e: self.exchange_5_btn("5"))


        # number 6 button
        self.btn_6 = tkinter.Button(self.third_temp_set_btns, text="6", width=6, font=("Arial", 16), bg="#404040", fg="white", relief='flat', command=lambda:self.exchange_6_btn("6"))
        self.btn_6.grid(row=1, column=2, sticky="n", padx=2, pady=2)
        # simple fg and bg change when hovered over.
        self.btn_6.bind('<Enter>', lambda e: self.btn_6.config(fg='black', bg='#4D4D4D'))
        self.btn_6.bind('<Leave>', lambda e: self.btn_6.config(fg='white', bg='#404040'))
        # keyboard press events **
        self.root.bind("6", lambda e: self.exchange_6_btn("6"))
        
        # ------------------------------- End Third Button Frame ----------------------------------- #



        # ------------------------------- Fourth Button Frame ----------------------------------- #
        
        self.fourth_temp_set_btns = customtkinter.CTkFrame(self.temperature_frame_for_all_buttons)
        self.fourth_temp_set_btns.grid(row=3, column=0, sticky='e')
        

        # number 1 button
        self.btn_1 = tkinter.Button(self.fourth_temp_set_btns, text="1", width=6, font=("Arial", 16), bg="#404040", fg="white", relief='flat', command=lambda:self.exchange_1_btn("1"))
        self.btn_1.grid(row=0, column=0, sticky="n", padx=2, pady=2)
        # simple fg and bg change when hovered over.
        self.btn_1.bind('<Enter>', lambda e: self.btn_1.config(fg='black', bg='#4D4D4D'))
        self.btn_1.bind('<Leave>', lambda e: self.btn_1.config(fg='white', bg='#404040'))
        # keyboard press events **
        self.root.bind("1", lambda e: self.exchange_1_btn("1"))


        # number 2 button
        self.btn_2 = tkinter.Button(self.fourth_temp_set_btns, text="2", width=6, font=("Arial", 16), bg="#404040", fg="white", relief='flat', command=lambda:self.exchange_2_btn("2"))
        self.btn_2.grid(row=0, column=1, sticky="n", padx=2, pady=2)
        # simple fg and bg change when hovered over.
        self.btn_2.bind('<Enter>', lambda e: self.btn_2.config(fg='black', bg='#4D4D4D'))
        self.btn_2.bind('<Leave>', lambda e: self.btn_2.config(fg='white', bg='#404040'))
        # keyboard press events **
        self.root.bind("2", lambda e: self.exchange_2_btn("2"))


        # number 3 button
        self.btn_3 = tkinter.Button(self.fourth_temp_set_btns, text="3", width=6, font=("Arial", 16), bg="#404040", fg="white", relief='flat', command=lambda:self.exchange_3_btn("3"))
        self.btn_3.grid(row=0, column=2, sticky="n", padx=2, pady=2)
        # simple fg and bg change when hovered over.
        self.btn_3.bind('<Enter>', lambda e: self.btn_3.config(fg='black', bg='#4D4D4D'))
        self.btn_3.bind('<Leave>', lambda e: self.btn_3.config(fg='white', bg='#404040'))
        # keyboard press events **
        self.root.bind("3", lambda e: self.exchange_3_btn("3"))
        
        # ------------------------------- End Fourth Button Frame ----------------------------------- #



        # ------------------------------- Fifth Button Frame ----------------------------------- #
        
        self.fifth_temp_set_btns = customtkinter.CTkFrame(self.temperature_frame_for_all_buttons)
        self.fifth_temp_set_btns.grid(row=4, column=0, sticky='e')

        # number 0 button
        self.btn_plus_min = tkinter.Button(self.fifth_temp_set_btns, text="+/-", width=6, font=("Arial", 16), bg="#404040", fg="white", relief='flat', command=lambda: self.exchange_0_btn("0"))
        self.btn_plus_min.grid(row=1, column=0, sticky="n", padx=2, pady=2)
        # simple fg and bg change when hovered over.
        self.btn_plus_min.bind('<Enter>', lambda e: self.btn_plus_min.config(fg='black', bg='#4D4D4D'))
        self.btn_plus_min.bind('<Leave>', lambda e: self.btn_plus_min.config(fg='white', bg='#404040'))
        # keyboard press events **
        self.root.bind("0", lambda e: self.exchange_0_btn("0"))

        
        # number 0 button
        self.temp_btn_0 = tkinter.Button(self.fifth_temp_set_btns, text="0", width=6, font=("Arial", 16), bg="#404040", fg="white", relief='flat', command=lambda: self.exchange_0_btn("0"))
        self.temp_btn_0.grid(row=1, column=1, sticky="n", padx=2, pady=2)
        # simple fg and bg change when hovered over.
        self.temp_btn_0.bind('<Enter>', lambda e: self.temp_btn_0.config(fg='black', bg='#4D4D4D'))
        self.temp_btn_0.bind('<Leave>', lambda e: self.temp_btn_0.config(fg='white', bg='#404040'))
        # keyboard press events **
        self.root.bind("0", lambda e: self.exchange_0_btn("0"))
        
        
        # number dot button
        self.btn_dot = tkinter.Button(self.fifth_temp_set_btns, text=".", width=6, font=("Arial", 16), bg="#404040", fg="white", relief='flat', state='disabled')
        self.btn_dot.grid(row=1, column=2, sticky="n", padx=2, pady=2)
        
        # ------------------------------- End Fifth Button Frame ----------------------------------- #
        
        
        
        # menu
        my_menu = Menu(self.root)


        # create menu items
        file_menu = Menu(my_menu, tearoff=0, background='#303030', fg='white')
        my_menu.add_cascade(label="Calculators", menu=file_menu)
        
        file_menu.add_command(label="Standard Option")
        file_menu.add_command(label="Advanced Option")
            


        edit_menu = Menu(my_menu, tearoff=0, background='#303030', fg='white')
        my_menu.add_cascade(label="Converters", menu=edit_menu)
        
        edit_menu.add_command(label="Currency Exchange")
        edit_menu.add_command(label="Temperature", state="disabled")
        
        self.root.config(menu=my_menu)

        # destorys the app if user presses escape key (convenience)
        self.root.bind("<Escape>", lambda e: self.root.destroy())
        # deleting stuff
        self.root.bind("<BackSpace>", lambda e: self.standard_backspace())
        # stops the user from resizing the app
        
        
        self.root.mainloop()
        
        
        
    # ---------------------------- Start of Temp Methods ---------------------------- #
    
    
    # ------------------------------ Numbers for Temperature Option ------------------------------- #
    
    def temp_number_9(self, e):
        value = self.input_temp_string_var.get()
        first_temp_selector = self.input_temp_first_selector.get()
        second_temp_selector = self.output_temp_second_selector.get()
        
        
        if value == "0":
            self.input_temp_string_var.set(value="9")
            
            # -- Checking Kelvin is first selected and Fahrenhit is second selected -- #
            if first_temp_selector == "Kelvin" and second_temp_selector == "Fahrenheit":
                K_VALUE = int(self.input_temp_string_var.get())
                K = (K_VALUE - 273.15) * 1.8 + 32
                self.output_temp_string_var.set(value=str(K)[:-13] + "°F")
                
            
            elif first_temp_selector == "Kelvin" and second_temp_selector == "Celsius":
                K_VALUE = int(self.input_temp_string_var.get())
                K = (K_VALUE - 273.15)
                self.output_temp_string_var.set(value=str(K) + "°C")
            
            
            elif first_temp_selector == "Kelvin" and second_temp_selector == "Kelvin":
                K_VALUE = int(self.input_temp_string_var.get())
                self.output_temp_string_var.set(value=str(K_VALUE))
            
            
            
            # Checking Fahrenheit is first
            elif first_temp_selector == "Fahrenhit" and second_temp_selector == "Celsius":
                F_VALUE = int(self.input_temp_string_var.get())
            
            elif first_temp_selector == "Fahrenhit" and second_temp_selector == "Kelvin":
                F_VALUE = int(self.input_temp_string_var.get())
            
            elif first_temp_selector == "Fahrenhit" and second_temp_selector == "Fahrenhit":
                F_VALUE = int(self.input_temp_string_var.get())
            
            
            
            # Checking Celsius is first
            elif first_temp_selector == "Celsius" and second_temp_selector == "Kelvin":
                C_VALUE = int(self.input_temp_string_var.get())
            
            elif first_temp_selector == "Celsius" and second_temp_selector == "Fahrenhit":
                C_VALUE = int(self.input_temp_string_var.get())
            
            elif first_temp_selector == "Celsius" and second_temp_selector == "Celsius":
                C_VALUE = int(self.input_temp_string_var.get())
            
            
        elif value != "0":
            self.input_temp_string_var.set(value=value + "9")
            
            # Checking Kelvin is first
            if first_temp_selector == "Kelvin" and second_temp_selector == "Fahrenheit":
                K_VALUE = int(self.input_temp_string_var.get())
                K = (K_VALUE - 273.15) * 9/5 + 32
                self.output_temp_string_var.set(value=str(K)[:-13] + "°F")
            
        
        
    # ----------------------------------- Temperature Selectors ------------------------------------- #
    
    def first_temperature_selector(self, e):
        temp_degree = self.input_temp_first_selector.get()
        value = self.input_temp_string_var.get()
    
    
    def second_temperature_selector(self):
        temp_degree = self.input_temp_first_selector.get()
        
        
        
        
        
    
    
    
    
app = App()