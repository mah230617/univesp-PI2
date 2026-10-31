from selenium import webdriver
from selenium.webdriver.common.by import By
import time


print("CT39 - Criar usuário duplicado")


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
# TENTAR DUPLICAR
# =====================================

usuario_existente = "beltrano"


print("Tentando cadastrar usuário:")
print(usuario_existente)



driver.find_element(
    By.ID,
    "username"
).send_keys(usuario_existente)



driver.find_element(
    By.ID,
    "senha"
).send_keys("Teste123@")


driver.find_element(
    By.XPATH,
    "//button[@type='submit']"
).click()


time.sleep(4)



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



mensagens_bloqueio = [

    "já está cadastrado",
    "já cadastrado",
    "já existe",
    "duplicado",
    "não permitido",
    "erro"

]



bloqueou = False


for mensagem in mensagens_bloqueio:

    if mensagem in texto_normalizado:
        bloqueou = True
        break



if bloqueou:

    print("\nCT39 aprovado!")
    print("Sistema bloqueou usuário duplicado.")


else:

    print("\nERRO!")
    print("Sistema permitiu usuário duplicado.")



driver.quit()


print("\nCT39 finalizado!")