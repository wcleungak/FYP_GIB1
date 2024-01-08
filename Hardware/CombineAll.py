import Ultrasonic_Sensor as US
import Servo_Motor as Servo
import Stepper_Motor as Stepper
import time
import RPi.GPIO as GPIO

if __name__ == '__main__':
    try:
        while True:
            dist_left = US.get_left_distance()
            print ("Measured Left Distance = %.1f cm" % dist_left)
            dist_bottom = US.get_bottom_distance()
            print ("Measured Bottom Distance = %.1f cm" % dist_bottom)
            time.sleep(1)
            # Servo.pen_control(180)
            # time.sleep(1)
            # Servo.pen_control(120)
            # time.sleep(1)
            # Stepper.left_motor_forward()
            # Stepper.right_motor_forward()
            # time.sleep(1)
            # Stepper.left_motor_backward()
            # Stepper.right_motor_backward()
            # time.sleep(1)
 
    # Reset by pressing CTRL + C
    except KeyboardInterrupt:
        print("Measurement stopped by User")
        # Clean up GPIO pins
        GPIO.cleanup()





