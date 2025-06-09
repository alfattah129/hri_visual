# Face Analysis and Recognition System for NAO Robot

This project provides a simple Python script to analyze an image from a NAO robot’s camera. It detects faces, estimates age, gender, emotion, and performs face recognition by comparing the input with reference images.

## Features

- Detect and analyze facial age, gender, and emotion using DeepFace.
- Perform face recognition by comparing detected faces with known faces in the reference folder.
- Known faces for recognition should be added as `.jpg` images in the reference folder, with filenames in the format `name.jpg` (e.g., `alice.jpg`, `bob.jpg`).
- Easily integrate with a robot planner (e.g., NAO robot) for decision-making by modifying the main.py

## Supported Models

You can use different models for face detection and recognition with DeepFace. The default setup uses DeepFace’s standard models, but you may select from:

- **Face Detectors:** `opencv`, `retinaface`, `mtcnn`, `ssd`, `dlib`, `mediapipe`
- **Face Recognition Models:** `VGG-Face`, `Facenet`, `OpenFace`, `DeepFace`, `DeepID`, `Dlib`, `ArcFace`, `SFace`

To change models or detectors, adjust the relevant arguments in `face_analysis.py`

## Requirements

Install the required packages using pip:

```bash
pip install deepface opencv-python numpy
