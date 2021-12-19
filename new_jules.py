from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from time import sleep

# initializam chrome
options = Options()
options.add_argument("start-maximized")
chrome = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

# navigam catre un url
chrome.get("https://www.jules.app")

# punem pauza de 2 secunda pana se incarca pagina
sleep(2)

# gasim un element dupa xpath - //*[@atribut="valoare"]
user_email = chrome.find_element(By.XPATH, '//*[@placeholder="Enter your email"]')
# trimitem date de la tastatura
user_email.send_keys("abc@email.com")
sleep(1)

# TODO: gasiti si completati voi parola


# gasim un element dupa textul de pe el - //*[text()="text"]
login_btn = chrome.find_element(By.XPATH, "//*[text()='Log in']")
# dam click pe el
login_btn.click()
sleep(1)

# TODO: gasiti si dati click pe Forgot password


# punem pauza de 2 secunda pana se incarca pagina
sleep(2)

# scriem un email gresit
forgot_email_input = chrome.find_element(By.XPATH, '//*[@placeholder="Enter your email"]')
forgot_email_input.send_keys("abc")
sleep(1)

# verificam ca mesajul de eroare este afisat
error = chrome.find_element(By.XPATH, '//*[text()="Please enter a valid email address!"]')
assert error.is_displayed() is True
sleep(1)

# printam un mesaj de succes
print('------- TEST PASSED -------')