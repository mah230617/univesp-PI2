from selenium import webdriver
from selenium.webdriver.common.by import By
import time


print("CT25 - Pesquisa de cliente por nome")


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


# Abrir lista de clientes

driver.get(
    "http://127.0.0.1:5000/cliente/lista"
)

time.sleep(3)


print("Pesquisando cliente pelo nome...")


# Campo de pesquisa por nome
nome = driver.find_element(
    By.NAME,
    "nome"
)

nome.send_keys(
    "Fulano"
)


# Enviar filtro

driver.find_element(
    By.XPATH,
    "//button[@type='submit']"
).click()


time.sleep(3)


pagina = driver.page_source


print("Verificando resultado...")


if "Fulano" in pagina:
    print("Pesquisa por nome funcionando corretamente!")
else:
    print("ERRO: cliente não encontrado na pesquisa.")


print("URL atual:")
print(driver.current_url)


driver.quit()


print("CT25 finalizado!")