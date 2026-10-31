from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


print("CT17 - Cadastro com CNPJ já existente")


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
            (By.ID, "cpfcnpj")
        )
    )



    # ==============================
    # PREENCHER DADOS
    # ==============================

    print("Tentando cadastrar CNPJ existente...")


    driver.find_element(
        By.ID,
        "nome"
    ).send_keys(
        "Empresa CNPJ Duplicada CT17"
    )



    # CNPJ que já existe no banco
    cnpj_existente = "11222333000181"


    campo_cnpj = driver.find_element(
        By.ID,
        "cpfcnpj"
    )


    campo_cnpj.clear()


    # Digitação lenta para máscara JS
    for numero in cnpj_existente:

        campo_cnpj.send_keys(numero)

        time.sleep(0.15)



    time.sleep(1)


    cnpj_exibido = campo_cnpj.get_attribute(
        "value"
    )


    print()

    print("CNPJ exibido:")

    print(cnpj_exibido)



    driver.find_element(
        By.ID,
        "data_nascimento"
    ).send_keys(
        "01012000"
    )


    driver.find_element(
        By.ID,
        "email"
    ).send_keys(
        "empresa.duplicada.ct17@email.com"
    )


    driver.find_element(
        By.ID,
        "telefone"
    ).send_keys(
        "11333334444"
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
        "Avenida Teste"
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


    driver.find_element(
        By.ID,
        "estado"
    ).send_keys(
        "SP"
    )



    # ==============================
    # SALVAR
    # ==============================

    print()

    print("Salvando...")


    driver.find_element(
        By.XPATH,
        "//button[@type='submit']"
    ).click()


    time.sleep(4)



    # ==============================
    # VALIDAR
    # ==============================

    pagina = driver.page_source

    texto = driver.find_element(
        By.TAG_NAME,
        "body"
    ).text



    print()

    print("URL atual:")

    print(
        driver.current_url
    )


    print()

    print("Mensagem:")

    print(
        texto[:1000]
    )



    if "já está cadastrado no sistema" in texto:

        print()

        print(
            "CT17 aprovado!"
        )

        print(
            "CNPJ duplicado bloqueado corretamente."
        )


    elif "Cliente criado com sucesso" in texto:

        print()

        print(
            "ERRO: CNPJ duplicado foi aceito!"
        )


    else:

        print()

        print(
            "ERRO: retorno inesperado."
        )

        print(
            "CNPJ enviado:"
        )

        print(
            cnpj_exibido
        )


finally:

    driver.quit()


print()

print(
    "CT17 finalizado!"
)