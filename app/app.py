from flask import Flask, render_template, request
from ultralytics import YOLO
from PIL import Image

app = Flask(__name__)

# Dictionary for label mapping (modify as needed)
label_mapping = {
    'caterpillar': 'Caterpillar',
    'grasshopper': 'Locusts',  
    'slug': 'Slug',
    'snail': 'Gastropoda',
    'weevil': 'Curculionoidea'
}

def predict_disease(image_path):
    # Load the YOLOv5 model
    model = YOLO('runs-20240311T165335Z-001/runs/classify/train6/weights/last.pt')

    # Read and resize the input image using Pillow (PIL)
    with Image.open(image_path) as img:
        img = img.resize((255, 255))

    # Perform prediction on the image
    results = model(img, show=True)

    # Extract relevant information from the prediction
    names_dict = results[0].names
    probs = results[0].probs.data.tolist()
    predictions = [(label_mapping.get(names_dict[i], names_dict[i]), probs[i]) for i in range(len(names_dict))]

    return predictions

@app.route('/')
def home():
    return render_template('index.html', prediction=None)

@app.route('/predict', methods=['POST'])
def predict():
    # Get the image file from the request
    file = request.files['image']

    # Save the file temporarily (optional)
    image_path = 'temp_image.jpg'
    file.save(image_path)

    # Pass the image to the YOLOv5 model for prediction
    prediction = predict_disease(image_path)

    # Determine the predicted label with the highest confidence
    predicted_label, _ = max(prediction, key=lambda x: x[1])  # Unpack label only

    # Render the template with the prediction result
    return render_template('index.html', prediction=prediction, predicted_label=predicted_label)

if __name__ == '__main__':
    app.run(debug=True)
