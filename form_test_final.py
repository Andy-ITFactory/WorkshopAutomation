# avem nevoie sa importam cateva librarii gratuite care ne ajuta sa controlam chrome
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

# initializam chrome
chrome = webdriver.Chrome()

# navigam catre un url
chrome.get("https://demoqa.com/automation-practice-form")

# cu sleep putem pune pauza de cateva secunde sa asteptam sa vedem si noi ceva
sleep(1)

'''
exercitiu - maximizam fereastra
toate comenzile incep cu chrome. si sunt intuitive
scrie mai jos chrome. si gandeste-te care ar putea fi comanda corecta
'''
chrome.maximize_window()

# gasim first name dupa ID si scriem valori in formular
chrome.find_element(By.ID, "firstName").send_keys("Andy")
sleep(1)

# exercitiu: completam impreuna last name apoi punem un sleep
chrome.find_element(By.ID, "lastName").send_keys("Sinpetrean")
sleep(1)

# exercitiu: completeaza singur email
chrome.find_element(By.ID, "userEmail").send_keys("email@email.com")
sleep(1)

# selectam gender
element = chrome.find_element(By.ID, "gender-radio-1")
chrome.execute_script("arguments[0].click();", element)
sleep(1)

# completam tel
chrome.find_element(By.ID, "userNumber").send_keys("0123456789")
sleep(1)

# dam click pe submit
element = chrome.find_element(By.ID, "submit")
chrome.execute_script("arguments[0].click();", element)
sleep(1)

# inchidem popup
element = chrome.find_element(By.ID, "closeLargeModal")
chrome.execute_script("arguments[0].click();", element)
sleep(1)

# inchidem chrome
chrome.quit()

# daca a trecut testul, printam in consola un mesaj de succes
print("SUCCESS - TEST PASSED")

'''
exercitiu final:
stergem toate comenzile de sleep pentru a vedea viteza testului in timp real
aceasta EFICIENTA ofera o valoare ENORMA si PERMANENTA angajatorilor
costul acestui test tinde spre 0, o data ce a fost scris
asa ca ei vor plati FOARTE BINE o data, ca sa primeasca si sa ramana cu aceasta valoare care ulterior, tinde spre ∞
'''
