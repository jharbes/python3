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
time.sleep(3) # faz esperar dois segundos antes do proximo comando
pyautogui.write('https://pages.hashtagtreinamentos.com/aula1-intensivao-sistema')
pyautogui.press('enter')

## Com o navegador aberto:
# pyautogui.hotkey('ctrl', 't')
# pyautogui.write('https://pages.hashtagtreinamentos.com/aula1-intensivao-sistema')
# pyautogui.press('enter')