# -*- coding: utf-8 -*-

# The data we have is: StnPres, StnPresMax, StnPresMin, Temperature
# RH, RHMin, WS, WsGust, WD, WDGust
 
import joblib
import numpy as np
from flask import Flask, render_template, request, url_for
import os

modelPretrained = joblib.load("./Precipitation_Predict.pkl")
app = Flask(__name__)

@app.route('/')
def formPage():
    return render_template("form.html")


@app.route("/submit", methods = ['POST'])
def submit():

    if request.method == 'POST':
        form_data = request.form
        # print(form_data)


        inputPressure = ""
        relativeHumidity = ""
        wind = ""
        gustWind = ""
        inputTemerature = ""

        
        result = modelPretrained.predict([[
        int(form_data["currentPressure"]), 
        int(form_data["todayMaximumPressure"]), 
        int(form_data["todayMinimumPressure"]), 
        int(form_data["currentTemperature"]), 
        int(form_data["todayMaximumTemperature"]),
        int(form_data["todayMinimumTemperature"]),
        int(form_data["currentRelativeHumidity"]), 
        int(form_data["todayMinimumRelativeHumidity"]), 
        int(form_data["currentWindSpeed"]), 
        int(form_data["currentWindDirection"]), 
        int(form_data["currentGustWindSpeed"]), 
        int(form_data["currentGustWindDirection"])
        ]])

        resultProba = modelPretrained.predict_proba([[
        int(form_data["currentPressure"]), 
        int(form_data["todayMaximumPressure"]), 
        int(form_data["todayMinimumPressure"]), 
        int(form_data["currentTemperature"]), 
        int(form_data["todayMaximumTemperature"]),
        int(form_data["todayMinimumTemperature"]),
        int(form_data["currentRelativeHumidity"]), 
        int(form_data["todayMinimumRelativeHumidity"]), 
        int(form_data["currentWindSpeed"]), 
        int(form_data["currentWindDirection"]), 
        int(form_data["currentGustWindSpeed"]), 
        int(form_data["currentGustWindDirection"])
        ]])

        print(f'Result:{result}')
        print(f'Result_Proba:{resultProba}')

        if result[0] == 1.:
            prediction = f'會下雨哦！ - 系統信心 {resultProba[0][1]:.10f}'
        else:
            prediction = f'不會下雨哦！ - 系統信心 {resultProba[0][0]:.10f}'
        
        
        return render_template('form.html',
        inputPressure = inputPressure,
        currentPressure = form_data["currentPressure"],
        todayMaximumPressure = form_data["todayMaximumPressure"],
        todayMinimumPressure = form_data["todayMinimumPressure"],
        inputTemerature = inputTemerature,
        currentTemperature = form_data["currentTemperature"],
        todayMaximumTemperature = form_data["todayMaximumTemperature"],
        todayMinimumTemperature = form_data["todayMinimumTemperature"],
        relativeHumidity = relativeHumidity, 
        currentRelativeHumidity = form_data["currentRelativeHumidity"],
        todayMinimumRelativeHumidity = form_data["todayMinimumRelativeHumidity"],
        wind = wind,
        currentWindSpeed = form_data["currentWindDirection"],
        currentWindDirection = form_data["currentWindDirection"],
        gustWind = gustWind,
        currentGustWindSpeed = form_data["currentGustWindSpeed"],
        currentGustWindDirection = form_data["currentGustWindDirection"],
        prediction = prediction)


if __name__ == "__main__":
    app.run()