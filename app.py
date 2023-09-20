from flask import Flask, request, jsonify
from tensorflow.keras.models import load_model
import numpy as np
from PIL import Image
import io

model = load_model('acne_classification_model.h5')

app = Flask(__name__)

class_to_skin_type = {
    0: "Acne-Cystic",
    1: "Acne-Closed",
    2: "Perioral Dermatitis",
    3: "Rosacea"
}

@app.route('/predict', methods=['POST'])
def predict_skin_type():
    try:
        image_data = request.files['image'].read()
        image = Image.open(io.BytesIO(image_data))

        # ...

        prediction = model.predict(np.array([preprocessed_image]))

        predicted_class_index = np.argmax(prediction)
        skin_type = class_to_skin_type.get(predicted_class_index, "Unknown")

        response = {
            "skin_type": skin_type
        }

        return jsonify(response)

    except Exception as e:
        return jsonify({"error": str(e)})

if __name__ == "__main__":
    app.run(debug=True)
