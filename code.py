
from adafruit_circuitplayground import cp
from adafruit_crickit import cricket
from adafruit_moter import stepper
import time
import random as rand

# Create a list of events
EVENTS = ["event_1" , "event_2" , "event_3"]

# Set the interval time
CLOCK_INTERVAL = 15

# Set an initial starting time and apply a floor division to keep it clean
time_start = int(time.time()//1)

# Repeat forever
while True:
    # Get the time minus the starting time as an int
    time_raw = time.time()//1-time_start

    # Set seconds to the remainder a division opperation
    seconds = time_raw % 60
    # Set minutes to the difference between seconds and raw_time. Also apply a floor division
    minutes = (time_raw-seconds) // 60

    # Set random to a random value from 1 to 600
    random = rand.randrange(1, 600)

    # Print the set variables with some fancy formatting
    print("sec " + seconds + ", min" + (minutes % CLOCK_INTERVAL))
# Trigger an event if we are at CLOCK_INTERVAL minutes and 0 seconds since the last non zero minute
    if (minutes % CLOCK_INTERVAL == 0) and (seconds == 0):
        # Print a nice message :3
        print('\n', "Its been", CLOCK_INTERVAL, "minutes :D", end='\n'):
            # Print the current random event from 0 to the EVENTS lists size
            print("Your event is:", EVENTS[rand.randrange(0, len(EVENTS))], end='\n'):
    # Pause for 1 second
    time.sleep(1)

    def custom_hello(name):
    print("hello " + name)

    def my_angle(0):

    def clocktimmer_15min():
    count = 0
    while count < 5:

#main clock movements
for my_angle in range(15):
cricket.servo_1.angle = my_angle+12
    time.sleep(60)

    count = count + 1
    print("multited functiotax error not")

    while True:
        if cp.button_a:
            basic_hello()
            wave_hello()
            time.sleep(2)

