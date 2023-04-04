# avem nevoie sa importam cateva librarii gratuite care ne ajuta sa controlam chrome
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

# initializam chrome
chrome = webdriver.Chrome()

# navigam catre un url
chrome.get('https://formy-project.herokuapp.com/form')

# cu sleep putem pune pauza de cateva secunde sa asteptam sa vedem si noi ceva
sleep(3)

# exercitiu - maximizam fereastra
# toate comenzile incep cu chrome. si sunt intuitive
# scrie mai jos chrome. si gandeste-te care ar putea fi comanda corecta


# gasim first name dupa ID si scriem valori in formular
chrome.find_element(By.ID, 'first-name').send_keys("Andy")
sleep(3)

# exercitiu: completam impreuna nume apoi punem un sleep de 3 secunde


# exercitiu: completeaza singur job title
# nu uitam de sleep


# exercitiu: select education - nu mai folosim .send_keys() la final. ce metoda crezi ca ar merge aici?
# nu uitam de sleep


# exercitiu: select gender
# nu uitam de sleep


# exercitiu: dam click pe submit apoi punem un sleep de 3 secunde
# vom invata ce sa facem cand elementul nu are ID


# inchidem chrome
chrome.quit()

# daca a trecut testul, printam in consola un mesaj de succes
print('SUCCESS - TEST PASSED')

# exercitiu final:
# stergem toate comenzile de sleep pentru a vedea viteza testului in timp real
# aceasta EFICIENTA ofera o valoare ENORMA si PERMANENTA angajatorilor
# costul acestui test tinde spre 0, o data ce a fost scris
# asa ca ei vor plati FOARTE BINE o data, ca sa primeasca si sa ramana cu aceasta valoare care ulterior, tinde spre ∞
