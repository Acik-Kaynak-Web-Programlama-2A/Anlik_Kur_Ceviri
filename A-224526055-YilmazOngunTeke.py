from tkinter import *
from tkinter import ttk
from bs4 import BeautifulSoup
import requests

window = Tk()
window.title("Kur")
window.geometry("500x400")
window.configure(background="gray")

from_currency = StringVar()
to_currency = StringVar()
money = StringVar()

def get_currency():
    url = f'https://www.google.com/finance/quote/{from_currency.get()}-{to_currency.get()}'
    response = requests.get(url)
    html_content = response.text
    html_content = BeautifulSoup(html_content, "html.parser")
    return float(html_content.find("div", class_="YMlKec fxKbKc").getText().replace(",", "."))

def calc():
    lbl_sonuc.configure(text=int(money.get()) * get_currency())

lbl_tlmik = Label(window, text="Paranızı girin: ")
lbl_tlmik.grid(row=0, column=0, padx="10")

money_entry = Entry(window, textvariable = money, font=('calibre',10,'normal'))
money_entry.grid(row=0, column=1, padx="10")

cmb_to_currency = ttk.Combobox(window, values=['USD', 'EUR', 'GBP', 'TRY'], textvariable=to_currency, state="readonly")
cmb_to_currency.grid(row=2, column=1, padx="10")

cmb_from_currency = ttk.Combobox(window, values=['USD', 'EUR', 'GBP', 'TRY'], textvariable=from_currency, state="readonly")
cmb_from_currency.grid(row=1, column=1, padx="10")

label2 = Label(window, text="Dönüştürülecek kuru seç: ")
label2.grid(row=2, column=0, padx="10", pady="5")

label3 = Label(window, text="Paranızın türü: ")
label3.grid(row=1, column=0, padx="10", pady="15")

btn_hes = ttk.Button(window, text="Hesapla", command=calc)
btn_hes.grid(row=4, column=1, padx="10", pady="15")

lbl1 = Label(window, text="Dönüştürülmüş paranız --> ")
lbl1.grid(row=3, column=0)

lbl_sonuc = Label(window, text="0")
lbl_sonuc.grid(row=3, column=1, padx="10")

btn1 = ttk.Button(window, text="Exit", command=window.destroy)
btn1.grid(row=5, column=1, pady="30")

window.mainloop()