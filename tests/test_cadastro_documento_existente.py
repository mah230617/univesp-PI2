from selenium import webdriver
from selenium.webdriver.common.by import By
import time


print("CT19 - Cadastro de cliente com CPF/CNPJ já existente")


driver = webdriver.Chrome()
driver.maximize_window()


# Login administrador
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


# Abrir cadastro
print("Abrindo cadastro...")

driver.get(
    "http://127.0.0.1:5000/cliente/novo"
)

time.sleep(3)



print("Tentando cadastrar CPF já existente...")


driver.find_element(
    By.ID,
    "nome"
).send_keys(
    "Cliente Duplicado Teste"
)


driver.find_element(
    By.ID,
    "cpfcnpj"
).send_keys(
    "52998224725"
)


driver.find_element(
    By.ID,
    "email"
).send_keys(
    "duplicado@email.com"
)


driver.find_element(
    By.ID,
    "telefone"
).send_keys(
    "11999998888"
)


driver.find_element(
    By.ID,
    "data_nascimento"
).send_keys(
    "01012000"
)


driver.find_element(
    By.ID,
    "cep"
).send_keys(
    "06400000"
)


driver.find_element(
    By.ID,
    "logradouro"
).send_keys(
    "Rua Teste"
)


driver.find_element(
    By.ID,
    "bairro"
).send_keys(
    "Centro"
)


driver.find_element(
    By.ID,
    "numero"
).send_keys(
    "100"
)


driver.find_element(
    By.ID,
    "cidade"
).send_keys(
    "Barueri"
)


driver.find_element(
    By.ID,
    "estado"
).send_keys(
    "SP"
)


driver.find_element(
    By.XPATH,
    "//button[@type='submit']"
).click()


time.sleep(4)


pagina = driver.page_source


url = driver.current_url


print("\nURL final:")
print(url)


if "já está cadastrado" in pagina or "já está cadastrado no sistema" in pagina:

    print("\nCPF/CNPJ duplicado bloqueado corretamente!")

else:

    print("\nERRO!")
    print("O sistema permitiu cadastro duplicado.")



driver.quit()

print("\nCT19 finalizado!")