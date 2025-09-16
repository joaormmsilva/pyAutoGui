import pyautogui,time
nome = ['fabio','joao','nicolas']
filme = ['A chegada','coraline','os incriveis']
idade = [20,56,12]
nota = [3,5,1]
comentario = ['bom','top','ruim']

time.sleep(2)
for i in range(3):
    pyautogui.click()
    

    pyautogui.moveTo(415,435, duration=0.25)
    pyautogui.click()
    pyautogui.write(nome[i])

    pyautogui.scroll(-200)
    
    pyautogui.moveTo(344,422, duration=0.25)
    pyautogui.click()
    pyautogui.write(filme[i])

    pyautogui.moveTo(316,566, duration=0.25)
    pyautogui.click()
    if idade[i] < 19:
        pyautogui.moveTo(329,636, duration=0.25)
        pyautogui.click()
    elif idade[i] < 36:
        pyautogui.moveTo(329,683, duration=0.25)
        pyautogui.click()
    elif idade[i] < 51:
        pyautogui.moveTo(329,683, duration=0.25)
        pyautogui.click()
    elif idade[i] < 71:
        pyautogui.moveTo(347,774, duration=0.25)
        pyautogui.click()
    else:
        pyautogui.moveTo(333,844, duration=0.25)
        pyautogui.click()
    
    if nota[i] == 1:
        pyautogui.moveTo(408,770, duration=0.25)
        pyautogui.click()
    elif nota[i] == 2:
        pyautogui.moveTo(478,772, duration=0.25)
        pyautogui.click()
    elif nota[i] == 3:
        pyautogui.moveTo(557,774, duration=0.25)
        pyautogui.click()
    elif nota[i] == 4:
        pyautogui.moveTo(628,765, duration=0.25)
        pyautogui.click()
    elif nota[i] == 5:
        pyautogui.moveTo(706,774, duration=0.25)
        pyautogui.click()

    pyautogui.moveTo(353,959, duration=0.25)
    pyautogui.click()
    pyautogui.write(comentario[i])

    pyautogui.moveTo(309,1026, duration=0.25)
    pyautogui.click()

    time.sleep(1)
    pyautogui.moveTo(327,245, duration=0.25)
    pyautogui.click()