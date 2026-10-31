from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time


print("TM02 - Ordem do TAB")


driver = webdriver.Chrome()
driver.maximize_window()


driver.get(
    "http://127.0.0.1:5000"
)

time.sleep(3)



print("Iniciando navegação por teclado...")


body = driver.find_element(
    By.TAG_NAME,
    "body"
)

body.click()



elementos_focados = []



for i in range(15):

    driver.switch_to.active_element.send_keys(
        Keys.TAB
    )

    time.sleep(0.3)



    elemento = driver.execute_script(
        "return document.activeElement;"
    )


    tag = elemento.tag_name

    identificador = (
        elemento.get_attribute("id")
        or elemento.get_attribute("name")
        or elemento.text.strip()
        or tag
    )


    elementos_focados.append(
        identificador
    )


    print(
        f"TAB {i+1}: {identificador}"
    )



print("\nSequência encontrada:")
print(elementos_focados)



# verifica se o TAB realmente percorreu elementos diferentes

unicos = len(set(elementos_focados))



if unicos >= 3:

    print("\nTM02 aprovado!")
    print("Ordem de navegação pelo TAB funcionando.")


else:

    print("\nERRO!")
    print("TAB não percorreu elementos suficientes.")



driver.quit()


print("\nTM02 finalizado!")