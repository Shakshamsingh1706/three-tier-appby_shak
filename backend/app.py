from flask import Flask
import mysql.connector

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello from Flask Backend!"

@app.route('/api')
def api():
    return "This is the /api endpoint from Backend from flask!"

@app.route('/db')
def db_check():
    try:
        conn = mysql.connector.connect(
            host='db',
            user='user',
            password='pass',
            database='appdb'
        )
        return "Connected to MySQL DB!"
    except Exception as e:
        return str(e)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

