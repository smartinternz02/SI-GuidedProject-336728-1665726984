# -*- coding: utf-8 -*-
"""
Created on Thu Nov 10 10:24:09 2022

@author: DIVYA
"""

from flask import Flask, render_template, request
import numpy as np
import pickle
import pandas as pd

model = pickle.load(open(r"C:\Users\SmartBridge-PC\rdf.pkl", 'rb'))



app = Flask(__name__)


@app.route("/") #rendering the html page
def home():
    return render_template('home.html')

@app.route('/predict',methods=['POST','GET']) #rendering the html page
def predict():
    return render_template('input.html.html')


@app.route("/submit", methods=['POST', 'GET']) #route to show the predictions in a web UI
def submit():
    #reading the inputs given by user
    input_features = [int(x) for x in request.form.values()]
    #input_feature = np.transpose(input_feature)
    input_features = [np.array(input_features)]
   
    print(input_features)
    
    names = ['Gender','Married','Dependents','Education','Self_Employed','ApplicantIncome','CoapplicantIncome','LoanAmount','Loan_Amount_Term','Credit_History','Property_Area']
    x = pd.DataFrame(input_features, columns=names)
    print(x)
    pred = model.predict(x)
    
    print(pred[0])
    return render_template('submit.html', prediction_text=str(pred))


if __name__ == "__main__":
    app.run(debug=False)
    