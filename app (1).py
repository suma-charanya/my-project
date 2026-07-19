from flask import Flask, render_template, request
import pickle
import numpy as np

app = Flask(__name__)

model = pickle.load(open("model.pkl", "rb"))

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/predict')
def predict_page():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
@app.route('/result', methods=['GET', 'POST'])
def predict():
    if request.method == 'POST':
        feature_names = [
            'ID','CODE_GENDER','FLAG_OWN_CAR','FLAG_OWN_REALTY','CNT_CHILDREN',
            'AMT_INCOME_TOTAL','NAME_INCOME_TYPE','NAME_EDUCATION_TYPE',
            'NAME_FAMILY_STATUS','NAME_HOUSING_TYPE','DAYS_BIRTH','DAYS_EMPLOYED',
            'FLAG_MOBIL','FLAG_WORK_PHONE','FLAG_PHONE','FLAG_EMAIL',
            'OCCUPATION_TYPE','CNT_FAM_MEMBERS','MONTHS_BALANCE','STATUS'
        ]
        features = []
        for name in feature_names:
            value = request.form.get(name.lower(), request.form.get(name))
            if value is None:
                value = 0
            features.append(float(value))

        final_input = [np.array(features)]
        prediction = model.predict(final_input)

        if prediction[0] == 1:
            result = "Credit Card Approved"
        else:
            result = "Credit Card Rejected"

        return render_template("result.html", prediction_text=result)

    return render_template("result.html", prediction_text="Prediction page")

if __name__ == "__main__":
    app.run(debug=True)