import cv2
import time
import cv2
import face_recognition
import sqlite3
import numpy as np

class FaceIDTask:

    def verifyUser(self):
        database_file = "./packages/face_encodings.db"
        connection = sqlite3.connect(database_file)
        cursor = connection.cursor()

        cursor.execute("SELECT encoding, name FROM face_encodings")
        rows = cursor.fetchall()

        known_encodings = []
        known_names = []
        for row in rows:
            encoding_bytes, name = row
            encoding = np.frombuffer(encoding_bytes, dtype=np.float64)
            encoding = encoding.reshape((128,))
            known_encodings.append(encoding)
            known_names.append(name)

        face_locations = []
        face_encodings = []
        face_names = []

        video_capture = cv2.VideoCapture(0)
            
        match_found = True

        while match_found:
            ret, frame = video_capture.read()
            small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)
            rgb_small_frame = cv2.cvtColor(small_frame, cv2.COLOR_BGR2RGB)

            face_locations = face_recognition.face_locations(rgb_small_frame)
            face_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations)

            face_names = []
            for face_encoding in face_encodings:
                matches = face_recognition.compare_faces(known_encodings, face_encoding)
                name = "Unknown"

                if True in matches:
                    matched_indices = [i for i, match in enumerate(matches) if match]
                    first_match_index = matched_indices[0]
                    name = known_names[first_match_index]
                    match_found = False

                face_names.append(name)
                self.access_control(matches, name)

            for (top, right, bottom, left), name in zip(face_locations, face_names):
                top *= 4
                right *= 4
                bottom *= 4
                left *= 4

                cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)
                cv2.putText(frame, name, (left + 6, bottom - 6), cv2.FONT_HERSHEY_SIMPLEX, 1.0, (0, 0, 255), 1)

            cv2.imshow("Video", frame)

            if cv2.waitKey(1) & 0xFF == ord("q"):
                break

        video_capture.release()
        cv2.destroyAllWindows()

    def access_control(self, matches, name):
        if True in matches:
            print("Access Granted")
            print(f"Welcome {name}")
            time.sleep(1)
            return "Access Granted"
        else:
            print("Access Denied") 
            time.sleep(1)
            return "Access Denied"

    def createDatabase(self, name, imageArray):
        connection = sqlite3.connect("./packages/face_encodings.db")
        cursor = connection.cursor()

        cursor.execute("CREATE TABLE IF NOT EXISTS face_encodings (id INTEGER PRIMARY KEY, encoding BLOB, name TEXT)")

        def process_images():
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

        process_images()
        connection.close()
    
    def registerUser(self):
        cap = cv2.VideoCapture(0)

        if not cap.isOpened():
            print("Unable to open camera")
            exit()

        interval = 0.25
        imageArray = []
        name = input("Enter your name: ")

        # Capture frames for 10 seconds
        start_time = time.time()
        while (time.time() - start_time) < 10:
            ret, frame = cap.read()

            if not ret:
                print("Unable to capture frame")
                continue
            
            imageArray.append(frame)
            
            time.sleep(interval)

        cap.release()
        cv2.destroyAllWindows()
        self.createDatabase(name, imageArray)


temp = FaceIDTask()
temp.verifyUser()