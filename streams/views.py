from django.views.decorators import gzip
from django.http import StreamingHttpResponse
from django.shortcuts import render
from rest_framework import response
from rest_framework import status
from .camera import VideoCamera, gen

url = []

@gzip.gzip_page
def Cam1(request):
    try:
        cam = VideoCamera("rtsp://192.168.100.5:5540/ch0")
        return StreamingHttpResponse(gen(cam), content_type='multipart/x-mixed-replace;boundary=frame')
    except:
        pass

    return render(request)

@gzip.gzip_page
def Cam2(request):
    try:
        cam = VideoCamera(0)
        return StreamingHttpResponse(gen(cam), content_type='multipart/x-mixed-replace;boundary=frame')
    except:
        pass

    return render(request)

@gzip.gzip_page
def Cam3(request):
    try:
        cam = VideoCamera("link")
        return StreamingHttpResponse(gen(cam), content_type='multipart/x-mixed-replace;boundary=frame')
    except:
        pass

    return render(request)

@gzip.gzip_page
def Cam4(request):
    try:
        cam = VideoCamera("link")
        return StreamingHttpResponse(gen(cam), content_type='multipart/x-mixed-replace;boundary=frame')
    except:
        pass

    return render(request)

@gzip.gzip_page
def Cam5(request):
    try:
        cam = VideoCamera("link")
        return StreamingHttpResponse(gen(cam), content_type='multipart/x-mixed-replace;boundary=frame')
    except:
        pass

    return render(request)

@gzip.gzip_page
def Cam6(request):
    try:
        cam = VideoCamera("link")
        return StreamingHttpResponse(gen(cam), content_type='multipart/x-mixed-replace;boundary=frame')
    except:
        pass

    return render(request)