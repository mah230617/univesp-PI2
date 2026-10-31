from selenium import webdriver
from selenium.webdriver.common.by import By
import time


print("TM14-TM18 - Teste de Responsividade")


driver = webdriver.Chrome()


try:

    driver.get("http://127.0.0.1:5000")

    time.sleep(2)


    tamanhos = {

        "TM14 - Desktop 1920px": (1920, 1080),

        "TM15 - Notebook": (1366, 768),

        "TM16 - Tablet": (768, 1024),

        "TM17 - Celular": (390, 844)

    }


    resultados = {}


    for teste, tamanho in tamanhos.items():

        print("\nTestando:", teste)


        driver.set_window_size(
            tamanho[0],
            tamanho[1]
        )


        time.sleep(2)


        try:

            # verifica se o conteúdo principal existe

            body = driver.find_element(
                By.TAG_NAME,
                "body"
            )


            visivel = body.is_displayed()


            resultados[teste] = visivel


            print(
                "Tela carregada corretamente"
            )


        except:

            resultados[teste] = False

            print(
                "Erro na resolução"
            )



    # ==========================
    # ZOOM 200%
    # ==========================

    print("\nTestando TM18 - Zoom 200%")


    driver.execute_script(
        "document.body.style.zoom='200%'"
    )


    time.sleep(3)


    try:

        body = driver.find_element(
            By.TAG_NAME,
            "body"
        )


        resultados["TM18 - Zoom 200%"] = (
            body.is_displayed()
        )


        print(
            "Zoom 200% funcionando"
        )


    except:

        resultados["TM18 - Zoom 200%"] = False

        print(
            "Falha no zoom"
        )



    print("\nResultado final:")

    for teste, resultado in resultados.items():

        print(
            teste,
            ":",
            "APROVADO" if resultado else "FALHOU"
        )



finally:

    driver.quit()


print("\nTestes finalizados!")