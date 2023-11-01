from flask import Flask

app = Flask(__name__)


def make_bold(function):
    def wrapper():
        return f"<b>{function()}</b>"

    return wrapper


def make_italic(function):
    def wrapper():
        return f"<em>{function()}</em>"

    return wrapper


def underline_text(function):
    def wrapper():
        return f"<u>{function()}</u>"

    return wrapper


@app.route("/")
@make_bold
@underline_text
@make_italic
def hello_world():
    return "<p>Hello, World!</p>"


if __name__ == '__main__':
    app.run()
