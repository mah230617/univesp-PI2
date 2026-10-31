from selenium import webdriver
from selenium.webdriver.common.by import By
import time


print("CT42 - Ativar usuário")


driver = webdriver.Chrome()
driver.maximize_window()


# LOGIN ADMIN

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



# USUÁRIOS

print("Abrindo usuários...")


driver.get(
    "http://127.0.0.1:5000/usuario/lista"
)


time.sleep(3)



# PROCURA USUÁRIO INATIVO

print("Procurando usuário inativo...")


links = driver.find_elements(
    By.XPATH,
    "//a[contains(@href,'alterar_status')]"
)


if len(links) == 0:

    print("ERRO: nenhum usuário encontrado.")

else:

    links[-1].click()

    time.sleep(4)



texto = driver.find_element(
    By.TAG_NAME,
    "body"
).text


print(texto[:800])



if "Ativo" in texto:

    print("\nCT42 aprovado!")
    print("Usuário ativado.")

else:

    print("\nERRO: usuário não foi ativado.")



driver.quit()


print("\nCT42 finalizado!")