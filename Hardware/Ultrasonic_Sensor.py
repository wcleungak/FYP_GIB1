import RPi.GPIO as GPIO
import time
from scipy.signal import savgol_filter

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

def left_distance():
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

def bottom_distance():
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

def filter_distance(distance_func, num_samples=10, filter_window=5, filter_polyorder=2, delay_between_samples=0.05):
    # Collect distance samples
    samples = []
    for _ in range(num_samples):
        samples.append(distance_func())
        time.sleep(delay_between_samples)
    samples = [s for s in samples if s is not None]  # Remove None values
    if not samples:  # If all samples are None, return None
        return None

    # Apply the Savitzky-Golay filter
    filtered_samples = savgol_filter(samples, filter_window, filter_polyorder)

    # Return the average of the filtered samples
    return sum(filtered_samples) / len(filtered_samples)

def get_left_distance():
    return filter_distance(left_distance)
     

def get_bottom_distance():
    return filter_distance(bottom_distance)


    
