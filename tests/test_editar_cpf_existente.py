from selenium import webdriver
from selenium.webdriver.common.by import By
import time


print("CT32 - Alterar CPF/CNPJ para um já existente")


driver = webdriver.Chrome()
driver.maximize_window()


# =========================
# LOGIN
# =========================

print("Abrindo login...")

driver.get("http://127.0.0.1:5000")

time.sleep(2)

driver.find_element(By.ID, "username").send_keys("projeto.admin")
driver.find_element(By.ID, "senha").send_keys("mudar@123")

driver.find_element(
    By.XPATH,
    "//button[@type='submit']"
).click()

time.sleep(3)


# =========================
# ABRIR EDIÇÃO DO CLIENTE
# =========================

print("Abrindo edição do cliente...")

driver.get("http://127.0.0.1:5000/cliente/editar/1")

time.sleep(3)


# =========================
# ALTERAR CPF/CNPJ
# =========================

print("Alterando CPF/CNPJ...")


# CPF de OUTRO cliente já cadastrado
# Cliente 4 no banco:
# Cliente CPF Teste - 52998224725

cpf_existente = "52998224725"


campo = driver.find_element(By.ID, "cpfcnpj")

campo.clear()
campo.send_keys(cpf_existente)



# =========================
# SALVAR ALTERAÇÃO
# =========================

print("Tentando salvar...")


driver.find_element(
    By.XPATH,
    "//button[@type='submit']"
).click()


time.sleep(4)



# =========================
# VALIDAR RESULTADO
# =========================

texto = driver.find_element(
    By.TAG_NAME,
    "body"
).text


print("\nURL:")
print(driver.current_url)


print("\nMensagem:")
print(texto[:1000])



if "já está cadastrado" in texto:

    print("\nCT32 aprovado!")
    print("O sistema bloqueou o CPF/CNPJ duplicado.")


elif "Cliente alterado com sucesso!" in texto:

    print("\nERRO!")
    print("O sistema permitiu alterar para um CPF/CNPJ já existente.")


elif "CPF / CNPJ inválido!" in texto:

    print("\nERRO!")
    print("O CPF/CNPJ informado foi considerado inválido.")


else:

    print("\nERRO!")
    print("O sistema retornou uma mensagem inesperada.")



driver.quit()


print("\nCT32 finalizado!")