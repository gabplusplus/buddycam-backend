import cv2
import threading
import datetime

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
    
    def release(self):
        self.video.release()

    def record_frame(self):
        return self.frame

    def update(self):
        while True:
            (self.grabbed, self.frame) = self.video.read()

def gen(camera, name):
    fourcc = cv2.VideoWriter_fourcc(*'XVID')
    current_time = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    # Change this path to save to your local
    video_path = f"D:/SE2/Project/backend/records/video_{name}_{current_time}.avi"
    out = cv2.VideoWriter(video_path, fourcc, 20.0, (640, 480))
    try:
        while True:
            frame = camera.get_frame()
            rec = camera.record_frame()
            out.write(rec)
            yield(b'--frame\r\n'
            b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')
    finally:
        out.release()
        print("Recording stopped")
