# 🏠 House-price-prediction-using-liner-regression

## 📄 Project Overview

This project aims to predict house prices using a **Linear Regression** model. By analyzing key features of residential properties, the model estimates the sale price, helping potential buyers, sellers, and real estate professionals make informed decisions.

---

## 📁 Project Structure

```
house-price-prediction/
│
├── train.csv           # Dataset 
├── house_price_model.py # Main Python script c
├── README.md           # Project documentation
└── plots/              
```

---

## 🛠️ Libraries Used

* **🐼 pandas** – For data manipulation and preprocessing
* **🤖 scikit-learn** – For:

  * Model building (`LinearRegression`)
  * Feature scaling (`StandardScaler`)
  * Data splitting (`train_test_split`)
  * Evaluation metrics (`mean_squared_error`, `r2_score`)
* **📊 matplotlib** – For data visualization

---

## 🔧 Data Preprocessing

1. **🧹 Missing Values**: Filled missing numeric values with column means.
2. **🔢 Categorical Encoding**: Converted categorical variables into numeric values using one-hot encoding.
3. **📏 Feature Scaling**: Scaled features using `StandardScaler` to normalize input for better model performance.

---

## ⭐ Important Features Used

The model uses 15 key features that strongly influence house prices:

| Feature          | Description                                    |
| ---------------- | ---------------------------------------------- |
| 🏗️ OverallQual  | Overall material and finish quality            |
| 🏠 GrLivArea     | Above grade (ground) living area in sq ft      |
| 🚗 GarageCars    | Size of garage in car capacity                 |
| ⛏️ TotalBsmtSF   | Total basement area in sq ft                   |
| 1️⃣ 1stFlrSF     | First-floor area in sq ft                      |
| 🛁 FullBath      | Number of full bathrooms                       |
| 🛋️ TotRmsAbvGrd | Total rooms above ground (excluding bathrooms) |
| 📅 YearBuilt     | Original construction year                     |
| 🔨 YearRemodAdd  | Remodel year                                   |
| 🚪 GarageArea    | Size of garage in sq ft                        |
| 🔥 Fireplaces    | Number of fireplaces                           |
| 📦 BsmtFinSF1    | Type 1 finished basement area in sq ft         |
| 🌳 LotArea       | Lot size in sq ft                              |
| 🧱 MasVnrArea    | Masonry veneer area in sq ft                   |
| 🪟 OpenPorchSF   | Open porch area in sq ft                       |



## 📈 Model Training & Evaluation

* **Model Used**: Linear Regression
* **Train-Test Split**: 80% training, 20% testing
* **Evaluation Metrics**:

  * **📉 Mean Squared Error (MSE)** – Measures the average squared difference between actual and predicted values.
  * **📊 R-squared (R²)** – Measures the proportion of variance explained by the model.

**Sample Output:**

```
Mean Squared Error: 1433232804.70
R-squared: 0.81
```

* **📊 Visualization**: Scatter plot of actual vs predicted prices to check prediction accuracy visually.

