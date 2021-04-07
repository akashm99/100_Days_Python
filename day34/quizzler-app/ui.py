from tkinter import *
from quiz_brain import QuizBrain
THEME_COLOR = "#375362"

class QuizInterface():
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(bg=THEME_COLOR)
        self.window.config(padx=20, pady=20)

        self.score_label = Label(text="Score: 0", bg=THEME_COLOR)
        self.score_label.grid(row=0, column=1)

        self.canvas = Canvas(width=300, height=250, bg="white")
        self.question_text = self.canvas.create_text(150, 125, text="Question",
                                                     font=("Arial", 20, "italic"), fill=THEME_COLOR,
                                                     width=280)
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)

        w_image = PhotoImage(file="images/false.png")
        self.w_button = Button(image=w_image, bg=THEME_COLOR, highlightthickness=0, command=self.false_ans)
        self.w_button.grid(row=2, column=1)

        r_image = PhotoImage(file="images/true.png")
        self.r_button = Button(image=r_image, bg=THEME_COLOR, highlightthickness=0, command=self.true_ans)
        self.r_button.grid(row=2, column=0)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            self.score_label.config(text=f"Score: {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(self.question_text, text="You have reached the end of game.")
            self.w_button.config(state="disabled")
            self.r_button.config(state="disabled")

    def false_ans(self):
        self.give_feedback(self.quiz.check_answer(str(False)))

    def true_ans(self):
        self.give_feedback(self.quiz.check_answer(str(True)))

    def give_feedback(self, is_right: bool):
        if is_right == True:
            self.canvas.config(bg="Green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, self.get_next_question)







