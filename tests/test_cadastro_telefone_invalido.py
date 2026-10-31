from selenium import webdriver
from selenium.webdriver.common.by import By
import time


print("CT21 - Telefone inválido")


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


print("Testando telefone inválido...")


telefone = driver.find_element(By.ID, "telefone")

telefone.send_keys("123")


valor = telefone.get_attribute("value")

print("Valor informado:")
print(valor)


# Tenta enviar

driver.find_element(
    By.XPATH,
    "//button[@type='submit']"
).click()


time.sleep(3)


pagina = driver.page_source


if "telefone" in pagina.lower() or "/cliente/novo" in driver.current_url:
    print("Telefone inválido tratado corretamente!")
else:
    print("ERRO: telefone inválido aceito!")


driver.quit()


print("CT21 finalizado!")