from selenium import webdriver
from selenium.webdriver.common.by import By
import time

print("CT03 - Login com campos vazios iniciado")

driver = webdriver.Chrome()
driver.maximize_window()

print("Abrindo sistema...")
driver.get("http://127.0.0.1:5000")

time.sleep(2)

print("Localizando botão de acesso...")

botao = driver.find_element(By.XPATH, "//button[@type='submit']")

print("Tentando enviar formulário vazio...")
botao.click()

time.sleep(3)

print("Verificando se permaneceu na tela de login...")

campo_usuario = driver.find_element(By.ID, "username")

if campo_usuario.is_displayed():
    print("Login bloqueado corretamente: campos obrigatórios não preenchidos")
else:
    print("Erro: sistema permitiu envio sem dados")

driver.quit()

print("CT03 finalizado")