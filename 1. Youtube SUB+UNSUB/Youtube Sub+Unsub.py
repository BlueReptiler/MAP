import pyautogui
import time
import keyboard
import os

import tkinter.filedialog                           #
from tkinter import Tk                              #
                                                    # Deschide browserul preferat
tkinter.Tk().withdraw()                             #
browser = tkinter.filedialog.askopenfilename()      #

def cautare_google():
    pyautogui.hotkey("alt", "d")
    pyautogui.write("https://youtube.com")
    pyautogui.press("enter")

def cautare_youtube():
    if pyautogui.locateOnScreen(r"C:\Users\stefa\Desktop\Python\YTS.png", confidence=0.7)!= None:
        x = pyautogui.locateOnScreen(r"C:\Users\stefa\Desktop\Python\YTS.png",confidence=0.7)
        pyautogui.click(x)
        pyautogui.write("coconut song")
        pyautogui.press("enter")

    else:
        print("Imaginea nu este pe ecran")

def cautare_melodie():
    if pyautogui.locateOnScreen(r"C:\Users\stefa\Desktop\Python\coconut.png", confidence=0.7)!= None:
        x = pyautogui.locateOnScreen(r"C:\Users\stefa\Desktop\Python\coconut.png",confidence=0.7)
        pyautogui.click(x)

    else:
        print("Imaginea nu este pe ecran")

def cautare_buton():
    if pyautogui.locateOnScreen(r"C:\Users\stefa\Desktop\Python\SUBS.png", confidence=0.7)!= None:
        x = pyautogui.locateOnScreen(r"C:\Users\stefa\Desktop\Python\SUBS.png",confidence=0.7)
        pyautogui.click(x)

    else:
        print("Imaginea nu este pe ecran")

def cautare_buton_unsub():
    if pyautogui.locateOnScreen(r"C:\Users\stefa\Desktop\Python\unsub.png", confidence=0.7)!= None:
        x = pyautogui.locateOnScreen(r"C:\Users\stefa\Desktop\Python\unsub.png",confidence=0.7)
        pyautogui.click(x)

    else:
        print("Imaginea nu este pe ecran")

def cautare_buton_unsub_sec():
    if pyautogui.locateOnScreen(r"C:\Users\stefa\Desktop\Python\unsub_sec.png", confidence=0.7)!= None:
        x = pyautogui.locateOnScreen(r"C:\Users\stefa\Desktop\Python\unsub_sec.png",confidence=0.7)
        pyautogui.click(x)

    else:
        print("Imaginea nu este pe ecran")


os.startfile(browser)
time.sleep(2)
cautare_google()
time.sleep(3)
cautare_youtube()
time.sleep(3)
cautare_melodie()
time.sleep(2)
cautare_buton()
time.sleep(5)
cautare_buton_unsub()
time.sleep(2)
cautare_buton_unsub_sec()
