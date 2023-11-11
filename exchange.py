from currency_converter import CurrencyConverter 
import tkinter as tk 
from tkinter import ttk

c = CurrencyConverter()

window = tk.Tk()
window.geometry("500x400")
window.title("Currency Exchange")
window.bg = "Silver"

def cervir():
    amount = int(entry1.get())
    cur1 = entry2.get()
    cur2 = entry3.get()
    data = c.convert(amount,cur1,cur2)
    label4 = tk.Label(window,text=data,font="Times 20 bold").place(x = 140,y = 320)


label = tk.Label(window,text="Currency Exchange",font="Times 20 bold").place(x = 100, y=40)

label1 = tk.Label(window,text = "Tutar Buraya Girin: ", font = "Times 16 bold ").place(x=70 , y=100)
entry1 = tk.Entry(window) 

label2 = tk.Label(window,text = "Para Biriminizi Secin: ", font = "Times 16 bold ").place(x=30 , y=150)
entry2 = ttk.Combobox(window, values=["USD","TRY","GBP","EUR","NZD","AUD","CHF"]) 

label3 = tk.Label(window,text = "İstediğiniz Para Birimi: ", font = "Times 16 bold ").place(x=15 , y=200)
entry3 = ttk.Combobox(window, values=["USD","TRY","GBP","EUR","NZD","AUD","CHF"]) 
 
button = tk.Button(window,text="click", font="Times 16 bold", command=cervir).place(x = 220,y = 250)

entry1.place(x=270 , y = 105)
entry2.place(x= 270, y = 155)
entry3.place(x= 270,y = 205)

window.mainloop() 


"""

https://pypi.org/project/CurrencyConverter/
pip install CurrencyConverter

Yükleyeceğimiz Kütüphane

"""