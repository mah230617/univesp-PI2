from selenium import webdriver
from selenium.webdriver.common.by import By
import time


print("TM04 - Inputs possuem labels")


driver = webdriver.Chrome()
driver.maximize_window()


driver.get(
    "http://127.0.0.1:5000/cliente/novo"
)

time.sleep(3)



inputs = driver.find_elements(
    By.TAG_NAME,
    "input"
)


print("Inputs encontrados:")
print(len(inputs))


sem_label = []


for campo in inputs:

    id_campo = campo.get_attribute("id")


    if id_campo:

        labels = driver.find_elements(
            By.CSS_SELECTOR,
            f"label[for='{id_campo}']"
        )


        if len(labels) == 0:

            sem_label.append(id_campo)



print("\nInputs sem label:")
print(sem_label)



if len(sem_label) == 0:

    print("\nTM04 aprovado!")
    print("Todos os inputs possuem label.")

else:

    print("\nERRO!")
    print("Existem inputs sem label.")



driver.quit()


print("\nTM04 finalizado!")