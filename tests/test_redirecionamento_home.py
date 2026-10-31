from selenium import webdriver
from selenium.webdriver.common.by import By
import time

print("CT05 - Redirecionamento para Home iniciado")

driver = webdriver.Chrome()
driver.maximize_window()

print("Abrindo sistema...")
driver.get("http://127.0.0.1:5000")

time.sleep(2)

print("Realizando login...")

usuario = driver.find_element(By.ID, "username")
usuario.send_keys("projeto.admin")

senha = driver.find_element(By.ID, "senha")
senha.send_keys("mudar@123")

botao = driver.find_element(By.XPATH, "//button[@type='submit']")
botao.click()

time.sleep(4)

print("Verificando acesso à Home...")

menu = driver.find_element(By.CLASS_NAME, "sidebar")

if menu.is_displayed():
    print("Usuário redirecionado para Home corretamente!")
else:
    print("Erro: Home não carregada")

driver.quit()

print("CT05 finalizado")