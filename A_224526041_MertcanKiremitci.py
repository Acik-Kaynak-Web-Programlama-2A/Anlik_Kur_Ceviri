# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
from tkinter import *
from tkinter import ttk
from bs4 import BeautifulSoup
import requests

def get_exchange_rates():
    weburl = "https://www.google.com/finance/quote/USD-TRY?hl=tr"
    websayfa1 = requests.get(weburl)
    html_websayfa1 = BeautifulSoup(websayfa1.content, "html.parser")
    edolar = float(html_websayfa1.find("div", class_="YMlKec fxKbKc").getText().replace(",", "."))

    weburl2 = "https://www.google.com/finance/quote/EUR-TRY?hl=tr"
    websayfa2 = requests.get(weburl2)
    html_websayfa2 = BeautifulSoup(websayfa2.content, "html.parser")
    e_euro = float(html_websayfa2.find("div", class_="YMlKec fxKbKc").getText().replace(",", "."))

    return edolar, e_euro

def hesapla():
    try:
        deger = float(e_deger_giris.get())
        girilen_deger = cmb_girilenkur.get()
        cevirilecek_kur_degeri = cmb_cevirilecekkur.get()

        if girilen_deger == "TL":
            girilen_deger_orani = 1
        elif girilen_deger == "USD":
            girilen_deger_orani = edolar
        elif girilen_deger == "EURO":
            girilen_deger_orani = e_euro
        else:
            girilen_deger_orani = 0

        if cevirilecek_kur_degeri == "TL":
            cevirilecek_kur_degeri_orani = 1
        elif cevirilecek_kur_degeri == "USD":
            cevirilecek_kur_degeri_orani = edolar
        elif cevirilecek_kur_degeri == "EURO":
            cevirilecek_kur_degeri_orani = e_euro
        else:
            cevirilecek_kur_degeri_orani = 0

        sonuc = (deger / girilen_deger_orani) * cevirilecek_kur_degeri_orani

        lbl_sonucdeger.config(text=f"Sonuç: {deger} {girilen_deger} = {sonuc:.2f} {cevirilecek_kur_degeri}")
    except ValueError:
        lbl_sonucdeger.config(text="Geçersiz deger!")

    guncelle_borsa()

def guncelle_borsa():
    global edolar, e_euro
    edolar, e_euro = get_exchange_rates()
    lbl_hesapsonucdeger.config(text="Kur güncellendi.")
    pencereform.after(2000, lambda: lbl_hesapsonucdeger.config(text=""))  # 2000 milisaniye (2 saniye) sonra temizle

pencereform = Tk()
pencereform.title("Kur Hesapla")
pencereform.geometry("400x400")

lbl_metindeger = Label(pencereform, text="DEĞER:")
lbl_girilenkurdeger = ttk.Label(pencereform, text="GİRİLEN KUR TÜRÜ:")
lbl_cevirilecekkurdeger = ttk.Label(pencereform, text="ÇEVİRİLECEK KUR TÜRÜ:")
lbl_sonucdeger = ttk.Label(pencereform, text="SONUÇ:")
lbl_hesapsonucdeger = ttk.Label(pencereform, text="")

cmb_girilenkur = ttk.Combobox(pencereform, values=["TL", "USD", "EURO"])
cmb_cevirilecekkur = ttk.Combobox(pencereform, values=["TL", "USD", "EURO"])
btn_hesapla = ttk.Button(pencereform, text="HESAPLA", command=hesapla)

e_deger_giris = ttk.Entry(pencereform)

lbl_metindeger.grid(row=0, column=0)
e_deger_giris.grid(row=0, column=1, padx=20)
lbl_girilenkurdeger.grid(row=1, column=0, pady=5)
cmb_girilenkur.grid(row=1, column=1, padx=20, pady=5)
lbl_cevirilecekkurdeger.grid(row=2, column=0, pady=5)
cmb_cevirilecekkur.grid(row=2, column=1, padx=20, pady=5)
btn_hesapla.grid(row=3, column=1, padx=20, pady=20)
lbl_sonucdeger.grid(row=4, column=0, columnspan=2)
lbl_hesapsonucdeger.grid(row=5, column=0, columnspan=2)

edolar, e_euro = get_exchange_rates()

pencereform.mainloop()