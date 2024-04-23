import board
from digitalio import DigitalInOut, Direction
from analogio import AnalogIn
from time import sleep
from math import floor

# setup pins
microphone = AnalogIn(board.IO1)

status = DigitalInOut(board.IO17)
status.direction = Direction.OUTPUT

led_pins = [
    board.IO21,
    board.IO26, # type: ignore
    board.IO47,
    board.IO33, # type: ignore
    board.IO34, # type: ignore
    board.IO48,
    board.IO35,
    board.IO36,
    board.IO37,
    board.IO38,
    board.IO39
]

leds = [DigitalInOut(pin) for pin in led_pins]

for led in leds:
    led.direction = Direction.OUTPUT

avgvolume = []
for _ in range(10):
    avgvolume.append(microphone.value)

avgvolume = sum(avgvolume) / len(avgvolume) ## avg volume in the room

maxvol = 48000
diff = maxvol - avgvolume
step = diff/11 

# main loop
while True:
    volume = microphone.value

    print(volume)

    curDiff = volume-avgvolume #difference in current vol

    numsTurnOn = floor(curDiff/step) # number to turn on

    for index, led in enumerate(leds):
        if index <= numsTurnOn:
            leds[index].value = 1
        else:
            leds[index].value = 0