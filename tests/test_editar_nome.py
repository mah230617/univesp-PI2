from selenium import webdriver
from selenium.webdriver.common.by import By
import time


print("CT29 - Alterar nome do cliente")


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



# Abrir edição cliente ID 1

driver.get(
    "http://127.0.0.1:5000/cliente/editar/1"
)

time.sleep(3)


novo_nome = "Cliente CT29 Alterado"



campo = driver.find_element(
    By.ID,
    "nome"
)


campo.clear()

campo.send_keys(
    novo_nome
)



driver.find_element(
    By.XPATH,
    "//button[@type='submit']"
).click()


time.sleep(4)



pagina = driver.page_source


if novo_nome in pagina:

    print(
        "Nome alterado com sucesso!"
    )

else:

    print(
        "ERRO: nome não alterado!"
    )



driver.quit()


print("CT29 finalizado!")