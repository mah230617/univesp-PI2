from selenium import webdriver
from selenium.webdriver.common.by import By
import time


print("CT18 - Cadastro com campos obrigatórios vazios")


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


print("Tentando enviar formulário vazio...")


# Clica no botão sem preencher nada

driver.find_element(
    By.XPATH,
    "//button[@type='submit']"
).click()


time.sleep(3)


# Verifica se permaneceu na tela de cadastro

url = driver.current_url

print("URL atual:")
print(url)


if "/cliente/novo" in url:
    print("Campos obrigatórios bloquearam o cadastro corretamente!")
else:
    print("ERRO: formulário vazio foi enviado!")


driver.quit()


print("CT18 finalizado!")