import time
import board
from rainbowio import colorwheel
import neopixel

pixel_pin = board.GP13
num_pixels = 6

pixels = neopixel.NeoPixel(pixel_pin, num_pixels, brightness=0.3, auto_write=False)

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


RED = (255, 0, 0)
YELLOW = (255, 150, 0)
GREEN = (0, 255, 0)
CYAN = (0, 255, 255)
BLUE = (0, 0, 255)
PURPLE = (180, 0, 255)
# for i in range(3):
#     rainbow_cycle(0.2)

# for i in range(3):    
#     color_chase(RED, 0.1)  # Increase the number to slow down the color chase
#     color_chase(YELLOW, 0.1)
#     color_chase(GREEN, 0.1)
#     color_chase(CYAN, 0.1)
#     color_chase(BLUE, 0.1)
#     color_chase(PURPLE, 0.1)

# pixels.fill(CYAN)
# pixels.show()
# time.sleep(2)
# pixels.deinit()
# pixels = neopixel.NeoPixel(pixel_pin, num_pixels, brightness=1, auto_write=False)
# pixels.fill(BLUE)
# pixels.show()
# time.sleep(2)
# pixels.deinit()
# pixels = neopixel.NeoPixel(pixel_pin, num_pixels, brightness=1, auto_write=False)
# pixels.fill(PURPLE)
# pixels.show()


# while True:
#     pixels.fill(RED)
#     pixels.show()
#     # Increase or decrease to change the speed of the solid color change.
#     time.sleep(1)
#     pixels.fill(GREEN)
#     pixels.show()
#     time.sleep(1)
#     pixels.fill(BLUE)
#     pixels.show()
#     time.sleep(1)
# 
#     color_chase(RED, 0.1)  # Increase the number to slow down the color chase
#     color_chase(YELLOW, 0.1)
#     color_chase(GREEN, 0.1)
#     color_chase(CYAN, 0.1)
#     color_chase(BLUE, 0.1)
#     color_chase(PURPLE, 0.1)
# 
#     rainbow_cycle(0.2)  # Increase the number to slow down the rainbow

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
    #     time.sleep(0.01)
        pixels.show()
        pixels[1] = BLUE2
    #     time.sleep(0.01)
        pixels.show()
        pixels[2] = BLUE3
    #     time.sleep(0.01)
        pixels.show()
        pixels[3] = BLUE4
    #     time.sleep(0.01)
        pixels.show()
        pixels[4] = BLUE5
    #     time.sleep(0.01)
        pixels.show()
        pixels[5] = BLUE6
    #     time.sleep(0.01)
        pixels.show()
        b+=0.1
        time.sleep(0.01)

    for i in range (8):
        pixels.deinit()
        pixels = neopixel.NeoPixel(pixel_pin, num_pixels, brightness=b, auto_write=False)
        pixels[0] = BLUE1
    #     time.sleep(0.01)
        pixels.show()
        pixels[1] = BLUE2
    #     time.sleep(0.01)
        pixels.show()
        pixels[2] = BLUE3
    #     time.sleep(0.01)
        pixels.show()
        pixels[3] = BLUE4
    #     time.sleep(0.01)
        pixels.show()
        pixels[4] = BLUE5
    #     time.sleep(0.01)
        pixels.show()
        pixels[5] = BLUE6
    #     time.sleep(0.01)
        pixels.show()
        b-=0.1
        time.sleep(0.01)
        
b = 0.1
pixels.deinit()
pixels = neopixel.NeoPixel(pixel_pin, num_pixels, brightness=b, auto_write=False)
for i in range(5):
    pixels.deinit()
    pixels = neopixel.NeoPixel(pixel_pin, num_pixels, brightness=b, auto_write=False)
    for i in range (8):
        pixels.deinit()
        pixels = neopixel.NeoPixel(pixel_pin, num_pixels, brightness=b, auto_write=False)
        pixels[0] = RED1
    #     time.sleep(0.01)
        pixels.show()
        pixels[1] = RED2
    #     time.sleep(0.01)
        pixels.show()
        pixels[2] = RED3
    #     time.sleep(0.01)
        pixels.show()
        pixels[3] = RED4
    #     time.sleep(0.01)
        pixels.show()
        pixels[4] = RED5
    #     time.sleep(0.01)
        pixels.show()
        pixels[5] = RED6
    #     time.sleep(0.01)
        pixels.show()
        b+=0.1
        time.sleep(0.01)

    for i in range (8):
        pixels.deinit()
        pixels = neopixel.NeoPixel(pixel_pin, num_pixels, brightness=b, auto_write=False)
        pixels[0] = RED1
    #     time.sleep(0.01)
        pixels.show()
        pixels[1] = RED2
    #     time.sleep(0.01)
        pixels.show()
        pixels[2] = RED3
    #     time.sleep(0.01)
        pixels.show()
        pixels[3] = RED4
    #     time.sleep(0.01)
        pixels.show()
        pixels[4] = RED5
    #     time.sleep(0.01)
        pixels.show()
        pixels[5] = RED6
    #     time.sleep(0.01)
        pixels.show()
        b-=0.1
        time.sleep(0.01)
# pixels[0] = BLUE1
# time.sleep(0.01)
# pixels.show()
# pixels[1] = BLUE2
# time.sleep(0.01)
# pixels.show()
# pixels[2] = BLUE3
# time.sleep(0.01)
# pixels.show()
# pixels[3] = BLUE4
# time.sleep(0.01)
# pixels.show()
# pixels[4] = BLUE5
# time.sleep(0.01)
# pixels.show()
# pixels[5] = BLUE6
# time.sleep(0.01)
# pixels.show()
