from selenium import webdriver
from selenium.webdriver.common.by import By
import time

print("CT06 - Usuário autenticado iniciado")

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

time.sleep(3)

print("Usuário autenticado")

print("Tentando acessar '/' novamente...")

driver.get("http://127.0.0.1:5000/")

time.sleep(3)

print("Verificando permanência na Home...")

menu = driver.find_element(By.CLASS_NAME, "sidebar")

if menu.is_displayed():
    print("Usuário permaneceu autenticado e foi mantido na Home!")
else:
    print("Erro: usuário retornou para login")

driver.quit()

print("CT06 finalizado")