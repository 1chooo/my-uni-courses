import joblib
import numpy as np
from flask import Flask, request, render_template

model_pretrained = joblib.load('./LoanOrNot-LR-20220502.pkl')
app = Flask(__name__)
 
@app.route("/")     # root directory
def formPage():
    return render_template('form.html')

 
@app.route("/submit", methods=['GET', 'POST'])
def submit():
    if request.method == 'POST':
        form_data = request.form

        #Credit_History
        Credit_History_Yes = ''
        Credit_History_No = ''
        if int(form_data['Credit_History']) == 1:
            Credit_History_Yes = 'checked'
        else:
            Credit_History_No = 'checked'

        #Gender
        Gender_Male = ''
        Gender_Female = ''
        if int(form_data['Gender'])== 1:
            Gender_Male = 'checked'
        else:
            Gender_Female = 'checked'

        #Married
        Married_Yes = ''
        Married_No = ''
        if int(form_data['Married']) == 1:
            Married_Yes = 'checked'
        else:
            Married_No = 'checked'

        #Education
        Education_Graduate = ''
        Education_NotGraduate = ''
        if int(form_data['Education']) == 0:
            Education_Graduate = 'checked'
        else:
            Education_NotGraduate = 'checked'

        #Dependents
        Dependents_0 = ''
        Dependents_1 = ''
        Dependents_2 = ''
        Dependents_3Plus = ''
        if int(form_data['Dependents']) == 0:
            Dependents_0 = 'selected'
        elif int(form_data['Dependents']) == 1:
            Dependents_1 = 'selected'
        elif int(form_data['Dependents']) == 2:
            Dependents_2 = 'selected'
        else:
            Dependents_3Plus = 'selected'

        #Self_Employed
        Self_Employed_No = ''
        Self_Employed_Yes = ''
        if int(form_data['Self_Employed']) == 0:
            Self_Employed_No = 'checked'
        else:
            Self_Employed_Yes = 'checked'

        #Property_Area
        Property_Area_Rural = ''
        Property_Area_Semiurban = ''
        Property_Area_Urban = ''
        if int(form_data['Property_Area']) == 0:
            Property_Area_Rural = 'selected'
        elif int(form_data['Property_Area']) == 1:
            Property_Area_Semiurban = 'selected'
        else:
            Property_Area_Urban = 'selected'

        """
        """
        
        # ['Credit_History','Gender','Married','Education','Dependents','Self_Employed','Property_Area','LoanAmount_log','TotalIncome_log']
        # model_pretrained.predict([[0,1,1,0,3,1,2,np.log(150),np.log(5000)]])
        result = model_pretrained.predict([[
        form_data['Credit_History'],
        form_data['Gender'],
        form_data['Married'],
        form_data['Education'],
        form_data['Dependents'],
        form_data['Self_Employed'],
        form_data['Property_Area'],
        np.log(int(form_data['LoanAmount'])),
        np.log(int(form_data['TotalIncome']))
        ]])

        result_proba = model_pretrained.predict_proba([[
        form_data['Credit_History'],
        form_data['Gender'],
        form_data['Married'],
        form_data['Education'],
        form_data['Dependents'],
        form_data['Self_Employed'],
        form_data['Property_Area'],
        np.log(int(form_data['LoanAmount'])),
        np.log(int(form_data['TotalIncome']))
        ]])

        print(f'Result:{result}')
        print(f'Result_Proba:{result_proba}')
        if result[0] == 1:
            prediction = f'核可(Y) - 系統信心 {result_proba[0][1]:.10f}'    # :.10f represent we wnt to see how many number of digits after DOT
        else:
            prediction = f'拒絕(N) - 系統信心 {result_proba[0][0]:.10f}'

        # reload html
        return render_template('form.html', 
        Credit_History_Yes = Credit_History_Yes, 
        Credit_History_No = Credit_History_No, 
        Gender_Male = Gender_Male, 
        Gender_Female = Gender_Female, 
        Married_Yes = Married_Yes, 
        Married_No = Married_No, 
        Education_Graduate = Education_Graduate, 
        Education_NotGraduate = Education_NotGraduate, 
        Dependents_0 = Dependents_0,
        Dependents_1 = Dependents_1,
        Dependents_2 = Dependents_2,
        Dependents_3Plus = Dependents_3Plus,
        Self_Employed_No = Self_Employed_No,
        Self_Employed_Yes = Self_Employed_Yes,
        Property_Area_Rural = Property_Area_Rural,
        Property_Area_Semiurban = Property_Area_Semiurban,
        Property_Area_Urban = Property_Area_Urban,
        LoanAmount = form_data['LoanAmount'],
        TotalIncome = form_data['TotalIncome'],
        prediction = prediction)


if __name__ == "__main__":
    app.run()