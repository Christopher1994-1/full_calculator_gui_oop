from turtle import right
import customtkinter
import tkinter
from tkinter import *



class App:
    def __init__(self):
        # all the main variables
        self.root = customtkinter.CTk()
        self.root.title("Simple Calculator")
        self.root.iconbitmap("darkModeV.ico")
        self.root.geometry("280x360") # L x H


        # standard/advanced label header for entry box
        self.header_label = customtkinter.CTkLabel(self.root, text="Standard", bg_color="#282828", height=0, width=0, text_font=("Arial", 14, "bold"))
        self.header_label.pack(pady=(15, 2), padx=(0, 156))

        # first frame of the GUI
        self.first_frame = customtkinter.CTkFrame(self.root)
        self.first_frame.pack(pady=(0, 15))


        # entry box widget
        self.entry = customtkinter.CTkEntry(self.first_frame, text_font=("Arial", 26), width=245, height=44)
        self.entry.grid(row=1, column=0, columnspan=3)

        #########################################
        # button frame
        self.btn_frame = customtkinter.CTkFrame(self.root)
        self.btn_frame.pack()

        # key press c button 
        self.btn_c = tkinter.Button(self.btn_frame, text="C", width=4, font=("Arial", 16), bg="grey", fg="white", command=self.c_key2)
        self.btn_c.grid(row=0, column=0, sticky="w", padx=2, pady=2)
        # simple fg and bg change when hovered over.
        self.btn_c.bind('<Enter>', lambda e: self.btn_c.config(fg='black', bg='lightgrey'))
        self.btn_c.bind('<Leave>', lambda e: self.btn_c.config(fg='white', bg='grey'))
        # keyboard press events **
        self.root.bind("c", lambda e: self.c_key("c"))


        # number / button
        self.btn_div = tkinter.Button(self.btn_frame, text="/", width=4, font=("Arial", 16), bg="grey", fg="white", command=lambda:self.div_func2("/"))
        self.btn_div.grid(row=0, column=1, sticky="w", padx=2, pady=2)
        # simple fg and bg change when hovered over.
        self.btn_div.bind('<Enter>', lambda e: self.btn_div.config(fg='black', bg='lightgrey'))
        self.btn_div.bind('<Leave>', lambda e: self.btn_div.config(fg='white', bg='grey'))
        # keyboard press events **
        self.root.bind("/", lambda e: self.div_func("/"))


        # number * button
        self.btn_mut = tkinter.Button(self.btn_frame, text="*", width=4, font=("Arial", 16), bg="grey", fg="white", command=lambda:self.mut_key2("*"))
        self.btn_mut.grid(row=0, column=2, sticky="w", padx=2, pady=2)
        # simple fg and bg change when hovered over.
        self.btn_mut.bind('<Enter>', lambda e: self.btn_mut.config(fg='black', bg='lightgrey'))
        self.btn_mut.bind('<Leave>', lambda e: self.btn_mut.config(fg='white', bg='grey'))
        # keyboard press events **
        self.root.bind("*", lambda e: self.mut_key("*"))


        # number - button
        self.btn_sub = tkinter.Button(self.btn_frame, text="-", width=4, font=("Arial", 16), bg="grey", fg="white", command=lambda:self.sub_key2("-"))
        self.btn_sub.grid(row=0, column=3, sticky="w", padx=2, pady=2)
        # simple fg and bg change when hovered over.
        self.btn_sub.bind('<Enter>', lambda e: self.btn_sub.config(fg='black', bg='lightgrey'))
        self.btn_sub.bind('<Leave>', lambda e: self.btn_sub.config(fg='white', bg='grey'))
        # keyboard press events **
        self.root.bind("-", lambda e: self.sub_key("-"))


        # second button frame #################################################################################

        self.second_btn_frame = customtkinter.CTkFrame(self.root)
        self.second_btn_frame.pack()

        
        # number 7 button
        self.btn_7 = tkinter.Button(self.second_btn_frame, text="7", width=4, font=("Arial", 16), bg="grey", fg="white", command=lambda:self.btn_click_7("7"))
        self.btn_7.grid(row=0, column=0, sticky="n", padx=2, pady=2)
        # simple fg and bg change when hovered over.
        self.btn_7.bind('<Enter>', lambda e: self.btn_7.config(fg='black', bg='lightgrey'))
        self.btn_7.bind('<Leave>', lambda e: self.btn_7.config(fg='white', bg='grey'))
        # keyboard press events **
        self.root.bind("7", lambda e: self.key_7("7"))


        # number 8 button
        self.btn_8 = tkinter.Button(self.second_btn_frame, text="8", width=4, font=("Arial", 16), bg="grey", fg="white", command=lambda:self.key_8("8"))
        self.btn_8.grid(row=0, column=1, sticky="n", padx=2, pady=2)
        # simple fg and bg change when hovered over.
        self.btn_8.bind('<Enter>', lambda e: self.btn_8.config(fg='black', bg='lightgrey'))
        self.btn_8.bind('<Leave>', lambda e: self.btn_8.config(fg='white', bg='grey'))
        # keyboard press events **
        self.root.bind("8", lambda e: self.key_8("8"))


        # number 9 button
        self.btn_9 = tkinter.Button(self.second_btn_frame, text="9", width=4, font=("Arial", 16), bg="grey", fg="white", command=lambda:self.key_9("9"))
        self.btn_9.grid(row=0, column=2, sticky="n", padx=2, pady=2)
        # simple fg and bg change when hovered over.
        self.btn_9.bind('<Enter>', lambda e: self.btn_9.config(fg='black', bg='lightgrey'))
        self.btn_9.bind('<Leave>', lambda e: self.btn_9.config(fg='white', bg='grey'))
        # keyboard press events **
        self.root.bind("9", lambda e: self.key_9("9"))

        # number add button
        self.btn_add = tkinter.Button(self.second_btn_frame, text="+", width=4, font=("Arial", 16), bg="grey", fg="white", height=3, command=lambda:self.add_func2("+"))
        self.btn_add.grid(row=0, column=3, padx=2, pady=2, rowspan=2)
        # simple fg and bg change when hovered over.
        self.btn_add.bind('<Enter>', lambda e: self.btn_add.config(fg='black', bg='lightgrey'))
        self.btn_add.bind('<Leave>', lambda e: self.btn_add.config(fg='white', bg='grey'))
        # keyboard press events **
        self.root.bind("+", lambda e: self.add_func("+"))
        
        ##########

        # number 4 button
        self.btn_4 = tkinter.Button(self.second_btn_frame, text="4", width=4, font=("Arial", 16), bg="grey", fg="white", command=lambda:self.key_4("4"))
        self.btn_4.grid(row=1, column=0, sticky="n", padx=2, pady=2)
        # simple fg and bg change when hovered over.
        self.btn_4.bind('<Enter>', lambda e: self.btn_4.config(fg='black', bg='lightgrey'))
        self.btn_4.bind('<Leave>', lambda e: self.btn_4.config(fg='white', bg='grey'))
        # keyboard press events **
        self.root.bind("4", lambda e: self.key_4("4"))


        # number 5 button
        self.btn_5 = tkinter.Button(self.second_btn_frame, text="5", width=4, font=("Arial", 16), bg="grey", fg="white", command=lambda:self.key_5("5"))
        self.btn_5.grid(row=1, column=1, sticky="n", padx=2, pady=2)
        # simple fg and bg change when hovered over.
        self.btn_5.bind('<Enter>', lambda e: self.btn_5.config(fg='black', bg='lightgrey'))
        self.btn_5.bind('<Leave>', lambda e: self.btn_5.config(fg='white', bg='grey'))
        # keyboard press events **
        self.root.bind("5", lambda e: self.key_5("5"))


        # number 6 button
        self.btn_6 = tkinter.Button(self.second_btn_frame, text="6", width=4, font=("Arial", 16), bg="grey", fg="white", command=lambda:self.key_6("6"))
        self.btn_6.grid(row=1, column=2, sticky="n", padx=2, pady=2)
        # simple fg and bg change when hovered over.
        self.btn_6.bind('<Enter>', lambda e: self.btn_6.config(fg='black', bg='lightgrey'))
        self.btn_6.bind('<Leave>', lambda e: self.btn_6.config(fg='white', bg='grey'))
        # keyboard press events **
        self.root.bind("6", lambda e: self.key_6("6"))


        
        # third button frame #############################################################
        self.third_btn_frame = customtkinter.CTkFrame(self.root, border_color='red')
        self.third_btn_frame.pack()

        
        # number 1 button
        self.btn_1 = tkinter.Button(self.third_btn_frame, text="1", width=4, font=("Arial", 16), bg="grey", fg="white", command=lambda:self.key_1("1"))
        self.btn_1.grid(row=0, column=0, sticky="n", padx=2, pady=2)
        # simple fg and bg change when hovered over.
        self.btn_1.bind('<Enter>', lambda e: self.btn_1.config(fg='black', bg='lightgrey'))
        self.btn_1.bind('<Leave>', lambda e: self.btn_1.config(fg='white', bg='grey'))
        # keyboard press events **
        self.root.bind("1", lambda e: self.key_1("1"))


        # number 2 button
        self.btn_2 = tkinter.Button(self.third_btn_frame, text="2", width=4, font=("Arial", 16), bg="grey", fg="white", command=lambda:self.key_2("2"))
        self.btn_2.grid(row=0, column=1, sticky="n", padx=2, pady=2)
        # simple fg and bg change when hovered over.
        self.btn_2.bind('<Enter>', lambda e: self.btn_2.config(fg='black', bg='lightgrey'))
        self.btn_2.bind('<Leave>', lambda e: self.btn_2.config(fg='white', bg='grey'))
        # keyboard press events **
        self.root.bind("2", lambda e: self.key_2("2"))


        # number 3 button
        self.btn_3 = tkinter.Button(self.third_btn_frame, text="3", width=4, font=("Arial", 16), bg="grey", fg="white", command=lambda:self.key_3("3"))
        self.btn_3.grid(row=0, column=2, sticky="n", padx=2, pady=2)
        # simple fg and bg change when hovered over.
        self.btn_3.bind('<Enter>', lambda e: self.btn_3.config(fg='black', bg='lightgrey'))
        self.btn_3.bind('<Leave>', lambda e: self.btn_3.config(fg='white', bg='grey'))
        # keyboard press events **
        self.root.bind("3", lambda e: self.key_3("3"))


        # number enter button
        self.btn_en = tkinter.Button(self.third_btn_frame, text="Enter", width=4, font=("Arial", 16), bg="#6495ED", fg="white", height=3, command=self.enter_key2)
        self.btn_en.grid(row=0, column=3, padx=2, pady=2, rowspan=2)
        # simple fg and bg change when hovered over.
        self.btn_en.bind('<Enter>', lambda e: self.btn_en.config(fg='black', bg='#3D59AB'))
        self.btn_en.bind('<Leave>', lambda e: self.btn_en.config(fg='white', bg='#6495ED'))
        # keyboard press events **
        self.root.bind("<Return>", lambda e: self.enter_key())
        
        ##########

        # number 0 button
        self.btn_0 = tkinter.Button(self.third_btn_frame, text="0", width=9, font=("Arial", 16), bg="grey", fg="white", command=lambda:self.key_0("0"))
        self.btn_0.grid(row=1, column=0, sticky="n", padx=2, pady=2, columnspan=2)
        # simple fg and bg change when hovered over.
        self.btn_0.bind('<Enter>', lambda e: self.btn_0.config(fg='black', bg='lightgrey'))
        self.btn_0.bind('<Leave>', lambda e: self.btn_0.config(fg='white', bg='grey'))
        # keyboard press events **
        self.root.bind("0", lambda e: self.key_0("0"))

        # number dot button
        self.btn_dot = tkinter.Button(self.third_btn_frame, text=".", width=4, font=("Arial", 16), bg="grey", fg="white", command=lambda:self.key_dot("."))
        self.btn_dot.grid(row=1, column=2, sticky="n", padx=2, pady=2)
        # simple fg and bg change when hovered over.
        self.btn_dot.bind('<Enter>', lambda e: self.btn_dot.config(fg='black', bg='lightgrey'))
        self.btn_dot.bind('<Leave>', lambda e: self.btn_dot.config(fg='white', bg='grey'))
        # keyboard press events **
        self.root.bind(".", lambda e: self.key_dot("."))


        # destorys the app if user presses escape key (convenience)
        self.root.bind("<Escape>", lambda e: self.root.destroy())
        # TODO also need a backspace for deleting
        self.root.bind("<BackSpace>", lambda e: self.backspace_key())


        # menu
        my_menu = Menu(self.root)


        # create menu items
        file_menu = Menu(my_menu, tearoff=0, background='#303030', fg='white')
        my_menu.add_cascade(label="File", menu=file_menu)
        file_menu.add_command(label="Clear:", accelerator="C key ", command=lambda:self.c_key(' '))
        file_menu.add_command(label="Errors", accelerator="H key", command=lambda:self.errors_win("e"))
        self.root.bind("h", lambda e: self.errors_win(e))
        file_menu.add_command(label="Advanced", accelerator="A key")
        file_menu.add_separator()
        file_menu.add_command(label="Currency", accelerator="Ctrl+c")

        edit_menu = Menu(my_menu, tearoff=0, background='#303030', fg='white')
        my_menu.add_cascade(label="Edit", menu=edit_menu)
        edit_menu.add_command(label="Theme", accelerator="T key")
        edit_menu.add_command(label="Last Cal", accelerator="Z key")

        self.root.config(menu=my_menu)

        # stops the user from resizing the app
        self.root.resizable(False,False)

        self.root.mainloop()

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




app = App()

# error codes

# error 99 = cannot divide by zero


# TODO add the button/window that examples the calculator error codes
# TODO add a label on top of the entry widget stating "Standard*" or "Advanced"
# TODO add a command to have a currency convert in menu
# TODO add functionality too all menu commands