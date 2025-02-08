
## AI-Based Smart Exam Proctoring System
# Project Overview
The AI-Based Smart Exam Proctoring System is a real-time monitoring application that enhances the security of online examinations by detecting suspicious activities. It uses computer vision and deep learning techniques to ensure fairness by tracking candidates’ faces, gaze, and objects in the exam environment.

# Key Features
Face Detection & Multiple Face Monitoring

Uses Dlib's face detector to detect candidates.
Identifies multiple faces in the frame to prevent proxy attempts.
Displays a warning if more than one face is detected.
Gaze Tracking & Head Movement Detection

Uses Dlib’s 68 facial landmark predictor to track eye positions.
Detects if a candidate looks away from the screen, which might indicate cheating.
Object Detection using YOLOv8

Integrates YOLOv8 (You Only Look Once) to detect unauthorized objects like mobile phones, books, or additional screens.
Labels detected objects and highlights them in the frame.
Real-Time Video Processing

Captures video from the webcam and processes each frame in real-time.
Uses OpenCV to display alerts and draw bounding boxes.
Automated Alerts

Displays “Looking Away!” warning if the candidate is not focused on the screen.
Shows “Multiple Faces Detected!” warning if unauthorized people are present.
Highlights detected objects that may indicate malpractice.
Technology Stack
Python (Primary language)
OpenCV (Image processing)
Dlib (Face detection & landmark tracking)
YOLOv8 (Deep learning-based object detection)
NumPy (Numerical computations)
Webcam (cv2.VideoCapture) (Real-time video feed)
Project Workflow
Initialize Models

Load YOLOv8 for object detection.
Load Dlib’s face detector and 68-point facial landmark predictor.
Capture Video from Webcam

Open webcam feed (cv2.VideoCapture(0)).
Convert each frame to grayscale for face detection.
Detect Faces and Monitor Activity

Use Dlib to detect faces.
Count the number of faces (flag proxy attempts).
Detect eye position and head orientation (flag if candidate looks away).
Detect Unauthorized Objects

Run YOLOv8 to detect objects (e.g., phone, book).
Draw bounding boxes and label detected objects.
Display Alerts & Logs

Show warnings for multiple faces or looking away.
Mark detected objects in the video frame.
Display the processed video stream with detections.
Exit on User Command

The system continues running until the user presses 'q' to quit.
# Use Cases
Online Examinations: Ensures fairness in remote exams.
Interview Monitoring: Prevents cheating in online interviews.
Remote Surveillance: Can be adapted for monitoring employees in virtual workspaces.
# Possible Enhancements
Automated Recording & Logging: Store logs for review.
AI-Based Suspicion Scoring: Assign scores based on activity.
Voice Detection: Monitor if candidates are speaking.
Web-Based Integration: Implement a cloud-based monitoring dashboard.
