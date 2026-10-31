from selenium import webdriver
from selenium.webdriver.common.by import By
import time


print("CT16 - Cadastro de cliente com CNPJ inválido")


driver = webdriver.Chrome()
driver.maximize_window()


# Login administrador

print("Abrindo login...")

driver.get("http://127.0.0.1:5000")

time.sleep(2)

driver.find_element(By.ID, "username").send_keys("projeto.admin")
driver.find_element(By.ID, "senha").send_keys("mudar@123")

driver.find_element(
    By.XPATH,
    "//button[@type='submit']"
).click()


time.sleep(3)


# Abrir cadastro

print("Abrindo cadastro...")

driver.get(
    "http://127.0.0.1:5000/cliente/novo"
)

time.sleep(3)


print("Preenchendo cadastro CNPJ inválido...")


driver.find_element(By.ID, "nome").send_keys(
    "Empresa CNPJ Invalido"
)


# CNPJ inválido
driver.find_element(By.ID, "cpfcnpj").send_keys(
    "11222333000182"
)


driver.find_element(By.ID, "email").send_keys(
    "cnpj.invalido@email.com"
)


driver.find_element(By.ID, "telefone").send_keys(
    "11333334444"
)


driver.find_element(By.ID, "cep").send_keys(
    "06400000"
)


driver.find_element(By.ID, "logradouro").send_keys(
    "Rua Teste"
)


driver.find_element(By.ID, "bairro").send_keys(
    "Centro"
)


driver.find_element(By.ID, "numero").send_keys(
    "100"
)


driver.find_element(By.ID, "cidade").send_keys(
    "Barueri"
)


# Estado
from selenium.webdriver.support.ui import Select

estado = Select(
    driver.find_element(By.ID, "estado")
)

estado.select_by_value("SP")


# Captura documento exibido

cnpj_exibido = driver.find_element(
    By.ID,
    "cpfcnpj"
).get_attribute("value")


print("CNPJ exibido:")
print(cnpj_exibido)


# Enviar formulário

driver.find_element(
    By.XPATH,
    "//button[@type='submit']"
).click()


time.sleep(3)


pagina = driver.page_source


print("\nURL final:")
print(driver.current_url)


if "CPF / CNPJ inválido" in pagina:
    print("\nCNPJ inválido bloqueado corretamente!")
else:
    print("\nERRO!")
    print("O sistema aceitou ou não exibiu mensagem de erro.")


print("\nCT16 finalizado!")


driver.quit()