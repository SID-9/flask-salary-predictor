import pickle
from flask import Flask, render_template, request

#OOPs concept will be appled

app=Flask(__name__)
model=pickle.load(open('model.pkl','rb'))


#route give the endpoint
#It can be assumed as"URL/"" 
@app.route('/')
#retur if the above is true
def index():
    return render_template("index.html")

@app.route('/predict',methods=['GET','POST'])
def predict():
    try:
        # converting input values to float
        age = float(request.form.get('Age'))
        gender = float(request.form.get('Gender'))
        education_level = float(request.form.get('Education Level'))
        years_of_experience = float(request.form.get('Years of Experience'))
        
        prediction = model.predict([[age,gender,education_level,years_of_experience]])
        
        output = round(prediction[0],2) # this will return outout as number instead of a list rounded upto 2 decimal places
        print(output)
        return render_template("index.html",prediction_text = f'Salary predicted is : Rs. {output}/-')
    
    except ValueError as e:
        # Handle the case where user didn't provide valid numeric input
        error_message = "Invalid input. Please enter numeric values."
        return render_template("index.html", prediction_error=error_message)


if __name__=='__main__':
    app.run(debug=True)



