import time
import board
import analogio

photo_resistor = analogio.AnalogIn(board.GP26)

while True:
    print(photo_resistor.value)
    time.sleep(0.5)