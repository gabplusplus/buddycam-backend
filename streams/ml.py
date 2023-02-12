import cv2
import numpy as np
import threading


#papaltan nung paths dito sa paths nyo, yung mga backslash gawin nyong forward slash

# # Load COCO class labels
# coco = "C:/Users/Vince/Downloads/backend_buddycam/buddycam-backend/streams/coco.names"
# with open(coco, "r") as f:
#     CLASSES = [line.strip() for line in f.readlines()]

CLASSES = ('background',
           'knife', 'bicycle', 'bird', 'keyboard',
           'bottle', 'laptop', 'car', 'cat', 'chair',
           'cup', 'diningtable', 'dog', 'cell phone',
           'mouse', 'person', 'spoon',
           'scissors', 'book', 'fork', 'tvmonitor',
           )

# Load MobileNet-SSD model for camera 1
model_file_1 = "C:/Users/Vince/Downloads/backend_buddycam/buddycam-backend/streams/mobilenet_iter_73000.caffemodel"
config_file_1 = "C:/Users/Vince/Downloads/backend_buddycam/buddycam-backend/streams/deploy.prototxt"
net_1 = cv2.dnn.readNetFromCaffe(config_file_1, model_file_1)

# Load MobileNet-SSD model for camera 2
model_file_2 = "C:/Users/Vince/Downloads/backend_buddycam/buddycam-backend/streams/mobilenet_iter_73000.caffemodel"
config_file_2 = "C:/Users/Vince/Downloads/backend_buddycam/buddycam-backend/streams/deploy.prototxt"
net_2 = cv2.dnn.readNetFromCaffe(config_file_2, model_file_2)

# Load MobileNet-SSD model for camera 3
model_file_3 = "C:/Users/Vince/Downloads/backend_buddycam/buddycam-backend/streams/mobilenet_iter_73000.caffemodel"
config_file_3 = "C:/Users/Vince/Downloads/backend_buddycam/buddycam-backend/streams/deploy.prototxt"
net_3 = cv2.dnn.readNetFromCaffe(config_file_3, model_file_3)

# Load MobileNet-SSD model for camera 4
model_file_4 = "C:/Users/Vince/Downloads/backend_buddycam/buddycam-backend/streams/mobilenet_iter_73000.caffemodel"
config_file_4 = "C:/Users/Vince/Downloads/backend_buddycam/buddycam-backend/streams/deploy.prototxt"
net_4 = cv2.dnn.readNetFromCaffe(config_file_4, model_file_4)

# Load MobileNet-SSD model for camera 5
model_file_5 = "C:/Users/Vince/Downloads/backend_buddycam/buddycam-backend/streams/mobilenet_iter_73000.caffemodel"
config_file_5 = "C:/Users/Vince/Downloads/backend_buddycam/buddycam-backend/streams/deploy.prototxt"
net_5 = cv2.dnn.readNetFromCaffe(config_file_5, model_file_5)

# Load MobileNet-SSD model for camera 6
model_file_6 = "C:/Users/Vince/Downloads/backend_buddycam/buddycam-backend/streams/mobilenet_iter_73000.caffemodel"
config_file_6= "C:/Users/Vince/Downloads/backend_buddycam/buddycam-backend/streams/deploy.prototxt"
net_6 = cv2.dnn.readNetFromCaffe(config_file_6, model_file_6)


COLORS = np.random.uniform(0, 255, size=(len(CLASSES), 3))


#this class is for the first camera
class VideoCamera1(object):

    def __init__(self, url):
        self.video = cv2.VideoCapture(url)
        self.video.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)
        self.video.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
        self.video.set(cv2.CAP_PROP_FPS, 25)
        (self.grabbed, self.frame) = self.video.read()
        threading.Thread(target=self.update, args=()).start()

    def __del__(self):
        self.video.release()

    def get_frame(self):
        image = self.frame
        # Perform object detection using MobileNet-SSD
        (h, w) = image.shape[:2]
        blob = cv2.dnn.blobFromImage(cv2.resize(image, (300, 300)), 0.007843, (300, 300), 127.5)
        net_1.setInput(blob)
        detections = net_1.forward()

        for i in np.arange(0, detections.shape[2]):
            confidence = detections[0, 0, i, 2]
            if confidence > 0.2:
                idx = int(detections[0, 0, i, 1])
                label = CLASSES[idx]
                box = detections[0, 0, i, 3:7] * np.array([w, h, w, h])
                (startX, startY, endX, endY) = box.astype("int")
                color = COLORS[idx]
                cv2.rectangle(image, (startX, startY), (endX, endY), color, 2)
                y = startY - 15 if startY > 15 else startY + 15
                text = "{}: {:.2f}%".format(label, confidence * 100)
                cv2.putText(image, text, (startX, y), cv2.FONT_HERSHEY_SIMPLEX, 0.5, color, 2)
        _, jpeg = cv2.imencode('.jpg', image)
        return jpeg.tobytes()

    def update(self):
        while True:
            (self.grabbed, self.frame) = self.video.read()

def gen1(camera):
    while True:
        frame = camera.get_frame()
        yield(b'--frame\r\n'
            b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')
        

#this class is for the second camera
class VideoCamera2(object):

    def __init__(self, url):
        self.video = cv2.VideoCapture(url)
        self.video.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)
        self.video.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
        self.video.set(cv2.CAP_PROP_FPS, 25)
        (self.grabbed, self.frame) = self.video.read()
        threading.Thread(target=self.update, args=()).start()

    def __del__(self):
        self.video.release()

    def get_frame2(self):
        image = self.frame
        # Perform object detection using MobileNet-SSD
        (h, w) = image.shape[:2]
        blob = cv2.dnn.blobFromImage(cv2.resize(image, (300, 300)), 0.007843, (300, 300), 127.5)
        net_2.setInput(blob)
        detections = net_2.forward()

        for i in np.arange(0, detections.shape[2]):
            confidence = detections[0, 0, i, 2]
            if confidence > 0.5:
                idx = int(detections[0, 0, i, 1])
                label = CLASSES[idx]
                box = detections[0, 0, i, 3:7] * np.array([w, h, w, h])
                (startX, startY, endX, endY) = box.astype("int")
                color = COLORS[idx]
                cv2.rectangle(image, (startX, startY), (endX, endY), color, 2)
                y = startY - 15 if startY > 15 else startY + 15
                text = "{}: {:.2f}%".format(label, confidence * 100)
                cv2.putText(image, text, (startX, y), cv2.FONT_HERSHEY_SIMPLEX, 0.5, color, 2)
        _, jpeg = cv2.imencode('.jpg', image)
        return jpeg.tobytes()

    def update(self):
        while True:
            (self.grabbed, self.frame) = self.video.read()

def gen2(camera):
    while True:
        frame = camera.get_frame2()
        yield(b'--frame\r\n'
            b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')
        

#this class is for the third camera
class VideoCamera3(object):

    def __init__(self, url):
        self.video = cv2.VideoCapture(url)
        self.video.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)
        self.video.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
        self.video.set(cv2.CAP_PROP_FPS, 25)
        (self.grabbed, self.frame) = self.video.read()
        threading.Thread(target=self.update, args=()).start()

    def __del__(self):
        self.video.release()

    def get_frame3(self):
        image = self.frame
        # Perform object detection using MobileNet-SSD
        (h, w) = image.shape[:2]
        blob = cv2.dnn.blobFromImage(cv2.resize(image, (300, 300)), 0.007843, (300, 300), 127.5)
        net_3.setInput(blob)
        detections = net_3.forward()

        for i in np.arange(0, detections.shape[2]):
            confidence = detections[0, 0, i, 2]
            if confidence > 0.5:
                idx = int(detections[0, 0, i, 1])
                label = CLASSES[idx]
                box = detections[0, 0, i, 3:7] * np.array([w, h, w, h])
                (startX, startY, endX, endY) = box.astype("int")
                color = COLORS[idx]
                cv2.rectangle(image, (startX, startY), (endX, endY), color, 2)
                y = startY - 15 if startY > 15 else startY + 15
                text = "{}: {:.2f}%".format(label, confidence * 100)
                cv2.putText(image, text, (startX, y), cv2.FONT_HERSHEY_SIMPLEX, 0.5, color, 2)
        _, jpeg = cv2.imencode('.jpg', image)
        return jpeg.tobytes()

    def update(self):
        while True:
            (self.grabbed, self.frame) = self.video.read()

def gen3(camera):
    while True:
        frame = camera.get_frame3()
        yield(b'--frame\r\n'
            b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')
        

#this class is for the fourth camera
class VideoCamera4(object):

    def __init__(self, url):
        self.video = cv2.VideoCapture(url)
        self.video.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)
        self.video.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
        self.video.set(cv2.CAP_PROP_FPS, 25)
        (self.grabbed, self.frame) = self.video.read()
        threading.Thread(target=self.update, args=()).start()

    def __del__(self):
        self.video.release()

    def get_frame4(self):
        image = self.frame
        # Perform object detection using MobileNet-SSD
        (h, w) = image.shape[:2]
        blob = cv2.dnn.blobFromImage(cv2.resize(image, (300, 300)), 0.007843, (300, 300), 127.5)
        net_4.setInput(blob)
        detections = net_4.forward()

        for i in np.arange(0, detections.shape[2]):
            confidence = detections[0, 0, i, 2]
            if confidence > 0.5:
                idx = int(detections[0, 0, i, 1])
                label = CLASSES[idx]
                box = detections[0, 0, i, 3:7] * np.array([w, h, w, h])
                (startX, startY, endX, endY) = box.astype("int")
                color = COLORS[idx]
                cv2.rectangle(image, (startX, startY), (endX, endY), color, 2)
                y = startY - 15 if startY > 15 else startY + 15
                text = "{}: {:.2f}%".format(label, confidence * 100)
                cv2.putText(image, text, (startX, y), cv2.FONT_HERSHEY_SIMPLEX, 0.5, color, 2)
        _, jpeg = cv2.imencode('.jpg', image)
        return jpeg.tobytes()

    def update(self):
        while True:
            (self.grabbed, self.frame) = self.video.read()

def gen4(camera):
    while True:
        frame = camera.get_frame4()
        yield(b'--frame\r\n'
            b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')
        

#this class is for the fifth camera
class VideoCamera5(object):

    def __init__(self, url):
        self.video = cv2.VideoCapture(url)
        self.video.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)
        self.video.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
        self.video.set(cv2.CAP_PROP_FPS, 25)
        (self.grabbed, self.frame) = self.video.read()
        threading.Thread(target=self.update, args=()).start()

    def __del__(self):
        self.video.release()

    def get_frame5(self):
        image = self.frame
        # Perform object detection using MobileNet-SSD
        (h, w) = image.shape[:2]
        blob = cv2.dnn.blobFromImage(cv2.resize(image, (300, 300)), 0.007843, (300, 300), 127.5)
        net_5.setInput(blob)
        detections = net_5.forward()

        for i in np.arange(0, detections.shape[2]):
            confidence = detections[0, 0, i, 2]
            if confidence > 0.5:
                idx = int(detections[0, 0, i, 1])
                label = CLASSES[idx]
                box = detections[0, 0, i, 3:7] * np.array([w, h, w, h])
                (startX, startY, endX, endY) = box.astype("int")
                color = COLORS[idx]
                cv2.rectangle(image, (startX, startY), (endX, endY), color, 2)
                y = startY - 15 if startY > 15 else startY + 15
                text = "{}: {:.2f}%".format(label, confidence * 100)
                cv2.putText(image, text, (startX, y), cv2.FONT_HERSHEY_SIMPLEX, 0.5, color, 2)
        _, jpeg = cv2.imencode('.jpg', image)
        return jpeg.tobytes()

    def update(self):
        while True:
            (self.grabbed, self.frame) = self.video.read()

def gen5(camera):
    while True:
        frame = camera.get_frame5()
        yield(b'--frame\r\n'
            b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')

#this class is for the sixth camera
class VideoCamera6(object):

    def __init__(self, url):
        self.video = cv2.VideoCapture(url)
        self.video.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)
        self.video.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
        self.video.set(cv2.CAP_PROP_FPS, 25)
        (self.grabbed, self.frame) = self.video.read()
        threading.Thread(target=self.update, args=()).start()

    def __del__(self):
        self.video.release()

    def get_frame6(self):
        image = self.frame
        # Perform object detection using MobileNet-SSD
        (h, w) = image.shape[:2]
        blob = cv2.dnn.blobFromImage(cv2.resize(image, (300, 300)), 0.007843, (300, 300), 127.5)
        net_6.setInput(blob)
        detections = net_6.forward()

        for i in np.arange(0, detections.shape[2]):
            confidence = detections[0, 0, i, 2]
            if confidence > 0.5:
                idx = int(detections[0, 0, i, 1])
                label = CLASSES[idx]
                box = detections[0, 0, i, 3:7] * np.array([w, h, w, h])
                (startX, startY, endX, endY) = box.astype("int")
                color = COLORS[idx]
                cv2.rectangle(image, (startX, startY), (endX, endY), color, 2)
                y = startY - 15 if startY > 15 else startY + 15
                text = "{}: {:.2f}%".format(label, confidence * 100)
                cv2.putText(image, text, (startX, y), cv2.FONT_HERSHEY_SIMPLEX, 0.5, color, 2)
        _, jpeg = cv2.imencode('.jpg', image)
        return jpeg.tobytes()

    def update(self):
        while True:
            (self.grabbed, self.frame) = self.video.read()

def gen6(camera):
    while True:
        frame = camera.get_frame()
        yield(b'--frame\r\n'
            b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')