from smtpd import SMTPServer
import requests
from bs4 import BeautifulSoup
import smtplib
from apscheduler.schedulers.blocking import BlockingScheduler
from hashlib import new

message = 'Buna ziua'
sender='data_scraping@coneasorin.ro'
subject='pretul a scazut la:'
to_addr_list=['stefanelbanu@gmail.com']
cc_addr_list=['data_scraping@coneasorin.ro']

def sendmail(sender,message,subject,to_addr_list,cc_addr_list=[]):
    try:
        smtpserver='mail.x-it.ro'
        header='From: %s/n'%sender
        header+='To: %s/n'%','.join(to_addr_list)
        header+='Cc: %s/n'%','.join(cc_addr_list)
        header+='Subject: %s/n/n'%subject
        message=header + message

        server=smtplib.SMTP(smtpserver,26)
        server.starttls()
        server.login(sender, "stiinte217_2022")
        problems=server.sendmail(sender,to_addr_list,message)
        server.quit()
        print("True")
        return True
    except:
        print("False")
        return False

def data_scraping():
    req=requests.get("https://www.emag.ro/telefon-mobil-apple-iphone-14-pro-max-128gb-5g-deep-purple-mq9t3rx-a/pd/DXDY4LMBM/?cmpid=99160&gclid=CjwKCAjw7p6aBhBiEiwA83fGutQEzd8jTFRrgGNgq-64rJSekVI_-HBUv2ljRnybUWvX7Ny_Rzh68hoClScQAvD_BwE")
    soup=BeautifulSoup(req.text,"html.parser")
    price=soup.find('p', attrs={'class': 'product-new-price'}).text
    new_price=price[0:5]
    new_price=new_price.replace(".","")
    print(new_price)
    sendmail(sender,message,subject,to_addr_list,cc_addr_list)

def trimitere_email ():
    server = smtplib.SMTP('mail.x-it.ro', 26)
    server.starttls()
    server.login("data_scraping@coneasorin.ro","stiinte217_2022")
    server.sendmail("data_scraping@coneasorin.ro","stefanelbanu@gmail.com","Subject: AVEM O MODIFICARE DA PRET")
    print("Emailul a fost trimis cu succes")
    server.quit

data_scraping()
#trimitere_email()
#send_simple_message()