import RPi.GPIO as GPIO
import time
from scipy.signal import medfilt

# Set GPIO mode to BCM
GPIO.setmode(GPIO.BCM)

# Define GPIO pins
TRIG_left = 20
ECHO_left = 21
TRIG_bottom = 12
ECHO_bottom = 13

# Set up GPIO pins
GPIO.setup(TRIG_left, GPIO.OUT)
GPIO.setup(ECHO_left, GPIO.IN)
GPIO.setup(TRIG_bottom, GPIO.OUT)
GPIO.setup(ECHO_bottom, GPIO.IN)

def raw_left_distance():
    # Send a 10us pulse to trigger the sensor
    GPIO.output(TRIG_left, True)
    time.sleep(0.00001)
    GPIO.output(TRIG_left, False)

    pulse_start = time.time()
    pulse_end = time.time()

    # Wait for the echo signal to start
    while GPIO.input(ECHO_left) == 0:
        pulse_start = time.time()

    # Wait for the echo signal to end
    while GPIO.input(ECHO_left) == 1:
        pulse_end = time.time()

    # Calculate the duration of the pulse
    pulse_duration = pulse_end - pulse_start

    # Calculate the distance in centimeters
    distance = pulse_duration * 17150

    return distance

def raw_bottom_distance():
    # Send a 10us pulse to trigger the sensor
    GPIO.output(TRIG_bottom, True)
    time.sleep(0.00001)
    GPIO.output(TRIG_bottom, False)

    pulse_start = time.time()
    pulse_end = time.time()

    # Wait for the echo signal to start
    while GPIO.input(ECHO_bottom) == 0:
        pulse_start = time.time()

    # Wait for the echo signal to end
    while GPIO.input(ECHO_bottom) == 1:
        pulse_end = time.time()

    # Calculate the duration of the pulse
    pulse_duration = pulse_end - pulse_start

    # Calculate the distance in centimeters
    distance = pulse_duration * 17150

    return distance

def filter_distance(distance_func, offset=0, num_samples=10, kernel_size=5, delay_between_samples=0.1, maximum_value=200):
    # Collect distance samples
    samples = []
    for _ in range(num_samples):
        samples.append(distance_func())
        time.sleep(delay_between_samples)

    # print(samples)  # Print raw detect value

    samples = [s for s in samples if s <= maximum_value]  # Remove obvious incorrect values
    samples = [s for s in samples if s is not None]  # Remove None values
    if not samples:  # If all samples are None, return None
        return None

    # print(samples)  # Print value after first filter

    # Apply the medfilt filter
    filtered_samples = medfilt(samples, kernel_size)

    # print(filtered_samples) # Print value after second filter

    # Return the average of the filtered samples
    return round(sum(filtered_samples) / len(filtered_samples) + offset, 3)

def get_left_distance():
    result = None
    while(result == None or result == 0):
        result = filter_distance(raw_left_distance, 7.3)
        if(result == None):
            print("None result obtained")
    return result
     

def get_bottom_distance():
    result = None
    while(result == None or result == 0):
        result = filter_distance(raw_bottom_distance, 14.6)
        if(result == None):
            print("None result obtained")
    return result


    
