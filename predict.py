import pickle

from flask import Flask
from flask import request
from flask import jsonify


model_file = 'model.bin'

with open(model_file, 'rb') as f_in: 
    dv, model = pickle.load(f_in)

app = Flask('churn')

@app.route('/predict', methods=['POST'])
def predict():
    applicant = request.get_json()

    X = dv.transform([applicant])
    y_prob = model.predict_proba(X)[0, 1]
    loan_apprv = y_prob >= 0.5

    result = {
        'churn_probability': float(y_prob),
        'churn': bool(loan_apprv)
    }

    return jsonify(result)


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=9696)
 