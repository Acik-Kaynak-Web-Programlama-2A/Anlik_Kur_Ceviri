from tkinter import *
from tkinter import ttk
from bs4 import BeautifulSoup
import requests

def get_exchange_rates():
    url1 = "https://www.google.com/finance/quote/USD-TRY?hl=tr"
    sayfa1 = requests.get(url1)
    html_sayfa1 = BeautifulSoup(sayfa1.content, "html.parser")
    roundeddolar = float(html_sayfa1.find("div", class_="YMlKec fxKbKc").getText().replace(",", "."))

    url2 = "https://www.google.com/finance/quote/EUR-TRY?hl=tr"
    sayfa2 = requests.get(url2)
    html_sayfa2 = BeautifulSoup(sayfa2.content, "html.parser")
    roundedeuro = float(html_sayfa2.find("div", class_="YMlKec fxKbKc").getText().replace(",", "."))

    return roundeddolar, roundedeuro


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
            girilen_kur_orani = roundeddolar
        elif girilen_kur == "EURO":
            girilen_kur_orani = roundedeuro
        else:
            girilen_kur_orani = 0
        if cevirilecek_kur == "TL":
            cevirilecek_kur_orani = 1
        elif cevirilecek_kur == "USD":
            cevirilecek_kur_orani = roundeddolar
        elif cevirilecek_kur == "EURO":
            cevirilecek_kur_orani = roundedeuro
        else:
            cevirilecek_kur_orani = 0
        sonuc = (miktar * girilen_kur_orani) / cevirilecek_kur_orani
        lbl_sonuc.config(text=f"Girilen : {miktar} {girilen_kur} = {sonuc:.2f} {cevirilecek_kur}")
    except ValueError:
        lbl_sonuc.config(text="Geçersiz miktar!")

    update_exchange_rates()

def update_exchange_rates():
    global roundeddolar, roundedeuro
    roundeddolar, roundedeuro = get_exchange_rates()
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



roundeddolar, roundedeuro = get_exchange_rates()

anaform.mainloop()