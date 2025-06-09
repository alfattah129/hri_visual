
# Face Analysis and Recognition System for NAO Robot

This project provides a simple Python script to analyze an image from a NAO robot’s camera. It detects the face, estimates age, gender, emotion, and performs face recognition by comparing the input image against known faces stored in a reference folder.

## Features

- Detect and analyze facial **age**, **gender**, and **emotion**.
- Perform **face recognition** by comparing with reference images.
- Easily integrate with a robot planner (e.g., NAO robot) for decision-making.
- Customize and extend the face recognition model and detector backend.

---

## Requirements

Install the required packages using pip:

```bash
pip install deepface opencv-python numpy
