import time
from rpi_ws281x import PixelStrip, Color

# LED strip configuration:
LED_COUNT = 60        # Number of LED pixels.
LED_PIN = 18          # GPIO pin connected to the pixels (18 uses PWM!).
LED_FREQ_HZ = 600000  # LED signal frequency in hertz (usually 800khz)
LED_DMA = 10          # DMA channel to use for generating signal (try 10)
LED_BRIGHTNESS = 255  # Set to 0 for darkest and 255 for brightest
LED_INVERT = False    # True to invert the signal (when using NPN transistor level shift)

# Create NeoPixel object with appropriate configuration.
strip = PixelStrip(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS)

# Intialize the library (must be called once before other functions).
strip.begin()

# Turn on all LEDs red.
color = Color(255, 0, 0)
for i in range(strip.numPixels()):
    strip.setPixelColor(i, color)
strip.show()

# Wait for 2 seconds
time.sleep(2)

# Turn off all LEDs.
strip.clear()
strip.show()

# Clean up resources.
strip.begin()
