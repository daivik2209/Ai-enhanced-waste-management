import tensorflow as tf
from flask import Flask, request, jsonify
from PIL import Image
import numpy as np

# Load the trained model
model = tf.keras.models.load_model('waste_classifier.h5')
app = Flask(__name__)

# Define waste categories
waste_labels = ['plastic', 'paper', 'metal', 'glass', 'compost']

# Helper function to preprocess image
def preprocess_image(image):
    image = image.resize((224, 224))
    image = np.array(image) / 255.0
    return np.expand_dims(image, axis=0)

@app.route('/classify-waste', methods=['POST'])
def classify_waste():
    if 'file' not in request.files:
        return jsonify({'error': 'No file uploaded'}), 400
    
    # Load image
    file = request.files['file']
    image = Image.open(file)
    processed_image = preprocess_image(image)

    # Predict waste category
    predictions = model.predict(processed_image)
    predicted_label = waste_labels[np.argmax(predictions[0])]
    
    return jsonify({'waste_type': predicted_label})

if __name__ == '__main__':
    app.run(debug=True)