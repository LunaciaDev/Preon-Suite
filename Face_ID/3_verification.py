import cv2
import face_recognition
import sqlite3
import numpy as np
import time
import sys

database_file = "Face_ID/face_encodings.db"
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
sent_names = set() 

video_capture = cv2.VideoCapture(0)

def access_control(matches):
    if True in matches:
        print("Access Granted")
        time.sleep(1)
        return True
    else:
        print("Access Denied")
        time.sleep(1)
        return False

while True:
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

        face_names.append(name)
        access_control(matches)

        if matches == True:
            time.sleep(1.5)
            sys.exit()

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