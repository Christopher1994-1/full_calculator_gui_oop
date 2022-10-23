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

        # number * button
        self.btn_mut = tkinter.Button(self.btn_frame, text="*", width=4, font=("Arial", 16), bg="grey", fg="white")
        self.btn_mut.grid(row=0, column=2, sticky="w", padx=2, pady=2)

        # number - button
        self.btn_sub = tkinter.Button(self.btn_frame, text="-", width=4, font=("Arial", 16), bg="grey", fg="white")
        self.btn_sub.grid(row=0, column=3, sticky="w", padx=2, pady=2)


        # second button frame #################################################################################

        self.second_btn_frame = customtkinter.CTkFrame(self.root)
        self.second_btn_frame.pack()

        
        # number 7 button
        self.btn_7 = tkinter.Button(self.second_btn_frame, text="7", width=4, font=("Arial", 16), bg="grey", fg="white")
        self.btn_7.grid(row=0, column=0, sticky="n", padx=2, pady=2)

        # number 7 button
        self.btn_8 = tkinter.Button(self.second_btn_frame, text="8", width=4, font=("Arial", 16), bg="grey", fg="white")
        self.btn_8.grid(row=0, column=1, sticky="n", padx=2, pady=2)

        # number 9 button
        self.btn_9 = tkinter.Button(self.second_btn_frame, text="9", width=4, font=("Arial", 16), bg="grey", fg="white")
        self.btn_9.grid(row=0, column=2, sticky="n", padx=2, pady=2)

        # number add button
        self.btn_add = tkinter.Button(self.second_btn_frame, text="+", width=4, font=("Arial", 16), bg="grey", fg="white", height=3)
        self.btn_add.grid(row=0, column=3, padx=2, pady=2, rowspan=2)
        
        ##########

        # number 4 button
        self.btn_4 = tkinter.Button(self.second_btn_frame, text="4", width=4, font=("Arial", 16), bg="grey", fg="white")
        self.btn_4.grid(row=1, column=0, sticky="n", padx=2, pady=2)

        # number 5 button
        self.btn_5 = tkinter.Button(self.second_btn_frame, text="5", width=4, font=("Arial", 16), bg="grey", fg="white")
        self.btn_5.grid(row=1, column=1, sticky="n", padx=2, pady=2)

        # number 6 button
        self.btn_6 = tkinter.Button(self.second_btn_frame, text="6", width=4, font=("Arial", 16), bg="grey", fg="white")
        self.btn_6.grid(row=1, column=2, sticky="n", padx=2, pady=2)


        
        # third button frame #############################################################
        self.third_btn_frame = customtkinter.CTkFrame(self.root, border_color='red')
        self.third_btn_frame.pack()

        
        # number 1 button
        self.btn_1 = tkinter.Button(self.third_btn_frame, text="1", width=4, font=("Arial", 16), bg="grey", fg="white")
        self.btn_1.grid(row=0, column=0, sticky="n", padx=2, pady=2)

        # number 2 button
        self.btn_2 = tkinter.Button(self.third_btn_frame, text="2", width=4, font=("Arial", 16), bg="grey", fg="white")
        self.btn_2.grid(row=0, column=1, sticky="n", padx=2, pady=2)

        # number 3 button
        self.btn_3 = tkinter.Button(self.third_btn_frame, text="3", width=4, font=("Arial", 16), bg="grey", fg="white")
        self.btn_3.grid(row=0, column=2, sticky="n", padx=2, pady=2)

        # number enter button
        self.btn_en = tkinter.Button(self.third_btn_frame, text="Enter", width=4, font=("Arial", 16), bg="grey", fg="white", height=3)
        self.btn_en.grid(row=0, column=3, padx=2, pady=2, rowspan=2)
        
        ##########

        # number 0 button
        self.btn_0 = tkinter.Button(self.third_btn_frame, text="0", width=9, font=("Arial", 16), bg="grey", fg="white")
        self.btn_0.grid(row=1, column=0, sticky="n", padx=2, pady=2, columnspan=2)

        # number dot button
        self.btn_dot = tkinter.Button(self.third_btn_frame, text=".", width=4, font=("Arial", 16), bg="grey", fg="white")
        self.btn_dot.grid(row=1, column=2, sticky="n", padx=2, pady=2)


        self.root.mainloop()


app = App()