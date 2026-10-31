from selenium import webdriver
from selenium.webdriver.common.by import By
import time


print("TM07 - Máscaras funcionando")


driver = webdriver.Chrome()
driver.maximize_window()


resultado = {}


try:

    # ==========================
    # LOGIN
    # ==========================

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



    # ==========================
    # CADASTRO CLIENTE
    # ==========================

    print("Abrindo cadastro...")


    driver.get(
        "http://127.0.0.1:5000/cliente/novo"
    )


    time.sleep(3)



    # ==========================
    # TELEFONE
    # ==========================

    print("Testando telefone...")


    telefone = driver.find_element(
        By.NAME,
        "telefone"
    )


    telefone.clear()


    telefone.send_keys(
        "11999998888"
    )


    time.sleep(1)


    valor_telefone = telefone.get_attribute(
        "value"
    )


    print(
        "Telefone:",
        valor_telefone
    )


    resultado["telefone"] = (
        valor_telefone == "(11) 99999-8888"
    )



    # ==========================
    # CEP
    # ==========================

    print("Testando CEP...")


    cep = driver.find_element(
        By.NAME,
        "cep"
    )


    cep.clear()


    cep.send_keys(
        "06400000"
    )


    time.sleep(1)


    valor_cep = cep.get_attribute(
        "value"
    )


    print(
        "CEP:",
        valor_cep
    )


    resultado["cep"] = (
        valor_cep == "06400-000"
    )



    # ==========================
    # DATA NASCIMENTO
    # ==========================

    print("Testando data...")


    data = driver.find_element(
        By.NAME,
        "data_nascimento"
    )


    data.clear()


    data.send_keys(
        "01012000"
    )


    time.sleep(1)


    valor_data = data.get_attribute(
        "value"
    )


    print(
        "Data:",
        valor_data
    )


    resultado["data"] = (
        valor_data == "01/01/2000"
    )



    # ==========================
    # RESULTADO
    # ==========================

    print("\nResultado:")
    print(resultado)



    if all(resultado.values()):

        print("\nTM07 aprovado!")
        print("Todas as máscaras funcionam.")


    else:

        print("\nERRO!")

        for campo, status in resultado.items():

            if not status:

                print(
                    "Falhou:",
                    campo
                )


finally:

    driver.quit()


print("\nTM07 finalizado!")