import ctypes
import time
for x in range(300,850,10):
    ctypes.windll.user32.SetCursorPos(x, 200)
    time.sleep(0.1)
for x in range(200,600,10):
    ctypes.windll.user32.SetCursorPos(850, x)
    time.sleep(0.1)
for x in range(850,200,-10):
    ctypes.windll.user32.SetCursorPos(x, 600)
    time.sleep(0.1)
for x in range(600,200,-10):
    ctypes.windll.user32.SetCursorPos(200, x)
    time.sleep(0.1)
