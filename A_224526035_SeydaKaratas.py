import requests

from tkinter import *
from tkinter import ttk

from bs4 import BeautifulSoup

def get_doviz_kurlari():
    url1 = "https://www.google.com/finance/quote/USD-TRY?hl=tr"
    sayfa1 = requests.get(url1)
    html_sayfa1 = BeautifulSoup(sayfa1.content, "html.parser")
    roundeddolar = float(html_sayfa1.find("div", class_="YMlKec fxKbKc").getText().replace(",", "."))

    url2 = "https://www.google.com/finance/quote/EUR-TRY?hl=tr"
    sayfa2 = requests.get(url2)
    html_sayfa2 = BeautifulSoup(sayfa2.content, "html.parser")
    roundedeuro = float(html_sayfa2.find("div", class_="YMlKec fxKbKc").getText().replace(",", "."))

    return roundeddolar, roundedeuro

def hesapla():
    try:
        miktar = float(e_miktar_giris.get())
        donusecek_kur = cmb_donusecekkur.get()
        istenen_kur = cmb_istenenkur.get()

        if donusecek_kur == "TL":
            donusecek_kur_orani = 1
        elif donusecek_kur == "USD":
            donusecek_kur_orani = roundeddolar
        elif donusecek_kur == "EURO":
            donusecek_kur_orani = roundedeuro
        else:
            donusecek_kur_orani = 0

        if istenen_kur == "TL":
            istenen_kur_orani = 1
        elif istenen_kur == "USD":
            istenen_kur_orani = roundeddolar
        elif istenen_kur == "EURO":
            istenen_kur_orani = roundedeuro
        else:
            istenen_kur_orani = 0

        sonuc = (miktar * donusecek_kur_orani) / istenen_kur_orani

        lbl_sonuc.config(text=f"Sonuç: {miktar} {donusecek_kur} = {sonuc:.2f} {istenen_kur}")
    except ValueError:
        lbl_sonuc.config(text="Geçersiz miktar!")

def inputSifirla():
    e_miktar_giris.delete(0, END)
    lbl_hesapsonuc.config(text="")
    
anaform = Tk()

anaform.title("Kur Hesapla")
anaform.geometry("300x300")

lbl_miktar = ttk.Label(anaform,
                   text="Miktar:")
lbl_donusecekkur = ttk.Label(anaform,
                           text="Dönüştürülecek Kur:")
lbl_istenenkur = ttk.Label(anaform,
                               text="İstenen Kur:")
lbl_sonuc = ttk.Label(anaform,
                      text="")

cmb_donusecekkur = ttk.Combobox(anaform, 
                              values=["TL", "USD", "EURO"])
cmb_istenenkur = ttk.Combobox(anaform, 
                                  values=["TL", "USD", "EURO"])
btn_hesapla = ttk.Button(anaform, 
                         text="Hesapla", command=hesapla)
btn_sifirla = ttk.Button(anaform,
                     text="Sıfırla", command=inputSifirla)

e_miktar_giris = ttk.Entry(anaform)

lbl_miktar.grid(row=0, column=0, padx=5, pady=5)
e_miktar_giris.grid(row=0, column=1, padx=5, pady=5)

lbl_donusecekkur.grid(row=2, column=0, padx=5, pady=5)
cmb_donusecekkur.grid(row=2, column=1, padx=5, pady=5)

lbl_istenenkur.grid(row=3, column=0, padx=5, pady=5)
cmb_istenenkur.grid(row=3, column=1, padx=5, pady=5)

btn_hesapla.grid(row=6, column=0, padx=5, pady=5)

btn_sifirla.grid(row=6, column=1, padx=5, pady=5)

lbl_sonuc.grid(row=5, column=0, padx=5, pady=5)

roundeddolar, roundedeuro = get_doviz_kurlari()

anaform.mainloop()
