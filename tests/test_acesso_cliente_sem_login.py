from selenium import webdriver
from selenium.webdriver.common.by import By
import time

print("CT08 - Acesso de cliente sem login iniciado")

driver = webdriver.Chrome()
driver.maximize_window()

print("Tentando acessar lista de clientes sem autenticação...")

driver.get("http://127.0.0.1:5000/cliente/lista")

time.sleep(3)

print("Verificando redirecionamento para login...")

campo_usuario = driver.find_element(By.ID, "username")

if campo_usuario.is_displayed():
    print("Acesso bloqueado corretamente! Usuário foi enviado para login.")
else:
    print("Erro: usuário conseguiu acessar clientes sem login.")

driver.quit()

print("CT08 finalizado")