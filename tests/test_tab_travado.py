from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time


print("TM03 - Elementos presos no TAB")


driver = webdriver.Chrome()
driver.maximize_window()



driver.get(
    "http://127.0.0.1:5000"
)

time.sleep(3)



print("Iniciando navegação...")


driver.find_element(
    By.TAG_NAME,
    "body"
).click()



focos = []



for i in range(20):

    driver.switch_to.active_element.send_keys(
        Keys.TAB
    )

    time.sleep(0.3)



    elemento = driver.execute_script(
        "return document.activeElement;"
    )


    identificador = (
        elemento.get_attribute("id")
        or elemento.get_attribute("name")
        or elemento.text.strip()
        or elemento.tag_name
    )


    focos.append(
        identificador
    )


    print(
        f"TAB {i+1}: {identificador}"
    )



print("\nSequência:")
print(focos)



# verifica se o foco ficou preso

quantidade_unicos = len(set(focos))


print(
    "\nElementos diferentes encontrados:",
    quantidade_unicos
)



if quantidade_unicos >= 3:

    print("\nTM03 aprovado!")
    print("Nenhum elemento ficou preso no TAB.")


else:

    print("\nERRO!")
    print("Possível elemento preso no TAB.")



driver.quit()


print("\nTM03 finalizado!")