import Ultrasonic_Sensor as US
import Servo_Motor as Servo
import Stepper_Motor as Stepper
import Auto_Adjustment as AA
import time
import RPi.GPIO as GPIO

if __name__ == '__main__':
    try:
        # while True:
            # dist_left = US.get_left_distance()
            # print ("Measured Left Distance = %i cm" % dist_left)
            # dist_bottom = US.get_bottom_distance()
            # print ("Measured Bottom Distance = %i cm" % dist_bottom)
            # time.sleep(2)
            # Servo.penDown()
            # time.sleep(1)
            # Servo.penUp()
            # time.sleep(1)
            Stepper.forward(3)
            # time.sleep(3)
            # Stepper.backward(3)
            # time.sleep(3)
            # Stepper.turn_left(50)
            # time.sleep(3)
            # Stepper.turn_right(50)
            # time.sleep(3)
            # AA.auto_adjustment()
            GPIO.cleanup()
            Stepper.release_motors()
 
    # Reset by pressing CTRL + C
    except KeyboardInterrupt:
        print("Measurement stopped by User")
        # Clean up GPIO pins
        GPIO.cleanup()
        Stepper.release_motors()





