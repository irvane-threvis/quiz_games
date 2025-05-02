import random

class QuizManager:
    def __init__(self, questions):
        self.questions = questions.copy()
        random.shuffle(self.questions)
        self.questions = self.questions[:10]  # Max 5 questions
        self.index = 0
        self.score = 0

    def get_question(self):
        if self.index < len(self.questions):
            q = self.questions[self.index]
            self.index += 1
            return q
        return None

    def check_answer(self, question, answer_index):
        return answer_index == question["correct_answer"]
