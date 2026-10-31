from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time


print("CT13 - Cadastro de cliente com dados válidos")


driver = webdriver.Chrome()
driver.maximize_window()


# Login
driver.get("http://127.0.0.1:5000")

time.sleep(2)

driver.find_element(By.ID, "username").send_keys("projeto.admin")
driver.find_element(By.ID, "senha").send_keys("mudar@123")

driver.find_element(
    By.XPATH,
    "//button[@type='submit']"
).click()

time.sleep(3)


# Ir para cadastro
driver.get(
    "http://127.0.0.1:5000/cliente/novo"
)

time.sleep(3)


print("Preenchendo cadastro...")


driver.find_element(By.ID, "nome").send_keys(
    "Cliente Teste Selenium"
)

driver.find_element(By.ID, "cpfcnpj").send_keys(
    "12345678909"
)

driver.find_element(By.ID, "data_nascimento").send_keys(
    "01/01/1990"
)

driver.find_element(By.ID, "email").send_keys(
    "cliente.selenium@email.com"
)

driver.find_element(By.ID, "telefone").send_keys(
    "11999999999"
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

driver.find_element(By.ID, "complemento").send_keys(
    "Casa"
)

driver.find_element(By.ID, "cidade").send_keys(
    "Barueri"
)


estado = Select(
    driver.find_element(By.ID, "estado")
)

estado.select_by_value("SP")


driver.find_element(
    By.XPATH,
    "//button[@type='submit']"
).click()


time.sleep(4)


print("URL final:")
print(driver.current_url)


pagina = driver.page_source


if "Cliente criado com sucesso" in pagina:
    print("Cadastro realizado com sucesso!")
else:
    print("Cadastro não confirmado.")


driver.quit()

print("CT13 finalizado!")