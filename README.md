# 💳 Credit Card Fraud Detection API

The **Credit Card Fraud Detection API** is a machine learning-powered Flask application designed to detect fraudulent credit card transactions. It uses a pre-trained model to classify incoming transaction data as either **fraudulent** or **legitimate**.

> 🔗 **Live Deployment**: [renda.com](https://renda.com)

## 📁 Project Files

```
Credit-card-Fraud-detection-API/
├── app.py                 # Main Flask app for API functionality
├── fraudmodule.pkl        # Pre-trained machine learning model
├── profile                # Configuration for deployment (e.g., Render or Gunicorn)
├── test_API.py            # Python script to test the API
├── test_data_0.json       # Sample test data (JSON format)
├── test_data_1.json       # Sample test data (JSON format)
├── test_data_2.json       # Sample test data (JSON format)
├── test_data_3.json       # Sample test data (JSON format)
└── README.md              # Project documentation
```

## 🚀 How the API Works

- Users send a POST request with JSON data representing a transaction.
- The API loads a trained model from `fraudmodule.pkl`.
- The model returns a prediction:
  - `0` → No fraud detected
  - `1` → Fraud detected

## 📬 API Endpoint

### `POST /predict`

- **URL**: `http://127.0.0.1:5000/predict` (local) or `https://renda.com/predict` (live)
- **Headers**:
  - `Content-Type: application/json`
- **Body**: JSON formatted transaction data  
- **Response**: JSON response  
  Example:
  ```json
  {
    "prediction": 1
  }
  ```

## 🧪 How to Test the API

You can use the provided `.json` test files to simulate real transaction predictions.

### ▶️ Using Python

```bash
python test_API.py
```

### ▶️ Using `curl` (Local)

```bash
curl -X POST http://127.0.0.1:5000/predict \
-H "Content-Type: application/json" \
-d @test_data_0.json
```

### ▶️ Using `curl` (Live on renda.com)

```bash
curl -X POST https://renda.com/predict \
-H "Content-Type: application/json" \
-d @test_data_1.json
```

## 👤 About the Developer

**Godknows Nyandoro**  
AI and ML student with a strong passion for Artificial Intelligence, software engineering, and building impactful real-world applications. This project showcases my ability to integrate machine learning with web APIs for practical fraud detection use cases.

## 🌟 Features

- Flask RESTful API  
- Pre-trained machine learning model (Logistic Regression / Random Forest)  
- Testable with local or live data  
- Easily deployable (e.g., Render, Heroku)  

## 🛠 Future Enhancements

- Secure the API with authentication (e.g., API keys or JWT)  
- Improve model accuracy with new datasets  
- Add logging and monitoring  
- Create a front-end interface for user interaction  

## 📜 License

This project is intended for academic and educational use. Please contact the author for commercial or large-scale deployment.

## 🧠 Final Note

This API is a small but powerful demonstration of what machine learning can do when combined with web technology. Use the sample JSON files (`test_data_0.json` to `test_data_3.json`) to test the prediction functionality, either locally or live via renda.com.
