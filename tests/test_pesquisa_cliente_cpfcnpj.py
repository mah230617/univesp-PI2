from selenium import webdriver
from selenium.webdriver.common.by import By
import time


print("CT26 - Pesquisa de cliente por CPF/CNPJ")


driver = webdriver.Chrome()
driver.maximize_window()


try:

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
    # PESQUISA
    # =========================

    print(
        "Pesquisando cliente pelo CPF/CNPJ..."
    )


    driver.get(
        "http://127.0.0.1:5000/cliente/lista"
    )


    time.sleep(3)


    campo = driver.find_element(
        By.NAME,
        "cpfcnpj"
    )


    campo.send_keys(
        "52998224725"
    )


    driver.find_element(
        By.XPATH,
        "//button[@type='submit']"
    ).click()


    time.sleep(3)



    # =========================
    # VALIDAR
    # =========================

    texto = driver.find_element(
        By.TAG_NAME,
        "body"
    ).text


    print()

    print("Resultado encontrado:")

    print(
        texto[:1000]
    )


    if (
        "Cliente CPF Teste" in texto
        and
        (
            "529.982.247-25" in texto
            or
            "52998224725" in texto
        )
    ):

        print()

        print(
            "CT26 aprovado!"
        )

        print(
            "Pesquisa por CPF/CNPJ funcionando corretamente."
        )


    else:

        print()

        print(
            "ERRO: cliente não encontrado pelo CPF/CNPJ."
        )



    print()

    print("URL atual:")

    print(
        driver.current_url
    )


finally:

    driver.quit()


print()

print(
    "CT26 finalizado!"
)