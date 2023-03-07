# importam selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

# initializam chrome
chrome = webdriver.Chrome()

# maximizam fereastra
chrome.maximize_window()

# navigam catre un url
chrome.get('https://www.mega-image.ro/')

# cu sleep putem pune pauza de cateva secunde sa asteptam sa vedem si noi ceva
sleep(3)

# dam click pe butonul de accept cookies
chrome.find_element(By.XPATH, '//button[@data-testid="cookie-popup-accept"]').click()
sleep(3)

# dam click pe butonul 'Contul meu'
chrome.find_element(By.XPATH, '//button[@data-testid="header-myhub-toggle"]').click()
sleep(3)

# completam email invalid
chrome.find_element(By.ID, 'emailOrPhoneNumber').send_keys('abc123')
sleep(3)

# dam click pe 'Continua'
chrome.find_element(By.XPATH, '//button[@data-testid="submit-button"]').click()
sleep(3)

# salvam textul din eroare
error = chrome.find_element(By.XPATH, '//p[@data-testid="form-error-message"]').text
sleep(3)

# Verificam sa fie textul corect
assert error == 'Te rugam sa introduci un format valid'

# inchidem chrome
chrome.quit()

# daca a trecut testul, printam in consola un mesaj de succes
print('SUCCESS - TEST PASSED')