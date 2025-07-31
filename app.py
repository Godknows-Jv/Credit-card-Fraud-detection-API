from flask import Flask, request, jsonify
from datetime import datetime
import pickle
import numpy as np

# Load the saved model
with open("fraud_model.pkl", "rb") as file:
    model = pickle.load(file)

app = Flask(__name__)

@app.route('/')
def home():
    return "Welcome to the Credit Card fraud detection API"

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()
    features = np.array([[data['V1'], data['V2'], data['V3'], data['V4'], data['V5'],
                      data['V6'], data['V7'], data['V8'], data['V9'], data['V10'],
                      data['V11'], data['V12'], data['V13'], data['V14'], data['V15'],
                      data['V16'], data['V17'], data['V18'], data['V19'], data['V20'],
                      data['V21'], data['V22'], data['V23'], data['V24'], data['V25'],
                      data['V26'], data['V27'], data['V28'], data['Amount']]])
    prediction = model.predict(features)
    
    return jsonify({
        'fraud_status': int(prediction[0]),
        'timestamp': datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    })


if __name__ == '__main__':
    app.run(debug=True)


