from selenium import webdriver
from selenium.webdriver.common.by import By
import time


print("CT18 - Cadastro de cliente com CPF inválido")


driver = webdriver.Chrome()
driver.maximize_window()


# Login

print("Abrindo login...")

driver.get(
    "http://127.0.0.1:5000"
)

time.sleep(2)


driver.find_element(
    By.ID,
    "username"
).send_keys(
    "projeto.admin"
)


driver.find_element(
    By.ID,
    "senha"
).send_keys(
    "mudar@123"
)


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


print("Preenchendo cadastro CPF inválido...")


driver.find_element(
    By.ID,
    "nome"
).send_keys(
    "Cliente CPF Invalido Teste"
)


# CPF inválido
driver.find_element(
    By.ID,
    "cpfcnpj"
).send_keys(
    "52998224726"
)


driver.find_element(
    By.ID,
    "email"
).send_keys(
    "cpf.invalido.teste@email.com"
)


driver.find_element(
    By.ID,
    "telefone"
).send_keys(
    "11999998888"
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
    "Rua Teste CPF"
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


# Estado

from selenium.webdriver.support.ui import Select

estado = Select(
    driver.find_element(By.ID, "estado")
)

estado.select_by_value("SP")


time.sleep(1)


cpf_exibido = driver.find_element(
    By.ID,
    "cpfcnpj"
).get_attribute("value")


print("\nCPF exibido:")
print(cpf_exibido)


# Enviar formulário

driver.find_element(
    By.XPATH,
    "//button[@type='submit']"
).click()


time.sleep(4)


pagina = driver.page_source


print("\nURL final:")
print(driver.current_url)


# Verificação

if (
    "CPF / CNPJ inválido" in pagina
    or
    "inválido" in pagina
):

    print("\nCPF inválido bloqueado corretamente!")

else:

    print("\nERRO!")
    print("O sistema permitiu CPF inválido.")


print("\nCT18 finalizado!")


driver.quit()