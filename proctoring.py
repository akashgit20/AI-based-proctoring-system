import cv2
import numpy as np
from ultralytics import YOLO

# Load YOLOv8 model for object detection (pre-trained)
model = YOLO("yolov8n.pt")  

# Load OpenCV's pre-trained face detector (Haar Cascade)
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")

# Start video capture
cap = cv2.VideoCapture(0)

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break
    
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(50, 50))

    # Detect multiple faces (potential cheating)
    if len(faces) > 1:
        cv2.putText(frame, "Multiple Faces Detected!", (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)

    for (x, y, w, h) in faces:
        # Draw rectangle around detected faces
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

        # Approximate nose position (center of the face)
        nose_x, nose_y = x + w // 2, y + h // 2

        # Check if the person is looking away
        if nose_x < x + 20 or nose_x > (x + w) - 20:
            cv2.putText(frame, "Looking Away!", (50, 100), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)

    # Object detection using YOLO
    results = model(frame)
    for result in results:
        for box in result.boxes:
            x1, y1, x2, y2 = map(int, box.xyxy[0])
            label = result.names[int(box.cls[0])]
            cv2.rectangle(frame, (x1, y1), (x2, y2), (255, 0, 0), 2)
            cv2.putText(frame, label, (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 0, 0), 2)

    # Display the proctoring system window
    cv2.imshow("AI Proctoring System", frame)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
