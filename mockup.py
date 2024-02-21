import time
import board
from digitalio import DigitalInOut, Direction, Pull
import pwmio
from adafruit_motor import servo
import analogio
from adafruit_motor import stepper
from rainbowio import colorwheel
import neopixel
import busio
from adafruit_st7735r import ST7735R
import displayio
import terminalio
from adafruit_display_text import label
import adafruit_ds1307

# Display setup
mosi_pin = board.GP11
clk_pin = board.GP10
reset_pin = board.GP17
cs_pin = board.GP18
dc_pin = board.GP16

displayio.release_displays()
spi = busio.SPI(clock=clk_pin, MOSI=mosi_pin)
display_bus = displayio.FourWire(spi, command=dc_pin, chip_select=cs_pin, reset=reset_pin)
display = ST7735R(display_bus, width=128, height=160, bgr = True)

bitmap = displayio.OnDiskBitmap("/slide_show/a.bmp")
bitmap1 = displayio.OnDiskBitmap("/slide_show/b.bmp")
bitmap2 = displayio.OnDiskBitmap("/slide_show/c.bmp")
bitmap3 = displayio.OnDiskBitmap("/slide_show/d.bmp")
bitmap4 = displayio.OnDiskBitmap("/slide_show/e.bmp")
bitmap5 = displayio.OnDiskBitmap("/slide_show/f.bmp")
group = displayio.Group()
display.show(group)

# RTC setup
i2c = busio.I2C(board.GP1, board.GP0)  # uses board.SCL and board.SDA
rtc = adafruit_ds1307.DS1307(i2c)
months = ['JANUARY', 'FEBRUARY', 'MARCH', 'APRIL', 'MAY', 'JUNE', 'JULY', 'AUGUST', 'SEPTEMBER', 'OCTOBER', 'NOVEMBER', 'DECEMBER']
week = ['MONDAY', 'TUESDAY', 'WEDNESDAY', 'THURSDAY', 'FRIDAY', 'SATURDAY', 'SUNDAY']
t = rtc.datetime

# Neopixel setup
pixel_pin = board.GP13
num_pixels = 6
pixels = neopixel.NeoPixel(pixel_pin, num_pixels, brightness=0.3, auto_write=False)


RED = (255, 0, 0)
YELLOW = (255, 150, 0)
GREEN = (0, 255, 0)
CYAN = (0, 255, 255)
BLUE = (0, 0, 255)
PURPLE = (180, 0, 255)

# Light Sensor setup
photo_resistor1 = analogio.AnalogIn(board.GP26)
photo_resistor2 = analogio.AnalogIn(board.GP27)
photo_resistor3 = analogio.AnalogIn(board.GP28)

switch = DigitalInOut(board.GP12)
switch.direction = Direction.INPUT
switch.pull = Pull.UP

redButton = DigitalInOut(board.GP14)
redButton.direction = Direction.INPUT
redButton.pull = Pull.UP

# Stepper motor setup
DELAY = 0.01  
STEPS = 1000  
coils = (
    DigitalInOut(board.GP19),  # A1 (In4)
    DigitalInOut(board.GP21),  # A2 (In2)
    DigitalInOut(board.GP22),  # B1 (In1)
    DigitalInOut(board.GP20),  # B2 (In3)
)

for coil in coils:
    coil.direction = Direction.OUTPUT

stepper_motor = stepper.StepperMotor(
    coils[0], coils[1], coils[2], coils[3], microsteps=None
)

def stepper_fwd(steps):
    for _ in range(steps):
        stepper_motor.onestep(direction=stepper.FORWARD)
        time.sleep(DELAY)
    stepper_motor.release()

def stepper_back(steps):
    global not_limit
    if not_limit:
        for _ in range(steps):
            stepper_motor.onestep(direction=stepper.BACKWARD)
            time.sleep(DELAY)
            if switch.value:
                not_limit = False
                break
    stepper_motor.release()
    if not not_limit:
        for _ in range(30):
            stepper_motor.onestep(direction=stepper.FORWARD)
            time.sleep(DELAY)
            not_limit = True
# Servo setup
petal1 = None
petal2 = None
petal3 = None
petal4 = None
petal5 = None
petal6 = None
pwm_servo_1 = None
pwm_servo_2 = None
pwm_servo_3 = None
pwm_servo_4 = None
pwm_servo_5 = None
pwm_servo_6 = None
pwm_servo_7 = None
pwm_servo_8 = None
lower_stem = None
upper_stem = None


def servo_initialize():
    global petal1, petal2, petal3, petal4, petal5, petal6, lower_stem, upper_stem, pwm_servo_1, pwm_servo_2, pwm_servo_3, pwm_servo_4,pwm_servo_5, pwm_servo_6, pwm_servo_7, pwm_servo_8
    pwm_servo_1 = pwmio.PWMOut(board.GP2, duty_cycle=2 ** 15, frequency=50)
    petal1 = servo.Servo(
        pwm_servo_1, min_pulse=500, max_pulse=2200
    )

    pwm_servo_2 = pwmio.PWMOut(board.GP3, duty_cycle=2 ** 15, frequency=50)
    petal2 = servo.Servo(
        pwm_servo_2, min_pulse=500, max_pulse=2200
    )

    pwm_servo_3 = pwmio.PWMOut(board.GP4, duty_cycle=2 ** 15, frequency=50)
    petal3 = servo.Servo(
        pwm_servo_3, min_pulse=500, max_pulse=2200
    )

    pwm_servo_4 = pwmio.PWMOut(board.GP5, duty_cycle=2 ** 15, frequency=50)
    petal4 = servo.Servo(
        pwm_servo_4, min_pulse=500, max_pulse=2200
    )

    pwm_servo_5 = pwmio.PWMOut(board.GP6, duty_cycle=2 ** 15, frequency=50)
    petal5 = servo.Servo(
        pwm_servo_5, min_pulse=500, max_pulse=2200
    )

    pwm_servo_6 = pwmio.PWMOut(board.GP7, duty_cycle=2 ** 15, frequency=50)
    petal6 = servo.Servo(
        pwm_servo_6, min_pulse=500, max_pulse=2200
    )

    pwm_servo_7 = pwmio.PWMOut(board.GP8, duty_cycle=2 ** 15, frequency=50)
    lower_stem = servo.Servo(
        pwm_servo_7, min_pulse=500, max_pulse=2200
    )

    pwm_servo_8 = pwmio.PWMOut(board.GP9, duty_cycle=2 ** 15, frequency=50)
    upper_stem = servo.Servo(
        pwm_servo_8, min_pulse=500, max_pulse=2200
    )

def servo_deinitialize():
    global pwm_servo_1, pwm_servo_2, pwm_servo_3, pwm_servo_4, pwm_servo_5, pwm_servo_6, pwm_servo_7, pwm_servo_8
    pwm_servo_1.deinit()
    pwm_servo_2.deinit()
    pwm_servo_3.deinit()
    pwm_servo_4.deinit()
    pwm_servo_5.deinit()
    pwm_servo_6.deinit()
    pwm_servo_7.deinit()
    pwm_servo_8.deinit()

      
servo_initialize()
lower_stem.angle = 15
upper_stem.angle = 20
time.sleep(0.1)
lower_stem.angle = None
upper_stem.angle = None
not_limit = True
step_count = 0
follow_light_cmd = False
step_reverse = False

# while True:
#     for i in range(50, 100):
#         servo1.angle = i
#         servo2.angle = i
#         servo3.angle = i
#         servo4.angle = i
#         servo5.angle = i
#         servo6.angle = i
#         time.sleep(0.02)
#     for i in reversed(range(50, 100)):
#         servo1.angle = i
#         servo2.angle = i
#         servo3.angle = i
#         servo4.angle = i
#         servo5.angle = i
#         servo6.angle = i
#         time.sleep(0.02)
# while True:
#     for i in range(20, 90):
#         servo8.angle = i
#         time.sleep(0.02)
#     for i in reversed(range(20, 90)):
#         servo8.angle = i
#         time.sleep(0.02)
# for i in range(15, 90):
#     servo7.angle = i
#     time.sleep(0.02)
# time.sleep(0.5)
# for i in range(20, 90):
#     servo8.angle = i
#     time.sleep(0.02)

       
def color_chase(color, wait):
    for i in range(num_pixels):
        pixels[i] = color
        time.sleep(wait)
        pixels.show()
    time.sleep(0.01)
    
def rainbow_cycle(wait):
    for j in range(255):
        for i in range(num_pixels):
            rc_index = (i * 256 // num_pixels) + j
            pixels[i] = colorwheel(rc_index & 255)
        pixels.show()
        time.sleep(wait)

def follow_light(micro_steps):
    global step_count, pixels
    servo_deinitialize()
    pixels.deinit()
    pixels = neopixel.NeoPixel(pixel_pin, num_pixels, brightness=0.3, auto_write=False)
    color_chase(PURPLE, 0.1)
    stepper_back(4000)
    while True:
        p3 = photo_resistor3.value
        p1 = photo_resistor1.value
        p2 = photo_resistor2.value
        if not redButton.value:
            break
        if p1 > p2:
            if step_count > 1600:
                stepper_back(1500)
                step_count-=1500
            if step_count <= 1600:
                stepper_fwd(100)
                step_count+=(100)
        if p2 > p1:
            if p2 > p3:
                if (p2 - p3) > 3000:
                    if step_count > 4000:
                        stepper_back(3900)
                        step_count-=3900
                    if step_count <= 4000:
                        stepper_fwd(micro_steps)
                        step_count+=micro_steps
                else:
                    pixels.deinit()
                    pixels = neopixel.NeoPixel(pixel_pin, num_pixels, brightness=0.3, auto_write=False)
                    color_chase(YELLOW, 0.1)
            if p3 > p2:
                if (p3 - p2) > 3000:
                    if step_count < 100:
                        stepper_fwd(3900)
                        step_count+=3900
                    if step_count >= 100:
                        stepper_back(micro_steps)
                        step_count-=micro_steps
                else:
                    pixels.deinit()
                    pixels = neopixel.NeoPixel(pixel_pin, num_pixels, brightness=0.3, auto_write=False)
                    color_chase(YELLOW, 0.1)
           


tile_grid = displayio.TileGrid(bitmap, pixel_shader=bitmap.pixel_shader)
group.append(tile_grid)
time.sleep(0.5)
tile_grid = displayio.TileGrid(bitmap1, pixel_shader=bitmap.pixel_shader)
group.append(tile_grid)
time.sleep(0.5)
tile_grid = displayio.TileGrid(bitmap2, pixel_shader=bitmap.pixel_shader)
group.pop()
group.append(tile_grid)
time.sleep(0.5)
tile_grid = displayio.TileGrid(bitmap3, pixel_shader=bitmap.pixel_shader)
group.pop()
group.append(tile_grid)
time.sleep(0.5)
tile_grid = displayio.TileGrid(bitmap4, pixel_shader=bitmap.pixel_shader)
group.pop()
group.append(tile_grid)
time.sleep(0.5)
tile_grid = displayio.TileGrid(bitmap5, pixel_shader=bitmap.pixel_shader)
group.pop()
group.append(tile_grid)
time.sleep(0.5)

splash = displayio.Group()
display.show(splash)
color_bitmap = displayio.Bitmap(128, 160, 1)
color_palette = displayio.Palette(1)
color_palette[0] = 0xe3c524  # Yellow
bg_sprite = displayio.TileGrid(color_bitmap, pixel_shader=color_palette, x=0, y=0)
splash.append(bg_sprite)
# Draw a smaller inner rectangle
inner_bitmap = displayio.Bitmap(118, 150, 1)
inner_palette = displayio.Palette(1)
inner_palette[0] = 0x000000  # Black
inner_sprite = displayio.TileGrid(inner_bitmap, pixel_shader=inner_palette, x=5, y=5)
splash.append(inner_sprite)
# Draw a label
text_time_label = displayio.Group(scale=1, x=50, y=24)
text_time_label_content = "TIME"
text_time_label_spot = label.Label(terminalio.FONT, text=text_time_label_content, color=0xe3c524)
text_time_label.append(text_time_label_spot)  # Subgroup for text scaling
splash.append(text_time_label)

text_time_value = displayio.Group(scale=2, x=35, y=54)
text_time_value_content = f"{t.tm_hour}:{t.tm_min}"
text_time_value_spot = label.Label(terminalio.FONT, text=text_time_value_content, color=0xf31c28)
text_time_value.append(text_time_value_spot)  # Subgroup for text scaling
splash.append(text_time_value)

text_date_label = displayio.Group(scale=1, x=50, y=84)
text_date_label_content = "DATE"
text_date_label_spot = label.Label(terminalio.FONT, text=text_date_label_content, color=0xe3c524)
text_date_label.append(text_date_label_spot)  # Subgroup for text scaling
splash.append(text_date_label)

text_date_value = displayio.Group(scale=1, x=35, y=110)
text_date_value_content = f"{t.tm_mday} {months[int(t.tm_mon)-1]}\n{week[int(t.tm_wday)-1]}"
text_date_value_spot = label.Label(terminalio.FONT, text=text_date_value_content, color=0xf31c28)
text_date_value.append(text_date_value_spot)  # Subgroup for text scaling
splash.append(text_date_value)



servo_deinitialize()
# pixels.deinit()
# pixels = neopixel.NeoPixel(pixel_pin, num_pixels, brightness=0.3, auto_write=False)

time.sleep(2)
pixels.deinit()
pixels = neopixel.NeoPixel(pixel_pin, num_pixels, brightness=0.3, auto_write=False)

for i in range(3):    
    color_chase(RED, 0.05)  # Increase the number to slow down the color chase
    color_chase(YELLOW, 0.05)
    color_chase(GREEN, 0.05)
    color_chase(CYAN, 0.05)
    color_chase(BLUE, 0.05)
    color_chase(PURPLE, 0.05)

stepper_fwd(1000)
time.sleep(0.5)
stepper_back(4000)
time.sleep(0.5)
servo_initialize()
lower_stem.angle = 15
upper_stem.angle = 20
time.sleep(1)
for i in range(15, 90):
    lower_stem.angle = i
    time.sleep(0.02)
time.sleep(0.5)
for i in range(20, 80):
    upper_stem.angle = i
    time.sleep(0.02)
upper_stem.angle = None
lower_stem.angle = None
time.sleep(1)

for _ in range(3):
    for i in range(50, 100):
        petal1.angle = i
        petal2.angle = i
        petal3.angle = i
        petal4.angle = i
        petal5.angle = i
        petal6.angle = i
        time.sleep(0.02)
    for i in reversed(range(50, 100)):
        petal1.angle = i
        petal2.angle = i
        petal3.angle = i
        petal4.angle = i
        petal5.angle = i
        petal6.angle = i
        time.sleep(0.02)

time.sleep(1)

for i in reversed(range(15, 90)):
    lower_stem.angle = i
    time.sleep(0.02)
time.sleep(0.5)
for i in reversed(range(20, 80)):
    upper_stem.angle = i
    time.sleep(0.02)
upper_stem.angle = None
lower_stem.angle = None

# time.sleep(2)
# 
# pixels.deinit()
# pixels = neopixel.NeoPixel(pixel_pin, num_pixels, brightness=0.3, auto_write=False)
# for i in range(3):    
#     color_chase(RED, 0.1)  # Increase the number to slow down the color chase
#     color_chase(YELLOW, 0.1)
#     color_chase(GREEN, 0.1)
#     color_chase(CYAN, 0.1)
#     color_chase(BLUE, 0.1)
#     color_chase(PURPLE, 0.1)




BLUE1 = (7, 0, 196)
BLUE2 = (0, 0, 255)
BLUE3 = (0, 82, 255)
BLUE4 = (0, 122, 255)
BLUE5 = (0, 163, 255)
BLUE6 = (0, 204, 255)

RED1 = (67, 28, 82)
RED2 = (90, 39, 118)
RED3 = (140, 49, 156)
RED4 = (169, 52, 189)
RED5 = (155, 35, 208)
RED6 = (136, 6, 206)

b = 0.1
for i in range(5):
    pixels.deinit()
    pixels = neopixel.NeoPixel(pixel_pin, num_pixels, brightness=b, auto_write=False)
    for i in range (8):
        pixels.deinit()
        pixels = neopixel.NeoPixel(pixel_pin, num_pixels, brightness=b, auto_write=False)
        pixels[0] = BLUE1
        pixels.show()
        pixels[1] = BLUE2
        pixels.show()
        pixels[2] = BLUE3
        pixels.show()
        pixels[3] = BLUE4
        pixels.show()
        pixels[4] = BLUE5
        pixels.show()
        pixels[5] = BLUE6
        pixels.show()
        b+=0.1
        time.sleep(0.01)

    for i in range (8):
        pixels.deinit()
        pixels = neopixel.NeoPixel(pixel_pin, num_pixels, brightness=b, auto_write=False)
        pixels[0] = BLUE1
        pixels.show()
        pixels[1] = BLUE2
        pixels.show()
        pixels[2] = BLUE3
        pixels.show()
        pixels[3] = BLUE4
        pixels.show()
        pixels[4] = BLUE5
        pixels.show()
        pixels[5] = BLUE6
        pixels.show()
        b-=0.1
        time.sleep(0.01)
        
# b = 0.1
# pixels.deinit()
# pixels = neopixel.NeoPixel(pixel_pin, num_pixels, brightness=b, auto_write=False)
# for i in range(5):
#     pixels.deinit()
#     pixels = neopixel.NeoPixel(pixel_pin, num_pixels, brightness=b, auto_write=False)
#     for i in range (8):
#         pixels.deinit()
#         pixels = neopixel.NeoPixel(pixel_pin, num_pixels, brightness=b, auto_write=False)
#         pixels[0] = RED1
#     #     time.sleep(0.01)
#         pixels.show()
#         pixels[1] = RED2
#     #     time.sleep(0.01)
#         pixels.show()
#         pixels[2] = RED3
#     #     time.sleep(0.01)
#         pixels.show()
#         pixels[3] = RED4
#     #     time.sleep(0.01)
#         pixels.show()
#         pixels[4] = RED5
#     #     time.sleep(0.01)
#         pixels.show()
#         pixels[5] = RED6
#     #     time.sleep(0.01)
#         pixels.show()
#         b+=0.1
#         time.sleep(0.01)
# 
#     for i in range (8):
#         pixels.deinit()
#         pixels = neopixel.NeoPixel(pixel_pin, num_pixels, brightness=b, auto_write=False)
#         pixels[0] = RED1
#     #     time.sleep(0.01)
#         pixels.show()
#         pixels[1] = RED2
#     #     time.sleep(0.01)
#         pixels.show()
#         pixels[2] = RED3
#     #     time.sleep(0.01)
#         pixels.show()
#         pixels[3] = RED4
#     #     time.sleep(0.01)
#         pixels.show()
#         pixels[4] = RED5
#     #     time.sleep(0.01)
#         pixels.show()
#         pixels[5] = RED6
#     #     time.sleep(0.01)
#         pixels.show()
#         b-=0.1
#         time.sleep(0.01)





