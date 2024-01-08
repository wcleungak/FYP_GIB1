# Below imports all neccessary packages to make this Python Script run
import time
import board
from adafruit_motor import stepper
from adafruit_motorkit import MotorKit

# Below initialises the variable kit to be our I2C Connected Adafruit Motor HAT
kit = MotorKit(i2c=board.I2C())

# The below loop will run 500 times. Each loop it will move one step, clockwise, then pause for 0.01 seconds
# This will almost look like a smooth rotation.

def left_motor_forward():
    for i in range(50):
        kit.stepper1.onestep(direction=stepper.FORWARD, style=stepper.DOUBLE)
        time.sleep(0.01)
    kit.stepper1.release()

def left_motor_backward():
    for i in range(50):
        kit.stepper1.onestep(direction=stepper.BACKWARD, style=stepper.DOUBLE)
        time.sleep(0.01)
    kit.stepper1.release()

def right_motor_forward():
    for i in range(50):
        kit.stepper2.onestep(direction=stepper.BACKWARD, style=stepper.DOUBLE)
        time.sleep(0.01)
    kit.stepper2.release()

def right_motor_backward():
    for i in range(50):
        kit.stepper2.onestep(direction=stepper.FORWARD, style=stepper.DOUBLE)
        time.sleep(0.01)
    kit.stepper2.release()


# for i in range(100):

#     kit.stepper1.onestep(direction=stepper.BACKWARD)
#     kit.stepper2.onestep(direction=stepper.FORWARD)
#     time.sleep(0.01)

# The below loop will run 500 times. Each loop it will move two step, anti-Clockwise, then pause for 0.01 seconds
# This will almost look like a smooth rotation.

# for i in range(100):
    
#     kit.stepper1.onestep(direction=stepper.FORWARD, style=stepper.DOUBLE)
#     kit.stepper2.onestep(direction=stepper.BACKWARD, style=stepper.DOUBLE)
#     time.sleep(0.01)  

# The below line will de-energise the Stepper Motor so it can freely move
# kit.stepper1.release()
# kit.stepper2.release()