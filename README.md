Attendance System Based on Facial Recognition Using Computer Vision

Project Overview
This project is an automated attendance system that leverages facial recognition technology. By utilizing Computer Vision and Machine Learning algorithms, it automates the manual process of taking attendance, reducing human intervention, and ensuring efficiency and accuracy.

Features
Real-time face detection and recognition using webcam.
Automated attendance logging into a MySQL database.
Tkinter-based GUI for ease of use.
Utilizes Haar Cascade Classifier for face detection.
Leverages the Local Binary Pattern Histogram (LBPH) algorithm for face recognition.
Easily extendable to include more complex ML models and databases.

Technologies Used
Python (for programming)
OpenCV (for image processing and computer vision)
NumPy (for array manipulation)
Tkinter (for building the GUI)
MySQL (for attendance record storage)
Pillow (for image handling)

Project Structure
├── dataset/                     # Directory for storing captured images
├── attendance/                  # Stores attendance logs in CSV format
├── login.py                     # Login Page for the project
├── main.py                      # Main Python script to run the system
├── train.py                     # Script for training the facial recognition model
├── requirements.txt             # Python dependencies list
└── README.md                    # This file

Usage
Add New Student: Register new users by capturing their facial images via the webcam.
Train Model: Train the system to recognize faces.
Mark Attendance: Detect and recognize faces in real-time via webcam, and log attendance automatically.

Author-Garv Gambhir
