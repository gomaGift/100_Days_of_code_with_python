from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"


class QuizInterface:
    def __init__(self, quiz_list: QuizBrain):
        self.quiz = quiz_list
        self.timer = ' '

        self.window = Tk()
        self.window.title("quiz")
        self.window.config(background=THEME_COLOR, padx=50, pady=50)

        # labels
        self.score = Label(text="Score: 0", bg=THEME_COLOR, fg="white", font=("Arial", '10', 'normal'))
        self.score.grid(row=0, column=1)

        self.canvas = Canvas(width=240, height=250, bg="white")
        self.canvas.grid(row=1, column=0, columnspan=2, pady=20)
        self.query_text = self.canvas.create_text(120, 125, text='Welcome to Quizler Enjoy while you learn',
                                                  font=("Arial", '15', 'italic'),
                                                  width=220)
        # buttons
        wrong_image = PhotoImage(file="./images/false.png")
        self.wrong_button = Button(image=wrong_image, command=self.check_false_answer)
        self.wrong_button.grid(row=2, column=0)

        right_image = PhotoImage(file="./images/true.png")
        self.right_button = Button(image=right_image, command=self.check_answer)
        self.right_button.grid(row=2, column=1)
        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg='white')
        if self.quiz.still_has_questions():
            self.score.config(text=f'Score: {self.quiz.score}')
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.query_text, text=q_text)
        else:
            self.canvas.itemconfig(self.query_text, text='You ve completed the quiz')
            self.right_button.config(state='disabled')
            self.wrong_button.config(state='disabled')

    def check_answer(self):
        answer = self.quiz.check_answer('True')
        self.give_feedback(answer)

    def check_false_answer(self):
        answer = self.quiz.check_answer('False')
        self.give_feedback(answer)

    def give_feedback(self, is_right):
        self.window.after_cancel(self.timer)
        if is_right:
            self.canvas.config(bg="green")

        else:
            self.canvas.config(bg='red')

        self.timer = self.window.after(1000, self.get_next_question)