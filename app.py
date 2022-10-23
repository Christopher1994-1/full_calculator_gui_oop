import customtkinter
import tkinter


class App:
    def __init__(self):
        # all the main variables
        self.root = customtkinter.CTk()
        self.root.title("Simple Calculator")
        self.root.iconbitmap("darkModeV.ico")
        self.root.geometry("280x340") # L x H

        # first frame of the GUI
        self.first_frame = customtkinter.CTkFrame(self.root)
        self.first_frame.pack(pady=15)
        # entry box widget
        self.entry = customtkinter.CTkEntry(self.first_frame, text_font=("Arial", 26), width=245)
        self.entry.grid(row=0, column=0)

        #########################################
        # button frame
        self.btn_frame = customtkinter.CTkFrame(self.root)
        self.btn_frame.pack()

        # number blank button 
        self.btn_blank = tkinter.Button(self.btn_frame, text=" ", width=4, font=("Arial", 16), bg="grey", fg="white", state="disabled")
        self.btn_blank.grid(row=0, column=0, sticky="w", padx=2, pady=2)

        # number / button
        self.btn_div = tkinter.Button(self.btn_frame, text="/", width=4, font=("Arial", 16), bg="grey", fg="white")
        self.btn_div.grid(row=0, column=1, sticky="w", padx=2, pady=2)
        # simple fg and bg change when hovered over.
        self.btn_div.bind('<Enter>', lambda e: self.btn_div.config(fg='black', bg='lightgrey'))
        self.btn_div.bind('<Leave>', lambda e: self.btn_div.config(fg='white', bg='grey'))

        # number * button
        self.btn_mut = tkinter.Button(self.btn_frame, text="*", width=4, font=("Arial", 16), bg="grey", fg="white")
        self.btn_mut.grid(row=0, column=2, sticky="w", padx=2, pady=2)
        # simple fg and bg change when hovered over.
        self.btn_mut.bind('<Enter>', lambda e: self.btn_mut.config(fg='black', bg='lightgrey'))
        self.btn_mut.bind('<Leave>', lambda e: self.btn_mut.config(fg='white', bg='grey'))

        # number - button
        self.btn_sub = tkinter.Button(self.btn_frame, text="-", width=4, font=("Arial", 16), bg="grey", fg="white")
        self.btn_sub.grid(row=0, column=3, sticky="w", padx=2, pady=2)
        # simple fg and bg change when hovered over.
        self.btn_sub.bind('<Enter>', lambda e: self.btn_sub.config(fg='black', bg='lightgrey'))
        self.btn_sub.bind('<Leave>', lambda e: self.btn_sub.config(fg='white', bg='grey'))


        # second button frame #################################################################################

        self.second_btn_frame = customtkinter.CTkFrame(self.root)
        self.second_btn_frame.pack()

        
        # number 7 button
        self.btn_7 = tkinter.Button(self.second_btn_frame, text="7", width=4, font=("Arial", 16), bg="grey", fg="white")
        self.btn_7.grid(row=0, column=0, sticky="n", padx=2, pady=2)
        #
        self.btn_7.bind('<Enter>', lambda e: self.btn_7.config(fg='black', bg='lightgrey'))
        self.btn_7.bind('<Leave>', lambda e: self.btn_7.config(fg='white', bg='grey'))

        # number 8 button
        self.btn_8 = tkinter.Button(self.second_btn_frame, text="8", width=4, font=("Arial", 16), bg="grey", fg="white")
        self.btn_8.grid(row=0, column=1, sticky="n", padx=2, pady=2)
        #
        self.btn_8.bind('<Enter>', lambda e: self.btn_8.config(fg='black', bg='lightgrey'))
        self.btn_8.bind('<Leave>', lambda e: self.btn_8.config(fg='white', bg='grey'))

        # number 9 button
        self.btn_9 = tkinter.Button(self.second_btn_frame, text="9", width=4, font=("Arial", 16), bg="grey", fg="white")
        self.btn_9.grid(row=0, column=2, sticky="n", padx=2, pady=2)
        #
        self.btn_9.bind('<Enter>', lambda e: self.btn_9.config(fg='black', bg='lightgrey'))
        self.btn_9.bind('<Leave>', lambda e: self.btn_9.config(fg='white', bg='grey'))

        # number add button
        self.btn_add = tkinter.Button(self.second_btn_frame, text="+", width=4, font=("Arial", 16), bg="grey", fg="white", height=3, command=self.add_func)
        self.btn_add.grid(row=0, column=3, padx=2, pady=2, rowspan=2)
        #
        self.btn_add.bind('<Enter>', lambda e: self.btn_add.config(fg='black', bg='lightgrey'))
        self.btn_add.bind('<Leave>', lambda e: self.btn_add.config(fg='white', bg='grey'))
        self.root.bind("+", lambda e: self.add_func("+"))
        
        ##########

        # number 4 button
        self.btn_4 = tkinter.Button(self.second_btn_frame, text="4", width=4, font=("Arial", 16), bg="grey", fg="white")
        self.btn_4.grid(row=1, column=0, sticky="n", padx=2, pady=2)
        #
        self.btn_4.bind('<Enter>', lambda e: self.btn_4.config(fg='black', bg='lightgrey'))
        self.btn_4.bind('<Leave>', lambda e: self.btn_4.config(fg='white', bg='grey'))

        # number 5 button
        self.btn_5 = tkinter.Button(self.second_btn_frame, text="5", width=4, font=("Arial", 16), bg="grey", fg="white")
        self.btn_5.grid(row=1, column=1, sticky="n", padx=2, pady=2)
        #
        self.btn_5.bind('<Enter>', lambda e: self.btn_5.config(fg='black', bg='lightgrey'))
        self.btn_5.bind('<Leave>', lambda e: self.btn_5.config(fg='white', bg='grey'))

        # number 6 button
        self.btn_6 = tkinter.Button(self.second_btn_frame, text="6", width=4, font=("Arial", 16), bg="grey", fg="white")
        self.btn_6.grid(row=1, column=2, sticky="n", padx=2, pady=2)
        #
        self.btn_6.bind('<Enter>', lambda e: self.btn_6.config(fg='black', bg='lightgrey'))
        self.btn_6.bind('<Leave>', lambda e: self.btn_6.config(fg='white', bg='grey'))


        
        # third button frame #############################################################
        self.third_btn_frame = customtkinter.CTkFrame(self.root, border_color='red')
        self.third_btn_frame.pack()

        
        # number 1 button
        self.btn_1 = tkinter.Button(self.third_btn_frame, text="1", width=4, font=("Arial", 16), bg="grey", fg="white")
        self.btn_1.grid(row=0, column=0, sticky="n", padx=2, pady=2)
        #
        self.btn_1.bind('<Enter>', lambda e: self.btn_1.config(fg='black', bg='lightgrey'))
        self.btn_1.bind('<Leave>', lambda e: self.btn_1.config(fg='white', bg='grey'))

        # number 2 button
        self.btn_2 = tkinter.Button(self.third_btn_frame, text="2", width=4, font=("Arial", 16), bg="grey", fg="white")
        self.btn_2.grid(row=0, column=1, sticky="n", padx=2, pady=2)
        #
        self.btn_2.bind('<Enter>', lambda e: self.btn_2.config(fg='black', bg='lightgrey'))
        self.btn_2.bind('<Leave>', lambda e: self.btn_2.config(fg='white', bg='grey'))

        # number 3 button
        self.btn_3 = tkinter.Button(self.third_btn_frame, text="3", width=4, font=("Arial", 16), bg="grey", fg="white")
        self.btn_3.grid(row=0, column=2, sticky="n", padx=2, pady=2)
        #
        self.btn_3.bind('<Enter>', lambda e: self.btn_3.config(fg='black', bg='lightgrey'))
        self.btn_3.bind('<Leave>', lambda e: self.btn_3.config(fg='white', bg='grey'))

        # number enter button
        self.btn_en = tkinter.Button(self.third_btn_frame, text="Enter", width=4, font=("Arial", 16), bg="grey", fg="white", height=3)
        self.btn_en.grid(row=0, column=3, padx=2, pady=2, rowspan=2)
        #
        self.btn_en.bind('<Enter>', lambda e: self.btn_en.config(fg='black', bg='lightgrey'))
        self.btn_en.bind('<Leave>', lambda e: self.btn_en.config(fg='white', bg='grey'))
        
        ##########

        # number 0 button
        self.btn_0 = tkinter.Button(self.third_btn_frame, text="0", width=9, font=("Arial", 16), bg="grey", fg="white")
        self.btn_0.grid(row=1, column=0, sticky="n", padx=2, pady=2, columnspan=2)
        # 
        self.btn_0.bind('<Enter>', lambda e: self.btn_0.config(fg='black', bg='lightgrey'))
        self.btn_0.bind('<Leave>', lambda e: self.btn_0.config(fg='white', bg='grey'))

        # number dot button
        self.btn_dot = tkinter.Button(self.third_btn_frame, text=".", width=4, font=("Arial", 16), bg="grey", fg="white")
        self.btn_dot.grid(row=1, column=2, sticky="n", padx=2, pady=2)
        # 
        self.btn_dot.bind('<Enter>', lambda e: self.btn_dot.config(fg='black', bg='lightgrey'))
        self.btn_dot.bind('<Leave>', lambda e: self.btn_dot.config(fg='white', bg='grey'))

        self.root.mainloop()

    # functions for buttons ********

    def add_func(self, a):
        print("lol")
        print(a)


app = App()