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


def kurHesapla():
    try:
        miktar = float(e_miktar_giris.get())
        girilen_kur = cmb_girilenkur.get()
        kursec = cmb_kursec.get()

        if girilen_kur == "₺ TL":
            girilen_kur_orani = 1
        elif girilen_kur == "$ USD":
            girilen_kur_orani = roundeddolar
        elif girilen_kur == "€ EURO":
            girilen_kur_orani = roundedeuro
        else:
            girilen_kur_orani = 0
            
        if girilen_kur == "₺ TL":
            girilen_kur_orani = 1
        elif girilen_kur == "$ USD":
            girilen_kur_orani = roundeddolar
        elif girilen_kur == "€ EURO":
            girilen_kur_orani = roundedeuro
        else:
            girilen_kur_orani = 0    
        
        sonuc = (miktar * girilen_kur_orani) / girilen_kur_orani
    
        update_exchange_rates()
    
        lbl_hesapsonuc.config(text=f"Sonuç: {miktar} {girilen_kur} = {sonuc:.2f} {girilen_kur_orani}")
    except ValueError:
        lbl_sonuc.config(text="Geçersiz miktar!")
    
    

def update_exchange_rates():
    global roundeddolar, roundedeuro
    roundeddolar, roundedeuro = get_exchange_rates()
    lbl_hesapsonuc.config(text="Kur güncellendi.")
    
          

        
def inputTemizle():
    e_miktar_giris.delete(0, END)
    lbl_hesapsonuc.config(text="")

anaform = Tk()
anaform.title("Kur Hesapla")
anaform.geometry("600x600")

lbl_tlmiktar= Label(anaform, text="Miktar")
cmb_kursec = ttk.Combobox(anaform, values=["₺ TL", "$ USD", "€ EURO"])
cmb_girilenkur = ttk.Combobox(anaform, values=["₺ TL", "$ USD", "€ EURO"])
lbl_kurmiktar = Label(anaform, text="Çevirilecek Kur")
lbl_kursec = Label(anaform, text="Kur")


btn_bos = Button(anaform, text="Temzile", command=inputTemizle)
btn_hesapla = ttk.Button(anaform, text="Hesapla", command=kurHesapla)
lbl_sonuc = Label(anaform, text="Sonuç")
lbl_hesapsonuc = Label(anaform, text="")

e_miktar_giris = ttk.Entry(anaform)

    
    
"""
lbl_tlmiktar.pack()
cmb_kursec.pack()
btn_bos.pack()
btn_hesapla.pack()
"""

lbl_tlmiktar.grid(row=0, column=0, padx=5, pady=5)
e_miktar_giris.grid(row=0, column=1, padx=5, pady=5)
lbl_kursec.grid(row=0, column=2, padx=5, pady=5)
lbl_kurmiktar.grid(row=1, column=0, padx=5)
cmb_kursec.grid(row=1, column=1, padx=5, pady=5)
cmb_girilenkur.grid(row=0, column=3, padx=20, pady=5)
lbl_sonuc.grid(row=2, column=0, padx=5, pady=5)
lbl_hesapsonuc.grid(row=2, column=1, padx=5, pady=5)
btn_bos.grid(row=3, column=0, padx=5, pady=5)
btn_hesapla.grid(row=3, column=1, padx=5, pady=5)

roundeddolar, roundedeuro = get_exchange_rates()

anaform.mainloop()
