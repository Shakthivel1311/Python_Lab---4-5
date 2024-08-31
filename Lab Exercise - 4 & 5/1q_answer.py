from abc import ABC, abstractmethod

class Question(ABC):
    def __init__(self, question_text):
        self.question_text = question_text

    def display_question(self):
        pass

    def evaluate_answer(self, answer):
        pass


class MultipleChoiceQuestion(Question):
    def __init__(self, question_text, choices, correct_choice):
        super().__init__(question_text)
        self.choices = choices
        self.correct_choice = correct_choice

    def display_question(self):
        print(f"Multiple Choice Question: {self.question_text}")
        for idx, choice in enumerate(self.choices, start=1):
            print(f"{idx}. {choice}")
        print()

    def evaluate_answer(self, answer):
        return answer == self.correct_choice


class TrueFalseQuestion(Question):
    def __init__(self, question_text, correct_answer):
        super().__init__(question_text)
        self.correct_answer = correct_answer

    def display_question(self):
        print(f"True/False Question: {self.question_text}")
        print("1. True")
        print("2. False\n")

    def evaluate_answer(self, answer):
        if answer == 1:
            user_answer = True
        elif answer == 2:
            user_answer = False
        else:
            raise ValueError("Invalid answer option.")
        return user_answer == self.correct_answer

class EssayQuestion(Question):
    def __init__(self, question_text, max_length):
        super().__init__(question_text)
        self.max_length = max_length

    def display_question(self):
        print(f"Essay Question: {self.question_text}")
        print(f"Please write your answer (Max {self.max_length} words).\n")

    def evaluate_answer(self, answer):
        word_count = len(answer.split())
        return word_count <= self.max_length


q1 = MultipleChoiceQuestion(
    question_text="\nWhat is the capital of India?",
    choices=["Berlin", "London", "Delhi", "Newyork"],
    correct_choice=3 
)

q2 = TrueFalseQuestion(
    question_text="The Earth is flat.",
    correct_answer=False
)

q3 = EssayQuestion(
    question_text="Discuss the impact of climate change on global economies.",
    max_length=500
)

questions = [q1, q2, q3]

answers = [3, 2, "Climate change affects economies through..."]

for question, answer in zip(questions, answers):
    question.display_question()
    is_correct = question.evaluate_answer(answer)
    print(f"Your Answer: {answer}")
    print(f"Is Correct: {is_correct}\n")
