#backup mysql

from flask import Flask, render_template, request
from flask_mysqldb import MySQL

app = Flask(__name__)

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'sistem_rekomendasi'

mysql = MySQL(app)
 
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login')
def loginpage():
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM user")
    fetchdata = cur.fetchall()
    cur.close()

    return render_template('login.html', data = fetchdata)

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
    app.run()