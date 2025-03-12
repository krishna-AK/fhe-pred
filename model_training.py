import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
import joblib

# Load the datasets
X = pd.read_csv("X_train.csv")
y = pd.read_csv("y_train.csv")

# Split the data into training and validation sets
X_train, X_val, y_train, y_val = train_test_split(X, y, test_size=0.2, random_state=42)

# Scale the data
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_val = scaler.transform(X_val)

# Train the model
model = LinearRegression()
model.fit(X_train, y_train)

# Evaluate the model
score = model.score(X_val, y_val)
print("R^2 score:", score)

# Save the model and scaler
joblib.dump(model, "model.joblib")
joblib.dump(scaler, "scaler.joblib")