# Pose Tracking with MediaPipe & OpenCV

This project performs real-time human pose tracking using MediaPipe and OpenCV. It captures webcam input, detects body landmarks, and renders a skeletal structure with custom visuals.

## Features

- Real-time pose detection from webcam
- Draws key body joints and limb connections
- Displays:
  - Original video feed with overlays
  - Clean skeletal view on a black canvas
- Head size visualized using ear distance

## Tech Stack

- [MediaPipe](https://google.github.io/mediapipe/) – Pose estimation
- [OpenCV](https://opencv.org/) – Video processing & visualization
- NumPy – Data handling and math utilities

## Structure

- `pose_tracking.py` – Main script
- `README.md` – Project overview

## Landmark Visualization

- Joints: red dots on visible keypoints
- Head: yellow circle based on ear-to-ear width
- Connections: green lines between visible joints


![2025-07-05T14:43:10,131426104+05:45](https://github.com/user-attachments/assets/a6f47514-08d8-493a-9e34-4505a9810c80)
