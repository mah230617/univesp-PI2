from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import random


print("CT28 - Lista atualizada após novo cadastro")


driver = webdriver.Chrome()
driver.maximize_window()

wait = WebDriverWait(driver, 10)


try:

    # =========================
    # LOGIN
    # =========================

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



    # =========================
    # ABRIR CADASTRO
    # =========================

    print("Abrindo cadastro de cliente...")


    driver.get(
        "http://127.0.0.1:5000/cliente/novo"
    )


    wait.until(
        EC.presence_of_element_located(
            (By.ID, "cpfcnpj")
        )
    )



    # =========================
    # DADOS CLIENTE
    # =========================

    numero = random.randint(100,999)


    nome_cliente = (
        f"Cliente CT28 {numero}"
    )


    # CNPJ válido conforme validação do projeto
    cpfcnpj = "16108005000172"


    email = (
        f"cliente.ct28.{numero}@teste.com"
    )


    print("Cliente:")
    print(nome_cliente)
    print(cpfcnpj)



    # =========================
    # PREENCHIMENTO
    # =========================


    driver.find_element(
        By.ID,
        "nome"
    ).send_keys(
        nome_cliente
    )



    # CPF/CNPJ com digitação lenta
    campo_cnpj = driver.find_element(
        By.ID,
        "cpfcnpj"
    )


    campo_cnpj.clear()


    for numero_cnpj in cpfcnpj:

        campo_cnpj.send_keys(
            numero_cnpj
        )

        time.sleep(0.15)



    time.sleep(1)



    print(
        "CNPJ exibido no campo:"
    )

    print(
        campo_cnpj.get_attribute(
            "value"
        )
    )



    driver.find_element(
        By.ID,
        "email"
    ).send_keys(
        email
    )


    driver.find_element(
        By.ID,
        "telefone"
    ).send_keys(
        "11999999999"
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
        "Rua Teste"
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
        "100"
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

    print(
        "Salvando cliente..."
    )


    driver.find_element(
        By.XPATH,
        "//button[@type='submit']"
    ).click()


    time.sleep(5)



    print(
        "\nURL após salvar:"
    )

    print(
        driver.current_url
    )



    texto = driver.find_element(
        By.TAG_NAME,
        "body"
    ).text



    print(
        "\nMensagem:"
    )

    print(
        texto[:1000]
    )



    if "Cliente criado com sucesso" in texto:

        print(
            "\nCadastro realizado!"
        )

    elif "CPF / CNPJ inválido!" in texto:

        print(
            "\nERRO: CNPJ considerado inválido."
        )

    elif "já está cadastrado" in texto:

        print(
            "\nERRO: CNPJ duplicado."
        )

    else:

        print(
            "\nERRO: Cadastro não concluído."
        )



    # =========================
    # VALIDAR LISTA
    # =========================

    print(
        "\nAbrindo lista..."
    )


    driver.get(
        "http://127.0.0.1:5000/cliente/lista"
    )


    time.sleep(4)



    pagina = driver.page_source



    if nome_cliente in pagina:

        print(
            "\nCT28 APROVADO!"
        )

        print(
            "Cliente apareceu na lista corretamente."
        )


    else:

        print(
            "\nERRO: cliente não apareceu na lista!"
        )



finally:

    driver.quit()



print(
    "\nCT28 finalizado!"
)