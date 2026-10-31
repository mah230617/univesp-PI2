from selenium import webdriver
from selenium.webdriver.common.by import By
import time


print("CT44 - Usuário protegido")


driver = webdriver.Chrome()
driver.maximize_window()



# =====================================
# LOGIN ADMIN
# =====================================

print("Abrindo login...")


driver.get(
    "http://127.0.0.1:5000"
)

time.sleep(2)


driver.find_element(
    By.ID,
    "username"
).send_keys("projeto.admin")


driver.find_element(
    By.ID,
    "senha"
).send_keys("mudar@123")


driver.find_element(
    By.XPATH,
    "//button[@type='submit']"
).click()


time.sleep(3)



# =====================================
# ABRIR LISTA DE USUÁRIOS
# =====================================

print("Abrindo usuários...")


driver.get(
    "http://127.0.0.1:5000/usuario/lista"
)


time.sleep(3)



texto = driver.find_element(
    By.TAG_NAME,
    "body"
).text



print("\nLista:")
print(texto[:1000])



# =====================================
# PROCURAR ADMINISTRADOR
# =====================================

if "projeto.admin" not in texto.lower():

    print("\nERRO: usuário administrador não encontrado.")

else:

    print("\nAdministrador encontrado.")



    # tenta localizar linha do administrador
    linha_admin = driver.find_elements(
        By.XPATH,
        "//tr[contains(translate(.,'ABCDEFGHIJKLMNOPQRSTUVWXYZ','abcdefghijklmnopqrstuvwxyz'),'projeto.admin')]"
    )



    if len(linha_admin) == 0:

        print("\nCT44 concluído.")
        print("Administrador existe, mas não possui ação disponível.")

    else:

        print("\nLinha do administrador encontrada.")



        botoes = linha_admin[0].find_elements(
            By.TAG_NAME,
            "a"
        )


        if len(botoes) == 0:

            print("\nCT44 aprovado!")
            print("Usuário protegido sem alteração disponível.")

        else:

            botoes[0].click()

            time.sleep(3)


            retorno = driver.find_element(
                By.TAG_NAME,
                "body"
            ).text


            print("\nRetorno:")
            print(retorno[:800])



            if (
                "não permitido" in retorno.lower()
                or "protegido" in retorno.lower()
                or "erro" in retorno.lower()
            ):

                print("\nCT44 aprovado!")
                print("Sistema protegeu o usuário.")

            else:

                print("\nATENÇÃO!")
                print("Sistema permitiu alteração do administrador.")



driver.quit()


print("\nCT44 finalizado!")