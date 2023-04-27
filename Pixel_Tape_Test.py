import time
import board
import neopixel

# Define the number of LEDs on your strip
num_leds = 60

# Create a neopixel object
pixels = neopixel.NeoPixel(board.D18, num_leds)

# Define a function that will create the rainbow chase effect
def rainbow_chase(wait):
    for j in range(255):
        for i in range(num_leds):
            # Set pixel i to rainbow color j
            pixels[i] = wheel((i+j) & 255)
        pixels.show()
        time.sleep(wait)

# A helper function that takes a position from 0 to 255 and returns an RGB color value.
def wheel(pos):
    if pos < 85:
        return (pos * 3, 255 - pos * 3, 0)
    elif pos < 170:
        pos -= 85
        return (255 - pos * 3, 0, pos * 3)
    else:
        pos -= 170
        return (0, pos * 3, 255 - pos * 3)

# Call the rainbow chase function with the desired wait time
while True:
    rainbow_chase(0.01)
