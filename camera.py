import cv2 as cv
from picamera import PiCamera
from picamera.array import PiRGBArray
import time
import numpy as np

class VideoCamera(object):
    def __init__(self, flip=False, file_type=".jpg", photo_string="stream_photo"):
        self.camera = PiCamera()
        self.camera.resolution = (160, 120)
        self.camera.framerate = 40 
        self.rawCapture = PiRGBArray(self.camera, size=(160, 120))
        time.sleep(2.0)

    def __del__(self):
        self.camera.close()

    def get_frame(self):
        for frame in self.camera.capture_continuous(self.rawCapture, format="jpeg", use_video_port=True):
            frame = frame.array
            ret, jpeg = cv.imencode('.jpg', frame)
            self.rawCapture.truncate(0)
            return jpeg.tobytes()
