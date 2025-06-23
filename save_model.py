from sklearn.linear_model import LinearRegression
import numpy as np
import joblib

# Training data
X = np.array([[1000], [1500], [2000], [2500], [3000]])
y = np.array([25, 55, 80, 85, 90])

model = LinearRegression()
model.fit(X, y)

joblib.dump(model, "model.pkl")
print("✅ Model saved successfully.")
