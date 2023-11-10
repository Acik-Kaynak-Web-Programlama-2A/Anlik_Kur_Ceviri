# -*- coding: utf-8 -*-
"""
Created on Fri Nov 10 09:56:19 2023

@author: C-117
"""

from tkinter import *
from tkinter import ttk
import requests

API_KEY = '3850c4deef802a82010ca7ed'
BASE_URL = 'https://open.er-api.com/v6/latest/'

def doviz_kurlarini_cek():
    try:
        # API'den döviz kurlarını al
        response_try = requests.get(BASE_URL + 'TRY')
        response_usd = requests.get(BASE_URL + 'USD')
        response_eur = requests.get(BASE_URL + 'EUR')

        # JSON verilerini çözümle (veriyapısına dönüştür.)
        data_try = response_try.json()
        data_usd = response_usd.json()
        data_eur = response_eur.json()

        # TRY, USD ve EUR kurlarını al
        roundedtry = 1 / data_try['rates']['TRY']
        roundeddolar = 1 / data_usd['rates']['TRY']
        roundedeuro = 1 / data_eur['rates']['TRY']

        return roundedtry, roundeddolar, roundedeuro

    except requests.RequestException as e:
        print(f"Kur hesaplamalarını hesaplarken hata oluştu: {e}")
        return 0, 0, 0

def hesapla(*args):
    try:
        # Girdi al
        miktar = float(e_miktar_giris.get())
        giris_kur = cmb_giriskur.get()
        cikis_kur = cmb_cikiskur.get()

        # Hesaplamadan önce döviz kurlarını güncelle
        global roundedtry, roundeddolar, roundedeuro
        roundedtry, roundeddolar, roundedeuro = doviz_kurlarini_cek()

        # Giriş ve çıkış kurlarını belirle
        if giris_kur == "TRY":
            giris_kur_degeri = roundedtry
        elif giris_kur == "USD":
            giris_kur_degeri = roundeddolar
        elif giris_kur == "EURO":
            giris_kur_degeri = roundedeuro
        else:
            giris_kur_degeri = 0

        if cikis_kur == "TRY":
            cikis_kur_degeri = roundedtry
        elif cikis_kur == "USD":
            cikis_kur_degeri = roundeddolar
        elif cikis_kur == "EURO":
            cikis_kur_degeri = roundedeuro
        else:
            cikis_kur_degeri = 0

        # Kuru Hesapla ve yazdır
        sonuc = miktar * (cikis_kur_degeri / giris_kur_degeri)
        lbl_sonuc.config(text=f"Girilen Miktar: {miktar} {giris_kur}, karşılığı {sonuc:.2f} {cikis_kur}")
    except ValueError:
        lbl_sonuc.config(text="Geçersiz miktar!")

def otomatik_döviz_kurlarını_güncelle():
    # Döviz kurlarını otomatik olarak güncelle
    global roundedtry, roundeddolar, roundedeuro
    roundedtry, roundeddolar, roundedeuro = doviz_kurlarini_cek()

    # Her 60000 milisaniye (1 dakika) sonra tekrar et
    anaform.after(60000, otomatik_döviz_kurlarını_güncelle)

# Ana form oluştur
anaform = Tk()
anaform.title("Kur Hesapla")
anaform.geometry("300x200")

# Arayüz elemanlarını oluştur
lbl_miktar = Label(anaform, text="Miktarı Yazınız:")
e_miktar_giris = ttk.Entry(anaform)

lbl_giriskur = ttk.Label(anaform, text="Giriş Kur:")
cmb_giriskur = ttk.Combobox(anaform, values=["TRY", "USD", "EURO"])

lbl_cikiskur = ttk.Label(anaform, text="Çıkış Kur:")
cmb_cikiskur = ttk.Combobox(anaform, values=["TRY", "USD", "EURO"])

lbl_sonuc = ttk.Label(anaform, text="Sonuç:")

# Elemanları grid'e yerleştir
lbl_miktar.grid(row=0, column=0, padx=10, pady=10)
e_miktar_giris.grid(row=0, column=1, padx=10, pady=10)

lbl_giriskur.grid(row=1, column=0, pady=10)
cmb_giriskur.grid(row=1, column=1, pady=10)

lbl_cikiskur.grid(row=2, column=0, pady=10)
cmb_cikiskur.grid(row=2, column=1, pady=10)

lbl_sonuc.grid(row=3, column=0, columnspan=2, pady=10)

# Kurları ilk defa güncelle
roundedtry, roundeddolar, roundedeuro = doviz_kurlarini_cek()

# Otomatik döviz kuru güncellemeyi başlat
otomatik_döviz_kurlarını_güncelle()

# Her değer değiştiğinde hesapla fonksiyonunu çağır
e_miktar_giris.bind("<KeyRelease>", hesapla)
cmb_giriskur.bind("<<ComboboxSelected>>", hesapla)
cmb_cikiskur.bind("<<ComboboxSelected>>", hesapla)

# Main loop'u başlat
anaform.mainloop()
