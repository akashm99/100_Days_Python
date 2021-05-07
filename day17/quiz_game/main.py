from flask import Flask, jsonify, redirect, url_for, render_template, send_from_directory
import json
import os
from question_model import Question
from data import question_data
from quiz_brain import QuizBrain
# print(question_data[1]["text"])

question_bank = []
for i in question_data:
    question_text = i["text"]
    question_answer = i["answer"]
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)

quiz = QuizBrain(question_bank)

# while quiz.still_has_questions():
#     quiz.next_question()
#
# print(f"You completed the quiz,"
#       f"Your final score is: {quiz.score}/{len(quiz.question_number)}")


app = Flask(__name__)

@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'),
                               'static/favicon.ico')#, mimetype='image/vnd.microsoft.icon'

@app.route('/')
def home():
    if quiz.still_has_questions():
        return quiz.next_question()
    else:
        return f"You completed the quiz, Your final score is: {quiz.score}"


@app.route('/<answer>')
def answer(answer):
    quiz.current_answer(answer)
    return redirect(url_for('home'))

if __name__=="__main__":
    app.run(debug=True)