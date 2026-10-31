from selenium import webdriver
from selenium.webdriver.common.by import By
import time


print("CT30 - Alterar endereço do cliente")


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
# ABRIR EDIÇÃO DO CLIENTE
# =========================

print("Abrindo edição do cliente...")


driver.get(
    "http://127.0.0.1:5000/cliente/editar/1"
)


time.sleep(3)



# =========================
# ALTERAR ENDEREÇO
# =========================

print("Alterando endereço...")


def preencher(id_campo, valor):

    try:

        campo = driver.find_element(
            By.ID,
            id_campo
        )

        campo.clear()

        campo.send_keys(valor)

    except:

        print(
            f"Campo {id_campo} não encontrado."
        )



preencher(
    "cep",
    "06410000"
)


preencher(
    "logradouro",
    "Rua CT30 Teste"
)


preencher(
    "bairro",
    "Centro CT30"
)


preencher(
    "numero",
    "200"
)


preencher(
    "cidade",
    "Barueri"
)



# Estado

try:

    estado = driver.find_element(
        By.ID,
        "estado"
    )

    estado.send_keys(
        "SP"
    )

except:

    print(
        "Campo estado não localizado."
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
        "\nAlteração de endereço realizada com sucesso!"
    )

else:

    print(
        "\nERRO: sistema não confirmou alteração."
    )



driver.quit()


print("\nCT30 finalizado!")