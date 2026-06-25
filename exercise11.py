import requests
import random
from datetime import datetime

from utils import get_grade,format_currency,clear_screen

# ------------------
# loading Questions
# ------------------

def load_questions():
    url = "https://opentdb.com/api.php?amount=10&type=multiple"
    response = requests.get(url)
    data = response.json()

    questions = []
    for item in data["results"]:
        question={"question":item["question"],
                  "answer":item["correct_answer"]}
        questions.append(question)
    return questions

# quiz 
clear_screen()
print("---Random Quiz Questions")
questions = load_questions()
random.shuffle(questions)
score = 0 
total_questions = len(questions)
start_time= datetime.now()
for q in questions:
    print("Question")
    print(q["question"])

    user_input = input("Answer a question")
    if user_input.lower() == q["answer"].lower():
        print("Correct")
        score += 1
    else:
        print("Incorrect")
end_time = datetime.now()
time_taken = end_time - start_time
percentage = (score / total_questions)*100
grade = get_grade(percentage)

print("score:",score,"/",total_questions)
print("Time Taken",time_taken)
print('Percentage',percentage,"%")
print("grade",grade)
print("Total score",format_currency(score * 100))






