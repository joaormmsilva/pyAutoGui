import pyautogui, time

time.sleep(5)

distancia = 300
change = 20

while distancia > 0:
    pyautogui.drag(distancia, 0, duration=0.2)
    distancia -= change
    pyautogui.drag(0, distancia, duration=0.2)
    pyautogui.drag(-distancia, 0, duration=0.2)
    distancia -= change
    pyautogui.drag(0, -distancia, duration=0.2)