from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import random


print("CT41 - Normalização do username")


driver = webdriver.Chrome()
driver.maximize_window()


# LOGIN

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



# ABRIR USUÁRIOS

print("Abrindo gerenciamento de usuários...")


driver.get(
    "http://127.0.0.1:5000/usuario/lista"
)


time.sleep(3)



# CRIAR USUÁRIO COM ESPAÇOS

numero = random.randint(1000,9999)


usuario_digitado = f"   usuarioTeste{numero}   "

usuario_esperado = f"USUARIOTESTE{numero}"


print("Usuário enviado:")
print(usuario_digitado)



driver.find_element(
    By.ID,
    "username"
).send_keys(usuario_digitado)



driver.find_element(
    By.ID,
    "senha"
).send_keys("Teste123@")


driver.find_element(
    By.XPATH,
    "//button[@type='submit']"
).click()


time.sleep(4)



# VALIDAR

texto = driver.find_element(
    By.TAG_NAME,
    "body"
).text


print("\nRetorno:")
print(texto[:1200])


texto = texto.upper()



if usuario_esperado in texto:

    print("\nCT41 aprovado!")
    print("Username normalizado corretamente.")


elif usuario_digitado.strip().upper() in texto:

    print("\nCT41 aprovado parcialmente!")
    print("Sistema removeu espaços ou normalizou parcialmente.")


else:

    print("\nERRO!")
    print("Username não foi encontrado normalizado.")



driver.quit()


print("\nCT41 finalizado!")