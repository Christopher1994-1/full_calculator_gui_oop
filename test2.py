import requests
from requests import Request, Session
import os
import customtkinter
import json
from currency_exchanges import exchanges, currency_symbols



class Test:
    def __init__(self):
        self.root = customtkinter.CTk()
        
        
        self.root.bind("r", lambda e: self.standard("0"))
        
        
        
        
        self.root.mainloop()
        
        
        
        
        
    def standard(self, e):
        self.main_label = customtkinter.CTkLabel(self.root, text="0")
        self.main_label.pack()
        
        
        
app = Test()