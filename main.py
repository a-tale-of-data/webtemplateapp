from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
import sqlite3
import logging
import data
import userinfo

web_site = Flask(__name__)
logging.basicConfig(level=logging.DEBUG)
web_site.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///webtemp.db'
web_site.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
web_site.secret_key = 'NIKITA'
db = SQLAlchemy(web_site)
print(data.result)


@web_site.route('/')
def index():
    return render_template('index.html')


@web_site.route('/Themes')
def dispthemes():
    s = data.result
    return (str(s))


@web_site.route('/Signup', methods=['POST', 'GET'])
def signup():
    if request.method == 'POST':

        try:
            username = request.form['username']
            password = request.form['password']
            email_id = request.form['email']
            conn = sqlite3.connect('user.db')
            c = conn.cursor()
            c.execute("INSERT INTO Users (name,email,password) VALUES (?,?,?)",
                      (username, email_id, password))
            conn.commit()
            msg = "You have successfully signed up.Kindly login to continue"
        except:
            conn.rollback()
            msg = "error in insert operation"

        finally:
            return render_template("Aftersignup.html", msg=msg)
            conn.close()

    elif (request.method == 'GET'):
        return render_template('Signup.html')


@web_site.route('/Landingpage')
def landingPage():
    return render_template('landing.html')


@web_site.route('/Login')
def login():
    return render_template('login.html')


@web_site.route('/Admin')
def Admin():
    con = sqlite3.connect("user.db")
    con.row_factory = sqlite3.Row

    cur = con.cursor()
    cur.execute("select * from Users")

    rows = cur.fetchall()
    return render_template("Admin.html", rows=rows)


web_site.run(host='0.0.0.0', port=8080)
