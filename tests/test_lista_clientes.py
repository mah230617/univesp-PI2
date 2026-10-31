from selenium import webdriver
from selenium.webdriver.common.by import By
import time


print("CT24 - Listagem dos clientes")


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


# Acessar lista de clientes

driver.get(
    "http://127.0.0.1:5000/cliente/lista"
)

time.sleep(3)


print("URL atual:")
print(driver.current_url)


pagina = driver.page_source


if "Clientes" in pagina:
    print("Lista de clientes carregada corretamente!")
else:
    print("ERRO: lista de clientes não encontrada.")


driver.quit()


print("CT24 finalizado!")