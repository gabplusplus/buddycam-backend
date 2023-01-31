from django.views.decorators import gzip
from django.http import StreamingHttpResponse
import cv2
import threading
from django.shortcuts import render
from rest_framework import response
from rest_framework import status


@gzip.gzip_page
def Cam1(request):
    try:
        cam = VideoCamera1()
        return StreamingHttpResponse(gen1(cam), content_type='multipart/x-mixed-replace;boundary=frame')
    except:
        return response.Response(status=status.HTTP_503_SERVICE_UNAVAILABLE)

    return render(request)



class VideoCamera1(object):
    
    def __init__(self):
        self.video1 = cv2.VideoCapture("rtsp://192.168.68.109:5540/ch0")
        (self.grabbed1, self.frame1) = self.video1.read()
        threading.Thread(target=self.update, args=()).start()

    def __del__(self):
        self.video1.release()

    def get_frame(self):
        image1 = self.frame1
        _, jpeg1 = cv2.imencode('.jpg', image1)
        return jpeg1.tobytes()

    def update(self):
        while True:
            (self.grabbed1, self.frame1) = self.video1.read()

def gen1(camera1):
    while True:
        frame1 = camera1.get_frame()
        yield(b'--frame\r\n'
              b'Content-Type: image/jpeg\r\n\r\n' + frame1 + b'\r\n\r\n')
