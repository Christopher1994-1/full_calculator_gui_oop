import os
import requests
from datetime import datetime
import sys




exchanges = {
    "United States - Dollar": "USD", 
    "Canadian - Dollar": "CAD", 
    "Australian - Dollar": "AUD", 
    "Europe - Euro": "EUR",
    "Indian - Rupee": "INR",
    "United Kingdom - Pound": "GBP",
    "Japan - Yen": "JPY",
    "Afghanistan - Afghani": "AFN",
    "Albania - Lek": "ALL",
    "Bermuda - Dollar": "BMD",
    "Barbados - Dollar": "BBD",
    "Algeria - Algerian Dinar": "DZD",
    "Belize - Dollar": "BZD",
    "Azerbatjan - Manat": "AZN",
    "Bangladesh - Taka": "BDT",
    "Bolivia - Boliviano": "BOB",
    "Brueni - Dollar": "BND",
    "Congo - Franc": "CDF",
    "Philippines - Peso": "PHP",
    "Bulgaria - Lev": "BGN",
    "Morocco - Dirham": "MAD",
    "Romania - Leu": "RON",
    "Papua New Guinea - Kina": "PGK",
    "Nigerian - Naira": "NGN",
    "Nicargua - Cordoba": "NIO",
    "Pakistan - Rupee": "PKR",
    "Qater - Riyal": "QAR",
    "Costa Rica - Colon": "CRC",
    "New Zealand - Dollar": "NZD",
    "Nepal - Rupee": "NPR",
    "Djibouti - Franc": "DJF",
    "Peru - Nuevo Sol": "PEN", 
    "Norway - Krone": "NOK",
    "Moldova - Leu": "MDL",
    "Dominican Republic - Peso": "DOP",
    "Guatemala - Quetzal": "GTQ",
    "Guinea - Franc": "GNF",
    "Serbia - Dinar": "RSD",
    "Mexico - Peso": "MXN",
    "Laos - Kip": "LAK",
    "Poland - Zloty": "PLN",
    "Labanon - Pound": "LBP",
    "Libya - Dinar": "LYD",
    "Liberia - Dollar": "LRD",
    "Haiti - Gourde": "HTG",
    "Honduras - Lempira": "HNL",
    "Russian - Rouble": "RUB",
    "Saudi Arabia - Riyal": "SAR",
    "Korea - Won": "KRW",
    "Kuwait - Dinar": "KWD",
    "Hong Kong SAR - Dollar": "HK$", 
    "Iraq - Dinar": "IQD",
    "Sri Lanka - Rupee": "LKR",
    "Israel - Shekel": "ILS",
    "Sweden - Krona": "SEK",
    "Jamaica - Dollar": "JMD",
    "Kenya - Shilling": "KES",
    "Jordan - Dinar": "JOD",
    "Sierra Leone - Leone": "SLE",
    "Singapore - Dollar": "SGD",
    "Somalia - Shilling": "SOS",
    "South Africa - Rand": "ZAR",
    "Kazakhstan - Tenge": "KZT",
    "Chile - Peso": "CLP",
    "Sudan - Pound": "SGD",
    "Iceland - Krona": "ISK",
    "Indonesia - Rupiah": "IRD",
    "Iran - Rial": "IRR",
    "Ethiopia - Birr": "ETB",
    "Georgia - Lari": "GEL",
    "Swaziland - Liangeni": "SZL",
    "Ghana - Cedi": "GHS",
    "Egypt - Pound": "EGP",
    "Croatia - Kuna": "HRK",
    "Colombia - Peso": "COP",
    "Venezuela - Bolivar": "VEF",
    "Vietnam - Dong": "WND",
    "Yemen - Rial": "YER",
    "Zambia - Kwacha": "ZMW",
    "Zimbabwe - Dollar": "ZWL",
    "Denmark - Krone": "DKK",
    "Thaliand - Baht": "THB",
    "Cuba - Peso": "CUP",
    "Brazil - Real": "BRL",
    "Botswana - Pula": "BWP",
    "Switezerland - Franc": "CHF",
    "Uzbekistan - Som": "UZS",
    "Taiwan - New Dollar": "TWD",
    "Tanzania - Shilling": "TJS",
    "Turkey - Lira": "TRY",
    "Uganda - Shilling": "UGX",
    "Ukraine - Hryvna": "UAH",
    "Czech Republic - Koruna": "CZK",
    "Belarus - Ruble": "BYN",
    "Bahamas - Dollar": "BSD",
    "United Arab Emirates - Dirham": "AED",
    "Uruguay - Peso": "UYI",
    "China - Yuan": "CNY",
    "Camodia - Riel": "KHR",
    "Bahrain - Dinar": "BHD",
    "Angola - Kwanza": "AOA",
    "Argentina - Peso": "ARS",
    "Aruba - Guilder": "AWG",
    }






currency_symbols = {
    "USD": "$", 
    "BND": "$",
    "CNY": "¥",
    "CLP": "$",
    "KHR": "៛",
    "BGN": "Лв",
    "DKK": "kr",
    "EGP": "ج.م",
    "DOP": "RD$",
    "GEL": "ლ",
    "GNF": "FG",
    "HTG": "G",
    "HNL": "L",
    "ILS": "₪",
    "LBP": ".ل.ل",
    "HKD": "HK$",
    "NOK": "kr",
    "AED": "د.إ",
    "UYI": "$U",
    "YER": "﷼",
    "VND": "₫",
    "ZMW": "K",
    "ZWL": "Z$",
    "UZS": "лв",
    "VEF": "Bs.S",
    "PLN": "zł",
    "QAR": "ر.ق",
    "UAH": "₴",
    "RON": "lei",
    "RUB": "₽",
    "SAR": "SR",
    "RSD": "дин",
    "SLE": "Le",
    "SGD": "S$",
    "SOS": "S",
    "ZAR": "R",
    "LKR": "Rs",
    "SGD": "ج.س.",
    "TWD": "NT$",
    "TJS": "TSh",
    "THB": "฿",
    "TRY": "TRY",
    "UGX": "Ush",
    "SZL": "E",
    "SEK": "kr",
    "CHF": "CHF",
    "PKR": "Rs",
    "PGK": "K",
    "PEN": "S/.",
    "PHP": "₱",    
    "KWD": "د.ك",
    "LAK": "₭",
    "NPR": "Rs",
    "NZD": "$",
    "NIO": "C$",
    "NGN": "₦",
    "COP": "$",
    "KES": "KSh",
    "GHS": "₵",
    "JMD": "J$",
    "GTQ": "Q",
    "MAD": ".د.م",
    "CUP": "$",
    "JOD": "د.ا",
    "KZT": "₸",
    "LYD": "ل.د",
    "MXN":"$",
    "MDL": "MDL",
    "IQD": "ع.د",
    "LRD": "$",
    "IRR": "﷼",
    "CAD": "$", 
    "ISK": "kr",
    "IRD": "Rp",
    "KRW": "₩",
    "BRL": "R$",
    "HRK": "kn",
    "DJF": "Fdj",
    "ETB": "ETB",
    "CRC": "₡",
    "BOB": "$b",
    "BYN": "Br",
    "CZK": "Kč",
    "CDF": "F",
    "BWP": "P",
    "BBD": "$",
    "BDT": "৳",
    "AZN": "₼",
    "BHD": ".د.ب",
    "BZD": "BZ$",
    "BMD": "$",
    "BSD": "B$",
    "AUD": "$", 
    "AWG": "ƒ",
    "ARS": "$",
    "AOA": "Kz",
    "INR": "₹",
    "EUR": "€",
    "DZD": "دج",
    "GBP": "£",
    "JPY": "¥",
    "AFN": "؋",
    "ALL": "ALL"

    }



# kam = ["a", "e", "b", "p", "c", "r", "d"]

# print(sorted(kam))

# import customtkinter
# from tkinter import ttk


# class App:
#     def __init__(self):
#         self.root = customtkinter.CTk()
#         self.values = []
#         self.combostyle = ttk.Style()

#         self.combostyle.theme_create('combostyle', parent='alt',
#                          settings = {'TCombobox':
#                                      {'configure':
#                                       {'selectbackground': 'blue',
#                                        'fieldbackground': 'grey',
#                                        'background': 'green',
#                                        "arrowbutton": 'black'
#                                        }}}
#                          )
#         self.combostyle.theme_use('combostyle') 

#         for inde in range(1, 100):
#             self.values.append(f"Test {inde}")

#         self.combo = ttk.Combobox(self.root, values=self.values)
#         self.combo.set("Test 1")
#         self.combo.pack()


#         self.root.mainloop()

# app = App()



if __name__ == "__main__":
    print(f"Size of Currency Symbols  Dict is {sys.getsizeof(currency_symbols)} Bytes")

    print(f"Size of Exchanges Dict is {sys.getsizeof(exchanges)} Bytes")