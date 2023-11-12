# -*- coding: utf-8 -*-
"""
Created on Sun Nov 10 20:15:07 2023

@author: Tunahan
"""


from tkinter import *
from tkinter import ttk
import requests

API_ANAHTARI = '3850c4deef802a82010ca7ed'
ANA_URL = 'https://open.er-api.com/v6/latest/'




# Open Exchange Rates API'sinden güncel döviz kurlarını çeker
def doviz_kurlarini_cek(): 
    # her bir birimin TL karşılığı bu kod bloğu içinde hesaplanıyor. TL karşılığı üzerinden ise birbirleri ile karşılaştırılabiliyor.
    try:
        try_rate = 1 / requests.get(ANA_URL + 'TRY').json()['rates']['TRY']
        usd_rate = 1 / requests.get(ANA_URL + 'USD').json()['rates']['TRY']
        eur_rate = 1 / requests.get(ANA_URL + 'EUR').json()['rates']['TRY']
        return try_rate, usd_rate, eur_rate
    except requests.RequestException:
        return 0, 0, 0


def hesapla(*args):
    try:
        miktar = float(miktar_girisi.get())#float ondalık değer
        giris_kur, cikis_kur = giris_kur_combobox.get(), cikis_kur_combobox.get()
        giris_kuru_deger, cikis_kuru_deger = kur_degeri(giris_kur), kur_degeri(cikis_kur)

        sonuc = miktar * (cikis_kuru_deger / giris_kuru_deger)
        ciktinin_etiketi.config(text=f"Girilen Miktar: {miktar} {giris_kur}, karşılığı {sonuc:.2f} {cikis_kur}")

    except ValueError:
        ciktinin_etiketi.config(text="Lütfen geçerli miktar giriniz!")


def kur_degeri(kur): 
    if kur == "TRY":
        return try_rate
    elif kur == "USD":
        return usd_rate
    elif kur == "EURO":
        return eur_rate
    else:
        return 0

def otomatik_kurlari_guncelle(): #Değişkenlerin döviz kurlarını ilk kez çekiyor.
    global try_rate, usd_rate, eur_rate
    try_rate, usd_rate, eur_rate = doviz_kurlarini_cek()
    ana_pencere.after(60000, otomatik_kurlari_guncelle)

# Arayüzün genişliği ve yazıların özelliği
ana_pencere = Tk()
ana_pencere.title("Güncel Kur Hesap - Tunahan Bozkurt")
ana_pencere.geometry("340x200")

etiket_miktar = Label(ana_pencere, text="Miktar:", font=("Arial", 12), fg="red")
miktar_girisi = ttk.Entry(ana_pencere, font=("Arial", 12), width=15)

etiket_giris_kur = ttk.Label(ana_pencere, text="Bu birimden:", font=("Helvetica", 12), foreground="blue")
giris_kur_combobox = ttk.Combobox(ana_pencere, values=["TRY", "USD", "EURO"], font=("Helvetica", 12))

etiket_cikis_kur = ttk.Label(ana_pencere, text="Bu birime dönüştür:", font=("Helvetica", 12), foreground="blue")
cikis_kur_combobox = ttk.Combobox(ana_pencere, values=["TRY", "USD", "EURO"], font=("Helvetica", 12))

ciktinin_etiketi = ttk.Label(ana_pencere, text="Lütfen Para Miktarını Giriniz", font=("Arial", 12))


# Değerlerin yazacağı bölümlerin pozisyonu ve boyut ayarlamaları
etiket_miktar.grid(row=0, column=0, padx=10, pady=10)
miktar_girisi.grid(row=0, column=1, padx=10, pady=10)

etiket_giris_kur.grid(row=1, column=0, pady=10)
giris_kur_combobox.grid(row=1, column=1, pady=10)

etiket_cikis_kur.grid(row=2, column=0, pady=10)
cikis_kur_combobox.grid(row=2, column=1, pady=10)

ciktinin_etiketi.grid(row=3, column=0, columnspan=2, pady=10)

#Program başlangıcındaki döviz kurlarını alır ve değişkenlere atayıp anlık güncellemeyi yapar.
try_rate, usd_rate, eur_rate = doviz_kurlarini_cek()
otomatik_kurlari_guncelle()

#Hesapla butonu yerine her tuşa basılıp çekildiğinde hesaplama işini gerçekleştirir. 
miktar_girisi.bind("<KeyRelease>", hesapla)
giris_kur_combobox.bind("<<ComboboxSelected>>", hesapla)
cikis_kur_combobox.bind("<<ComboboxSelected>>", hesapla)



#Tüm kod satırını döngüye alır ve tek hesaplamadan sonra kodun durmasını engeller.
ana_pencere.mainloop()
