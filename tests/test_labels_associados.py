from selenium import webdriver
from selenium.webdriver.common.by import By
import time


print("TM05 - Labels associados corretamente")


driver = webdriver.Chrome()
driver.maximize_window()



driver.get(
    "http://127.0.0.1:5000/cliente/novo"
)


time.sleep(3)



labels = driver.find_elements(
    By.TAG_NAME,
    "label"
)



print("Quantidade de labels:")
print(len(labels))



erros = []



for label in labels:

    alvo = label.get_attribute("for")


    # ignora labels sem for
    if alvo:


        campos = driver.find_elements(
            By.ID,
            alvo
        )


        if len(campos) == 0:

            erros.append(alvo)



print("\nLabels apontando para campos inexistentes:")
print(erros)



if len(erros) == 0:

    print("\nTM05 aprovado!")
    print("Todos os labels estão associados corretamente.")


else:

    print("\nERRO!")
    print("Existem labels sem associação válida.")



driver.quit()


print("\nTM05 finalizado!")