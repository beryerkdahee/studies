from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://user:password@db:5432/mydatabase'
db = SQLAlchemy(app)

@app.route('/')
def index():
    return "1, 2, 3, 4, 5"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
