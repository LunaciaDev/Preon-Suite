import os
import cv2
import face_recognition
import sqlite3
import numpy as np
import time

connection = sqlite3.connect("Face_ID\\face_encodings.db")
cursor = connection.cursor()

cursor.execute("CREATE TABLE IF NOT EXISTS face_encodings (id INTEGER PRIMARY KEY, encoding BLOB, name TEXT)")

root_folder = "Face_ID\\faces"

def extract_name_from_filename(filename):
    parts = filename.split("_")
    name_parts = os.path.splitext(parts[-1])[0].split()
    name_parts = [part for part in name_parts if not part.isdigit()]

    full_name = " ".join(parts[:-1] + name_parts)

    return full_name

def process_images(folder_path):
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            if file.endswith(".jpg") or file.endswith(".png") or file.endswith(".jpeg"):
                image_path = os.path.join(root, file)
                image = cv2.imread(image_path)
                rgb_image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

                face_locations = face_recognition.face_locations(rgb_image)
                face_encodings = face_recognition.face_encodings(rgb_image, face_locations)
                name = extract_name_from_filename(file)

                cursor.execute("SELECT name FROM face_encodings WHERE name=?", (name,))
                existing_files = cursor.fetchall()
                if not existing_files:
                    for encoding in face_encodings:
                        cursor.execute("INSERT INTO face_encodings (encoding, name) VALUES (?, ?)", (encoding.tobytes(), name))

        connection.commit()

process_images(root_folder)
connection.close()