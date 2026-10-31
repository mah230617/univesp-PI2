from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time


print("CT16 - Cadastro com CPF já existente")


driver = webdriver.Chrome()
driver.maximize_window()


# Login

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


print("Tentando cadastrar CPF existente...")


# CPF do cliente que já existe no banco
driver.find_element(By.ID, "nome").send_keys(
    "Cliente CPF Duplicado"
)

driver.find_element(By.ID, "cpfcnpj").send_keys(
    "52998224725"
)

driver.find_element(By.ID, "data_nascimento").send_keys(
    "10/05/1995"
)

driver.find_element(By.ID, "email").send_keys(
    "duplicado@email.com"
)

driver.find_element(By.ID, "telefone").send_keys(
    "11977778888"
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
    "10"
)

driver.find_element(By.ID, "cidade").send_keys(
    "Barueri"
)


Select(
    driver.find_element(By.ID, "estado")
).select_by_value("SP")


driver.find_element(
    By.XPATH,
    "//button[@type='submit']"
).click()


time.sleep(3)


pagina = driver.page_source


if "já está cadastrado" in pagina:
    print("CPF duplicado bloqueado corretamente!")
else:
    print("ERRO: CPF duplicado foi aceito!")


print("URL atual:")
print(driver.current_url)


driver.quit()


print("CT16 finalizado!")