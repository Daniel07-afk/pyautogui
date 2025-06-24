import pyautogui

pyautogui.press('Win') #Usando para prescionar uma tecla desejada
pyautogui.sleep(1) # usando para ajustar o tempo de execução entre uma ordem e outra
pyautogui.write('Google Chrome', interval=0.2) # utilizando para escrever
pyautogui.press('Enter')
pyautogui.sleep(1)
pyautogui.write('Senai - Santana de Parnaíba', interval=0.1)
pyautogui.press('Enter')
pyautogui.sleep(1)
pyautogui.moveTo(906,507, duration=0.4) #Utilizando para mover o mouse nas coordenadas de X e Y
pyautogui.click() #clica com o botão esquerdo do mouse 
pyautogui.sleep(1)
pyautogui.hotkey('shift', 'win', 's')
pyautogui.sleep(1)
pyautogui.moveTo(811,226, duration=0.5)

#clica e arrasta até o ponto final do recorte

pyautogui.mouseDown()
pyautogui.moveTo(1751,1025, duration=0.5)
pyautogui.mouseUp()
pyautogui.sleep(2)
pyautogui.press('Win')
pyautogui.sleep(1)
pyautogui.write('Paint', interval=0.2)
pyautogui.press('Enter')
pyautogui.sleep(2)
pyautogui.hotkey('ctrl', 'v')

#fim