import sys
import turtle
import pandas as pd

screen = turtle.Screen()
screen.title("U.S STATES QUIZ")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

correct_state_count = 0

states_50 = pd.read_csv("50_states.csv")
states = states_50.qstate.to_list()

guessed_states = []
while len(guessed_states) < 50:
    state = screen.textinput(title=f"{len(guessed_states)}/{len(states)} "
                                   f"correct states", prompt="whats another city name").title()
    if state == "Exit":
        not_guessed_states = [state for state in states_50 if state not in guessed_states]
        un_guessed_states = pd.DataFrame(not_guessed_states)
        un_guessed_states.to_csv("states_to_learn.csv")
        break
    if state in states:
        t = turtle.Turtle()
        t.penup()
        t.hideturtle()
        correct_state_count += 1
        state_cord = states_50[states_50.qstate == state]
        t.goto(int(state_cord.x), int(state_cord.y))
        t.write(f"{state}")
        guessed_states.append(state)


