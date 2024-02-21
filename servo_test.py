import time
import board
from digitalio import DigitalInOut, Direction, Pull
import pwmio
from adafruit_motor import servo

# Servo setup
pwm_servo_1 = pwmio.PWMOut(board.GP0, duty_cycle=2 ** 15, frequency=50)
servo1 = servo.Servo(
    pwm_servo_1, min_pulse=500, max_pulse=2200
)

pwm_servo_2 = pwmio.PWMOut(board.GP9, duty_cycle=2 ** 15, frequency=50)
servo2 = servo.Servo(
    pwm_servo_2, min_pulse=500, max_pulse=2200
)

pwm_servo_3 = pwmio.PWMOut(board.GP8, duty_cycle=2 ** 15, frequency=50)
servo3 = servo.Servo(
    pwm_servo_3, min_pulse=500, max_pulse=2200
)

# tune pulse for specific servo

def servo_direct_test():
    print("servo test: 90")
    servo1.angle = 90
    time.sleep(2)
    print("servo test: 0")
    servo1.angle = 0
    time.sleep(2)
    print("servo test: 90")
    servo1.angle = 90
    time.sleep(2)
    print("servo test: 180")
    servo1.angle = 180
    time.sleep(2)
    
while True:
    for i in range(10, 120):
        servo1.angle = i
        servo2.angle = i
        servo3.angle = i
        time.sleep(0.01)
    for i in reversed(range(10, 120)):
        servo1.angle = i
        servo2.angle = i
        servo3.angle = i
        time.sleep(0.01)
# servo1.angle = 50
    