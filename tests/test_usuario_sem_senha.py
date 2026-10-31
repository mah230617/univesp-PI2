from selenium import webdriver
from selenium.webdriver.common.by import By
import time


print("CT40 - Criar usuário sem senha")


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
# ABRIR USUÁRIOS
# =====================================

print("Abrindo gerenciamento de usuários...")


driver.get(
    "http://127.0.0.1:5000/usuario/lista"
)


time.sleep(3)



# =====================================
# PREENCHER SEM SENHA
# =====================================

usuario = "usuario_sem_senha"


print("Criando usuário sem senha:")
print(usuario)



driver.find_element(
    By.ID,
    "username"
).send_keys(usuario)



# NÃO PREENCHE SENHA


driver.find_element(
    By.XPATH,
    "//button[@type='submit']"
).click()



time.sleep(3)



# =====================================
# VALIDAR
# =====================================

texto = driver.find_element(
    By.TAG_NAME,
    "body"
).text


print("\nRetorno:")
print(texto[:1000])



texto_normalizado = texto.lower()



if (
    "obrigatório" in texto_normalizado
    or "senha" in texto_normalizado
    or "required" in texto_normalizado
):

    print("\nCT40 aprovado!")
    print("Sistema impediu cadastro sem senha.")



else:

    print("\nERRO!")
    print("Sistema permitiu usuário sem senha.")



driver.quit()


print("\nCT40 finalizado!")