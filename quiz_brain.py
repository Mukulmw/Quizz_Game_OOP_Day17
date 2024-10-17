class QuizBrain:
    def __init__(self, question_list):
        self.question_no = 0
        self.question_list = question_list
        self.score = 0

    def next_question(self):

        user_answer = input(f"Q.{self.question_no + 1}: {self.question_list[self.question_no].text} (True/False)?")
        self.check_answer(user_answer, self.question_list[self.question_no].answer)
        self.question_no += 1

    def still_has_question(self):
        if len(self.question_list) > self.question_no:
            return True
        else:
            return False

    def check_answer(self, user_answer, actual_answer):
        if user_answer.lower() == actual_answer.lower():
            print("You got it right !")
            self.score += 1

        else:
            print("That's wrong.")
            print(f"The correct answer is: {actual_answer}.")
        print(f"Your current score is: {self.score}/{self.question_no + 1}")