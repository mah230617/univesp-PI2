from selenium import webdriver
from selenium.webdriver.common.by import By
import time

print("CT10 - Usuário comum tentando excluir cliente")

driver = webdriver.Chrome()
driver.maximize_window()

# Abrir login
driver.get("http://127.0.0.1:5000")

time.sleep(2)

print("Fazendo login como usuário comum...")

driver.find_element(By.ID, "username").send_keys("testecomum")
driver.find_element(By.ID, "senha").send_keys("Teste123@")

driver.find_element(
    By.XPATH,
    "//button[@type='submit']"
).click()

time.sleep(3)

print("Login realizado. Tentando excluir cliente...")

driver.get(
    "http://127.0.0.1:5000/cliente/delete/1"
)

time.sleep(3)

url = driver.current_url

print("URL após tentativa:", url)

pagina = driver.page_source

if "Acesso negado" in pagina or "403" in pagina or "/login" in url:
    print("Usuário comum bloqueado corretamente!")
else:
    print("Verificar: usuário comum conseguiu acessar a rota.")

driver.quit()

print("CT10 finalizado!")