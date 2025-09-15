import pyautogui, time

time.sleep(3)
pyautogui.write('hellow word!')

pyautogui.hotkey('ctrl','a')
pyautogui.hotkey('ctrl','c')
pyautogui.write(['right'])
pyautogui.hotkey('ctrl','v')


pyautogui.keyDown('shift')
pyautogui.press('4')
pyautogui.keyUp('shift')
