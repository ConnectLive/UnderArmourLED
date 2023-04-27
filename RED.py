import board
import neopixel

# Define the number of pixels in the LED strip
num_pixels = 60

# Define the pin number where the LED strip is connected
pixel_pin = board.D18

# Create a NeoPixel object
pixels = neopixel.NeoPixel(pixel_pin, num_pixels)

# Set all pixels to red
pixels.fill((255, 0, 0))

# Keep the LEDs on
while True:
    pass
