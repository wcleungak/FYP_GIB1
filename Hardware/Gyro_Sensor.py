import smbus            
from time import sleep, time
import math
import RPi.GPIO as GPIO
import sys
 
PWR_MGMT_1   = 0x6B
SMPLRT_DIV   = 0x19
CONFIG       = 0x1A
GYRO_CONFIG  = 0x1B
INT_ENABLE   = 0x38
ACCEL_XOUT_H = 0x3B
ACCEL_YOUT_H = 0x3D
ACCEL_ZOUT_H = 0x3F
GYRO_XOUT_H  = 0x43
GYRO_YOUT_H  = 0x45
GYRO_ZOUT_H  = 0x47
bus = smbus.SMBus(1)

Device_Address = 0x68  

startTime = time()
currentTime = 0
GyroErrorZ = 0
yaw = 0
 
def MPU_Init():
    bus.write_byte_data(Device_Address, SMPLRT_DIV, 7)
    bus.write_byte_data(Device_Address, PWR_MGMT_1, 1)
    bus.write_byte_data(Device_Address, CONFIG, 0)
    bus.write_byte_data(Device_Address, GYRO_CONFIG, 24)
    bus.write_byte_data(Device_Address, INT_ENABLE, 1)
 
def read_raw_data(addr):
        high = bus.read_byte_data(Device_Address, addr)
        low = bus.read_byte_data(Device_Address, addr+1)
        value = ((high << 8) | low)
        if(value > 32768):
                value = value - 65536
        return value
 
 
def dist(a, b):
    return math.sqrt((a*a) + (b*b))
 
def get_y_rotation(x, y, z):
    radians = math.atan2(y, z)
    return -(radians * (180.0 / math.pi))
  
def get_x_rotation(x, y, z):
    radians = math.atan2(x, dist(y, z))
    return -(radians * (180.0 / math.pi))

def get_z_rotation():
    global currentTime, startTime, yaw, GyroErrorZ
    currentTime = time()
    elapsedTime = (currentTime - startTime)
    print("currentTime ", currentTime)
    print("startTime ", startTime)
    print("elapsedTime ", elapsedTime)
    startTime = currentTime
    GyroZ = readGyroZ() - GyroErrorZ
    print("Inside GyroZ ", GyroZ)
    print("Inside GyroErrorZ ", GyroErrorZ)
    yaw += GyroZ * elapsedTime
    return yaw

def readGyroZ():
    return read_raw_data(GYRO_ZOUT_H) / 131.0

def calculateError():
    global GyroErrorZ
    t = 0
    while(t < 200):
        GyroErrorZ += readGyroZ()
        t += 1
    GyroErrorZ = GyroErrorZ / 200

def init():
    MPU_Init()
    calculateError()
    print("Reading MPU6050...")

def read():
    try:
        # acc_x = read_raw_data(ACCEL_XOUT_H)
        # acc_y = read_raw_data(ACCEL_YOUT_H)
        # acc_z = read_raw_data(ACCEL_ZOUT_H)
            
        # acclX_scaled = acc_x * .000061 * 9.80665
        # acclY_scaled = acc_y * .000061 * 9.80665
        # acclZ_scaled = acc_z * .000061 * 9.80665
            
        # x_angle = round(get_x_rotation(acclX_scaled, acclY_scaled, acclZ_scaled))
        # y_angle = round(get_y_rotation(acclX_scaled, acclY_scaled, acclZ_scaled))
        z_angle = round(get_z_rotation())
        # print("X rotation: ", x_angle)
        # print("Y rotation: ",y_angle)
        print("Z rotation: ",z_angle)
        sleep(.50)
    except Exception as e:
        print(e)
        sys.exit(0)
 
# if __name__ == "__main__":
         
#     Device_Address = 0x68   
#     MPU_Init()
     
#     print("Reading MPU6050...")
#     try:
#         while True:
#             acc_x = read_raw_data(ACCEL_XOUT_H)
#             acc_y = read_raw_data(ACCEL_YOUT_H)
#             acc_z = read_raw_data(ACCEL_ZOUT_H)
             
#             acclX_scaled = acc_x * .000061 * 9.80665
#             acclY_scaled = acc_y * .000061 * 9.80665
#             acclZ_scaled = acc_z * .000061 * 9.80665
             
#             x_angle = round(get_x_rotation(acclX_scaled, acclY_scaled, acclZ_scaled))
#             y_angle = round(get_y_rotation(acclX_scaled, acclY_scaled, acclZ_scaled))
#             print("X rotation: ", x_angle)
#             print("Y rotation: ",y_angle)
#             sleep(.50)
#     except KeyboardInterrupt:
#         sys.exit(0)
#     except Exception as e:
#         print(e)
#         sys.exit(0)