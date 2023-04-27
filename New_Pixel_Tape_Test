import time
from rpi_ws281x import PixelStrip, Color

# LED strip configuration
LED_COUNT = 60         # Number of LED pixels.
LED_PIN = 18           # GPIO pin connected to the pixels (18 uses PWM!).
LED_FREQ_HZ = 800000   # LED signal frequency in hertz (usually 800khz)
LED_DMA = 10           # DMA channel to use for generating signal (try 10)
LED_BRIGHTNESS = 255   # Set to 0 for darkest and 255 for brightest
LED_INVERT = False     # True to invert the signal (when using NPN transistor level shift)
LED_CHANNEL = 0        # set to '1' for GPIOs 13, 19, 41, 45 or 53

# Define the colors of the rainbow
RED = Color(255, 0, 0)
ORANGE = Color(255, 127, 0)
YELLOW = Color(255, 255, 0)
GREEN = Color(0, 255, 0)
BLUE = Color(0, 0, 255)
INDIGO = Color(75, 0, 130)
VIOLET = Color(148, 0, 211)

# Define a function to create a rainbow effect
def rainbow(strip, wait_ms=20):
    for j in range(256):
        for i in range(strip.numPixels()):
            pixel_index = (i * 256 // strip.numPixels()) + j
            strip.setPixelColor(i, wheel(pixel_index & 255))
        strip.show()
        time.sleep(wait_ms / 1000.0)

# Define a function to convert a color value to a wheel value
def wheel(pos):
    if pos < 85:
        return Color(pos * 3, 255 - pos * 3, 0)
    elif pos < 170:
        pos -= 85
        return Color(255 - pos * 3, 0, pos * 3)
    else:
        pos -= 170
        return Color(0, pos * 3, 255 - pos * 3)

# Create an instance of the PixelStrip class
strip = PixelStrip(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS, LED_CHANNEL)
strip.begin()

# Run the rainbow effect
while True:
    rainbow(strip)
