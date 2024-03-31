from flask import Flask, render_template, request, jsonify
from keras.models import load_model
from keras.preprocessing import image
import numpy as np
import base64
import io

app = Flask(__name__)
model = load_model('model/model.h5')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/predict', methods=['POST'])
def predict():
    if 'file' not in request.files:
        return jsonify({'error': 'No file provided'}), 400

    file = request.files['file']
    img = image.load_img(file, target_size=(224, 224))
    img = image.img_to_array(img)
    img = np.expand_dims(img, axis=0)
    img = img / 255.0

    prediction = model.predict(img)
    result = 'benign' if prediction[0][0] > 0.5 else 'malignant'
    accuracy = 0.95 # Placeholder for actual accuracy calculation

    return jsonify({'classification': result, 'accuracy': accuracy})
