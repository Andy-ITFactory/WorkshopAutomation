# importam selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

# deschidem chrome
chrome = webdriver.Chrome()

# cu sleep putem pune pauza de cateva secunde sa asteptam sa vedem si noi ceva
sleep(3)

# maximizam fereastra (Aici incercati sa gasiti singuri comanda)

# navigam catre un url: "https://www.mega-image.ro/" (Aici incercati sa gasiti singuri comanda)

# dam click pe Accept cookies (Aici explica host)
# chrome.find_element(By.XPATH, '//*[@data-testid="de_gasit_si_completat_id_corect"]').click()

# dam click pe Contul meu (Aici recapitulam impreuna)

# dam click pe Continua (Aici faceti singuri sa verificati daca ati inteles)

# verificam mesajul de eroare "Te rugam sa introduci adresa de e-mail sau numarul de telefon" (Explica host)

# inchidem chrome
chrome.quit()

# daca a trecut testul, printam in consola un mesaj de succes
print('SUCCESS - TEST PASSED')

# la final scoatem sleep-urile pentru a vedea viteza unui test si pentru a intelege valoarea si necesitatea unui automation engineer
# la final va aratam si un exemplu de raport generat automat
