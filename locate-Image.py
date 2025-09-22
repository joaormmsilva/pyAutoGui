import pyautogui, time

pyautogui.PAUSE = 1
pyautogui.alert('Abra a calculadora para o robo começar ')


five = pyautogui.locateOnScreen('five.png', grayscale=True)
two = pyautogui.locateOnScreen('two.png', grayscale=True)
equal = pyautogui.locateOnScreen('equal.png', grayscale=True)
sum = pyautogui.locateOnScreen('sum.png', grayscale=True)
delete = pyautogui.locateOnScreen('delete.png', grayscale=True)
print(five)

pyautogui.moveTo(five,duration=0.5)
pyautogui.click()

pyautogui.moveTo(sum, duration=0.5)
pyautogui.click()

pyautogui.moveTo(two,duration=0.5)
pyautogui.click()

pyautogui.moveTo(equal,duration=0.5)
pyautogui.click()

time.sleep(3)

pyautogui.moveTo(delete, duration=1)
pyautogui.click()