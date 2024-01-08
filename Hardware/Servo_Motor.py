import RPi.GPIO as GPIO
from time import sleep

# Stops all warnings from appearing
GPIO.setwarnings(False)

pwm_pin = 5

# We name all the pins on BOARD mode
GPIO.setmode(GPIO.BCM)
# Set an output for the PWM Signal
GPIO.setup(pwm_pin, GPIO.OUT)

# Set up the PWM on pin #5 at 50Hz
pwm = GPIO.PWM(pwm_pin, 50)
pwm.start(0)

def pen_control(angle):
   duty = (angle / 18) + 2
   GPIO.output(pwm_pin, True)
   pwm.ChangeDutyCycle(duty)
   sleep(1)
   GPIO.output(pwm_pin, False)
   pwm.ChangeDutyCycle(0)
   sleep(0.5)

# for i in range(0,181):
#    sig=(i/18)+2  
#    pwm.ChangeDutyCycle(sig)  
#    sleep(0.03)  
# for i in range(180,-1,-1):
#    sig=(i/18)+2  
#    pwm.ChangeDutyCycle(sig)  
#    sleep(0.03)  
# pwm.stop()  
# GPIO.cleanup()