# importam selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

# deschidem chrome
chrome = webdriver.Chrome()

# cu sleep putem pune pauza de cateva secunde sa asteptam sa vedem si noi ceva
sleep(3)

# maximizam fereastra
chrome.maximize_window()
sleep(3)

# navigam catre un url (mega image home page)
chrome.get('https://www.mega-image.ro/')
sleep(3)

# dam click pe Accept cookies
chrome.find_element(By.XPATH, '//*[@data-testid="cookie-popup-accept"]').click()
sleep(3)

# dam click pe Contul meu
chrome.find_element(By.XPATH, '//*[@data-testid="header-myhub-toggle"]').click()
sleep(3)

# dam click pe Continua
chrome.find_element(By.XPATH, '//*[@data-testid="submit-button"]').click()
sleep(3)

# verificam mesajul de eroare "Te rugam sa introduci adresa de e-mail sau numarul de telefon"
assert chrome.find_element(By.XPATH, '//*[@data-testid="form-error-message"]').text == "Te rugam sa introduci adresa de e-mail sau numarul de telefon"

# inchidem chrome
chrome.quit()

# daca a trecut testul, printam in consola un mesaj de succes
print('SUCCESS - TEST PASSED')
