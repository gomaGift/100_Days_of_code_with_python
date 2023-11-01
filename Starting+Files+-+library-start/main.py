from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

all_books = []


@app.route('/')
def home():
    return render_template('index.html', books=all_books)


@app.route("/add")
def add():
    return render_template('add.html')


@app.route("/add_book", methods=['POST'])
def book_entry():
    book_info = {}
    book_info['title'] = request.form["book_name"]
    book_info['author'] = request.form['book_author']
    book_info['rating'] = f'{request.form["rating"]}/10'
    all_books.append(book_info)
    return render_template('index.html', books=all_books)


if __name__ == "__main__":
    app.run(debug=True)
