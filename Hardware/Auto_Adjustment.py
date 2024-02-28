import time
import Ultrasonic_Sensor as US
import Stepper_Motor as Stepper

default_distance=4
min_distance=1

def left_detection(distance):
    previous_position = US.get_bottom_distance()
    Stepper.turn_left(distance)
    time.sleep(1)
    current_position = US.get_bottom_distance()
    result = previous_position - current_position
    print("left_detection: ", previous_position, current_position, result)
    return result

def right_detection(distance):
    previous_position = US.get_bottom_distance()
    Stepper.turn_right(distance)
    time.sleep(1)
    current_position = US.get_bottom_distance()
    result = previous_position - current_position
    print("right_detection: ", previous_position, current_position, result)
    return result

def auto_adjustment():
    distance = default_distance
    direction = True
    result = 100
    temp = 0
    while(distance != min_distance or abs(temp) > 0.05):
        print("distance: ", distance, ", direction: ", direction, ", result: ", result)
        if direction:
            result = right_detection(distance)
            if result < 0:
                distance = min_distance if distance == min_distance else int(distance / 2)
                direction = False
        else:
            result = left_detection(distance)
            if result < 0:
                distance = min_distance if distance == min_distance else int(distance / 2)
                direction = True
        temp = result
        time.sleep(1)
        # print("After        distance: ", distance, ", direction: ", direction, ", result: ", result)

