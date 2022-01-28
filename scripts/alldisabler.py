from ctypes import windll

while True:
    windll.user32.BlockInput(True)