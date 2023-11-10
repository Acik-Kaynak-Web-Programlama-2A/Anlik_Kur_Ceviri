from tkinter import *
from tkinter import ttk
from bs4 import BeautifulSoup
import requests

dolarUrl = "https://www.google.com/finance/quote/USD-TRY?hl=tr"
requestURLDolar = requests.get(dolarUrl)

euroUrl = "https://www.google.com/finance/quote/EUR-TRY?hl=tr"
requestURLEuro = requests.get(euroUrl)

def getExchangeData():
    webDolarPage = BeautifulSoup(requestURLDolar.content, "html.parser")
    valueDolar = float(webDolarPage.find("div", class_="YMlKec fxKbKc").getText().replace(",","."))
    
    webEuroPage = BeautifulSoup(requestURLEuro.content, "html.parser")
    valueEuro = float(webEuroPage.find("div", class_="YMlKec fxKbKc").getText().replace(",","."))
    
    return valueDolar, valueEuro
    
def calculateExchange():
    try:
        inputValue = float(input_widget.get())
        exchangeValue1 = cmbx_ex1_widget.get()
        exchangeValue2 = cmbx_ex2_widget.get()
        
        if exchangeValue1 == "USD":
            exchange = valueDolar
        elif exchangeValue1 == "EURO":
            exchange = valueEuro
        elif exchangeValue1 == "TL":
            exchange = 1
        else:
            exchange = 0
        
        
        if exchangeValue2 == "USD":
            exchange2 = valueDolar
        elif exchangeValue2 == "EURO":
            exchange2 = valueEuro
        elif exchangeValue2 == "TL":
            exchange2 = 1
        else:
            exchange2 = 0
            
        value = (inputValue * exchange) / exchange2
            
        labelValue_widget.config(text=f"{inputValue} {exchangeValue1} = {value:.2f} {exchangeValue2}")
    except ValueError:
        labelValue_widget.config(text="Geçersiz Değer!!")
    updateExchange()
    

def updateExchange():
    global valueDolar, valueEuro
    valueDolar, valueEuro = getExchangeData()
    
def clearAll():
    labelValue_widget.config(text="....")
    input_widget.delete(0, END)
    
mainView = Tk()

mainView.title("Kur Hesapla")
mainView.geometry("400x400")

label1_widget = Label(
    mainView,
    fg="black",
    font="Nunito 10 bold"
   )
label1_widget.grid(row=0,column=1,padx=10,pady=10)

input_widget = ttk.Entry(mainView)
input_widget.grid(row=0, column=2,pady=10)


label2_widget = Label(
      mainView,
      fg="black",
      font="Nunito 10 bold"
    )
label2_widget.grid(row=1,column=1,padx=10,pady=10)

cmbx_ex1_widget = ttk.Combobox(mainView)
cmbx_ex1_widget.grid(row=1,column=2,pady=10,padx=10)

label3_widget = Label(
      mainView,
      fg="black",
      font="Nunito 10 bold"
    )
label3_widget.grid(row=2,column=1,padx=10,pady=10)

cmbx_ex2_widget = ttk.Combobox(mainView)
cmbx_ex2_widget.grid(row=2,column=2,padx=10,pady=10)

label4_widget = Label(
      mainView,
      fg="red",
      font="Nunito 10 bold"
    )
label4_widget.grid(row=3,column=1,padx=10,pady=10)

labelValue_widget = Label(
    mainView,
    fg="red",
    font="Nunito 10 bold"
   )
labelValue_widget.grid(row=3, column=2,padx=10,pady=10)

btn_widget = ttk.Button(
    mainView,
    width=25,
    command=calculateExchange
   )
btn_widget.grid(row=4, column=2,padx=10,pady=10)

btnclear_widget = ttk.Button(
    mainView,
    width=25,
    command=clearAll
   )
btnclear_widget.grid(row=5,column=2,padx=10,pady=10)

# combobox values list
cmbx_ex1_widget['values'] = ["USD", "EURO", "TL"]
cmbx_ex2_widget['values'] = ["USD", "EURO", "TL"]

# texts
label1_widget['text'] = "Para Girişi: *"
label2_widget['text'] = "Girişi Yapılan Para: *"
label3_widget['text'] = "2. Para Tipi: *"
label4_widget['text'] = "Kur Sonucu: "
btn_widget['text'] = "Hesapla"
btnclear_widget['text'] = "Temizle"


valueDolar, valueEuro = getExchangeData()

mainView.mainloop()
