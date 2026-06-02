from flask import Flask, jsonify
from models import db, Book

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///library.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

with app.app_context():
    db.create_all()

@app.route('/')
def home():
    return "Library Management API Running!"

@app.route('/addsample')
def addsample():

    book = Book(
        title="Python Basics",
        author="Ritika"
    )

    db.session.add(book)
    db.session.commit()

    return "Sample Book Added!"

@app.route('/books')
def get_books():

    books = Book.query.all()

    result = []

    for book in books:
        result.append({
            "id": book.id,
            "title": book.title,
            "author": book.author,
            "available": book.available
        })

    return jsonify(result)

@app.route('/books/<int:id>')
def get_book(id):

    book = Book.query.get_or_404(id)

    return jsonify({
        "id": book.id,
        "title": book.title,
        "author": book.author,
        "available": book.available
    })

if __name__ == "__main__":
    app.run(debug=True)