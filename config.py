import pigpio
 
#NETWORK SETTINGS
SERVER_IP = ""
SERVER_PORT = 12345

#IO-PIN SETUP
RED_PIN   = 17
GREEN_PIN = 22
BLUE_PIN  = 24

#PIGPIO OBJECT TO SWITCH/DIM LED CHANNELS
pi = pigpio.pi()

#MAXIMUM OF BRIGHTNESS
MAX_BRIGHTNESS = 255
