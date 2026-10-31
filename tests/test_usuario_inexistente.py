from selenium import webdriver
from selenium.webdriver.common.by import By
import time

print("CT03 - Usuário inexistente iniciado")

driver = webdriver.Chrome()
driver.maximize_window()

print("Abrindo sistema...")
driver.get("http://127.0.0.1:5000")

time.sleep(2)

print("Digitando usuário inexistente...")

usuario = driver.find_element(By.ID, "username")
usuario.send_keys("usuario_teste_fake")

print("Digitando senha...")

senha = driver.find_element(By.ID, "senha")
senha.send_keys("123456")

print("Enviando formulário...")

botao = driver.find_element(By.XPATH, "//button[@type='submit']")
botao.click()

time.sleep(3)

print("Verificando mensagem de erro...")

erro = driver.find_element(By.CLASS_NAME, "alert-danger")

print("Mensagem encontrada:")
print(erro.text)

driver.quit()

print("CT03 finalizado")