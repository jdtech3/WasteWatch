from mpu6050 import mpu6050
from math import asin, degrees

class Accelerometer:
    def __init__(self, bus_address=0x68):
        self.sensor = mpu6050(bus_address)

    def read_accel(self):
        data = self.sensor.get_accel_data()
        return (data['x'], data['y'], data['z'])

    def get_angle(self):
        x, y, z = self.read_accel()
        z = max(-1.0, min(1.0, z))
        angle = degrees(asin(z))
        return angle

    def bin_open(self):  # bool return 
        return self.get_angle() >= 20
