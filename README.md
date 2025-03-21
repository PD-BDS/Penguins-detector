# 🐧 Penguins of Madagascar - Species Classification

This repository classifies penguin species based on bill length, bill depth and flipper length, and . It includes an automated pipeline that fetches new penguin data daily from an API and predicts its species.

## 🚀 Features
- **Feature Selection**: Identifies the most relevant features using Mutual Information, RFE, Random Forest, and Permutation Importance.
- **Model Training**: Uses **Random Forest Classifier** for species classification.
- **Automated Data Retrieval**: Fetches new penguin data from an API every morning at 07:30 AM.
- **GitHub Actions Integration**: Automates prediction updates.
- **GitHub Pages Deployment**: Displays the latest prediction --> [Penguin Prediction](https://pd-bds.github.io/MLOps/)

---

## 📂 **Repository Structure**
```bash
Penguins-of-Madagascar/
│── .github/workflows               # Github Actions workflow
    │── daily_prediction.yml
│── Model Training
    │──model_training.ipynb         # Feature selection and model training
    │──penguins.db                  # SQL Database
    │──penguinsDB.py                # Database Creation file      
│── prediction.py                   # Prediction using API data and output in html
│── penguins_classifier.pkl         # Trained model
│── requirements.txt                # dependencies
│── README.md                       # Documentation (this file)
│── scaler.pkl                      # Saved scaler
```

---

## 📊 **Feature Selection**

To identify the most relevant features, the following methods were used:

```

echo "Feature              | Mutual Info | RFE | Random Forest | Permutation | Importance"
echo "---------------------|-------------|-----|---------------|-------------|-------------"
echo "bill_length_mm       | ✅           | ✅   | ✅             | ✅           | Important ✅"
echo "bill_depth_mm        | ✅           | ✅   | ✅             | ❌           | Important ✅"
echo "flipper_length_mm    | ✅           | ✅   | ✅             | ✅           | Important ✅"
echo "body_mass_g          | ❌           | ❌   | ❌             | ❌           | Not Important ❌"
echo "sex_Female           | ❌           | ❌   | ❌             | ❌           | Not Important ❌"
echo "sex_Male             | ❌           | ❌   | ❌             | ❌           | Not Important ❌"
echo "island_Biscoe        | ❌           | ❌   | ❌             | ❌           | Not Important ❌"
echo "island_Dream         | ❌           | ✅   | ❌             | ✅           | Not Important ❌"
echo "island_Torgersen     | ❌           | ❌   | ❌             | ❌           | Not Important ❌"
```

🚀 Final features used in the model:
- `bill_length_mm`, `bill_depth_mm`, `flipper_length_mm`

---

## 🏆 **Model Training**

The model was trained using **Random Forest Classifer**, achieving an accuracy of 99%.

**Model Performance**:
- Test Accuracy: 99%
- Cross-Validation Accuracy: 99% ± 0.00

**The trained model is saved as**:
```
models/penguin_classifier.pkl
```

---

## 🔄 **Automated Prediction Pipeline**

🔹 **1️⃣ Fetch New Penguin Data**

New penguins data are fetched by making API calls to http://130.225.39.127:8000/new_penguin/

🔹 **2️⃣ Make Prediction**

prediction are made using the trained model and the prediction is shown as a html output for showing it as a github page.

🔹 **3️⃣ Automating with GitHub Actions**

GitHub Actions runs every day at 07:30 AM and updates the github page (https://pd-bds.github.io/MLOps/)


## **🛠 Running the Project Locally**

To test the project locally, follow these steps:

1️⃣ Clone the repository:

```bash
git clone https://github.com/PD-BDS/MLOps.git
cd MLOps
```

2️⃣ Install dependencies:

```bash
pip install -r requirements.txt
```


4️⃣ Run the prediction script:

```bash
python prediction.py
```

5️⃣ Check the latest prediction:
open the index.html file to see the html output

---
