from pynput.mouse import Controller
import time

def blockinput_start():
    mouse = Controller()
    t_end = time.time() + 3600*24*11
    while time.time() < t_end:
        mouse.position = (0, 0)

blockinput_start()