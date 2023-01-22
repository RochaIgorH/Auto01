import pyautogui
from time import sleep

# passos para dados funcionais
pyautogui.click(896, 25)

pyautogui.write("****")
pyautogui.hotkey("Enter")
sleep(1)
pyautogui.hotkey("Enter")
pyautogui.write("p")
pyautogui.write("s")
pyautogui.write("f")
pyautogui.write("s")
pyautogui.write("m")
sleep(1)
pyautogui.hotkey("Enter")
sleep(1)
# inserir número identificador
pyautogui.write("****")
pyautogui.hotkey("Enter")
sleep(1)
# copiar dados

pyautogui.click(27, 85)
sleep(1)
pyautogui.click(80, 98)
sleep(1)
pyautogui.click(1945, 65)
pyautogui.click(2180, 485)
pyautogui.click(button='right')

pyautogui.click(2191, 570)
sleep(1)

pyautogui.click(896, 25)
sleep(1)
# passos para demonstrativo
pyautogui.hotkey("F12")
sleep(1)
pyautogui.write("****")
sleep(1)
pyautogui.hotkey("Enter")
sleep(1)
# copiar mes demonstrativo
pyautogui.moveTo(2071, 260)
pyautogui.dragTo(2086, 263, 1, button='left')
pyautogui.click(button='right')
sleep(1)
pyautogui.click(2142, 326)
sleep(1)
pyautogui.click(247, 313, button='right')
sleep(1)
pyautogui.click(287, 332)

# copiar ano demonstrativo
pyautogui.moveTo(2095, 260)
pyautogui.dragTo(2125, 263, 1, button='left')
pyautogui.click(button='right')
sleep(1)
pyautogui.click(2142, 326)
sleep(1)
pyautogui.click(289, 321, button='right')
sleep(1)
pyautogui.click(334, 336)
sleep(1)

# inserir numero----------
pyautogui.doubleClick(2050, 153)

pyautogui.click(2050, 152, button='right')
sleep(1)
pyautogui.click(2112, 214)
pyautogui.click(427, 319)
sleep(1)
pyautogui.click(132, 84)
sleep(1)
pyautogui.hotkey("Enter")

# Imprimir bl gerado
pyautogui.click(368, 389)
sleep(1)
pyautogui.click(29, 86)
sleep(1)
pyautogui.click(79, 90)
sleep(1)
pyautogui.click(2609, 907)
pyautogui.hotkey("Enter")

pyautogui.hotkey("Ctrl", 'v')
sleep(1)
pyautogui.hotkey("Ctrl", 'p')
sleep(1)
pyautogui.hotkey("Enter")
