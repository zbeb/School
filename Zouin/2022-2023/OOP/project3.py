with open('qcm.txt', "r") as file:
    lines = file.readlines()

questions = []
answers = []
correct_answers = []

i = 0
while i < len(lines):
    if lines[i].startswith("q:"):
        question = lines[i].replace("q:", "").strip()
        questions.append(question)
        i += 1
        answer_choices = []
        while not lines[i].startswith("Correct:"):
            answer = lines[i].strip()
            answer_choices.append(answer)
            i += 1
        answers.append(answer_choices)
        correct_answer = lines[i].replace("Correct:", "").strip()
        correct_answers.append(int(correct_answer))
    i += 1

for question in range(len(questions)):
    print("Question:", questions[question])
    print("Answers:", answers[question])
    for answer in range(len(answers[question])):
        print(answers[question][answer])
    print("Correct Answer:", correct_answers[question])
    userInput = int(input("Enter your answer: "))
    if userInput == correct_answers[question]:
        print("Correct!")
    else:
        print("Incorrect!")
