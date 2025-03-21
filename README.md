# 🐧 Penguins of Madagascar - Species Classification

This repository classifies penguin species based on bill length, bill depth and flipper length, and . It includes an automated pipeline that fetches new penguin data daily from an API and predicts its species.

## 🚀 Features
- **Database Creation**: Stores the penguin dataset in an SQLite database with two tables: `penguins` and `islands`, where `island_id` is a foreign key.
- **Data Extraction**: Retrieves and preprocesses data from the database for model training.
- **Feature Selection**: Identifies the most relevant features using Mutual Information, RFE, Random Forest, and Permutation Importance.
- **Data Preprocessing**: Standardizes features using MinMaxScaler and balances data using SMOTE.
- **Model Training**: Uses **Random Forest Classifier**, optimized with **GridSearchCV**.
- **Model & Scaler Saving**: Saves the trained model and scaler for consistent predictions.
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

## 📊 **Database Creation & Data Extraction**
The dataset is stored in an SQLite database named `penguins.db`.
The `penguinsDB.py` script creates the database and inserts the dataset into two tables:

- **penguins:** Contains penguin features and species information.

- **island:** Stores island names with `island_id` as a primary key, which is referenced in `penguins`.

### **Extracting Data**
The data is extracted using SQL queries and converted into a Pandas DataFrame by joining island name using `island_id` for preprocessing and model training.


## 📊 **Feature Selection**

To identify the most relevant features, the following methods were used:

```

Feature              | Mutual Info   | RFE  | Random Forest  | Permutation  | Importance
---------------------|---------------|------|----------------|--------------|-------------
bill_length_mm       | ✅           | ✅   | ✅             | ✅           | Important ✅
bill_depth_mm        | ✅           | ✅   | ✅             | ❌           | Important ✅
flipper_length_mm    | ✅           | ✅   | ✅             | ✅           | Important ✅
body_mass_g          | ❌           | ❌   | ❌             | ❌           | Not Important ❌
sex_Female           | ❌           | ❌   | ❌             | ❌           | Not Important ❌
sex_Male             | ❌           | ❌   | ❌             | ❌           | Not Important ❌
island_Biscoe        | ❌           | ❌   | ❌             | ❌           | Not Important ❌
island_Dream         | ❌           | ✅   | ❌             | ✅           | Not Important ❌
island_Torgersen     | ❌           | ❌   | ❌             | ❌           | Not Important ❌
```

🚀 Final features used in the model:
- `bill_length_mm`, `bill_depth_mm`, `flipper_length_mm`

---

## 🏆 **Model Training**

The model was trained using **Random Forest Classifier**, optimized with **GridSearchCV** for hyperparameter tuning.

### **Data Preprocessing**
- **Scaling**: Features are standardized using MinMaxScaler.
- **Balancing**: The dataset is balanced using **SMOTE** to handle class imbalances.

### **Best Hyperparameters Found with GridSearchCV**
```
Best Parameters: {'class_weight': 'balanced', 'max_depth': None, 'min_samples_leaf': 1, 'min_samples_split': 2, 'n_estimators': 100, 'random_state': 42}
```

### **Classification Report**
```
              precision    recall  f1-score   support

      Adelie       1.00      0.97      0.98        29
   Chinstrap       0.93      1.00      0.97        14
      Gentoo       1.00      1.00      1.00        24

    accuracy                           0.99        67
   macro avg       0.98      0.99      0.98        67
weighted avg       0.99      0.99      0.99        67
```

### **Saving the Model and Scaler**
The trained model and used scaler is saved as joblib to making future prediction.  
```
penguin_classifier.pkl
scaler.pkl
```

---


---

## 🔄 **Automated Prediction Pipeline**

The prediction pipeline is automated using **GitHub Actions**, which runs daily at **07:30 AM UTC**. It fetches new penguin data from an API, predicts its species using the trained model, updates an HTML file with the latest prediction, and deploys the result on **GitHub Pages**.

### **Workflow Setup (GitHub Actions)**
The workflow is defined in `.github/workflows/daily_prediction.yml` and consists of the following steps:

1. **Trigger**: The workflow runs automatically at **07:30 AM UTC** every day using a cron job and can also be triggered manually.
2. **Checkout Repository**: The latest version of the repository is pulled.
3. **Set Up Python**: Installs Python and dependencies.
4. **Fetch New Data & Make Predictions**: Runs `prediction.py` to fetch new penguin data, preprocess it, and predict the species.
5. **Deploy to GitHub Pages**: Updates `index.html` with the new prediction and pushes it to the `gh-pages` branch.


### **Prediction Script (`prediction.py`)**
The script fetches the latest penguin data from the API, preprocesses it using the saved `scaler.pkl`, predicts the species using the `penguin_classifer.pkl`, and updates `index.html` with the results.


### **Deployment to GitHub Pages**
Once `index.html` is updated, GitHub Actions commits the changes to the `gh-pages` branch, making the latest prediction accessible at:  
🔗 **[Penguin Prediction](https://pd-bds.github.io/MLOps/)**

---

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
