from mpu6050 import mpu6050
from math import acos, degrees, sqrt

class Accelerometer:
    def __init__(self, bus_address=0x68):
        self.sensor = mpu6050(bus_address)
        self.sensor.set_filter_range(mpu6050.FILTER_BW_5)

    def read_accel(self):
        data = self.sensor.get_accel_data()
        return (data['x'], data['y'], data['z'])

    def get_angle(self):
        x, y, z = self.read_accel()
        if z > 10 or z < -10:
            return 0
        mag = sqrt(x**2 + y**2 + z**2)
        z = max(-mag,min(mag,z))
        angle = degrees(acos(z/mag))
        return angle

    def bin_open(self):  # bool return 
        return self.get_angle() >= 50
