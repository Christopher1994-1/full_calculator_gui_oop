import customtkinter
import tkinter
from tkinter import *



class App:
   def __init__(self):
      self.root = customtkinter.CTk()
      self.root.title("Simple Calculator")
      self.root.iconbitmap("darkModeV.ico")
      self.root.geometry("280x340") # L x H


      # label here
      self.label_pack = customtkinter.CTkFrame(self.root)
      self.label_pack.pack(pady=5, padx=(10, 0))

      self.header_label = customtkinter.CTkLabel(self.label_pack, text="Standard", bg_color="#282828", height=0, width=0, text_font=("Arial", 14, "bold"))
      self.header_label.pack(side=TOP, anchor="w", padx=(15, 0), pady=(10, 0)) # pady=(top, bottom) padx=(left, right) in px


      # entry box here
      self.entry_pack = customtkinter.CTkFrame(self.root)
      self.entry_pack.pack(pady=5, padx=(10, 0))

      # entry box widget
      self.entry = customtkinter.CTkEntry(self.entry_pack, text_font=("Arial", 26), width=245, height=44)
      self.entry.grid(row=1, column=0, columnspan=3)



      # first set of standard cals
      self.first_pack = customtkinter.CTkFrame(self.root)
      self.first_pack.pack(pady=5, side=LEFT, anchor='nw', padx=(10, 0))


      # second set of standard cals
      self.second_pack = customtkinter.CTkFrame(self.root)
      self.second_pack.pack(pady=5, side=LEFT, anchor='ne', padx=(10, 0))




      
      self.root.bind("a", lambda e: self.advanced_option("1"))

      self.root.mainloop()


   def advanced_option(self, e):
      self.root.geometry("570x340")
      self.root.title("Simple Calculator - Advanced")
      #self.header_label.configure(text="Advanced")
      #self.entry.configure(width=570)
      self.root.bind("r", lambda e: self.return_resize(e))

   def return_resize(self, e):
      self.root.geometry("280x340")
      self.root.title("Simple Calculator")
      #self.header_label.configure(text="Standard")



app = App()