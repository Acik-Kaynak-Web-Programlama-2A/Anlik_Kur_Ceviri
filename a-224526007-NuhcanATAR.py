from tkinter import *
from tkinter import ttk
from bs4 import BeautifulSoup
import requests

def get_exchange_rates():
    urlDolar = "https://www.google.com/finance/quote/USD-TRY?hl=tr"
    dolarPage = requests.get(urlDolar)
    htmlDOLARPAGE = BeautifulSoup(dolarPage.content, "html.parser")
    dolarValue = float(htmlDOLARPAGE.find("div", class_="YMlKec fxKbKc").getText().replace(",", "."))

    urlEuro = "https://www.google.com/finance/quote/EUR-TRY?hl=tr"
    euroPage = requests.get(urlEuro)
    htmlEUROPAGE = BeautifulSoup(euroPage.content, "html.parser")
    euroValue = float(htmlEUROPAGE.find("div", class_="YMlKec fxKbKc").getText().replace(",", "."))

    return dolarValue, euroValue

def temizle():
    e_miktar_giris.delete(0, END)
    lbl_sonuc.config(text="")
    
def hesapla():
    try:
        miktar = float(e_miktar_giris.get())
        girilen_kur = cmb_girilenkur.get()
        cevirilecek_kur = cmb_cevirilecekkur.get()

        if girilen_kur == "TL":
            girilen_kur_orani = 1
        elif girilen_kur == "USD":
            girilen_kur_orani = dolarValue
        elif girilen_kur == "EURO":
            girilen_kur_orani = euroValue
        else:
            girilen_kur_orani = 0
        if cevirilecek_kur == "TL":
            cevirilecek_kur_orani = 1
        elif cevirilecek_kur == "USD":
            cevirilecek_kur_orani = dolarValue
        elif cevirilecek_kur == "EURO":
            cevirilecek_kur_orani = euroValue
        else:
            cevirilecek_kur_orani = 0
        sonuc = (miktar * girilen_kur_orani) / cevirilecek_kur_orani
        lbl_sonuc.config(text=f"Girilen : {miktar} {girilen_kur} = {sonuc:.2f} {cevirilecek_kur}")
    except ValueError:
        lbl_sonuc.config(text="Geçersiz miktar!")

    update_exchange_rates()

def update_exchange_rates():
    global dolarValue, euroValue
    dolarValue, euroValue = get_exchange_rates()
    lbl_hesapsonuc.config(text="Değerler Yazdırıldı!.")
    anaform.after(2000, lambda: lbl_hesapsonuc.config(text=""))
    

anaform = Tk()
anaform.title("Kur Hesapla Pyhton")
anaform.geometry("400x300")

lbl_miktar = Label(anaform, text="Miktar:")
lbl_miktar.grid(row=0, column=0,pady=20)

lbl_girilenkur = ttk.Label(anaform, text="Girilen Kur:")
lbl_girilenkur.grid(row=1, column=0, pady=5)

lbl_cevirilecekkur = ttk.Label(anaform, text="Çevrilecek Kur:")
lbl_cevirilecekkur.grid(row=2, column=0, pady=5)

lbl_sonuc = ttk.Label(anaform, text="")
lbl_sonuc.grid(row=4, column=1, columnspan=2)

cmb_girilenkur = ttk.Combobox(anaform, values=["TL", "USD", "EURO"])
cmb_girilenkur.grid(row=1, column=1, padx=20, pady=5)

e_miktar_giris = ttk.Entry(anaform)
e_miktar_giris.grid(row=0, column=1, padx=20)

cmb_cevirilecekkur = ttk.Combobox(anaform, values=["TL", "USD", "EURO"])
cmb_cevirilecekkur.grid(row=2, column=1, padx=20, pady=5)

btn_hesapla_guncelle = ttk.Button(anaform, text="Hesapla", command=hesapla)
btn_hesapla_guncelle.grid(row=3, column=1, padx=20, pady=20)

lbl_hesapsonuc = ttk.Label(anaform, text="")
lbl_hesapsonuc.grid(row=5, column=1, columnspan=2)

btn_temizle = ttk.Button(anaform, text="Temizle",command=temizle)
btn_temizle.grid(row=6, column=1)



dolarValue, euroValue = get_exchange_rates()

anaform.mainloop()