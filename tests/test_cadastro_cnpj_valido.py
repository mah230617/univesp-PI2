from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


print("CT15 - Cadastro de cliente com CNPJ válido")


driver = webdriver.Chrome()
driver.maximize_window()

wait = WebDriverWait(driver, 10)


try:

    # ==============================
    # LOGIN
    # ==============================

    print("Abrindo login...")

    driver.get(
        "http://127.0.0.1:5000"
    )


    wait.until(
        EC.presence_of_element_located(
            (By.ID, "username")
        )
    )


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



    # ==============================
    # ABRIR CADASTRO
    # ==============================

    print("Abrindo cadastro...")


    driver.get(
        "http://127.0.0.1:5000/cliente/novo"
    )


    wait.until(
        EC.presence_of_element_located(
            (By.ID,"cpfcnpj")
        )
    )



    print("Preenchendo cadastro CNPJ...")



    # ==============================
    # DADOS CLIENTE
    # ==============================


    driver.find_element(
        By.ID,
        "nome"
    ).send_keys(
        "Empresa CNPJ Teste"
    )


    campo_cnpj = driver.find_element(
        By.ID,
        "cpfcnpj"
    )


    campo_cnpj.clear()


    # Digitação lenta para respeitar máscara JS
    for numero in "91258662000111":

        campo_cnpj.send_keys(numero)

        time.sleep(0.15)



    time.sleep(1)


    cnpj_exibido = campo_cnpj.get_attribute(
        "value"
    )


    print(
        "CNPJ exibido no campo:"
    )

    print(
        cnpj_exibido
    )



    driver.find_element(
        By.ID,
        "email"
    ).send_keys(
        "empresa.teste@email.com"
    )


    driver.find_element(
        By.ID,
        "telefone"
    ).send_keys(
        "11333334444"
    )


    driver.find_element(
        By.ID,
        "data_nascimento"
    ).send_keys(
        "01012000"
    )


    driver.find_element(
        By.ID,
        "cep"
    ).send_keys(
        "06400000"
    )


    driver.find_element(
        By.ID,
        "logradouro"
    ).send_keys(
        "Avenida Empresa"
    )


    driver.find_element(
        By.ID,
        "bairro"
    ).send_keys(
        "Centro"
    )


    driver.find_element(
        By.ID,
        "numero"
    ).send_keys(
        "200"
    )


    driver.find_element(
        By.ID,
        "cidade"
    ).send_keys(
        "Barueri"
    )



    estado = Select(
        driver.find_element(
            By.ID,
            "estado"
        )
    )


    estado.select_by_value(
        "SP"
    )



    # ==============================
    # ENVIO
    # ==============================


    driver.find_element(
        By.XPATH,
        "//button[@type='submit']"
    ).click()


    time.sleep(4)



    pagina = driver.page_source



    print()

    print(
        "URL final:"
    )

    print(
        driver.current_url
    )



    # ==============================
    # RESULTADO
    # ==============================


    if "Cliente criado com sucesso" in pagina:

        print()

        print(
            "CNPJ válido aceito corretamente!"
        )


    elif "CPF / CNPJ inválido" in pagina:

        print()

        print(
            "ERRO!"
        )

        print(
            "O JavaScript considerou o CNPJ inválido."
        )

        print()

        print(
            "CNPJ enviado:"
        )

        print(
            cnpj_exibido
        )


    else:

        print()

        print(
            "ERRO!"
        )

        print(
            "Cadastro não concluído."
        )


        print()

        print(
            "Primeiros 2000 caracteres:"
        )

        print(
            pagina[:2000]
        )



finally:


    driver.quit()


print()

print(
    "CT15 finalizado!"
)