from selenium import webdriver
from selenium.webdriver.common.by import By
import time


print("CT23 - Máscaras funcionando durante a digitação")


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


print("Testando máscara de CPF...")


cpf = driver.find_element(By.ID, "cpfcnpj")

cpf.send_keys("52998224725")

time.sleep(1)

valor_cpf = cpf.get_attribute("value")

print("CPF exibido:")
print(valor_cpf)


if "." in valor_cpf or "-" in valor_cpf:
    print("Máscara CPF funcionando!")
else:
    print("Máscara CPF não aplicada.")


print("\nTestando máscara de telefone...")


telefone = driver.find_element(By.ID, "telefone")

telefone.send_keys("11999999999")

time.sleep(1)

valor_tel = telefone.get_attribute("value")

print("Telefone exibido:")
print(valor_tel)


if "(" in valor_tel or "-" in valor_tel:
    print("Máscara telefone funcionando!")
else:
    print("Máscara telefone não aplicada.")


print("\nTestando máscara de CEP...")


cep = driver.find_element(By.ID, "cep")

cep.send_keys("06400000")

time.sleep(1)

valor_cep = cep.get_attribute("value")

print("CEP exibido:")
print(valor_cep)


if "-" in valor_cep:
    print("Máscara CEP funcionando!")
else:
    print("Máscara CEP não aplicada.")


driver.quit()


print("\nCT23 finalizado!")