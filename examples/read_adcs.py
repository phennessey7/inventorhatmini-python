import time
from machine import Pin
from pimoroni import Analog
from inventorhatmini import InventorHATMini, ADCS, NUM_ADCS, LED_ADC_1

"""
Shows how to initialise and read the 4 ADC headers of Inventor HAT Mini.

Press "User" to exit the program.
"""

BRIGHTNESS = 0.4      # The brightness of the LEDs
UPDATES = 10          # How many times to update LEDs per second
ADC_NAMES = ("A0", "A1", "A2", "A3")

# Create a new InventorHATMini
board = InventorHATMini()

# Create an analog object for each ADC
analogs = [Analog(i) for i in ADCS]

# Create an accompanying pin object to each analog,
# so that they can be pulled low. This avoids random
# numbers when nothing is connected to any of the pins.
pulls = [Pin(i, Pin.IN, Pin.PULL_DOWN) for i in ADCS]


# Read the ADCs until the user button is pressed
while not board.switch_pressed():

    # Read each ADC in turn and print its voltage
    for i in range(NUM_ADCS):
        voltage = analogs[i].read_voltage()
        print(ADC_NAMES[i], " = ", round(voltage, 3), sep="", end=", ")

        # Set the neighbouring LED to a colour based on the
        # voltage, with Green for high and Blue for low
        hue = (2.0 - (voltage / 3.3)) * 0.333
        board.leds.set_hsv(i + LED_ADC_1, hue, 1.0, BRIGHTNESS)

    # Print a new line
    print()

    time.sleep(1.0 / UPDATES)

# Turn off the LED bars
board.leds.clear()
