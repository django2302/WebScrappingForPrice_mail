# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import requests
from bs4 import BeautifulSoup
import smtplib

def main_function():
    
    URL = 'https://www.flipkart.com/realme-x-space-blue-128-gb/p/itmfgybqzcgbxs26?pid=MOBFGYBQKYA5Y7HG&lid=LSTMOBFGYBQKYA5Y7HGREW5GK&fm=neo%2Fmerchandising&iid=M_9d6b8954-a3d2-4ea5-a94f-bc9467a22a32_15.GEIZE4KI3G8U&ppt=hp&ppn=hp&ssid=jmd4xlcw800000001568239742920&otracker=hp_omu_Dual%2BCamera%2BPhone_2_7.dealCard.OMU_GEIZE4KI3G8U_5&otracker1=hp_omu_WHITELISTED_neo%2Fmerchandising_Dual%2BCamera%2BPhone_NA_dealCard_cc_2_NA_view-all_5&cid=GEIZE4KI3G8U'
    
    headers = {"User-Agent":'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36'}
    
    page = requests.get(URL,headers=headers)
    
    soup = BeautifulSoup(page.content, 'html.parser')
    
      
    
#    mydivs = soup.findAll("div", {"class": "_1vC4OE _3qQ9m1"})
#    
#    price = mydivs.get_text()
#    print(price)
    
    for el in soup.find_all('div', attrs={'class': '_1vC4OE _3qQ9m1'}):
        print (el.get_text())
        
#    
    
#    price = soup.find(id = "priceblock_dealprice").get_text()
#    
#    converted_price = float(price[1:5])
#    print(converted_price)
#    
#    if(converted_price < 100):
#        send_mail()
    

def send_mail():
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.ehlo()
    server.login('test.project2302@gmail.com','qbgnbnkcyyfnenhx')
    
    subject = 'price down!!!!'
    body = 'price down check link https://www.amazon.co.uk/Projector-Speaker-Support-Compatible-Tablets/dp/B07SDNXCMS?ref_=Oct_DLandingS_PC_4c26ae45_0&smid=A2PGPJL0BBLHLX'
    
    msg = f"Subject: {subject}\n\n{body}"
    
    server.sendmail('test.project2302@gmail.com','test.project2302@gmail.com',msg)
    
    print("email sent!!!")
    
    server.quit()
    
main_function()