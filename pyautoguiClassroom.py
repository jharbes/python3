# Utilizando biblioteca de automacao pyautogui

import pyautogui
import time # para usar o time.sleep()

pyautogui.click # clique com o mouse
pyautogui.write # escrever um texto
pyautogui.press # apertar uma tecla
pyautogui.hotkey # apertar uma combinacao de teclas, ex: CTRL+D

# Passo a passo

# Passo 1: Entrar no sistema da empresa (no link)

## Com o navegador fechado:
pyautogui.press('win')
pyautogui.write('chrome')
pyautogui.press('enter')
time.sleep(5) # faz esperar cinco segundos antes do proximo comando
pyautogui.write('https://pages.hashtagtreinamentos.com/aula1-intensivao-sistema')
pyautogui.press('enter')

## Com o navegador aberto:
# pyautogui.hotkey('ctrl', 't')
# pyautogui.write('https://pages.hashtagtreinamentos.com/aula1-intensivao-sistema')
# pyautogui.press('enter')



# Passo 2: Fazer login

## Clicar no espaço de login e escrever o login

#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!https://pages.hashtagtreinamentos.com/aula1-intensivao-sistema

# utilizaremos os procedimentos abaixo para descobrir qual a posicao do mouse na tela na aba de navegacao ou qualquer outra tela desejada, o time sera o tempo habil de posicionar onde quer o mouse, depois ele ira printar o ponto exato desejado
# time.sleep(5)
# print(pyautogui.position())
time.sleep(3)
pyautogui.click(x=700, y=371)
pyautogui.write('teste')