from selenium import webdriver
from selenium.webdriver.common.by import By
import time

print("CT12 - Administrador consegue acessar todas as páginas")

driver = webdriver.Chrome()
driver.maximize_window()

# Login
driver.get("http://127.0.0.1:5000")

time.sleep(2)

print("Fazendo login administrador...")

driver.find_element(By.ID, "username").send_keys("projeto.admin")
driver.find_element(By.ID, "senha").send_keys("mudar@123")

driver.find_element(
    By.XPATH,
    "//button[@type='submit']"
).click()

time.sleep(3)

print("Página após login:")
print(driver.current_url)


# Verifica menu Usuários

print("\nVerificando menu de usuários...")

pagina = driver.page_source

if "Usuários" in pagina:
    print("Menu Usuários visível!")
else:
    print("Menu Usuários NÃO apareceu.")


# Teste rota usuários

print("\nAcessando gerenciamento de usuários...")

driver.get(
    "http://127.0.0.1:5000/usuario/lista"
)

time.sleep(3)

print("URL:")
print(driver.current_url)


if "usuario/lista" in driver.current_url:
    print("Administrador acessou usuários corretamente!")
else:
    print("Falha no acesso aos usuários.")


# Teste clientes

print("\nAcessando clientes...")

driver.get(
    "http://127.0.0.1:5000/cliente/lista"
)

time.sleep(3)

print("URL:")
print(driver.current_url)


if "cliente/lista" in driver.current_url:
    print("Administrador acessou clientes corretamente!")
else:
    print("Falha no acesso aos clientes.")


driver.quit()

print("\nCT12 finalizado!")