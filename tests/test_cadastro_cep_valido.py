from selenium import webdriver
from selenium.webdriver.common.by import By
import time


print("CT19 - CEP preenchido corretamente")


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


print("Testando preenchimento do CEP...")


cep = driver.find_element(By.ID, "cep")

cep.send_keys("06400000")


time.sleep(5)


valor_cep = cep.get_attribute("value")

print("Valor preenchido no CEP:")
print(valor_cep)


if valor_cep:
    print("CEP preenchido corretamente!")
else:
    print("ERRO: CEP não foi preenchido!")


driver.quit()


print("CT19 finalizado!")