from selenium import webdriver
from selenium.webdriver.common.by import By
import time


print("CT43 - Desativar usuário")


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



# LISTA DE USUÁRIOS

print("Abrindo gerenciamento de usuários...")


driver.get(
    "http://127.0.0.1:5000/usuario/lista"
)


time.sleep(3)



texto_antes = driver.find_element(
    By.TAG_NAME,
    "body"
).text


print("\nAntes:")
print(texto_antes[:800])



# =====================================
# CLICAR NO STATUS ATIVO
# =====================================

print("\nAlterando status...")


status = driver.find_elements(
    By.XPATH,
    "//a[contains(.,'Ativo')]"
)



if len(status) == 0:

    print("ERRO: nenhum usuário ativo encontrado.")

    driver.quit()
    quit()



status[-1].click()



time.sleep(4)



# =====================================
# VALIDAR
# =====================================

texto_depois = driver.find_element(
    By.TAG_NAME,
    "body"
).text



print("\nDepois:")
print(texto_depois[:800])



if "Inativo" in texto_depois:

    print("\nCT43 aprovado!")
    print("Usuário desativado corretamente.")


else:

    print("\nERRO!")
    print("Usuário não foi desativado.")



driver.quit()


print("\nCT43 finalizado!")