import time
from neopixel import *

# LED strip configuration:
LED_COUNT = 60         # Number of LED pixels.
LED_PIN = 18           # GPIO pin connected to the pixels (18 uses PWM!).
LED_FREQ_HZ = 800000   # LED signal frequency in hertz (usually 800khz)
LED_DMA = 10           # DMA channel to use for generating signal (try 10)
LED_BRIGHTNESS = 255   # Set to 0 for darkest and 255 for brightest
LED_INVERT = False     # True to invert the signal (when using NPN transistor level shift)

def color_chase(strip, color, wait_ms=50):
    """Color chase animation."""
    for i in range(strip.numPixels()):
        strip.setPixelColor(i, color)
        strip.show()
        time.sleep(wait_ms/1000.0)

def rainbow_cycle(strip, wait_ms=20, iterations=5):
    """Rainbow cycle animation."""
    for j in range(256*iterations):
        for i in range(strip.numPixels()):
            pixel_index = (i * 256 // strip.numPixels()) + j
            strip.setPixelColor(i, wheel(pixel_index & 255))
        strip.show()
        time.sleep(wait_ms/1000.0)

def wheel(pos):
    """Generate rainbow colors across 0-255 positions."""
    if pos < 85:
        return Color(pos * 3, 255 - pos * 3, 0)
    elif pos < 170:
        pos -= 85
        return Color(255 - pos * 3, 0, pos * 3)
    else:
        pos -= 170
        return Color(0, pos * 3, 255 - pos * 3)

# Create NeoPixel object with appropriate configuration.
strip = Adafruit_NeoPixel(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS)
# Initialize the library (must be called once before other functions).
strip.begin()

# Rainbow chase animation.
while True:
    color_chase(strip, Color(255, 0, 0))  # Red
    color_chase(strip, Color(255, 127, 0))  # Orange
    color_chase(strip, Color(
