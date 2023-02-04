from django.views.decorators import gzip
from django.http import StreamingHttpResponse, HttpResponse
from django.shortcuts import render
from rest_framework import response
from rest_framework import status
from .camera import VideoCamera, gen
import cv2
from streams_switch.url_manager import cam_list
import json


@gzip.gzip_page
def Cam1(request):
    print(cam_list.get("cam1")[1])
    check = cv2.VideoCapture(f'{cam_list.get("cam1")[1]}')
    if check.isOpened():
        try:
            cam = VideoCamera(f'{cam_list.get("cam1")[1]}')
            return StreamingHttpResponse(gen(cam), content_type='multipart/x-mixed-replace;boundary=frame', status=status.HTTP_200_OK)
        except:
            pass
    else:
        return HttpResponse(status=status.HTTP_503_SERVICE_UNAVAILABLE)

    return render(request)


@gzip.gzip_page
def Cam2(request):
    print(cam_list.get("cam2")[1])
    check = cv2.VideoCapture(f'{cam_list.get("cam2")[1]}')
    if check.isOpened():
        try:
            cam = VideoCamera(f'{cam_list.get("cam2")[1]}')
            return StreamingHttpResponse(gen(cam), content_type='multipart/x-mixed-replace;boundary=frame')
        except:
            pass
    else:
        return HttpResponse(status=status.HTTP_503_SERVICE_UNAVAILABLE)

    return render(request)

@gzip.gzip_page
def Cam3(request):
    check = cv2.VideoCapture(f'{cam_list.get("cam3")[1]}')
    if check.isOpened():
        try:
            cam = VideoCamera(f'{cam_list.get("cam3")[1]}')
            return StreamingHttpResponse(gen(cam), content_type='multipart/x-mixed-replace;boundary=frame')
        except:
            pass
    else:
        return HttpResponse(status=status.HTTP_503_SERVICE_UNAVAILABLE)

    return render(request)

@gzip.gzip_page
def Cam4(request):
    check = cv2.VideoCapture(f'{cam_list.get("cam4")[1]}')
    if check.isOpened():
        try:
            cam = VideoCamera(f'{cam_list.get("cam4")[1]}')
            return StreamingHttpResponse(gen(cam), content_type='multipart/x-mixed-replace;boundary=frame')
        except:
            pass
    else:
        return HttpResponse(status=status.HTTP_503_SERVICE_UNAVAILABLE)

    return render(request)

@gzip.gzip_page
def Cam5(request):
    check = cv2.VideoCapture(f'{cam_list.get("cam5")[1]}')
    if check.isOpened():
        try:
            cam = VideoCamera(f'{cam_list.get("cam5")[1]}')
            return StreamingHttpResponse(gen(cam), content_type='multipart/x-mixed-replace;boundary=frame')
        except:
            pass
    else:
        return HttpResponse(status=status.HTTP_503_SERVICE_UNAVAILABLE)

    return render(request)

@gzip.gzip_page
def Cam6(request):
    check = cv2.VideoCapture(f'{cam_list.get("cam6")[1]}')
    if check.isOpened():
        try:
            cam = VideoCamera(f'{cam_list.get("cam6")[1]}')
            return StreamingHttpResponse(gen(cam), content_type='multipart/x-mixed-replace;boundary=frame')
        except:
            pass
    else:
        return HttpResponse(status=status.HTTP_503_SERVICE_UNAVAILABLE)

    return render(request)

def camlist(request):
    cam = json.dumps(cam_list)
    return HttpResponse(cam, content_type="application/json")