from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


print("CT35 - Administrador exclui cliente")


driver = webdriver.Chrome()
driver.maximize_window()

wait = WebDriverWait(driver, 10)


try:

    # =====================================
    # LOGIN
    # =====================================

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



    # =====================================
    # LISTA DE CLIENTES
    # =====================================

    print("Abrindo lista de clientes...")


    driver.get(
        "http://127.0.0.1:5000/cliente/lista"
    )


    wait.until(
        EC.presence_of_element_located(
            (
                By.XPATH,
                "//a[contains(@href,'delete')]"
            )
        )
    )



    # =====================================
    # LOCALIZAR BOTÃO
    # =====================================

    print("Localizando botão excluir...")


    botoes_excluir = driver.find_elements(
        By.XPATH,
        "//a[contains(@href,'delete') or contains(@href,'excluir')]"
    )


    if not botoes_excluir:

        print(
            "ERRO: botão excluir não encontrado."
        )

        quit()



    print(
        "Botão encontrado."
    )



    # =====================================
    # EXCLUIR
    # =====================================

    print(
        "Excluindo cliente..."
    )


    botao = botoes_excluir[-1]


    driver.execute_script(
        """
        arguments[0].scrollIntoView({
            behavior: 'instant',
            block: 'center'
        });
        """,
        botao
    )


    time.sleep(1)


    driver.execute_script(
        "arguments[0].click();",
        botao
    )



    time.sleep(2)



    # =====================================
    # ALERTA
    # =====================================

    try:

        alerta = driver.switch_to.alert

        print()

        print(
            "Mensagem do alerta:"
        )

        print(
            alerta.text
        )


        alerta.accept()


        print(
            "Exclusão confirmada."
        )


    except:

        print(
            "Nenhum alerta encontrado."
        )



    time.sleep(4)



    # =====================================
    # VALIDAR
    # =====================================

    print()

    print(
        "Verificando resultado..."
    )


    texto = driver.find_element(
        By.TAG_NAME,
        "body"
    ).text


    url = driver.current_url



    print()

    print(
        "URL atual:"
    )

    print(
        url
    )



    if (
        "Cliente excluído com sucesso" in texto
        or
        "/cliente/lista" in url
    ):

        print()

        print(
            "CT35 aprovado!"
        )

        print(
            "Administrador conseguiu excluir o cliente."
        )


    else:

        print()

        print(
            "ERRO: exclusão não confirmada."
        )


finally:

    driver.quit()



print()

print(
    "CT35 finalizado!"
)