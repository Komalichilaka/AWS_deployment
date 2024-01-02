from flask import Flask,render_template,request
import pickle
import numpy as np
app=Flask(__name__)
'''@app.route('/')
def hello():
    """test function"""
    return "welcome to flask"


@app.route('/komali',methods=['GET'])
def check():
    """new function"""
    return "codegnan is in kits college"'''

with open('House_Price.pkl','rb')as f:
    model=pickle.load(f)
@app.route('/',methods=['GET'])
def home():
    return render_template('index.html')

@app.route('/predict',methods=['POST'])
def predictions():
    Rooms=int(request.form['bedrooms'])
    Bathrooms=int(request.form['bathrooms'])
    Place=int(request.form['location'])
    Area=int(request.form['area'])
    Status=int(request.form['status'])
    Facing=int(request.form['facing'])
    P_Type=int(request.form['type'])

    input_data=np.array([[Place,Area,Status,Rooms,Bathrooms,Facing,P_Type]])

    prediction=model.predict(input_data)[0]

    return render_template('index.html',prediction=prediction)

app.run()
