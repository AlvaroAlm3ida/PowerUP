# Passo 1 - entrar no sistema da empresa
#   Link do sistema da empresa: https://dlp.hashtagtreinamentos.com/python/intensivao/login

# Passo 2 - Fazer login

# Passo 3 - Pegar/ importar base de dados

# Passo 4 - Cadastrar um produto

# Passo 5 - Repetir o passo 4 até cadastrar todos os produtos.

import pyautogui
import time

# pyautogui.click -  clicar com o mouse
# pyautogui.write -  escrever um texto
# pyautogui.press - apertar 1 tecla
# pyautogui.hotkey - combinação de teclas (Ctrl C)
# pyautogui.scroll - rolar a tela para cima ou para baixo

pyautogui.PAUSE = 0.5

# Passo 1 - entrar no sistema da empresa
# abrir o navegador
pyautogui.press("win")
pyautogui.write("chrome")
pyautogui.press("enter")

time.sleep(3)

# Entrar no login: https://dlp.hashtagtreinamentos.com/python/intensivao/login
pyautogui.write("https://dlp.hashtagtreinamentos.com/python/intensivao/login")
pyautogui.press("enter")

time.sleep(3)

# Passo 2 - Fazer login
pyautogui.click(x=848, y=466)
pyautogui.hotkey("Ctrl", "a") #seleciona tudo
pyautogui.write("Teste@gmail.com")

# Passar para o campo de senha 
pyautogui.press("Tab")
pyautogui.write("senha")

pyautogui.click(x=944, y=620)

time.sleep(3)

# Passo 3 - Importar a base de dados
import pandas

tabela = pandas.read_csv("produtos.csv")

print(tabela)

# Passo 4 - Cadastrar um produto
# Para cada linha da minha tabela:
for linha in tabela.index:
    # codigo
    pyautogui.click(x=656, y=337)

    codigo = str(tabela.loc[linha, "codigo"]) # string = texto
    pyautogui.write("Codigo")

    # marca
    marca = str(tabela.loc[linha, "marca"])
    pyautogui.press("tab")
    pyautogui.write("marca")

    # categoria
    categoria = str(tabela.loc[linha, "categoria"])
    pyautogui.press("tab")
    pyautogui.write("categoria")

    # preco_unitario
    preco_unitario = str(tabela.loc[linha, "preco_unitario"])
    pyautogui.press("tab")
    pyautogui.write("preco_unitario")

    # custo
    custo = str(tabela.loc[linha, "custo"])
    pyautogui.press("tab")
    pyautogui.write("custo")

    # obs 
    obs = str(tabela.loc[linha, "obs"])
    pyautogui.press("tab")
    if obs != "nan":     # Ele irá escrever se o OBS for diferente de nan
     pyautogui.write("obs")

    # Clicar no botão de enviar 
    pyautogui.press("tab")
    pyautogui.press("enter")

    pyautogui.scroll(1000)

    # Passo 5 - Repetir para todas as linhas da tabela
