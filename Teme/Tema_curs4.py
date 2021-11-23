import selenium.common.exceptions
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd
import time

header_flag = True
s = Service(ChromeDriverManager().install())
browser = webdriver.Chrome(service=s)
header = []
dictionary = {}
for i in range(13, 20): #parcurgerea linkurilor din data de 13 ianuarie pana pe 19 ianuarie
    browser.get("https://www.mai.gov.ro/informare-covid-19-grupul-de-comunicare-strategica-"+str(i)+"-ianuarie-ora-13-00/")
    try: #verificam daca linkul are tabelul cu datele care trebuie extrase, daca nu trecem la urmatorul link
        link = "/html/body/div[3]/div/div[1]/main/article/div/div/table[1]/tbody/tr[1]/td[1]"
        a = browser.find_element(By.XPATH, link).text
    except selenium.common.exceptions.NoSuchElementException:
        print("Linkul " + browser.current_url + "nu are informatii utile!")
        continue
    if not header: #initializarea header-ului daca acesta nu contine date
        for i in range(5):
            link = "/html/body/div[3]/div/div[1]/main/article/div/div/table[1]/tbody/tr[1]/td["+str(i+1)+"]"
            header.append(browser.find_element(By.XPATH, link).text)
    if not dictionary: #initializarea dictionarului daca acesta nu contine date
        dictionary = {i : [] for i in header}
    for j in range(0, 43): #parcurgerea tabelului pe randuri
        for i in range(0, len(header)): #pe coloane si punerea datelor in key-ul corespunzator
            link = "/html/body/div[3]/div/div[1]/main/article/div/div/table[1]/tbody/tr["+str(j+2)+"]/td["+str(i+1)+"]"
            dictionary[header[int(i)]].append(browser.find_element(By.XPATH, link).text)
    #punerea datelor de pe ultimul rand din tabel in dictionar
    dictionary[header[int(0)]].append(browser.find_element(By.XPATH, "/html/body/div[3]/div/div[1]/main/article/div/div/table[1]/tbody/tr[45]/td[1]").text)
    dictionary[header[int(1)]].append("")
    dictionary[header[int(2)]].append(browser.find_element(By.XPATH, "/html/body/div[3]/div/div[1]/main/article/div/div/table[1]/tbody/tr[45]/td[2]").text)
    dictionary[header[int(3)]].append(browser.find_element(By.XPATH, "/html/body/div[3]/div/div[1]/main/article/div/div/table[1]/tbody/tr[45]/td[3]").text)
    dictionary[header[int(4)]].append("")

df = pd.DataFrame(dictionary, columns=header)
df.to_csv("DateMAI.csv", columns=header)
time.sleep(10)
