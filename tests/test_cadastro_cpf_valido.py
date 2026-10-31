from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time


print("CT14 - Cadastro de cliente com CPF válido")


driver = webdriver.Chrome()
driver.maximize_window()


try:

    # =========================
    # LOGIN
    # =========================

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
    # CADASTRO
    # =========================

    driver.get(
        "http://127.0.0.1:5000/cliente/novo"
    )

    time.sleep(3)


    print("Preenchendo cadastro CPF...")


    driver.find_element(
        By.ID,
        "nome"
    ).send_keys(
        "Cliente CPF Teste"
    )


    # =========================
    # CPF COM DIGITAÇÃO LENTA
    # =========================

    cpf = "22879268877"


    campo_cpf = driver.find_element(
        By.ID,
        "cpfcnpj"
    )


    campo_cpf.clear()


    for numero in cpf:

        campo_cpf.send_keys(
            numero
        )

        time.sleep(0.15)


    time.sleep(1)


    print(
        "CPF exibido no campo:"
    )

    print(
        campo_cpf.get_attribute(
            "value"
        )
    )



    driver.find_element(
        By.ID,
        "data_nascimento"
    ).send_keys(
        "10/05/1995"
    )


    driver.find_element(
        By.ID,
        "email"
    ).send_keys(
        "cpf.teste@email.com"
    )


    driver.find_element(
        By.ID,
        "telefone"
    ).send_keys(
        "11988887777"
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
        "Rua Teste CPF"
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
        "50"
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



    # =========================
    # SALVAR
    # =========================

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



    if "Cliente criado com sucesso" in pagina:

        print(
            "CPF válido aceito corretamente!"
        )


    elif "CPF / CNPJ inválido" in pagina:

        print(
            "ERRO: CPF considerado inválido."
        )


    else:

        print(
            "CPF válido não foi aceito ou cadastro falhou."
        )


finally:

    driver.quit()


print(
    "CT14 finalizado!"
)