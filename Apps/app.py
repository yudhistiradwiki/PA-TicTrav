from flask import Flask, render_template, request, make_response
from flask_sqlalchemy import SQLAlchemy
import pdfkit

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://yudhistiradwiki:TRPL2k19@localhost/tictrav'
db = SQLAlchemy(app)

class Admin(db.Model):
    user_id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True)
    password = db.Column(db.String(120))

    def __init__(self, email, password):
        self.email = email
        self.password = password

    def __repr__(self):
        return '<Admin %r>' % self.email

class User(db.Model):
    User_Id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True)
    password = db.Column(db.String(120))

    def __init__(self, email, password):
        self.email = email
        self.password = password
    
    def __repr__(self):
        return '<User %r>' % self.email

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/ticket')
def ticket():
    return render_template('ticket.html')


@app.route('/ticket/<user>/<location>')
def tickett(user, location):
    css = 'static/ticket/style.css'
    rendered = render_template('ticket.html', user=user, location=location)
    pdf = pdfkit.from_string(rendered, css=css)
    response = make_response(pdf)
    response.headers['Content-Type'] = 'application/pdf'
    response.headers['Content-Disposition'] = 'inline; filename=output.pdf'
    return response

@app.route('/login')
def loginpage():
    myUser = User.query.all()
    return render_template('login.html', datauser = myUser)

@app.route('/registration')
def registpage():
    return render_template('registration.html')

@app.route('/submit', methods=['POST'])
def submit():
    if request.method == 'POST':
        id = request.form['id']
        pswd = request.form['pass']
        #print(name,password)
        if id == '' or pswd == '':
            return render_template('index.html', message = 'please enter input')
        return render_template('2.html')

if __name__ == '__main__':
    app.run(debug=True)