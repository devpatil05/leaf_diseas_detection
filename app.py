from flask import Flask, render_template, request
import tensorflow as tf
from keras.preprocessing import image
import numpy as np
import os

app = Flask(__name__)
model = tf.keras.models.load_model('leaf_disease_model.keras')

classes = ['Early Blight', 'Healthy', 'Late Blight']
treatments = {
    "Early Blight": "Remove infected leaves, avoid overhead watering, and apply a recommended fungicide.",
    "Late Blight": "Improve air circulation, avoid excess moisture, and apply an appropriate fungicide immediately.",
    "Healthy": "No disease detected. Continue regular watering and balanced fertilization."
}

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    file = request.files['file']
    filepath = os.path.join('uploads', file.filename)
    os.makedirs('uploads', exist_ok=True)
    file.save(filepath)

    img = image.load_img(filepath, target_size=(128,128))
    img = image.img_to_array(img) / 255.0
    img = np.expand_dims(img, axis=0)

    pred = model.predict(img)
    predicted_class =classes[np.argmax(pred)]
    confidence = np.max(pred) * 100

    return render_template(
        "index.html",
        prediction=predicted_class,
        confidence=f"{confidence:.2f}%",
        treatment=treatments[predicted_class]
    )
if __name__== "__main__":
    app.run(debug=True)