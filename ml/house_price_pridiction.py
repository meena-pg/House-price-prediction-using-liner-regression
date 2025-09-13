import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv('train.csv')

# Fill missing numeric values with column means
numeric_cols = df.select_dtypes(include=['number']).columns
df[numeric_cols] = df[numeric_cols].fillna(df[numeric_cols].mean())

# Convert categorical variables into numbers
df = pd.get_dummies(df)

# Define features and target
important_features = ['OverallQual', 'GrLivArea', 'GarageCars', 'TotalBsmtSF',
                      '1stFlrSF', 'FullBath', 'TotRmsAbvGrd', 'YearBuilt',
                      'YearRemodAdd', 'GarageArea', 'Fireplaces',
                      'BsmtFinSF1', 'LotArea', 'MasVnrArea', 'OpenPorchSF']

x = df[important_features]
y = df['SalePrice']

# Scale features
scaler = StandardScaler()
x_scaled = scaler.fit_transform(x)

# Split into train and test sets
x_train, x_test, y_train, y_test = train_test_split(x_scaled, y, test_size=0.2, random_state=42)

# Train the model
model = LinearRegression()
model.fit(x_train, y_train)

# Predict
y_pred = model.predict(x_test)

# Evaluate
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print(f"Mean Squared Error: {mse:.2f}")
print(f"R-squared: {r2:.2f}")

# Comparison of actual vs predicted
results = pd.DataFrame({'Actual': y_test, 'Predicted': y_pred})
print(results.head())

# Plot Actual vs Predicted
plt.figure(figsize=(8,6))
plt.scatter(y_test, y_pred, alpha=0.6, color='blue')
plt.plot([y_test.min(), y_test.max()], [y_test.min(), y_test.max()], color='red', linewidth=2)
plt.xlabel('Actual Sale Price')
plt.ylabel('Predicted Sale Price')
plt.title('Actual vs Predicted Sale Price')
plt.grid(True)
plt.show()