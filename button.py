import asyncio
import board
import keypad
import time
from digitalio import DigitalInOut, Direction, Pull
import pwmio
from adafruit_motor import servo

pwm_servo_1 = pwmio.PWMOut(board.GP12, duty_cycle=2 ** 15, frequency=50)
servo1 = servo.Servo(
    pwm_servo_1, min_pulse=500, max_pulse=2200
)

async def catch_pin_transitions(pin):
    with keypad.Keys((pin,), value_when_pressed=False) as keys:
        while True:
            event = keys.events.get()
            if event:
                if event.pressed:
                    print("Yellow Button pressed")
#                 elif event.released:
#                     print("Pin went High")
            await asyncio.sleep(0)

async def catch_pin_transitions2(pin):
    with keypad.Keys((pin,), value_when_pressed=False) as keys:
        while True:
            event = keys.events.get()
            if event:
                if event.pressed:
                    print("Red Button pressed")
#                 elif event.released:
#                     print("Pin went High")
            await asyncio.sleep(0)

async def some_func():
    while True:
        for i in range(0, 120):
            servo1.angle = i
            time.sleep(0.01)
        for i in reversed(range(0, 120)):
            servo1.angle = i
            time.sleep(0.01)
        await asyncio.sleep(0)
            
async def main_func():
    interrupt_task = asyncio.create_task(catch_pin_transitions(board.GP0))
    interrupt_task2 = asyncio.create_task(some_func())
    interrupt_task3 = asyncio.create_task(catch_pin_transitions2(board.GP1))
    await asyncio.gather(interrupt_task, interrupt_task2)
   
    

asyncio.run(main_func())

