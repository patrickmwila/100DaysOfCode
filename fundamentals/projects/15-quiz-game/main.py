from question_model import Question
from quiz_brain import QuizBrain
from data import question_data

# TODO: create a question_bank from the question_data, appending a question object to question_bank
question_bank = []
for question in question_data:
    new_q = Question(question["question"], question["correct_answer"])
    question_bank.append(new_q)

# TODO: create a QuizBrain() object
quiz = QuizBrain(question_bank)

# TODO: start asking question
while quiz.still_has_question():
    quiz.next_question()

# TODO: display results
print(f"You've completed the quiz. \nYour final score was: {quiz.score}/{quiz.question_number}")
