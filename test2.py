import customtkinter
from tkinter import *


class App:
    def __init__(self):
        self.root = customtkinter.CTk()
        self.root.geometry("500x500")
        
        self.first_pack = customtkinter.CTkFrame(self.root)
        self.first_pack.pack()
        
        self.first_pack_button = customtkinter.CTkButton(self.first_pack, text="Second Frame", command=self.second_frame)
        self.first_pack_button.pack()
        
        
        self.my_menu = Menu(self.root)


        # create menu items
        self.file_menu = Menu(self.my_menu, tearoff=0, background='#303030', fg='white')
        self.my_menu.add_cascade(label="File", menu=self.file_menu)

        self.file_menu.add_command(label="New") # command=lambda:self.c_key(' ')
        
        self.root.config(menu=self.my_menu)
        
        
        
        
        self.root.mainloop()
        
        
        
    def second_frame(self):
        self.root.geometry("400x400")
        self.first_pack.pack_forget()
        self.my_menu = Menu(self.root)


        # create menu items
        self.file_menu = Menu(self.my_menu, tearoff=0, background='#303030', fg='white')
        self.my_menu.add_cascade(label="File", menu=self.file_menu)

        self.file_menu.add_command(label="No New", command=self.first_frame) # command=lambda:self.c_key(' ')
        
        self.root.config(menu=self.my_menu)
        
        self.second_pack = customtkinter.CTkFrame(self.root)
        self.second_pack.pack()
        
        self.second_button = customtkinter.CTkButton(self.second_pack, text="First Frame", command=self.first_frame)
        self.second_button.pack()
        
            
            
            
    def first_frame(self):
        self.my_menu = Menu(self.root)


        # create menu items
        self.file_menu = Menu(self.my_menu, tearoff=0, background='#303030', fg='white')
        self.my_menu.add_cascade(label="File", menu=self.file_menu)

        self.file_menu.add_command(label="New", command=self.second_frame) # command=lambda:self.c_key(' ')
        
        self.root.config(menu=self.my_menu)
        self.root.geometry("500x500")
        self.second_pack.pack_forget()
        self.first_pack.pack()
        

        

app = App()