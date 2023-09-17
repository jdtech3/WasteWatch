import tensorflow as tf
import numpy as np
import keras
from io import BytesIO
from PIL import Image

model = keras.models.load_model('CNN')

def load_file(filename): #metadata file that extracts the class names 
    with open(filename, "r") as file:
        class_names = [line.strip() for line in file.readlines()]
    return class_names

def preprocess(image_bytes, size=(128,128)):
    image = Image.open(BytesIO(image_bytes)) #load image in from memory 
    img = image.resize(size)
    
    img_arr = tf.keras.preprocessing.image.img_to_array(img)
    img_arr = np.expand_dims(img_arr, axis=0) 
    return img_arr

def inference_loop(image_bytes):  
    predictions = model.predict(preprocess(image_bytes))
    class_names = load_file('metadata.txt')
    predicted_label = class_names[np.argmax(predictions[0])]
    print(f'Predicted Label: {predicted_label}') #send this back to joe

# image is loaded into memory as a byte stream 
inference_loop(image_bytes)