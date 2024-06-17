# questions.py

quiz_questions = [
    {
        "question": "What is the capital of France?",
        "options": ["London", "Paris", "Rome", "Berlin"],
        "answer": "Paris"
    },
    {
        "question": "Which planet is known as the Red Planet?",
        "options": ["Earth", "Mars", "Venus", "Jupiter"],
        "answer": "Mars"
    },
    {
        "question": "Who wrote 'Harry Potter'?",
        "options": ["J.R.R. Tolkien", "J.K. Rowling", "Stephen King", "George R.R. Martin"],
        "answer": "J.K. Rowling"
    }
    # Add more questions as needed
]

# quiz.py

from questions import quiz_questions

def run_quiz():
    score = 0
    for question in quiz_questions:
        print(question["question"])
        for idx, option in enumerate(question["options"], start=1):
            print(f"{idx}. {option}")
        user_answer = input("Enter your answer (1-4): ")
        if user_answer.isdigit() and 1 <= int(user_answer) <= 4:
            selected_option = question["options"][int(user_answer) - 1]
            if selected_option == question["answer"]:
                print("Correct!")
                score += 1
            else:
                print(f"Wrong! The correct answer is: {question['answer']}")
        else:
            print("Invalid input. Skipping question.")
    print(f"Quiz completed! Your score is {score}/{len(quiz_questions)}")

if __name__ == "__main__":
    run_quiz()
