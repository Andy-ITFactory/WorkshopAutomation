# importam selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

# deschidem chrome
chrome = webdriver.Chrome()

# cu sleep putem pune pauza de cateva secunde sa asteptam sa vedem si noi ceva
sleep(3)

# maximizam fereastra (Aici incercati sa gasiti singuri comanda)

# navigam catre un url: 'https://demoqa.com/automation-practice-form' (Aici incercati sa gasiti singuri comanda)

# gasim un element dupa ID si trimitem date de la tastatura
# chrome.find_element(By.ID, 'firstName').send_keys('Andy')
