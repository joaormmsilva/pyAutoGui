import pyautogui,time,pyperclip, openpyxl

pyautogui.PAUSE = 1
pyautogui.alert('Abra o Chrome para começar o robo')

pyautogui.hotkey("ctrl", "t")
pyperclip.copy('https://mail.google.com/mail/u/1/#inbox')
pyautogui.hotkey("ctrl", "v")
pyautogui.press('enter')

time.sleep(3)

compose = pyautogui.locateOnScreen('compose.png', grayscale=True)

wb = openpyxl.load_workbook('testeAuto.xlsx')
sheet = wb['Planilha1']
print(sheet)
products = {}
for row in sheet.iter_rows(min_row=2, max_row=10, min_col=1, max_col=3, values_only=True):
    product ={
        "to": row[0],
        "Object": row[1],
        "mail": row[2]
    }

    pyautogui.moveTo(compose,duration=0.2)
    pyautogui.click()

    pyautogui.write(product['to'])
    pyautogui.press('enter')

    pyautogui.press('tab')
    pyautogui.write(product['Object'])

    pyautogui.press('tab')
    pyautogui.write(product['mail'])   

    pyautogui.press('tab')
    pyautogui.press('enter')