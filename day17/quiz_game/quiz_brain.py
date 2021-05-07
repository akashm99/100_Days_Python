
class QuizBrain:
    def __init__(self, q_list):
        self.question_number = 0
        self.question_list = q_list
        self.score = 0

    def still_has_questions(self):
        return self.question_number < len(self.question_list)

    def next_question(self):
        self.current_question = self.question_list[self.question_number]
        self.question_number += 1
        return f"Q.{self.question_number}: {self.current_question.text}, (True/False)?: "

    def current_answer(self, answer):
        current_answer = answer
        self.check_answer(current_answer, self.current_question.answer)

    def check_answer(self, current_answer, current_question):
        if current_answer.lower() == current_question.lower():
            self.score += 1
            #print(f"You got it right! Score is {self.score}/{self.question_number}")
        #else:
            #print(f"That's wrong. Score is {self.score}/{self.question_number}")
        #print(f"Correct answer was: {current_question} \n")

