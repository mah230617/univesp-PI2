from selenium import webdriver
from selenium.webdriver.common.by import By
import time

print("1 - Iniciando navegador...")

driver = webdriver.Chrome()
driver.maximize_window()

print("2 - Abrindo sistema...")
driver.get("http://127.0.0.1:5000")

time.sleep(3)

print("3 - Página carregada")

print("4 - Procurando campo usuário...")
usuario = driver.find_element(By.ID, "username")

print("5 - Digitando usuário...")
usuario.send_keys("projeto.admin")

print("6 - Procurando campo senha...")
senha = driver.find_element(By.ID, "senha")

print("7 - Digitando senha...")
senha.send_keys("mudar@123")

print("8 - Clicando no botão...")
botao = driver.find_element(By.XPATH, "//button[@type='submit']")
botao.click()

print("9 - Aguardando login...")
time.sleep(5)

print("Título atual:", driver.title)

driver.quit()

print("10 - Finalizado!")