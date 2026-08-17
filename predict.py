import tensorflow as tf
import numpy as np
from tensorflow.keras.preprocessing import image

# Load trained model
model = tf.keras.models.load_model("leaf_disease_model.keras")

# Class names
classes = ["early_blight", "healthy", "late_blight"]

# Test image path
img_path = "test_leaf.jpg"

# Load and preprocess image
img = image.load_img(img_path, target_size=(128, 128))
img_array = image.img_to_array(img)
img_array = np.expand_dims(img_array, axis=0)
img_array = img_array / 255.0

# Predict
prediction = model.predict(img_array)
predicted_class = classes[np.argmax(prediction)]

print("Predicted Disease:", predicted_class)