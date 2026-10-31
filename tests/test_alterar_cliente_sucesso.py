from selenium import webdriver
from selenium.webdriver.common.by import By
import random
import time

print("CT33 - Alterar dados do cliente com sucesso")

driver = webdriver.Chrome()
driver.maximize_window()

# ==========================
# LOGIN
# ==========================

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

# ==========================
# ABRIR EDIÇÃO
# ==========================

print("Abrindo edição do cliente...")

driver.get("http://127.0.0.1:5000/cliente/editar/1")

time.sleep(2)

# ==========================
# ALTERAR DADOS
# ==========================

numero = random.randint(100, 999)

print("Alterando dados...")

nome = driver.find_element(By.ID, "nome")
nome.clear()
nome.send_keys(f"Cliente Alterado CT33 {numero}")

telefone = driver.find_element(By.ID, "telefone")
telefone.clear()
telefone.send_keys("11987654321")

email = driver.find_element(By.ID, "email")
email.clear()
email.send_keys(f"ct33{numero}@teste.com")

# ==========================
# SALVAR
# ==========================

print("Salvando alterações...")

driver.find_element(
    By.XPATH,
    "//button[@type='submit']"
).click()

time.sleep(4)

# ==========================
# VALIDAR
# ==========================

texto = driver.find_element(By.TAG_NAME, "body").text

print("\nURL:")
print(driver.current_url)

print("\nMensagem:")
print(texto[:1000])

if "Cliente alterado com sucesso!" in texto:

    print("\nCT33 aprovado!")
    print("O cliente foi alterado com sucesso.")

else:

    print("\nERRO!")
    print("O sistema não confirmou a alteração.")

driver.quit()

print("\nCT33 finalizado!")