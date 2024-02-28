'''
kit.stepper1 --> right motor (FORWARD == forward, BACKWARD == backward)
kit.stepper2 --> left motor (FORWARD == backward, BACKWARD == forward)
wheel diameter = 6.8cm
'''

# Below imports all neccessary packages to make this Python Script run
import time
import board
import math
from adafruit_motor import stepper
from adafruit_motorkit import MotorKit

# Below initialises the variable kit to be our I2C Connected Adafruit Motor HAT
kit = MotorKit(i2c=board.I2C())

def distance_to_step(distance):
    return round(distance / (6.8 * math.pi) * 200) # convert cm to motor step 

def angle_to_step(angle): # Task - convent angle to step
    return

def run_motor(distance, rmt_direction, lmt_direction, turning=False):
    if not turning:
        step = distance_to_step(distance) # Conversion function for cm to step
        # print("distance: ", distance, " cm, step: ", step, " step")
    else:
        step = distance # Task - Conversion function for angle to step
    
    for i in range(step):
        kit.stepper1.onestep(direction=rmt_direction)
        kit.stepper2.onestep(direction=lmt_direction)
        time.sleep(0.01)
    kit.stepper1.release()
    kit.stepper2.release()


def forward(distance):
    run_motor(distance, stepper.FORWARD, stepper.BACKWARD)

def backward(distance):
    run_motor(distance, stepper.BACKWARD, stepper.FORWARD)

def turn_left(distance):
    run_motor(distance, stepper.FORWARD, stepper.FORWARD, True)

def turn_right(distance):
    run_motor(distance, stepper.BACKWARD, stepper.BACKWARD, True)

def release_motors():
    kit.stepper1.release()
    kit.stepper2.release()