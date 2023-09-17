import tensorflow as tf
import numpy as np
from io import BytesIO
from PIL import Image
import yaml
import cv2
import os

print("TensorFlow version:", tf.__version__)
print("NumPy version:", np.__version__)
print("OpenCV version:", cv2.__version__)

def load_file(filename):  # metadata file that extracts the class names
    with open(filename, 'r') as file:
        class_names = yaml.safe_load(file)
    return class_names

def load_model(model_path):
    return tf.keras.models.load_model(model_path)

def inference(model, image_bytes, class_names):
    image = Image.open(BytesIO(image_bytes))
    img_processed = cv2.resize(np.array(image), (128, 128))
    img_processed = img_processed / 255.0
    
    # inference
    predictions = model.predict(np.array([img_processed]), verbose=0)\
    
    return class_names[np.argmax(predictions)]
