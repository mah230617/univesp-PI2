from selenium import webdriver
from selenium.webdriver.common.by import By
import time


print("CT36 - Cliente desaparece da lista")


driver = webdriver.Chrome()
driver.maximize_window()


# =====================================
# LOGIN ADMIN
# =====================================

print("Abrindo login...")


driver.get(
    "http://127.0.0.1:5000"
)

time.sleep(2)


driver.find_element(
    By.ID,
    "username"
).send_keys("projeto.admin")


driver.find_element(
    By.ID,
    "senha"
).send_keys("mudar@123")


driver.find_element(
    By.XPATH,
    "//button[@type='submit']"
).click()


time.sleep(3)



# =====================================
# ABRIR LISTA
# =====================================

print("Abrindo lista de clientes...")


driver.get(
    "http://127.0.0.1:5000/cliente/lista"
)


time.sleep(3)



# =====================================
# VERIFICAR CLIENTES
# =====================================

print("Verificando clientes cadastrados...")


texto = driver.find_element(
    By.TAG_NAME,
    "body"
).text


print("\nLista atual:")

print(texto[:1000])



# =====================================
# VALIDAR
# =====================================

# O teste usa o cliente que foi excluído no CT35.
# Caso queira verificar um cliente específico,
# altere essa variável.

cliente_excluido = "Fulano da silva de jesus cristo"



if cliente_excluido not in texto:

    print("\nCT36 aprovado!")
    print("Cliente não aparece mais na lista.")

else:

    print("\nERRO!")
    print("Cliente excluído ainda aparece na lista.")



driver.quit()


print("\nCT36 finalizado!")