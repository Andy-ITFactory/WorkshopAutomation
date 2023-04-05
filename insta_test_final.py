# importam selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

# initializam chrome
chrome = webdriver.Chrome()

# maximizam fereastra
chrome.maximize_window()

# navigam catre un url
chrome.get('https://www.instagram.com/')

# cu sleep putem pune pauza de cateva secunde sa asteptam sa vedem si noi ceva
sleep(3)

# vrem sa dam click pe accept cookies
chrome.find_element(By.XPATH, '//button[text()="Only allow essential cookies"]').click()
sleep(3)

# dam click pe sign up
chrome.find_element(By.XPATH, '//span[text()="Sign up"]').click()
sleep(3)

# dam click pe log in
chrome.find_element(By.XPATH, '//a[text()="Log in"]').click()
sleep(3)

# completam user
chrome.find_element(By.NAME, 'username').send_keys('user123')
sleep(3)

# completam pass
chrome.find_element(By.NAME, 'password').send_keys('user123')
sleep(3)

# dam click pe log in
chrome.find_element(By.XPATH, '//div[text()="Log in"]').click()
sleep(3)

# salvam mesajul asteptat intr-o variabila
mesaj_asteptat = 'Sorry, your password was incorrect. Please double-check your password.'

# salvam mesajul primit din pagina
mesaj_primit = chrome.find_element(By.ID, 'slfErrorAlert').text

# comparam mesajele si verificam sa fie egale
assert mesaj_asteptat == mesaj_primit

# inchidem chrome
chrome.quit()

# daca a trecut testul, printam in consola un mesaj de succes
print('SUCCESS - TEST PASSED')
