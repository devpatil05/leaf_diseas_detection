# 🌿 Leaf Disease Detection

An AI/ML based web application that detects plant leaf diseases from images using Deep Learning and Computer Vision.

## 📌 Project Overview

Leaf Disease Detection is a machine learning project that identifies diseases in plant leaves from uploaded images.

The project uses a Convolutional Neural Network (CNN) trained with TensorFlow/Keras. A Flask web application provides a simple interface where users can upload a leaf image and get the predicted disease.

## 🛠️ Technologies Used

- Python
- TensorFlow / Keras
- CNN (Convolutional Neural Network)
- Flask
- HTML / CSS
- Git & GitHub

## 🎯 Objective

- Detect plant leaf diseases automatically.
- Classify leaf images using Deep Learning.
- Provide predictions through a simple web interface.
- Demonstrate the use of AI/ML in agriculture.

## ⚙️ How It Works

1. User uploads a leaf image.
2. Flask receives the image.
3. The image is preprocessed.
4. The trained CNN model analyzes the image.
5. The model predicts the disease.
6. The prediction is displayed on the web interface.

## 🧠 Model

The project uses a CNN-based image classification model trained using TensorFlow/Keras.

The model achieved approximately **99.28% validation accuracy** during training.

## 📂 Project Structure

```text
leaf_diseas_detection/
│
├── app.py
├── train.py
├── predict.py
├── leaf_disease_model.h5
├── leaf_disease_model.keras
├── test_leaf.jpg
│
└── templates/
    └── index.html
## 🚀 How to Run

### 1. Install dependencies

```bash
pip install tensorflow flask pillow numpy
2. Run the Flask application
python app.py
3. Open in browser
http://127.0.0.1:5000
