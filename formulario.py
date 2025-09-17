import pyautogui,time
nome = ['fabio','joao','nicolas']
filme = ['A chegada','coraline','os incriveis']
idade = [20,56,12]
nota = [3,5,1]
comentario = ['bom','top','ruim']

pyautogui.mouseInfo()
pyautogui.alert('Abra o fomulario')
for i in range(3):
    pyautogui.click()
    

    pyautogui.moveTo(677,430, duration=0.25)
    pyautogui.click()
    pyautogui.write(nome[i])

    pyautogui.scroll(-200)
    
    pyautogui.moveTo(694,407, duration=0.25)
    pyautogui.click()
    pyautogui.write(filme[i])

    pyautogui.moveTo(724,577, duration=0.25)
    pyautogui.click()
    if idade[i] < 19 :
        pyautogui.moveTo(696,794, duration=0.25)
        pyautogui.click()
    elif idade[i] <= 35:
        pyautogui.moveTo(703,838, duration=0.25)
        pyautogui.click()
    elif idade[i] <= 50:
        pyautogui.moveTo(701,884, duration=0.25)
        pyautogui.click()
    elif idade[i] <= 70:
        pyautogui.moveTo(705,936, duration=0.25)
        pyautogui.click()
    elif idade[i] >= 71:
        pyautogui.moveTo(713,983, duration=0.25)
        pyautogui.click()
    
    if nota[i] == 1:
        pyautogui.moveTo(788,761, duration=0.25)
        pyautogui.click()
    elif nota[i] == 2:
        pyautogui.moveTo(867,766, duration=0.25)
        pyautogui.click()
    elif nota[i] == 3:
        pyautogui.moveTo(941,765, duration=0.25)
        pyautogui.click()
    elif nota[i] == 4:
        pyautogui.moveTo(1017,763, duration=0.25)
        pyautogui.click()
    elif nota[i] == 5:
        pyautogui.moveTo(1083,764, duration=0.25)
        pyautogui.click()

    pyautogui.moveTo(719,958, duration=0.25)
    pyautogui.click()
    pyautogui.write(comentario[i])

    pyautogui.moveTo(691,1024, duration=0.25)
    pyautogui.click()

    time.sleep(1)
    pyautogui.moveTo(702,247, duration=0.25)
    pyautogui.click()

