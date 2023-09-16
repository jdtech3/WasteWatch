from camera import Camera
from led_control import LED
from accel import Accelerometer #samar needs to pass open or close
from jetson_socket import JetsonSocket

socket_comm = JetsonSocket("http://10.33.135.204:5000")
accelerometer = Accelerometer()

led = LED()
pi_cam = Camera(90,(360,480))

while True:
    if accelerometer.bin_open():
        led.on()
        pi_cam.start_camera(accelerometer,socket_comm)


 

    