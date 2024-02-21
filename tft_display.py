import board,busio
from time import sleep
from adafruit_st7735r import ST7735R
import displayio
import terminalio
from adafruit_display_text import label
import adafruit_ds1307

mosi_pin = board.GP11
clk_pin = board.GP10
reset_pin = board.GP17
cs_pin = board.GP18
dc_pin = board.GP16

i2c = busio.I2C(board.GP1, board.GP0)  # uses board.SCL and board.SDA
rtc = adafruit_ds1307.DS1307(i2c)
months = ['JANUARY', 'FEBRUARY', 'MARCH', 'APRIL', 'MAY', 'JUNE', 'JULY', 'AUGUST', 'SEPTEMBER', 'OCTOBER', 'NOVEMBER', 'DECEMBER']
week = ['MONDAY', 'TUESDAY', 'WEDNESDAY', 'THURSDAY', 'FRIDAY', 'SATURDAY', 'SUNDAY']
t = rtc.datetime

displayio.release_displays()
spi = busio.SPI(clock=clk_pin, MOSI=mosi_pin)
display_bus = displayio.FourWire(spi, command=dc_pin, chip_select=cs_pin, reset=reset_pin)
display = ST7735R(display_bus, width=128, height=160, bgr = True)
splash = displayio.Group()
display.show(splash)
color_bitmap = displayio.Bitmap(128, 160, 1)
color_palette = displayio.Palette(1)
color_palette[0] = 0x00FF00  # Bright Green
bg_sprite = displayio.TileGrid(color_bitmap, pixel_shader=color_palette, x=0, y=0)
splash.append(bg_sprite)
# Draw a smaller inner rectangle
inner_bitmap = displayio.Bitmap(118, 150, 1)
inner_palette = displayio.Palette(1)
inner_palette[0] = 0x000000  # Black
inner_sprite = displayio.TileGrid(inner_bitmap, pixel_shader=inner_palette, x=5, y=5)
splash.append(inner_sprite)
# Draw a label
text_time_label = displayio.Group(scale=1, x=11, y=24)
text_time_label_content = "TIME"
text_time_label_spot = label.Label(terminalio.FONT, text=text_time_label_content, color=0xe3c524)
text_time_label.append(text_time_spot)  # Subgroup for text scaling
splash.append(text_time_label)

text_time_value = displayio.Group(scale=2, x=11, y=44)
text_time_value_content = f"{t.tm_hour} Hours\n{t.tm_min} Mins"
text_time_value_spot = label.Label(terminalio.FONT, text=text_time_value_content, color=0xf31c28)
text_time_value.append(text_time_value_spot)  # Subgroup for text scaling
splash.append(text_time_value)

text_date_label = displayio.Group(scale=1, x=11, y=24)
text_date_label_content = "DATE"
text_date_label_spot = label.Label(terminalio.FONT, text=text_date_label_content, color=0xe3c524)
text_date_label.append(text_date_spot)  # Subgroup for text scaling
splash.append(text_date_label)

text_date_value = displayio.Group(scale=2, x=11, y=44)
text_date_value_content = f"{t.tm_mday} {months[int(t.tm_mon)-1]}"
text_date_value_spot = label.Label(terminalio.FONT, text=text_date_value_content, color=0xf31c28)
text_date_value.append(text_date_value_spot)  # Subgroup for text scaling
splash.append(text_date_value)



while True:
    pass
# \nDate is {t.tm_mday} of {months[int(t.tm_mon)-1]}\n{week[int(t.tm_wday)-1]}
# \n{t.tm_hour} Hours {t.tm_min} Mins