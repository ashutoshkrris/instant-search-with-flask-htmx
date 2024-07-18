from flask import render_template, request
from core import app
from core.models import Book


@app.route('/')
def index():
    # Fetch the first 20 songs to display by default
    books = Book.query.limit(20).all()
    return render_template("index.html", books=books)


@app.route('/search')
def search():
    query = request.args.get("query")
    if query:
        results = Book.query.filter(Book.title.ilike(f"%{query}%") | Book.author.ilike(f"%{query}%")).limit(10).all()
    else:
        # If query is empty, return the first 20 songs
        results = Book.query.limit(20).all()

    return render_template("search_results.html", results=results)
