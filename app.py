from flask import Flask, render_template, request
import pandas as pd # Flask is a application
# used to run/serve our application
# request is used to access the file which is uploaded by the user in out application
# render_template is used for rendering the html pages
import pickle # pickle is used for serializing and de-serializing Python object structures
import joblib
import subprocess
app=Flask(__name__) # our flask app
import os
#Import Libraries


    #Figure to display on page
@app.route('/') # rendering the html template
def home():
    return render_template('home.html')

@app.route('/home') # rendering the html template
def home1():
    return render_template('home.html')
@app.route('/result') # rendering the html template
def result():
    return render_template('result.html')

@app.route('/about') # rendering the html template
def dash():
    return render_template('Dahboard.html')

@app.route('/index') # rendering the html template
def index() :
    return render_template("index.html")

@app.route('/data_predict', methods=['GET','POST']) # route for our prediction
def predict():
    
    # loading model which we saved
    model = joblib.load('r1.joblib')
    
    da = [[int(x) for x in request.form.values()]] 
    #data = [[1,	2,	2,	51400,	-6300,	1,	0,	3,	4,	22,	1,	2,	10790,	5,	4,	2,]]
    print(da)
    c = pd.DataFrame(list(da),
               columns =['Month',	'DayOfWeek'	,'Make'	,'AccidentArea'		,'Sex'	,'MaritalStatus',	'Age'	,	'PolicyType',	'VehicleCategory',	'DriverRating',	'Days:Policy-Accident',	'Days:Policy-Claim','PastNumberOfClaims',	'AgeOfVehicle',	'PoliceReportFiled'	,'WitnessPresent'	,'NumberOfCars'	,'BasePolicy'])

    print(c)
    prediction= model.predict(c)
    if prediction==[0]:
        result="Insurance Claim is Genuine"
    elif prediction==[1]:
        result="Insurance Claim is Fraud"
    print(prediction)
    return render_template('result.html', prediction=result)

if __name__ == '__main__':
    app.run()