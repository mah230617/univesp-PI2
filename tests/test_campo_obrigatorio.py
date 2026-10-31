from selenium import webdriver
from selenium.webdriver.common.by import By
import time


print("TM06 - Campo obrigatório informa erro")


driver = webdriver.Chrome()
driver.maximize_window()



# ==============================
# LOGIN
# ==============================

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



# ==============================
# CADASTRO CLIENTE
# ==============================

print("Abrindo cadastro de cliente...")


driver.get(
    "http://127.0.0.1:5000/cliente/novo"
)


time.sleep(3)



print("Tentando salvar vazio...")


botao = driver.find_elements(
    By.XPATH,
    "//button[@type='submit']"
)



if len(botao) == 0:

    print("ERRO: botão salvar não encontrado.")

    driver.quit()
    quit()



botao[0].click()



time.sleep(3)



texto = driver.find_element(
    By.TAG_NAME,
    "body"
).text



print("\nRetorno:")
print(texto[:1500])



mensagens = [
    "obrigatório",
    "obrigatorio",
    "informe",
    "preencha",
    "inválido",
    "invalido"
]


erro = False


for msg in mensagens:

    if msg.lower() in texto.lower():

        erro = True
        break



if erro:

    print("\nTM06 aprovado!")
    print("Sistema informou erro para campo obrigatório.")


else:

    print("\nERRO!")
    print("Nenhuma mensagem de validação encontrada.")



driver.quit()


print("\nTM06 finalizado!")