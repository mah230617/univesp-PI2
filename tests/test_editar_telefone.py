from selenium import webdriver
from selenium.webdriver.common.by import By
import time


print("CT31 - Alterar telefone do cliente")


driver = webdriver.Chrome()
driver.maximize_window()



# =========================
# LOGIN
# =========================

print("Abrindo login...")


driver.get(
    "http://127.0.0.1:5000"
)


time.sleep(2)


driver.find_element(
    By.ID,
    "username"
).send_keys(
    "projeto.admin"
)


driver.find_element(
    By.ID,
    "senha"
).send_keys(
    "mudar@123"
)


driver.find_element(
    By.XPATH,
    "//button[@type='submit']"
).click()


time.sleep(3)



# =========================
# ABRIR EDIÇÃO
# =========================

print("Abrindo edição do cliente...")


driver.get(
    "http://127.0.0.1:5000/cliente/editar/1"
)


time.sleep(3)



# =========================
# ALTERAR TELEFONE
# =========================

print("Alterando telefone...")


campo = driver.find_element(
    By.ID,
    "telefone"
)


campo.clear()


campo.send_keys(
    "11988887777"
)



# =========================
# SALVAR
# =========================

print("Salvando alterações...")


driver.find_element(
    By.XPATH,
    "//button[@type='submit']"
).click()


time.sleep(5)



# =========================
# VALIDAR
# =========================

print("\nURL após salvar:")
print(
    driver.current_url
)


texto = driver.find_element(
    By.TAG_NAME,
    "body"
).text



print("\nRetorno:")
print(
    texto[:600]
)



if "Cliente alterado com sucesso!" in texto:

    print(
        "\nTelefone alterado com sucesso!"
    )

else:

    print(
        "\nERRO: telefone não foi alterado."
    )



driver.quit()


print("\nCT31 finalizado!")