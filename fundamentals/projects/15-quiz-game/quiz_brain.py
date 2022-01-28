class QuizBrain:
    def __init__(self, a_list):
        self.question_number = 0
        self.score = 0
        self.question_list = a_list

    def still_has_question(self):
        return self.question_number < len(self.question_list)

    def next_question(self):
        q_num = self.question_number
        new_q = self.question_list[q_num]
        self.question_number += 1
        ans = input(f"Q.{self.question_number}: {new_q.text} (True/False)?: ").capitalize()
        correct_ans = self.question_list[q_num].answer
        self.check_answer(ans, correct_ans)

    def check_answer(self, user_answer, correct_answer):
        if user_answer == correct_answer:
            self.score += 1
            print("You got it right!")
        else:
            print("That's wrong")
        print(f"The correct answer was {correct_answer}.")
        print(f"Your current score is {self.score}/{self.question_number}\n")
