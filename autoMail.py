import pyautogui,time,pyperclip

pyautogui.PAUSE = 1
pyautogui.alert('Abra o Chrome para começar o robo')

pyautogui.hotkey("ctrl", "t")
pyperclip.copy('https://mail.google.com/mail/u/1/#inbox')
pyautogui.hotkey("ctrl", "v")
pyautogui.press('enter')

time.sleep(3)

compose = pyautogui.locateOnScreen('compose.png', grayscale=True)


for _ in range(3):
    pyautogui.moveTo(compose,duration=0.2)
    pyautogui.click()

    pyautogui.write('joaormms@gmal.com',)
    pyautogui.press('enter')

    pyautogui.press('tab')
    pyautogui.write('teste de automacao')

    pyautogui.press('tab')
    pyautogui.write('teste de automacao')   

    pyautogui.press('tab')
    pyautogui.press('enter')

