from picamera import PiCamera
from io import BytesIO
from picamera.exc import PiCameraClosed
from time  import sleep, time


class Camera:
    def __init__(self,framerate,resolution):
        self.camera = None
        self.framerate = framerate
        self.resolution = resolution
        self.video_state = False

    def start_camera(self, accelerometer,socket_comm,led):
        if self.camera == None:
            self.camera = PiCamera()
            self.camera.resolution = self.resolution
            self.camera.framerate = self.framerate
        
        stream = BytesIO()
        count=0
        try:
            batch= []
            for _ in self.camera.capture_continuous(stream,format='jpeg',use_video_port=True):
                count+=1
                if not accelerometer.bin_open() :
                    break
                
                stream.seek(0)
                frame_data = stream.read() #where to pass how
                batch.append(frame_data)
                stream.seek(0)
                stream.truncate()
                
                if count %10 ==0:
                    socket_comm.send('frame_data',batch)  
                    batch = []
                    
               
                #count+=1
                #print("sending frame data", count)
        except PiCameraClosed:
            print("Done")
        finally:
            led.off()
            self.end_camera()
            self.camera = None


    def end_camera(self):
        self.camera.close()

