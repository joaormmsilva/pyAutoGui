import pyautogui,time

alert = pyautogui.alert('esse é uma mensagem importante', 'importante')
confirma = pyautogui.confirm('vc deseja continuar?')
prompt = pyautogui.prompt('qual é seu nome?')
password = pyautogui.password('digite sua senha')
print(password)