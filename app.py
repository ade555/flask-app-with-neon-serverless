from flask import Flask, request, jsonify
import os
from dotenv import load_dotenv
from flask_sqlalchemy import SQLAlchemy

load_dotenv()

app = Flask(__name__)
url = os.getenv('URL')

app.config["SQLALCHEMY_DATABASE_URI"]=url
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)

class Book(db.Model):
    book_id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String)

with app.app_context():
    db.create_all()

@app.route('/add_book', methods=['POST'])
def add_book():
    if request.method == 'POST':
        data = request.get_json()

        # Validate if the required fields are present in the request
        if 'title' not in data:
            return jsonify({'error': 'Missing title'}), 400

        title = data['title']

        # Create a new Book instance and add it to the database
        new_book = Book(title=title)
        db.session.add(new_book)
        db.session.commit()

        return jsonify({'message': 'Book added successfully'}), 201