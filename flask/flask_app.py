from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# Database configuration
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:newpassword@localhost:5432/db'
db = SQLAlchemy(app)

# Define a model
class WaveForecast(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    forecast_date = db.Column(db.Date, nullable=False)
    wave_height = db.Column(db.Numeric(5, 2))
    swell_wave_height = db.Column(db.Numeric(5, 2))

@app.route('/')
def home():
    return jsonify({"message": "Welcome to the Flask server!"})

if __name__ == '__main__':
    app.run(debug=True)

