from django.views.decorators import gzip
from django.http import StreamingHttpResponse
import cv2
import threading
from django.shortcuts import render
from rest_framework import response
from rest_framework import status

@gzip.gzip_page
def Cam2(request):
    try:
        cam = VideoCamera2()
        return StreamingHttpResponse(gen2(cam), content_type='multipart/x-mixed-replace;boundary=frame')
    except:
        return response.Response(status=status.HTTP_503_SERVICE_UNAVAILABLE)

    return render(request)

class VideoCamera2(object):
    
    def __init__(self):
        self.video2 = cv2.VideoCapture("rtsp://192.168.68.110:5540/ch0")
        (self.grabbed2, self.frame2) = self.video2.read()
        threading.Thread(target=self.update, args=()).start()

    def __del__(self):
        self.video2.release()

    def get_frame(self):
        image2 = self.frame2
        _, jpeg2 = cv2.imencode('.jpg', image2)
        return jpeg2.tobytes()

    def update(self):
        while True:
            (self.grabbed2, self.frame2) = self.video2.read()


def gen2(camera2):
    while True:
        frame2 = camera2.get_frame()
        yield(b'--frame\r\n'
              b'Content-Type: image/jpeg\r\n\r\n' + frame2 + b'\r\n\r\n')

