from zio_loudness_sensor import LoudnessSensor
import time

mic = LoudnessSensor()

mic.led_on()
time.sleep(0.5)
mic.led_off()

while True:
    print(mic.read_value())
    time.sleep(1)