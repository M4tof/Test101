import pyautogui
import time

pyautogui.hotkey('win')
pyautogui.typewrite('git bash')
pyautogui.hotkey('enter')
time.sleep(1.2)
pyautogui.typewrite('cd ./auto-py-to-exe/')
pyautogui.hotkey('enter')
time.sleep(0.3)
pyautogui.typewrite('python -m auto_py_to_exe')
pyautogui.hotkey('enter')