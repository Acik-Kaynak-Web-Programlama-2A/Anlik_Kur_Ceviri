import tkinter as tk
from tkinter import ttk
import math

def sayi_tikla(sayi):
    ekran_entry.insert(tk.END, sayi)

def islem_tikla(operasyon):
    ekran_entry.insert(tk.END, operasyon)

def hesapla():
    try:
        if "^" in ekran_entry.get():
            sayi1, sayi2 = ekran_entry.get().split("^")
            sonuc = float(sayi1) ** float(sayi2)
        else:
            sonuc = eval(ekran_entry.get())
        ekran_entry.delete(0, tk.END)
        ekran_entry.insert(tk.END, sonuc)
    except:
        ekran_entry.delete(0, tk.END)
        ekran_entry.insert(tk.END, "Hata")

def karekok_al():
      sayi = float(ekran_entry.get())
      sonuc = math.sqrt(sayi)
      ekran_entry.delete(0, tk.END)
      ekran_entry.insert(0, sonuc)

def temizle():
    ekran_entry.delete(0, tk.END)

def bellek_artir():
    global bellek
    try:
        ekran_entry = str(float(bellek) + float(ekran.get()))
    except:
        bellek = "Hata"

def bellek_azalt():
    global bellek
    try:
       ekran_entry = str(float(bellek) - float(ekran.get()))
    except:
        bellek = "Hata"    

app = tk.Tk()
app.title("Hesap Makinesi")

ekran_entry = ttk.Entry(app, font=('Arial', 20))
ekran_entry.grid(row=0, column=0, columnspan=4)

butonlar = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    '0', '.', '^', '+'
]

row, col = 1, 0

for buton in butonlar:
    ttk.Button(app, text=buton, command=lambda b=buton: sayi_tikla(b) if b != '^' else islem_tikla(b)).grid(row=row, column=col)
    col += 1
    if col > 3:
        col = 0
        row += 1

ttk.Button(app, text="=", command=hesapla).grid(row=5, column=0, columnspan=4)
ttk.Button(app, text="C", command=temizle).grid(row=6, column=0, columnspan=4)
tk.Button(app, text="√", width=5, command=karekok_al).grid(row=5, column=0)
tk.Button(app, text="MC", width=5, command=temizle).grid(row=7, column=1, columnspan=2)
tk.Button(app, text="M+", width=5, command=bellek_artir).grid(row=8, column=1, columnspan=2)
tk.Button(app, text="M-", width=5, command=bellek_azalt).grid(row=9, column=1, columnspan=2)
app.mainloop()