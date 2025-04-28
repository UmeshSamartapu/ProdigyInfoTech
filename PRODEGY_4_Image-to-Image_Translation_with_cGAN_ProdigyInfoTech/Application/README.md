# Architect Visionary

A web application that transforms hand-drawn architectural sketches into photorealistic building facades using deep learning.

## Features

- Interactive HTML5 canvas for drawing sketches
- Image upload support (JPG/PNG, up to 5MB)
- Real-time image generation using TensorFlow Pix2Pix model
- Mobile-responsive design
- Before/after comparison view
- Simple and intuitive user interface

## Prerequisites

- Python 3.8 or higher
- TensorFlow 2.12.0
- Flask 2.0.1
- Pillow 9.5.0
- Other dependencies listed in requirements.txt

## Installation

1. Clone the repository:
```bash
git clone <repository-url>
cd architect-visionary
```

2. Create a virtual environment (recommended):
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Place your trained Pix2Pix model in the `model` directory:
- The model should be in `.keras` or `.h5` format
- Name it `pix2pix_model.keras`

## Usage

1. Start the Flask server:
```bash
python app.py
```

2. Open your web browser and navigate to:
```
http://localhost:5000
```

3. Use the application:
   - Draw directly on the canvas
   - Upload an existing image
   - Click "Generate" to create the photorealistic facade
   - View the results in the output panel

## Project Structure

```
architect-visionary/
├── app.py              # Flask application
├── requirements.txt    # Python dependencies
├── model/             # Directory for the trained model
│   └── pix2pix_model.keras
├── templates/         # HTML templates
│   └── index.html
└── uploads/          # Generated output images
```

## Notes

- The model expects input images to be 128x128 pixels
- Generated images are automatically resized to match the input dimensions
- The application supports both mouse and touch input for drawing
- All uploaded and generated images are stored in the `uploads` directory

## License

This project is licensed under the MIT License - see the LICENSE file for details. 