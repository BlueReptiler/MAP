import pyautogui
import time
import keyboard
import urllib
import os
import webbrowser
import requests

x=((os.path.abspath(__file__).replace(os.path.basename(__file__),"")) + "Python") #x = path-ul fisierului "Python"
if not os.path.exists(x):
    os.mkdir(x) #Daca nu exista acest folder, il creem.
thisdir = os.getcwd()

path1 = x + r"\like1.png" #Setam path-ul de instalare al pozelor ce urmeaza cautate.
path2 = x + r"\like2.png" #


def Find_Browser(): #Cautam un browser din calculator, incercand sa deschidem browserul utilizat de persoana.
    force = False #Force este o variabila creeata pentru a forta scrierea linkului prin pyautogui.
    try:
        os.startfile('decentr.exe')
        force = True
    except: #Daca nu se gaseste browserul anterior mentionat trece prin exceptie la cautarea urmatorului browser.
        force = False
        try:
            os.startfile('brave.exe')
            force = True
        except:
            force = False
            try:
                os.startfile('opera.exe')
                force = True
            except:
                force = False
                try:
                    os.startfile('chrome.exe')
                    force = True
                except:
                    force = False
                    try:
                        os.startfile('msedge.exe')
                        force = True
                    except: #Daca niciun browser din lista nu este gasit, atunci se va deschide browserul predefinit din calculator.
                        force = False #Setam force in fals deoarece comanda de mai jos poate deschide in mod direct un link.
                        webbrowser.open("https://www.facebook.com/tnl.bacau")

    if(force == True): #Daca este gasit un browser din lista, se forteaza o deschidere a site ului prestabilit.
        time.sleep(1)
        pyautogui.hotkey("alt", "d")
        time.sleep(0.2)
        pyautogui.typewrite("https://www.facebook.com/tnl.bacau")
        pyautogui.press('enter')



def Download(): #Instalam pozele referinta de pe tumblr, adica de unde le-am uploadat.
    img_url = 'https://64.media.tumblr.com/63e1fe5bbda4c2144fd61b79b3f332e8/58f50439d66a2fda-c7/s250x400/ad30e8bb92d6df907248ab36a4228308ff009ab3.pnj'
    urllib.request.urlretrieve(img_url, path1) #Preia poza de pe internet si o instaleaza in path ul setat mai sus, sub numele "like1.png".
    img_url = 'https://64.media.tumblr.com/95f669f82b6ce4935d62ae41f5bd8cb1/58f50439d66a2fda-4b/s250x400/6ee64789a9cbd347e61d10718a0a29046922cd81.pnj'
    urllib.request.urlretrieve(img_url, path2) # -,,- "like2.png".


def Like(): #Cat timp nu se apasa butonul "Escape", cautam progresiv pe ecran cele 2 imagini de referinta.
    while not keyboard.is_pressed("Esc"):
        try:
            pyautogui.scroll(-300)
        except:
            pass
        if pyautogui.locateOnScreen(path1,confidence=0.7) != None:
            like = pyautogui.locateOnScreen(path1,confidence=0.7)
            pyautogui.click(like)
        elif pyautogui.locateOnScreen(path2,confidence=0.7) != None:
            like = pyautogui.locateOnScreen(path2,confidence=0.7)
            pyautogui.click(like)

#1
Find_Browser()
#2
Download()
#3
Like()