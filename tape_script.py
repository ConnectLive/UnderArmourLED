import time
from bluepy.btle import Peripheral, UUID
from rpi_ws281x import PixelStrip, Color

# Define the Bluetooth UUIDs for the Garmin HRM Pro heart rate service and characteristic
hr_service_uuid = UUID("0000180D-0000-1000-8000-00805f9b34fb")
hr_characteristic_uuid = UUID("00002A37-0000-1000-8000-00805f9b34fb")

# Define the LED strip parameters
led_count = 60
led_pin = 18
led_freq_hz = 800000
led_dma = 10
led_brightness = 255
led_invert = False

# Initialize the LED strip object
strip = PixelStrip(led_count, led_pin, led_freq_hz, led_dma, led_invert, led_brightness)
strip.begin()

# Define a function to convert a heart rate value (0-255) to a color for the LED strip
def hr_to_color(hr):
    if hr < 120:
        # Blue for low heart rate
        return Color(0, 0, 255)
    elif hr < 160:
        # Green for medium heart rate
        return Color(0, 255, 0)
    elif hr < 180:
        # Yellow for high heart rate
        return Color(255, 255, 0)
    else:
        # Red for very high heart rate
        return Color(255, 0, 0)

# Define a function to handle heart rate notifications from the Garmin HRM Pro
def handle_hr_notification(handle, value):
    # Parse the heart rate value from the notification data
    hr = value[1]
    # Convert the heart rate to a color for the LED strip
    color = hr_to_color(hr)
    # Set all LEDs on the strip to the heart rate color
    for i in range(led_count):
        strip.setPixelColor(i, color)
    strip.show()
    # If the heart rate is above 180 bpm, turn the strip red
    if hr > 180:
        for i in range(led_count):
            strip.setPixelColor(i, Color(255, 0, 0))
        strip.show()

# Connect to the Garmin HRM Pro and enable heart rate notifications
garmin_hrm = Peripheral()
garmin_hrm.connect("00:11:22:33:44:55")
hr_service = garmin_hrm.getServiceByUUID(hr_service_uuid)
hr_characteristic = hr_service.getCharacteristics(hr_characteristic_uuid)[0]
hr_descriptor = hr_characteristic.getDescriptors(forUUID=0x2902)[0]
hr_descriptor.write(b"\x01\x00")
hr_characteristic.write(b"\x01\x00")
garmin_hrm.delegate.handleNotification = handle_hr_notification

# Main loop to receive heart rate notifications and update the LED strip
while True:
    if garmin_hrm.waitForNotifications(1.0):
        continue
