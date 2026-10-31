from selenium import webdriver
from selenium.webdriver.common.by import By
import time


print("CT20 - CEP inválido")


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


print("Informando CEP inválido...")


cep = driver.find_element(By.ID, "cep")

cep.send_keys("00000000")


time.sleep(5)


valor_cep = cep.get_attribute("value")

print("Valor informado:")
print(valor_cep)


# Verifica se algum tratamento ocorreu

pagina = driver.page_source


if "CEP inválido" in pagina or "não encontrado" in pagina:
    print("CEP inválido tratado corretamente!")
else:
    print("CEP inválido informado. Verificar validação do sistema.")


driver.quit()


print("CT20 finalizado!")