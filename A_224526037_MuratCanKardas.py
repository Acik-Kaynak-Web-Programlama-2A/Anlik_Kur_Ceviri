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

def hesapla_guncelle():
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

        sonuc = (miktar / girilen_kur_orani) * cevirilecek_kur_orani

        lbl_sonuc.config(text=f"Sonuç: {miktar} {girilen_kur} = {sonuc:.2f} {cevirilecek_kur}")
    except ValueError:
        lbl_sonuc.config(text="Geçersiz miktar!")

    update_exchange_rates()

def update_exchange_rates():
    global roundeddolar, roundedeuro
    roundeddolar, roundedeuro = get_exchange_rates()
    lbl_hesapsonuc.config(text="Kur güncellendi.", font="Britannic 18 bold italic")
    anaform.after(2000, lambda: lbl_hesapsonuc.config(text=""))  # 3000 milisaniye (3 saniye) sonra temizle

anaform = Tk()
anaform.title("Kur Hesapla")
anaform.geometry("400x600")

lbl_miktar = Label(anaform, text="Miktar:")
lbl_girilenkur = ttk.Label(anaform, text="Girilen Kur:")
lbl_cevirilecekkur = ttk.Label(anaform, text="Çevrilecek Kur:")
lbl_sonuc = ttk.Label(anaform, text="Sonuç:")
lbl_hesapsonuc = ttk.Label(anaform, text="")

cmb_girilenkur = ttk.Combobox(anaform, values=["TL", "USD", "EURO"])
cmb_cevirilecekkur = ttk.Combobox(anaform, values=["TL", "USD", "EURO"])
btn_hesapla_guncelle = ttk.Button(anaform, text="Hesapla ve Kur Güncelle", command=hesapla_guncelle)

e_miktar_giris = ttk.Entry(anaform)

lbl_miktar.grid(row=0, column=0)
e_miktar_giris.grid(row=0, column=1, padx=20)
lbl_girilenkur.grid(row=1, column=0, pady=5)
cmb_girilenkur.grid(row=1, column=1, padx=20, pady=5)
lbl_cevirilecekkur.grid(row=2, column=0, pady=5)
cmb_cevirilecekkur.grid(row=2, column=1, padx=20, pady=5)
btn_hesapla_guncelle.grid(row=5, column=1, padx=20, pady=20)
lbl_sonuc.grid(row=4, column=0, columnspan=2)
lbl_hesapsonuc.grid(row=3, column=0, columnspan=2)

roundeddolar, roundedeuro = get_exchange_rates()

anaform.mainloop()
