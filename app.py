from flask import Flask, render_template, request, jsonify
import joblib

app = Flask(__name__)

# Load trained model
model = joblib.load("model.joblib")

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():
    data = request.get_json()
    query = data.get("query", "")

    # Perform prediction
    try:
        prediction = model.predict([query])[0]

        # SVM models do not have predict_proba, so we try decision_function
        try:
            score = model.decision_function([query])[0]
            probability = round(abs(score) * 10, 2)   # scale to %
        except:
            probability = 50

        result = "unsafe" if prediction == 1 else "safe"

        return jsonify({
            "prediction": result,
            "probability": probability
        })

    except Exception as e:
        return jsonify({
            "error": str(e),
            "prediction": "error",
            "probability": 0
        })


if __name__ == "__main__":
    app.run(debug=True)