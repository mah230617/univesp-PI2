from selenium import webdriver
from selenium.webdriver.common.by import By
import time


print("CT22 - Email inválido")


driver = webdriver.Chrome()
driver.maximize_window()


# Login administrador

driver.get("http://127.0.0.1:5000")

time.sleep(2)

driver.find_element(By.ID, "username").send_keys(
    "projeto.admin"
)

driver.find_element(By.ID, "senha").send_keys(
    "mudar@123"
)

driver.find_element(
    By.XPATH,
    "//button[@type='submit']"
).click()


time.sleep(3)


# Abrir cadastro

driver.get(
    "http://127.0.0.1:5000/cliente/novo"
)

time.sleep(3)


print("Testando email inválido...")


email = driver.find_element(By.ID, "email")

email.send_keys(
    "email-invalido"
)


driver.find_element(
    By.XPATH,
    "//button[@type='submit']"
).click()


time.sleep(3)


pagina = driver.page_source


print("URL atual:")
print(driver.current_url)


# Validação HTML5 do tipo email normalmente impede o envio
if "/cliente/novo" in driver.current_url:
    print("Email inválido bloqueado corretamente!")
else:
    print("ERRO: email inválido aceito!")


driver.quit()


print("CT22 finalizado!")