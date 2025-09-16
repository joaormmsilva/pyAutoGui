import pyautogui, time

window = pyautogui.getActiveWindow()
print(window)
print(window.size)
print(window.left, window.right)

window.maximize()
time.sleep(2)
window.minimize()
time.sleep(2)
window.restore()