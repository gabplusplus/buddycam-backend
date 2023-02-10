import cv2
import numpy as np
import threading
import torch
import torch.nn as nn
import torchvision.models as models


#papaltan nung paths dito sa paths nyo, yung mga backslash gawin nyong forward slash

# Load COCO class labels
coco = "D:/SE2/Project/backend/buddycam-backend/streams/coco.names"
with open(coco, "r") as f:
    CLASSES = [line.strip() for line in f.readlines()]

# Load MobileNet-SSD model
model_file = "D:/SE2/Project/backend/buddycam-backend/streams/bvlc_alexnet.caffemodel"
config_file = "D:/SE2/Project/backend/buddycam-backend/streams/deploy2.prototxt"



net = cv2.dnn.readNetFromCaffe(config_file, model_file)
COLORS = np.random.uniform(0, 255, size=(len(CLASSES), 3))

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

    # def get_frame(self):
    #     image = self.frame
    #     # Perform object detection using MobileNet-SSD
    #     (h, w) = image.shape[:2]
    #     blob = cv2.dnn.blobFromImage(cv2.resize(image, (300, 300)), 0.007843, (300, 300), 127.5)
    #     net.setInput(blob)
    #     detections = net.forward()

    #     for i in np.arange(0, detections.shape[2]):
    #         confidence = detections[0, 0, i, 2]
    #         if confidence > 0.5:
    #             idx = int(detections[0, 0, i, 1])
    #             label = CLASSES[idx]
    #             box = detections[0, 0, i, 3:7] * np.array([w, h, w, h])
    #             (startX, startY, endX, endY) = box.astype("int")
    #             color = COLORS[idx]
    #             cv2.rectangle(image, (startX, startY), (endX, endY), color, 2)
    #             y = startY - 15 if startY > 15 else startY + 15
    #             cv2.putText(image, label, (startX, y), cv2.FONT_HERSHEY_SIMPLEX, 0.5, color, 2)
    #     _, jpeg = cv2.imencode('.jpg', image)
    #     return jpeg.tobytes()

    def get_frame(self):
        image = self.frame
        # Convert the image to a 4-dimensional tensor
        image = cv2.resize(image, (224, 224))
        image = np.expand_dims(image, axis=0)
        image = image.transpose((0, 3, 1, 2))
        
        # Load the AlexNet model
        model = models.alexnet(pretrained=True)
        model.eval()
        
        # Perform object classification using AlexNet
        with torch.no_grad():
            image = torch.from_numpy(image).float()
            output = model(image)
            predictions = torch.nn.functional.softmax(output, dim=1)
            _, predicted_class = torch.max(predictions, 1)
        
        # Draw a rectangle and put the class label on the image
        cv2.rectangle(image, (0, 0), (224, 224), (0, 255, 0), 2)
        cv2.putText(image, str(predicted_class), (100, 100), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
        
        # Encode the image as JPEG and return it
        _, jpeg = cv2.imencode('.jpg', image[0])
        return jpeg.tobytes()

    def update(self):
        while True:
            (self.grabbed, self.frame) = self.video.read()

def gen1(camera):
    while True:
        frame = camera.get_frame()
        yield(b'--frame\r\n'
            b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')
