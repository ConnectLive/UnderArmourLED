import bluetooth
import serial
import time

# Define the MAC address of the Garmin HRM Pro
garmin_mac = '00:11:22:33:44:55'

# Define the serial port to communicate with the Arduino
serial_port = '/dev/ttyACM0'
baud_rate = 9600

# Connect to the Garmin HRM Pro using its MAC address
sock = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
sock.connect((garmin_mac, 1))

# Open a serial connection to the Arduino
ser = serial.Serial(serial_port, baud_rate)

# Continuously read heart rate data from the Garmin HRM Pro and send it to the Arduino
while True:
    # Read the heart rate data from the HRM Pro
    data = sock.recv(1024)
    heart_rate = int.from_bytes(data[2:3], byteorder='big')
    
    # Send the heart rate data to the Arduino
    ser.write(bytes([heart_rate]))
    
    # Wait for a short amount of time before reading the next heart rate data
    time.sleep(0.1)
