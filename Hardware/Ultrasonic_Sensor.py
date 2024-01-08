import RPi.GPIO as GPIO
import time

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

def get_left_distance():
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
    distance = round(pulse_duration * 17150, 2)

    return distance

def get_bottom_distance():
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
    distance = round(pulse_duration * 17150, 2)

    return distance

# # Print the distance in centimeters
# print("Left Distance: %.2f cm" % get_left_distance())
# print("Bottom Distance: %.2f cm" % get_left_distance())

# if __name__ == '__main__':
#     try:
#         while True:
#             dist_left = get_left_distance()
#             dist_bottom = get_bottom_distance()
#             print ("Measured Left Distance = %.1f cm" % dist_left)
#             print ("Measured Bottom Distance = %.1f cm" % dist_bottom)
#             time.sleep(1)
 
#         # Reset by pressing CTRL + C
#     except KeyboardInterrupt:
#         print("Measurement stopped by User")
#         # Clean up GPIO pins
#         GPIO.cleanup()
