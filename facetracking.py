import cv2
import serial  # Make sure this is 'pyserial' (installed via pip)
import time

# Load Haar Cascade
face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

# Open camera
cap = cv2.VideoCapture(0)

# Connect to Arduino (adjust COM port)
arduino = serial.Serial('COM4', 9600)  # Now this should work
time.sleep(2)  # Allow connection to establish

while True:
    ret, frame = cap.read()
    if not ret:
        break

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 6)

    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)
        center_x = x + w // 2
        center_y = y + h // 2
        
        # Map camera coords to servo angles (0-180)
        servo_x = int((center_x / 640) * 180)
        servo_y = int((center_y / 480) * 180)
        
        # Send to Arduino (format: "Xangle,Yangle\n")
        arduino.write(f"{servo_x},{servo_y}\n".encode())

    cv2.imshow('Face Tracking', frame)
    if cv2.waitKey(1) == 27:  # Exit on ESC
        break

cap.release()
cv2.destroyAllWindows()
arduino.close()