import time
import busio
import adafruit_ds1307
import board

i2c = busio.I2C(board.GP1, board.GP0)  # uses board.SCL and board.SDA
rtc = adafruit_ds1307.DS1307(i2c)

#Set the time
#rtc.datetime = time.struct_time((2023,8,9,5,48,0,3,9,-1))

t = rtc.datetime
print(t)
print(t.tm_hour, t.tm_min)
print(t.tm_mon, t.tm_mday) # Month and Day
print(t.tm_wday) #Day of week

