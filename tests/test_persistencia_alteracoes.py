from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import random
import time


print("CT34 - Persistência das alterações")


driver = webdriver.Chrome()
driver.maximize_window()


# ==========================
# LOGIN
# ==========================

print("Abrindo login...")

driver.get("http://127.0.0.1:5000")

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



# ==========================
# EDITAR CLIENTE
# ==========================

print("Abrindo edição do cliente...")


driver.get(
    "http://127.0.0.1:5000/cliente/editar/1"
)


time.sleep(3)



# ==========================
# DADOS
# ==========================

numero = random.randint(1000,9999)


nome_teste = f"Cliente Persistência {numero}"

telefone_teste = "11999998888"

email_teste = f"persistencia{numero}@teste.com"



# ==========================
# FUNÇÃO PREENCHER
# ==========================

def preencher(id_campo, valor):

    campo = driver.find_element(
        By.ID,
        id_campo
    )

    campo.click()

    campo.send_keys(
        Keys.CONTROL,
        "a"
    )

    campo.send_keys(
        Keys.BACKSPACE
    )


    for letra in valor:

        campo.send_keys(letra)

        # importante para a máscara
        time.sleep(0.15)


    campo.send_keys(Keys.TAB)

    time.sleep(1)


# ==========================
# ALTERAR
# ==========================

print("Alterando dados...")


preencher(
    "nome",
    nome_teste
)


preencher(
    "telefone",
    telefone_teste
)


preencher(
    "email",
    email_teste
)



campo_telefone = driver.find_element(
    By.ID,
    "telefone"
)


print("\nTelefone antes de salvar:")
print(
    campo_telefone.get_attribute("value")
)



# ==========================
# SALVAR
# ==========================

print("Salvando...")


driver.find_element(
    By.XPATH,
    "//button[@type='submit']"
).click()


time.sleep(4)



# ==========================
# REABRIR
# ==========================

print("Reabrindo cadastro...")


driver.get(
    "http://127.0.0.1:5000/cliente/editar/1"
)


time.sleep(3)



nome = driver.find_element(
    By.ID,
    "nome"
).get_attribute("value")


telefone = driver.find_element(
    By.ID,
    "telefone"
).get_attribute("value")


email = driver.find_element(
    By.ID,
    "email"
).get_attribute("value")



telefone_limpo = "".join(
    filter(str.isdigit, telefone)
)



print("\nValores encontrados:")

print("Nome:", nome)

print("Telefone:", telefone)

print("Email:", email)



# ==========================
# TESTE
# ==========================

if (
    nome == nome_teste
    and telefone_limpo == telefone_teste
    and email == email_teste
):

    print("\nCT34 APROVADO!")
    print("Persistência confirmada.")


else:

    print("\nCT34 FALHOU!")

    print("\nEsperado:")
    print(nome_teste)
    print(telefone_teste)
    print(email_teste)


    print("\nObtido:")
    print(nome)
    print(telefone_limpo)
    print(email)



driver.quit()


print("\nCT34 finalizado!")