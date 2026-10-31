from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import random


print("CT38 - Criar usuário válido")


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
# GERAR USUÁRIO TESTE
# =====================================

numero = random.randint(1000, 9999)


novo_usuario = f"usuario{numero}"

senha = "Teste123@"


print("Criando usuário:")
print(novo_usuario)



# =====================================
# PREENCHER FORMULÁRIO
# =====================================

campo_usuario = driver.find_element(
    By.ID,
    "username"
)


campo_usuario.send_keys(
    novo_usuario
)



campo_senha = driver.find_element(
    By.ID,
    "senha"
)


campo_senha.send_keys(
    senha
)



driver.find_element(
    By.XPATH,
    "//button[@type='submit']"
).click()



time.sleep(4)



# =====================================
# VALIDAR RESULTADO
# =====================================

texto = driver.find_element(
    By.TAG_NAME,
    "body"
).text


print("\nPágina retornada:")
print(texto[:1000])



texto_normalizado = texto.lower()

usuario_normalizado = novo_usuario.lower()



if usuario_normalizado in texto_normalizado:

    print("\nCT38 aprovado!")
    print("Usuário criado e exibido na lista.")


elif "já existe" in texto_normalizado:

    print("\nERRO: usuário duplicado.")


elif "erro" in texto_normalizado:

    print("\nERRO no cadastro.")


else:

    print("\nERRO: usuário não apareceu na lista.")



driver.quit()


print("\nCT38 finalizado!")