from selenium import webdriver
from selenium.webdriver.common.by import By
import time

print("CT09 - Usuário não logado acessando Usuários iniciado")

driver = webdriver.Chrome()
driver.maximize_window()

print("Tentando acessar gerenciamento de usuários sem login...")

driver.get("http://127.0.0.1:5000/usuario/lista")

time.sleep(3)

print("Verificando redirecionamento para login...")

campo_usuario = driver.find_element(By.ID, "username")

if campo_usuario.is_displayed():
    print("Acesso bloqueado corretamente! Usuário foi direcionado para login.")
else:
    print("Erro: usuário acessou área administrativa sem autenticação.")

driver.quit()

print("CT09 finalizado")