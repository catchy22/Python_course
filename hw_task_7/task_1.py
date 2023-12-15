import cv2 as cv

class task_7:
    def __init__(self,frame,w=None,h=None):
        self.w = w
        self.h = h
        if frame.split('.')[1] == 'jpg' or frame.split('.')[1] == 'png':
            self.filetype='img'
            self.frame = cv.imread(frame)
            self.load()
            self.detect()
            self.infer()
            self.view()
        elif frame.split('.')[1] == 'mp4' or frame.split('.')[1] == 'avi':
            self.filetype='vid'
            cap = cv.VideoCapture(frame)
            while cap.isOpened():
                read, self.frame = cap.read()
                self.load()
                self.detect()
                self.infer()
                self.view()

                if cv.waitKey(1) == ord('q'):
                    break

    def load(self):

        self.face_cascade = cv.CascadeClassifier(cv.data.haarcascades + 'haarcascade_frontalface_default.xml')
        self.eyes_cascade = cv.CascadeClassifier(cv.data.haarcascades + 'haarcascade_eye.xml')
        frame_gray = cv.cvtColor(self.frame, cv.COLOR_BGR2GRAY)
        self.frame_gray = cv.equalizeHist(frame_gray)

    def detect(self):
        self.faces = self.face_cascade.detectMultiScale(self.frame_gray)

    def infer(self):
        for (x, y, w, h) in self.faces:
            center = (x + w // 2, y + h // 2)
            frame = cv.ellipse(self.frame, center, (w // 2, h // 2), 0, 0, 360, (255, 0, 255), 4)
            face_ROI = self.frame_gray[y:y + h, x:x + w]

            eyes = self.eyes_cascade.detectMultiScale(face_ROI)
            for (x2, y2, w2, h2) in eyes:
                eye_center = (x + x2 + w2 // 2, y + y2 + h2 // 2)
                radius = int(round((w2 + h2) * 0.25))

                frame = cv.circle(self.frame, eye_center, radius, (255, 0, 0), 4)
    def view(self):
        if self.w and self.h != None:
            self.frame = cv.resize(self.frame, (self.w, self.h))
        if self.filetype=='img':
            cv.imshow('Capture - Face detection', self.frame)
            cv.waitKey(0)
        elif self.filetype=='vid':
            cv.imshow('Capture - Face detection', self.frame)




photo3=task_7('img3.jpg',250,250)
# photo3=task_7('img3.jpg')
video3=task_7('111.mp4',500,500)

