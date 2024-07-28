import requests
response = requests.get(url="https://opentdb.com/api.php?amount=10&category=22&difficulty=easy&type=boolean")
response.raise_for_status()
data = response.json()
question_data = []
for item in data["results"]:
    question_dict = {
        "question" : item["question"],
        "correct_answer" : item["correct_answer"]
    }
    question_data.append(question_dict)


