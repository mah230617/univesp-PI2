from selenium import webdriver
from selenium.webdriver.common.by import By
import time

print("1 - Iniciando teste de login inválido...")

driver = webdriver.Chrome()
driver.maximize_window()

print("2 - Abrindo sistema...")
driver.get("http://127.0.0.1:5000")

time.sleep(2)

print("3 - Digitando usuário...")
usuario = driver.find_element(By.ID, "username")
usuario.send_keys("projeto.admin")

print("4 - Digitando senha incorreta...")
senha = driver.find_element(By.ID, "senha")
senha.send_keys("senhaerrada123")

print("5 - Clicando em acessar...")
botao = driver.find_element(By.XPATH, "//button[@type='submit']")
botao.click()

time.sleep(3)

print("6 - Verificando mensagem de erro...")

erro = driver.find_element(By.CLASS_NAME, "alert-danger")

print("Mensagem encontrada:", erro.text)

driver.quit()

print("7 - Teste finalizado!")