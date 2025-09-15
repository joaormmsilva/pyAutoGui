import pyautogui

window = pyautogui.getActiveWindow()
print(window)
print(window.size)
print(window.left, window.right)