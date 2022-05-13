from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

ENV = 'dev'

if ENV == 'dev':
    app.debug = True
    app.config['SQLACHEMY_DATABASE_URI'] = 'postgresql://yudhistiradwiki:TRPL2k19@localhost/sis'
else:
    app.debug = False
    app.config['SQLACHEMY_DATABASE_URI'] = ''

app.config['SQLACHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class Login(db.Model):
    __tablename__ = 'login'
    id = db.Column(db.Integer, primary_key = True)
    pswd = db.Column(db.String(200))

    def __init__(self, id, pswd):
        self.id = id
        self.pswd = pswd

@app.route('/')
def index():
    return render_template('index.html')


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
    app.run()