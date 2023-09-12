from flask import Flask, render_template, request, redirect, url_for
import requests
import pickle
app= Flask(__name__)
model = pickle.load(open('model.pickle', 'rb'))
@app.route('/')
def home():
    return render_template('index.html')

@app.route('/true')
def true():
    return render_template('true.html')

@app.route('/false')
def false():
    return render_template('false.html')

@app.route('/submit',methods=['POST','GET'])
def submit():
    if request.method=='POST':
        age=int(request.form['age'])
        hypertension=request.form['hypertension']
        if hypertension=='no':
            hypertension=0
        else:
            hypertension=1
        heartdisease=request.form['heartDisease']
        if heartdisease=='no':
            heartdisease=0
        else:
            heartdisease=1
        bmi=float(request.form['bmi'])
        HbA1clevel=float(request.form['hba1c'])
        bloodglucoselevel=float(request.form['glucoseLevel'])
        gender=request.form['gender']
        if gender=='Male':
            male = 1
            other = 0
        elif gender=='Female':
            male = 0
            other = 0
        else:
            male = 0
            other = 1
        smokinghistory=request.form['smokingHistory']
        if smokinghistory=='current':
            current = 1
            ever = 0
            former = 0
            never = 0
            not_current = 0
        elif smokinghistory=='ever':
            current = 0
            ever = 1
            former = 0
            never = 0
            not_current = 0
        elif smokinghistory=='former':
            current = 0
            ever = 0
            former = 1
            never = 0
            not_current = 0
        elif smokinghistory=='never':
            current = 0
            ever = 0
            former = 0
            never = 1
            not_current = 0
        elif smokinghistory=='notCurrent':
            current = 0
            ever = 0
            former = 0
            never = 0
            not_current = 1
        else:
            current = 0
            ever = 0
            former = 0
            never = 0
            not_current = 0

        prediction = model.predict([[age,hypertension,heartdisease,bmi,HbA1clevel,bloodglucoselevel,male,other,current,ever,former,never,not_current]])[0]
        output = ""
        if prediction == 0:
            output="false"
        else:
            output="true"
    return redirect(url_for(output))


if __name__=='__main__':
    app.run(host='0.0.0.0',port=8080)
