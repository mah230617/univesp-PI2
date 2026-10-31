from selenium import webdriver
from selenium.webdriver.common.by import By
import time

print("CT07 - Logout iniciado")

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

print("Login realizado")

print("Localizando botão de logout...")

logout = driver.find_element(
    By.CSS_SELECTOR,
    "a[aria-label='Sair do sistema']"
)

logout.click()

time.sleep(3)

print("Verificando encerramento da sessão...")

campo_usuario = driver.find_element(By.ID, "username")

if campo_usuario.is_displayed():
    print("Logout realizado corretamente!")
else:
    print("Erro: usuário continua autenticado")

driver.quit()

print("CT07 finalizado")