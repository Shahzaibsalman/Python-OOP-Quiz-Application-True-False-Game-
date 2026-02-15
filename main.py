
from data import Question_data
from quiz_brain import Quiz_brain
from question_modle import Question

question_bank = []

for item in Question_data:
    question = Question(item["question"], item["answer"])
    question_bank.append(question)

quiz = Quiz_brain(question_bank)

while quiz.question_number < len(question_bank):
    quiz.next_question()

print(f"Your final score is: {quiz.score}/{len(question_bank)}")






