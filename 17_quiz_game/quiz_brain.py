class QuizBrain:
    
    def __init__(self, q_list):
        self.question_number = 0
        self.score = 0
        self.question_list = q_list
    
    def still_has_questions(self):
        return (len(self.question_list) > self.question_number)
        

    def check_answer(self, u_answer, q_answer):
        if (q_answer.lower() == u_answer.lower()):
            print("You got it right!")
            self.score += 1
        else:
            print("That's wrong")
        print(f"The correct answer was: {q_answer}.")
        print(f"Your current score is: {self.score}/{self.question_number}.")
        print("\n")

    def next_question(self):
        question = self.question_list[self.question_number]
        self.question_number += 1
        u_answer = input(f"Q.{self.question_number}: {question.text} (True/False)?: ")
        self.check_answer(u_answer, question.answer)        

