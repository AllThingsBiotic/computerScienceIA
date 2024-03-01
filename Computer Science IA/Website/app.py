from flask import Flask, render_template, url_for,jsonify,request
from flask_sqlalchemy import SQLAlchemy
import os
from datetime import datetime
from basedata import load_reservations, write_reservations

app = Flask(__name__)

def __repr__(self):
    return '<Name %r>' % self.id

#Loads front page
@app.route('/')
def index():
    return render_template('FrontPage.html')

#Routes it to render staff_login template
@app.route('/login')
def login_folder():
    return render_template('staff_login.html')

#Recieves data from form from the page that sent the /staff transfer
@app.route('/staff', methods=['post'])
def staff_folder():
    #checks if the password and username are both correct and then 
    #loads database to the staff.html template
    if(request.form['username'] == 'a' and request.form['password'] == 'a'):
        data = load_reservations()
        return render_template('Staff.html', reservation_data = data)
    else:
        return render_template('staff_login.html')

@app.route('/contactus')
def index3():
    return render_template('ContactUs.html')

@app.route('/submit_reserve', methods=['post'])
def index4():
    data=request.form
    write_reservations(data)
    return render_template('submitted.html', data = data)


if __name__ == '__main__':
  app.run(host='0.0.0.0', debug=True)



