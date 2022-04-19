# avem nevoie sa importam cateva librarii gratuite care ne ajuta sa controlam chrome
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from time import sleep

# initializam chrome
s = Service(ChromeDriverManager().install())
chrome = webdriver.Chrome(service=s)

# maximizam fereastra
chrome.maximize_window()

# navigam catre un url
chrome.get('https://formy-project.herokuapp.com/form')

# cu sleep putem pune pauza de cateva secunde sa asteptam sa vedem si noi ceva
sleep(3)

# gasim first name dupa ID si scriem valori in formular
chrome.find_element(By.ID, 'first-name').send_keys("Andy")
sleep(3)

# vom completa la workshop last name si job title

# gasim butonul de Submit dupa textul de pe link si dam click pe el
chrome.find_element(By.LINK_TEXT, 'Submit').click()
sleep(3)

# gasim titlul si verificam mesajul
thank_you_msg = chrome.find_element(By.XPATH, '/html/body/div/h1').text
assert thank_you_msg == 'Thanks for submitting your form'

# verificati voi mesajul de mai jos "The form was successfully submitted!"

# daca a trecut testul, printam in consola un mesaj de succes
print('SUCCES - TEST PASSED')
