import pyautogui

shot = pyautogui.screenshot()
print(shot.getpixel((10,10)))
print(pyautogui.pixel(50,200))
# shot.save('test.jpg')