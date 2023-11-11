import cv2
import face_recognition
import sqlite3
import numpy as np

from PySide6.QtCore import QObject, Signal, Slot, Qt, QTimer
from PySide6.QtGui import QImage

class FaceIDTask(QObject):
    sendImageSignIn = Signal(QImage)
    sendImageRegister = Signal(QImage)
    finishRegistration = Signal()
    userVerified = Signal(bool)

    def __init__(self, myThread):
        super(FaceIDTask, self).__init__()

        self.myThread = myThread
        self.verifyLoop = QTimer(self)
        self.registerLoop = QTimer(self)
        self.updateFaceData()

    def updateFaceData(self):
        database_file = "./packages/face_encodings.db"
        connection = sqlite3.connect(database_file)
        cursor = connection.cursor()

        try:
            cursor.execute("SELECT encoding, name FROM face_encodings")
        except:
            return
        
        rows = cursor.fetchall()

        self.known_encodings = []
        self.known_names = []
        for row in rows:
            encoding_bytes, name = row
            encoding = np.frombuffer(encoding_bytes, dtype=np.float64)
            encoding = encoding.reshape((128,))
            self.known_encodings.append(encoding)
            self.known_names.append(name)
    
    @Slot()
    def interruptFaceIDSignIn(self):
        self.verifyLoop.stop()

    @Slot()
    def interruptFaceIDRegister(self):
        self.registerLoop.stop()

    @Slot()
    def verifyUser(self):
        self.video_capture = cv2.VideoCapture(0)

        self.verifyLoop = QTimer(self)
        self.verifyLoop.timeout.connect(self.analyzeFrame)
        self.verifyLoop.start(30)

    @Slot()
    def analyzeFrame(self):
        ret, frame = self.video_capture.read()
        small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)
        rgb_small_frame = cv2.cvtColor(small_frame, cv2.COLOR_BGR2RGB)

        face_locations = face_recognition.face_locations(rgb_small_frame)
        face_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations)

        face_names = []
        for face_encoding in face_encodings:
            matches = face_recognition.compare_faces(self.known_encodings, face_encoding)
            name = "Unknown"

            if True in matches:
                matched_indices = [i for i, match in enumerate(matches) if match]
                first_match_index = matched_indices[0]
                name = self.known_names[first_match_index]

                self.userVerified.emit(name)
                self.verifyLoop.stop()
                self.video_capture.release()
                cv2.destroyAllWindows()

                return

            face_names.append(name)

        color_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        color_frame = cv2.flip(color_frame, 1)
        self.sendImageSignIn.emit(QImage(color_frame.data, color_frame.shape[1], color_frame.shape[0], color_frame.strides[0], QImage.Format_RGB888))

    def createDatabase(self, name, imageArray):
        self.finishRegistration.emit()
        connection = sqlite3.connect("./packages/face_encodings.db")
        cursor = connection.cursor()

        cursor.execute("CREATE TABLE IF NOT EXISTS face_encodings (id INTEGER PRIMARY KEY, encoding BLOB, name TEXT)")
        
        for image in imageArray:
            rgb_image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

            face_locations = face_recognition.face_locations(rgb_image)
            face_encodings = face_recognition.face_encodings(rgb_image, face_locations)

            cursor.execute("SELECT name FROM face_encodings WHERE name=?", (name,))
            existing_files = cursor.fetchall()
            if not existing_files:
                for encoding in face_encodings:
                    cursor.execute("INSERT INTO face_encodings (encoding, name) VALUES (?, ?)", (encoding.tobytes(), name))

        connection.commit()
        connection.close()
    
    @Slot(str)
    def registerUser(self, username):
        cap = cv2.VideoCapture(0)

        if not cap.isOpened():
            print("Unable to open camera")
            exit()

        imageArray = []

        @Slot()
        def captureImage():
            ret, frame = cap.read()

            if not ret:
                print("Unable to capture frame")
            
            imageArray.append(frame)
            color_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            color_frame = cv2.flip(color_frame, 1)
            self.sendImageRegister.emit(QImage(color_frame.data, color_frame.shape[1], color_frame.shape[0], color_frame.strides[0], QImage.Format_RGB888))

            if (len(imageArray) == 10): 
                self.registerLoop.stop()

                cap.release()
                cv2.destroyAllWindows()
                self.createDatabase(username, imageArray)

        self.registerLoop = QTimer(self)
        self.registerLoop.timeout.connect(captureImage)

        self.registerLoop.start(250)
    
    @Slot()
    def terminateThread(self):
        self.verifyLoop.stop()
        self.registerLoop.stop()
        self.myThread.quit()