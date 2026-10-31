from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time


print("TM01 - Navegação dos links pelo teclado")


driver = webdriver.Chrome()
driver.maximize_window()



driver.get(
    "http://127.0.0.1:5000"
)

time.sleep(3)



links = driver.find_elements(
    By.TAG_NAME,
    "a"
)


print("Quantidade de links encontrados:")
print(len(links))



if len(links) == 0:

    print("\nERRO: nenhum link encontrado.")

    driver.quit()
    quit()



driver.find_element(
    By.TAG_NAME,
    "body"
).click()



links_focados = 0



for i in range(10):

    driver.switch_to.active_element.send_keys(
        Keys.TAB
    )

    time.sleep(0.5)



    elemento = driver.execute_script(
        "return document.activeElement;"
    )


    tag = elemento.tag_name

    texto = elemento.text.strip()



    print(
        f"Foco {i+1}: {tag} - {texto}"
    )



    if tag == "a":

        links_focados += 1



print("\nLinks focados:")
print(links_focados)



if links_focados > 0:

    print("\nTM01 aprovado!")
    print("Links acessíveis pelo teclado.")


else:

    print("\nERRO!")
    print("Nenhum link recebeu foco pelo TAB.")



driver.quit()


print("\nTM01 finalizado!")