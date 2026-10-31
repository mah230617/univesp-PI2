from selenium import webdriver
from selenium.webdriver.common.by import By
import time

print("CT11 - Usuário comum tentando acessar gerenciamento de usuários")

driver = webdriver.Chrome()
driver.maximize_window()

# Abrir tela de login
driver.get("http://127.0.0.1:5000")

time.sleep(2)

print("Realizando login como usuário comum...")

driver.find_element(By.ID, "username").send_keys("testecomum")
driver.find_element(By.ID, "senha").send_keys("Teste123@")

driver.find_element(
    By.XPATH,
    "//button[@type='submit']"
).click()

time.sleep(3)

print("Tentando acessar lista de usuários...")

driver.get(
    "http://127.0.0.1:5000/usuario/lista"
)

time.sleep(3)

url_atual = driver.current_url

print("URL atual:", url_atual)

pagina = driver.page_source

if "/login" in url_atual or "403" in pagina or "Acesso negado" in pagina:
    print("Usuário comum bloqueado corretamente!")
else:
    print("Erro: usuário comum conseguiu acessar gerenciamento de usuários.")

driver.quit()

print("CT11 finalizado!")