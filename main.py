import question_model
import data
import quiz_brain

question_bank = []
for i in range(0, len(data.question_data)):
    question = question_model.Question(data.question_data[i]["question"], data.question_data[i]["correct_answer"])
    question_bank.append(question)
    # print(question_bank[i].text)
    # print(question_bank[i].answer)


quiz = quiz_brain.QuizBrain(question_bank)
while quiz.still_has_question():
    quiz.next_question()
    print("\n")
print("You have completed the quiz")
print(f"Your final score was: {quiz.score}/{quiz.question_no}.")