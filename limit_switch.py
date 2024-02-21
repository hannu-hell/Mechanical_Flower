import time
import board
from digitalio import DigitalInOut, Direction, Pull

switch = DigitalInOut(board.GP0)
switch.direction = Direction.INPUT
switch.pull = Pull.UP

while True:
    # We could also do "led.value = not switch.value"!
    if switch.value:
        print("Not Pressed")
    else:
        print("Pressed")

    time.sleep(0.01)  # debounce delay