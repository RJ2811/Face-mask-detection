# 😷 Real-Time Face Mask Detection using Deep Learning

A real-time face mask detection system that uses Deep Learning and Computer Vision to identify whether a person is wearing a face mask through a live webcam feed.

---

## 📌 Overview

This project leverages **TensorFlow**, **OpenCV**, and **MobileNetV2** to detect human faces and classify them as **Mask** or **No Mask** in real time. It combines a deep learning classifier with OpenCV's face detection pipeline to provide fast and accurate predictions.

---

## 🚀 Features

- Real-time webcam face mask detection
- Face detection using OpenCV DNN
- MobileNetV2-based mask classifier
- Live prediction with confidence score
- Bounding boxes with color-coded labels
- Lightweight and fast inference

---

## 🛠 Tech Stack

- Python
- TensorFlow / Keras
- OpenCV
- MobileNetV2
- NumPy
- imutils

---

## 📂 Project Structure

```
face-mask-detection/

│── detect_mask_video.py
│── mask_detector.h5
│── test.py
│── face_detector/
│   ├── deploy.prototxt
│   └── res10_300x300_ssd_iter_140000.caffemodel
│
└── README.md
```

---

## ⚙️ How It Works

```
Webcam
   │
   ▼
Capture Frame
   │
   ▼
Face Detection
(OpenCV DNN)
   │
   ▼
Face Extraction
   │
   ▼
Image Preprocessing
   │
   ▼
MobileNetV2 Model
   │
   ▼
Mask / No Mask Prediction
   │
   ▼
Display Result
```

---

## 📈 Output

For every detected face, the system displays:

- Face Bounding Box
- Mask / No Mask Label
- Prediction Confidence Score

---

## ▶️ Installation

Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/face-mask-detection.git
```

Navigate to the project

```bash
cd face-mask-detection
```

Install dependencies

```bash
pip install tensorflow opencv-python imutils numpy
```

Run the application

```bash
python detect_mask_video.py
```

---

## 📌 Future Improvements

- Improve model accuracy with larger datasets
- Support multiple camera inputs
- Deploy as a web application
- Mobile deployment using TensorFlow Lite
- Edge device optimization

---

## 📜 License

This project is intended for educational and learning purposes.

---

## 👨‍💻 Author

**Rithvik Jaswal**

Computer Science Engineering Student

Interested in Artificial Intelligence, Computer Vision, Machine Learning, and Data Science.

---

⭐ If you found this project useful, consider giving it a star.
