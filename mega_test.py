# importam selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

# deschidem chrome
chrome = webdriver.Chrome()

# cu sleep putem pune pauza de cateva secunde sa asteptam sa vedem si noi ceva
sleep(3)

# maximizam fereastra

# navigam catre un url (mega image home page)

# dam click pe Accept cookies
# chrome.find_element(By.XPATH, '//*[@data-testid="de_gasit_si_completat_id_corect"]').click()

# dam click pe Contul meu

# dam click pe Continua

# verificam mesajul de eroare "Te rugam sa introduci adresa de e-mail sau numarul de telefon"

# inchidem chrome
chrome.quit()

# daca a trecut testul, printam in consola un mesaj de succes
print('SUCCESS - TEST PASSED')
