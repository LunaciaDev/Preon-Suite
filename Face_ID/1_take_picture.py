import cv2
import time

cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Unable to open camera")
    exit()

interval = 0.25

name = input("Enter your name: ")

# Capture frames for 10 seconds
start_time = time.time()
while (time.time() - start_time) < 10:
    ret, frame = cap.read()
    if not ret:
        print("Unable to capture frame")
        continue

    filename = f"Face_ID/faces/{name}_{int(time.time())}.jpg"
    cv2.imwrite(filename, frame)
    time.sleep(interval)

cap.release()
cv2.destroyAllWindows()