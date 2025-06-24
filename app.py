from flask import Flask, render_template, request
import joblib
import os

app = Flask(__name__)
model = joblib.load("model.pkl")

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/predict', methods=['POST'])
def predict():
    area = float(request.form['area'])
    prediction = model.predict([[area]])
    return render_template("index.html", prediction=prediction[0])

# ✅ Correct place and way to run the app
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))  # Render will set PORT
    app.run(host="0.0.0.0", port=port)


