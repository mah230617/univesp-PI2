from selenium import webdriver
from selenium.webdriver.common.by import By
import time


print("CT27 - Pesquisa sem resultados")


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


# Lista de clientes

driver.get(
    "http://127.0.0.1:5000/cliente/lista"
)

time.sleep(3)


print("Pesquisando cliente inexistente...")


campo_nome = driver.find_element(
    By.NAME,
    "nome"
)

campo_nome.send_keys(
    "ClienteNaoExiste123"
)


driver.find_element(
    By.XPATH,
    "//button[@type='submit']"
).click()


time.sleep(3)


print("Verificando tabela de resultados...")


# pega somente a área da tabela
tabela = driver.find_element(
    By.TAG_NAME,
    "table"
)


texto_tabela = tabela.text


if "ClienteNaoExiste123" not in texto_tabela:
    print("Pesquisa sem resultados tratada corretamente!")
else:
    print("ERRO: cliente inexistente apareceu na tabela!")


driver.quit()


print("CT27 finalizado!")