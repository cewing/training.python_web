from flask import Flask
import bookdb

app = Flask(__name__)

db = bookdb.BookDB()


@app.route('/')
def books():
    # put code here that provides a list of books to a template named 
    # "book_list.html"
    pass


@app.route('/book/<book_id>/')
def book(book_id):
    # put code here that provides the details of a single book to a template 
    # named "book_detail.html"
    pass


if __name__ == '__main__':
    app.run(debug=True)
