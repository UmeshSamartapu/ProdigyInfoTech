import os
from flask import Flask, request, jsonify, render_template, send_from_directory
from werkzeug.utils import secure_filename
import tensorflow as tf
from PIL import Image
import numpy as np
import io
import base64
import time

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads'
app.config['MAX_CONTENT_LENGTH'] = 5 * 1024 * 1024  # 5MB limit
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}

# Create uploads directory if it doesn't exist
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

# Load the model
try:
    model = tf.keras.models.load_model('model/pix2pix_generator_model.h5')
    print("Model loaded successfully!")
except Exception as e:
    print(f"Warning: Error loading model: {str(e)}")
    model = None

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def preprocess_image(image):
    # Convert to RGB if image is RGBA
    if image.mode == 'RGBA':
        image = image.convert('RGB')
    
    # Resize to 256x256 (model's expected input size)
    image = image.resize((256, 256))
    # Convert to numpy array and normalize
    image = np.array(image) / 255.0
    # Add batch dimension
    image = np.expand_dims(image, axis=0)
    return image

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate', methods=['POST'])
def generate():
    if 'image' not in request.files and 'canvas_data' not in request.form:
        return jsonify({'error': 'No image data provided'}), 400

    try:
        if 'image' in request.files:
            file = request.files['image']
            if file and allowed_file(file.filename):
                # Process uploaded file
                image = Image.open(file.stream)
        else:
            # Process canvas data
            canvas_data = request.form['canvas_data']
            print(f"Received canvas data length: {len(canvas_data)}")
            
            # Remove the data URL prefix (e.g., "data:image/png;base64,")
            base64_data = canvas_data.split(',')[1]
            # Decode base64 data
            image_data = base64.b64decode(base64_data)
            image = Image.open(io.BytesIO(image_data))
            
            # Convert to RGB if needed
            if image.mode == 'RGBA':
                image = image.convert('RGB')
            
            # Check if the image has content
            image_array = np.array(image)
            # Calculate the mean of non-white pixels
            non_white_pixels = image_array[image_array < 250]
            if len(non_white_pixels) == 0 or np.mean(non_white_pixels) > 240:
                return jsonify({'error': 'Please draw something on the canvas first'}), 400

        # Preprocess the image
        processed_image = preprocess_image(image)
        print(f"Processed image shape: {processed_image.shape}")
        
        # Generate the output
        if model is not None:
            output = model.predict(processed_image)
            print(f"Model output shape: {output.shape}")
            
            # Convert output to image
            output_image = Image.fromarray((output[0] * 255).astype(np.uint8))
            
            # Save the output image with a unique name
            output_filename = f'output_{int(time.time())}.png'
            output_path = os.path.join(app.config['UPLOAD_FOLDER'], output_filename)
            output_image.save(output_path)
            
            return jsonify({'success': True, 'output_path': output_filename})
        else:
            return jsonify({'error': 'Model not loaded'}), 500

    except Exception as e:
        print(f"Error in generate route: {str(e)}")
        return jsonify({'error': str(e)}), 500

@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)

if __name__ == '__main__':
    app.run(debug=True) 