import requests
from tkinter import *
from tkinter import ttk
from bs4 import BeautifulSoup

class CurrencyConverter:
    def __init__(anlıkkur, master):
        anlıkkur.master = master
        anlıkkur.master.title("Anlık Kur Hesapla")
        anlıkkur.master.geometry("400x200")
        
        anlıkkur.master.configure(bg='Deep Sky Blue')


        anlıkkur.lbl_miktar = Label(master, text="Miktar:")
        anlıkkur.lbl_donusecekkur = ttk.Label(master, text="Para birimi seçiniz:")
        anlıkkur.lbl_istenenkur = ttk.Label(master, text="Dönüştürülmesini İstenen Kur:")
        anlıkkur.lbl_sonuc = ttk.Label(master, text="")
        
        anlıkkur.cmb_donusecekkur = ttk.Combobox(master, values=["USD", "EURO", "TL"])
        anlıkkur.cmb_istenenkur = ttk.Combobox(master, values=["USD", "EURO", "TL"])

        anlıkkur.btn_hesapla = ttk.Button(master, text="Hesapla", command=anlıkkur.hesapla)
        anlıkkur.btn_sifirla = ttk.Button(master, text="Sıfırla", command=anlıkkur.input_sifirla)

        anlıkkur.e_miktar_giris = ttk.Entry(master)
        
        anlıkkur.lbl_donusecekkur.grid(row=2, column=0, padx=5, pady=5)
        anlıkkur.cmb_donusecekkur.grid(row=2, column=1, padx=5, pady=5)
        
        anlıkkur.lbl_miktar.grid(row=0, column=0, padx=5, pady=5)
        anlıkkur.e_miktar_giris.grid(row=0, column=1, padx=5, pady=5)

        anlıkkur.lbl_istenenkur.grid(row=3, column=0, padx=5, pady=5)
        anlıkkur.cmb_istenenkur.grid(row=3, column=1, padx=5, pady=5)

        anlıkkur.btn_hesapla.grid(row=6, column=1, padx=5, pady=5)
        anlıkkur.btn_sifirla.grid(row=6, column=0, padx=5, pady=5)

        anlıkkur.lbl_sonuc.grid(row=5, column=0, columnspan=2, padx=5, pady=5)

        anlıkkur.roundeddolar, anlıkkur.roundedeuro = anlıkkur.get_doviz_kurlari()

    def get_doviz_kurlari(anlıkkur):
        url1 = "https://www.google.com/finance/quote/USD-TRY?hl=tr"
        sayfa1 = requests.get(url1)
        html_sayfa1 = BeautifulSoup(sayfa1.content, "html.parser")
        roundeddolar = float(html_sayfa1.find("div", class_="YMlKec fxKbKc").getText().replace(",", "."))

        url2 = "https://www.google.com/finance/quote/EUR-TRY?hl=tr"
        sayfa2 = requests.get(url2)
        html_sayfa2 = BeautifulSoup(sayfa2.content, "html.parser")
        roundedeuro = float(html_sayfa2.find("div", class_="YMlKec fxKbKc").getText().replace(",", "."))

        return roundeddolar, roundedeuro

    def hesapla(anlıkkur):
        try:
            miktar = float(anlıkkur.e_miktar_giris.get())
            donusecek_kur = anlıkkur.cmb_donusecekkur.get()
            istenen_kur = anlıkkur.cmb_istenenkur.get()

            if donusecek_kur == "TL":
                donusecek_kur_orani = 1
            elif donusecek_kur == "USD":
                donusecek_kur_orani = anlıkkur.roundeddolar
            elif donusecek_kur == "EURO":
                donusecek_kur_orani = anlıkkur.roundedeuro
            else:
                donusecek_kur_orani = 0

            if istenen_kur == "TL":
                istenen_kur_orani = 1
            elif istenen_kur == "USD":
                istenen_kur_orani = anlıkkur.roundeddolar
            elif istenen_kur == "EURO":
                istenen_kur_orani = anlıkkur.roundedeuro
            else:
                istenen_kur_orani = 0

            sonuc = (miktar * donusecek_kur_orani) / istenen_kur_orani

            anlıkkur.lbl_sonuc.config(text=f"Sonuç: {miktar} {donusecek_kur} = {sonuc:.2f} {istenen_kur}")
        except ValueError:
            anlıkkur.lbl_sonuc.config(text="Geçersiz miktar!")

    def input_sifirla(anlıkkur):
        anlıkkur.e_miktar_giris.delete(0, END)
        anlıkkur.lbl_sonuc.config(text="")

if __name__ == "__main__":
    root = Tk()
    app = CurrencyConverter(root)
    root.mainloop()
