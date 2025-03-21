import requests
import numpy as np
from joblib import load
from datetime import datetime
import warnings
warnings.filterwarnings('ignore')

# Function for fetching new penguin data from API 
def fetch_new_penguin():
    url = "http://130.225.39.127:8000/new_penguin/"
    response = requests.get(url)

    if response.status_code == 200:
        new_penguin = response.json()
        print("✅ New penguin picked up:", new_penguin)
        return new_penguin
    else:
        print("Error retrieving penguin:", response.status_code)
        return None
    
# Loading the trained model and scaler
model = load("penguin_classifier.pkl")
scaler = load("scaler.pkl")

new_penguin = fetch_new_penguin()

if new_penguin:
    # Extract important features
    feature_values = np.array([[new_penguin["bill_length_mm"], 
                                new_penguin["bill_depth_mm"], 
                                new_penguin["flipper_length_mm"]]])
    
    scaled_features = scaler.transform(feature_values)
    predicted_class = model.predict(scaled_features)[0]
    
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"Prediction: The penguin is a {predicted_class}!")
    
    with open("prediction.txt", "a") as file:
        file.write(f"{timestamp}: {predicted_class}\n")
