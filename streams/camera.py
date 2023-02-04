# from django.views.decorators import gzip
# from django.http import StreamingHttpResponse
import cv2
import threading
# from django.shortcuts import render
# from rest_framework import response
# from rest_framework import status


# @gzip.gzip_page
# def Cam(request):
#     try:
#         cam = VideoCamera()
#         return StreamingHttpResponse(gen(cam), content_type='multipart/x-mixed-replace;boundary=frame')
#     except:
#         pass

#     return render(request)


class VideoCamera(object):
    
    def __init__(self, url):
        self.video = cv2.VideoCapture(url)
        self.video.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)
        self.video.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
        self.video.set(cv2.CAP_PROP_FOURCC, 0x32595559)
        self.video.set(cv2.CAP_PROP_FPS, 25)
        (self.grabbed, self.frame) = self.video.read()
        threading.Thread(target=self.update, args=()).start()

    def __del__(self):
        self.video.release()

    def get_frame(self):
        image = self.frame
        _, jpeg = cv2.imencode('.jpg', image)
        return jpeg.tobytes()

    def update(self):
        while True:
            (self.grabbed, self.frame) = self.video.read()


def gen(camera):
        while True:
            frame = camera.get_frame()
            yield(b'--frame\r\n'
                b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')
