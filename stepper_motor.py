import time
import board
from digitalio import DigitalInOut, Direction, Pull
from adafruit_motor import stepper

switch = DigitalInOut(board.GP0)
switch.direction = Direction.INPUT
switch.pull = Pull.UP

not_limit = True

# Stepper motor setup
DELAY = 0.003  # fastest is ~ 0.004, 0.01 is still very smooth, gets steppy after that
STEPS = 1000  # this is a full 360º
coils = (
    DigitalInOut(board.GP22),  # A1 (In4)
    DigitalInOut(board.GP21),  # A2 (In2)
    DigitalInOut(board.GP20),  # B1 (In1)
    DigitalInOut(board.GP19),  # B2 (In3)
)

for coil in coils:
    coil.direction = Direction.OUTPUT

stepper_motor = stepper.StepperMotor(
    coils[0], coils[1], coils[2], coils[3], microsteps=None
)


def stepper_fwd():
    global not_limit
    print("stepper forward")
    if not_limit:
        for _ in range(STEPS):
            stepper_motor.onestep(direction=stepper.FORWARD)
            time.sleep(DELAY)
            if switch.value:
                not_limit = False
                break
    stepper_motor.release()

def stepper_back():
    print("stepper backward")
    for _ in range(STEPS):
        stepper_motor.onestep(direction=stepper.BACKWARD)
        time.sleep(DELAY)
    stepper_motor.release()

while True:
    stepper_fwd();