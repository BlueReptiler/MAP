from tkinter import *
import tkinter.ttk as tsk
import requests
import json

window = Tk()
window.title("Monetary Converter")
window.configure(background="#001016")
#window.geometry("350x350")
window.title("Convertor Valutar")
tsk.Style().configure("combobox.TLabel", background='#001016', foreground='#ECB365', arrowcolor='#ECB365',bd=1, bordercolor='#ECB365')

frame1 = Frame(window,background='#001016',bd=1, bg='#ecb365')
frame1.pack(pady=20)
#height = numarul de elemente care pot fi afisate simultan cand se deschide lista pentru selectie
#width = numarul maxim de caractere al fiecarei optiuni
#justify = "center" -> seteaza pozitia textului pe mijlocul obiectului
combo = tsk.Combobox(frame1,cursor="hand2",justify="center",style="combobox.TLabel",font=("Arial_Black", 12, "bold"),height=10,width=31, values=["AED", "AFN", "ALL", "AMD", "ANG", "AOA", "ARS", "AUD", "AWG", "AZN", "BAM", "BBD", "BDT", "BGN", "BHD", "BIF", "BMD", "BND", "BOB", "BRL", "BSD", "BTC", "BTN", "BWP", "BYN", "BZD", "CAD", "CDF", "CHF", "CLF", "CLP", "CNH", "CNY", "COP", "CRC", "CUC", "CUP", "CVE", "CZK", "DJF", "DKK", "DOP", "DZD", "EGP", "ERN", "ETB", "EUR", "FJD", "FKP", "GBP", "GEL", "GGP", "GHS", "GIP", "GMD", "GNF", "GTQ", "GYD", "HKD", "HNL", "HRK", "HTG", "HUF", "IDR", "ILS", "IMP", "INR", "IQD", "IRR", "ISK", "JEP", "JMD", "JOD", "JPY", "KES", "KGS", "KHR", "KMF", "KPW", "KRW", "KWD", "KYD", "KZT", "LAK", "LBP", "LKR", "LRD", "LSL", "LYD", "MAD", "MDL", "MGA", "MKD", "MMK", "MNT", "MOP", "MRO", "MUR", "MVR", "MWK", "MXN", "MYR", "MZN", "NAD", "NGN", "NIO", "NOK", "NPR", "NZD", "OMR", "PAB", "PEN", "PGK", "PHP", "PKR", "PLN", "PYG", "QAR", "RON", "RSD", "RUB", "RWF", "SAR", "SBD", "SCR", "SDG", "SEK", "SGD", "SHP", "SLL", "SOS", "SRD", "SSP", "STD", "SVC", "SYP", "SZL", "THB", "TJS", "TMT", "TND", "TOP", "TRY", "TTD", "TWD", "TZS", "UAH", "UGX", "USD", "UYU", "UZS", "VEF", "VND", "VUV", "WST", "XAF", "XAG", "XAU", "XCD", "XDR", "XOF", "XPD", "XPF", "XPT","YEN","YUAN", "YER", "ZAR", "ZMK", "ZMW", "ZWL"])
combo.pack()

entry = tsk.Entry(frame1,justify="center",style="combobox.TLabel",font=("Arial_Black", 14), textvariable="value",width=25)
entry.pack()

frame2 = Frame(window,background='#001016',bd=1, bg='#ecb365')
frame2.pack()

combo2 = tsk.Combobox(frame2,cursor="hand2",justify="center",style="combobox.TLabel",font=("Arial_Black", 12,"bold"),height=10,width=31, values=["AED", "AFN", "ALL", "AMD", "ANG", "AOA", "ARS", "AUD", "AWG", "AZN", "BAM", "BBD", "BDT", "BGN", "BHD", "BIF", "BMD", "BND", "BOB", "BRL", "BSD", "BTC", "BTN", "BWP", "BYN", "BZD", "CAD", "CDF", "CHF", "CLF", "CLP", "CNH", "CNY", "COP", "CRC", "CUC", "CUP", "CVE", "CZK", "DJF", "DKK", "DOP", "DZD", "EGP", "ERN", "ETB", "EUR", "FJD", "FKP", "GBP", "GEL", "GGP", "GHS", "GIP", "GMD", "GNF", "GTQ", "GYD", "HKD", "HNL", "HRK", "HTG", "HUF", "IDR", "ILS", "IMP", "INR", "IQD", "IRR", "ISK", "JEP", "JMD", "JOD", "JPY", "KES", "KGS", "KHR", "KMF", "KPW", "KRW", "KWD", "KYD", "KZT", "LAK", "LBP", "LKR", "LRD", "LSL", "LYD", "MAD", "MDL", "MGA", "MKD", "MMK", "MNT", "MOP", "MRO", "MUR", "MVR", "MWK", "MXN", "MYR", "MZN", "NAD", "NGN", "NIO", "NOK", "NPR", "NZD", "OMR", "PAB", "PEN", "PGK", "PHP", "PKR", "PLN", "PYG", "QAR", "RON", "RSD", "RUB", "RWF", "SAR", "SBD", "SCR", "SDG", "SEK", "SGD", "SHP", "SLL", "SOS", "SRD", "SSP", "STD", "SVC", "SYP", "SZL", "THB", "TJS", "TMT", "TND", "TOP", "TRY", "TTD", "TWD", "TZS", "UAH", "UGX", "USD", "UYU", "UZS", "VEF", "VND", "VUV", "WST", "XAF", "XAG", "XAU", "XCD", "XDR", "XOF", "XPD", "XPF", "XPT","YEN","YUAN", "YER", "ZAR", "ZMK", "ZMW", "ZWL"])
combo2.pack()

#state = readonly -> face acest entry sa poata fi doar citit de utilizator
entry_result = tsk.Entry(frame2,justify="center",style="combobox.TLabel",font=("Arial_Black", 14), textvariable="result_value",width=25,state="readonly")
entry_result.setvar("result_value","0.95")
entry_result.pack()

combo.set("USD")
combo2.set("EUR")
entry.insert(0, "1")

def convert():
    url = "https://api.apilayer.com/exchangerates_data/convert?to="+tsk.Combobox.get(combo2).__str__()+"&from="+tsk.Combobox.get(combo).__str__()+"&amount="+entry.get()
    payload = {}
    headers= {
    "apikey": "opSKicXaO1S3Wec888I9SkIVGGKZQDgl"
    }
    response = requests.request("GET", url, headers=headers, data = payload)
    status_code = response.status_code
    data = json.loads(response.text) #incarca raspunsul text in json
    result = data["result"] #extrage din fisierul json valoarea din dreptul textului "result" (rezultatul calculului automat)
    entry_result.setvar("result_value",result) #setam rezultatul din dreptul "result" in entry_result din tkinter

button1 = Button(window,font=("Arial_Black", 14), text="Convert", fg="#001016", bg="#ecb365", command=convert)
button1.pack(pady=20)

window.mainloop()