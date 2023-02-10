import cv2
import numpy as np
import threading


#papaltan nung paths dito sa paths nyo, yung mga backslash gawin nyong forward slash

# Load COCO class labels
coco = "C:/Users/Vince/Downloads/backend_buddycam/buddycam-backend/streams/coco.names"
with open(coco, "r") as f:
    CLASSES = [line.strip() for line in f.readlines()]

# Load MobileNet-SSD model
model_file = "C:/Users/Vince/Downloads/backend_buddycam/buddycam-backend/streams/mobilenet_iter_73000.caffemodel"
config_file = "C:/Users/Vince/Downloads/backend_buddycam/buddycam-backend/streams/deploy.prototxt"



net = cv2.dnn.readNetFromCaffe(config_file, model_file)
COLORS = np.random.uniform(0, 255, size=(len(CLASSES), 3))

class VideoCamera1(object):

    def __init__(self, url):
        self.video = cv2.VideoCapture(url)
        self.video.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)
        self.video.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
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
        net.setInput(blob)
        detections = net.forward()

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
                cv2.putText(image, label, (startX, y), cv2.FONT_HERSHEY_SIMPLEX, 0.5, color, 2)
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
