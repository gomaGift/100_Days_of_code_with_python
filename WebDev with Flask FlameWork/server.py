from flask import Flask
import random

app = Flask(__name__)

random_number = random.randint(0, 9)


# todo:  Create a new Flask application where the home route displays an <h1> that says
#  "Guess a number between 0 and 9"

@app.route('/')
def game_board():
    return "<h1>Guess a number between 0 and 9</h1>" \
           "<img src = 'https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExOTE2NmE4ODcxNWEwZDAyY" \
           "jM1ZDgyZDZmZGQ1NDY1ZjA5NDUwYTNkOCZjdD1n/3o7aCSPqXE5C6T8tBC/giphy.gif'>"


@app.route('/<int:number>')
def check_guess(number):
    if number < random_number:
        return "<h1 style='color:red'> Sorry,your number is too low</h1>" \
               "<img src='https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif'/>"
    elif number > random_number:
        return "<h1 style='color:blue'> Sorry,your number is too high</h1>" \
               "<img src='https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif'/>"
    else:
        return f"<h1 style='color:green'> You guessed correctly, the number is: {number}</h1>" \
               "<img src='https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif'/>"


if __name__ == '__main__':
    app.run(debug=True)
