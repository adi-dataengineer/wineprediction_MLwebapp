import flask
from flask import Flask, request, jsonify, render_template, url_for
import pandas as pd
import pickle

app = flask.Flask(__name__)
app.config["DEBUG"] = True
filename = 'winepred.sav'
loaded_model = pickle.load(open(filename, 'rb'))

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/predict',methods = ['POST'])
def predict():
    import numpy as np
    int_features = [float(x) for x in request.form.values()]
    final_features = [np.array(int_features)]
    #a = [1.204, 4.300, 2.380, 2.200, 8.000, 2.100,
    #     1.750, 4.200, 1.350, 2.600, 7.900, 2.570,
    #     5.800]
    pred = loaded_model.predict(final_features)
    choice = str("")
    if pred[0] == 1:
        choice = "A Good selection"
    elif pred[0] == 2:
        choice = "An Excellent selection"
    else:
        choice = "Not Recommended"
    return render_template('home.html', prediction_text="We Predict your choice of wine as :{}".format(str(choice)))


if __name__ == '__main__':
    app.run(debug=True)



