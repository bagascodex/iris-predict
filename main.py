#Define Library
import json
import joblib
from flask import Flask, request

app = Flask(__name__)

model = joblib.load("iris_model.joblib")

@app.route("/")
def hello_world():
    return "Hello, Mr Bagas"

@app.route("/predict", methods=['POST'])
def predict():
    request_json = request.json

    prediction = model.predict(request_json.get("data"))
    prediction_string = [str(d) for d in prediction]

    response_json = {
        "data" : request_json.get("data"),
        "prediction": list(prediction_string)
    }

    return json.dumps(response_json)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)