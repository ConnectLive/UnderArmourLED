import time
from rpi_ws281x import *
import argparse

# LED strip configuration
LED_COUNT = 60         # Number of LED pixels.
LED_PIN = 18           # GPIO pin connected to the pixels (18 uses PWM!).
LED_FREQ_HZ = 400000  # LED signal frequency in hertz (usually 800khz)
LED_DMA = 10           # DMA channel to use for generating signal (try 10)
LED_BRIGHTNESS = 255   # Set to 0 for darkest and 255 for brightest
LED_INVERT = False     # True to invert the signal (when using NPN transistor level shift)

# Define the color of even and odd LEDs
BLUE = Color(0, 0, 255)
WHITE = Color(255, 255, 255)

# Initialize the LED strip
strip = Adafruit_NeoPixel(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS)
strip.begin()

# Set the colors of the LEDs
for i in range(strip.numPixels()):
    if i % 2 == 0:
        strip.setPixelColor(i, BLUE)
    else:
        strip.setPixelColor(i, WHITE)
        
# Update the LED strip
strip.show()

# Wait for 5 seconds
time.sleep(5)

# Clear the LED strip
for i in range(strip.numPixels()):
    strip.setPixelColor(i, Color(0, 0, 0))
strip.show()
