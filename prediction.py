import requests
import numpy as np
from joblib import load
from datetime import datetime
import warnings

warnings.filterwarnings('ignore')

# Function to fetch new penguin data from API
def fetch_new_penguin():
    url = "http://130.225.39.127:8000/new_penguin/"
    response = requests.get(url)

    if response.status_code == 200:
        new_penguin = response.json()
        print("✅ New penguin picked up:", new_penguin)
        return new_penguin
    else:
        print("❌ Error retrieving penguin:", response.status_code)
        return None

# Load trained model and scaler
model = load("penguin_classifier.pkl")
scaler = load("scaler.pkl")

new_penguin = fetch_new_penguin()

if new_penguin:
    # Extract important features
    bill_length = new_penguin["bill_length_mm"]
    bill_depth = new_penguin["bill_depth_mm"]
    flipper_length = new_penguin["flipper_length_mm"]

    feature_values = np.array([[bill_length, bill_depth, flipper_length]])
    
    # Scale features and predict species
    scaled_features = scaler.transform(feature_values)
    predicted_class = model.predict(scaled_features)[0]
    
    # Get current timestamp
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    print(f"Prediction: The penguin is a {predicted_class}!")

    # Generate updated HTML content
    new_content = f"""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Penguin Species Prediction</title>
        <style>
            * {{
                margin: 0;
                padding: 0;
                box-sizing: border-box;
            }}
            body {{
                font-family: 'Arial', sans-serif;
                background-color: #f0f8ff;
                color: #333;
                padding: 20px;
                display: flex;
                justify-content: center;
                align-items: center;
                height: 100vh;
                text-align: center;
                flex-direction: column;
            }}
            h1 {{
                font-size: 3rem;
                color: #2f4f4f;
                margin-bottom: 20px;
            }}
            h2 {{
                font-size: 2rem;
                color: #4682b4;
                margin-bottom: 10px;
            }}
            .info-box {{
                background-color: #ffffff;
                border-radius: 10px;
                box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
                padding: 20px;
                width: 80%;
                max-width: 500px;
                margin-top: 20px;
                transition: transform 0.2s ease-in-out;
            }}
            .info-box:hover {{
                transform: scale(1.05);
            }}
            .info-box p {{
                font-size: 1.2rem;
                color: #333;
                padding: 10px;
                border-bottom: 1px solid #4682b4;
            }}
            .prediction-box {{
                background-color: #dff0d8;
                color: #3c763d;
                font-size: 1.5rem;
                padding: 15px;
                border-radius: 10px;
                margin-top: 20px;
                font-weight: bold;
            }}
            .timestamp {{
                font-size: 1rem;
                color: #888;
                margin-top: 10px;
            }}
            @media (max-width: 600px) {{
                h1 {{
                    font-size: 2.5rem;
                }}
                h2 {{
                    font-size: 1.5rem;
                }}
                .info-box {{
                    padding: 15px;
                }}
                .prediction-box {{
                    font-size: 1.2rem;
                }}
            }}
        </style>
    </head>
    <body>
        <h1>Penguin Species Prediction</h1>
        <h2>Latest Penguin Data</h2>
        <div class="info-box">
            <p><strong>Bill Length:</strong> {bill_length} mm</p>
            <p><strong>Bill Depth:</strong> {bill_depth} mm</p>
            <p><strong>Flipper Length:</strong> {flipper_length} mm</p>
        </div>
        <h2>Prediction</h2>
        <div class="prediction-box">
            🐧 The penguin is a <strong>{predicted_class}</strong>!
        </div>
        <div class="timestamp">Last updated: {timestamp}</div>
    </body>
    </html>
    """

    # Write updated HTML content to index.html
    with open("index.html", "w", encoding="utf-8") as file:
        file.write(new_content)

    print(f"✅ Prediction updated in index.html: {predicted_class}")
