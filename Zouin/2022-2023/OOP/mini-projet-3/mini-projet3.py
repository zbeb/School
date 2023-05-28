import os
import time

# TODO: ADD CONSULTER LES RESULTATS DUN ELEVE
#       ADD TIMER TO QUIZ   


class Style:
    WHITE = '\033[97m'
    PURPLE = '\033[95m'
    CYAN = '\033[96m'
    DARKCYAN = '\033[36m'
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    END = '\033[0m'
    CLEAR = '\033c'


defaultColor = Style.WHITE
appHeaderColor = Style.DARKCYAN
backgroundColor = Style.CYAN
headerColor = Style.RED
questionColor = Style.BLUE
correctColor = Style.GREEN
errorColor = Style.RED
goodbyeColor = Style.YELLOW


class GestionExamens:
    def __init__(self):
        self.username = ""
        self.password = ""
        self.folderName = ""
    
    def ActionForm(self, actions):
        '''
        Print a menu with the given actions and execute the corresponding function
        '''
        while True:
            for key in actions:
                # Print the action and the corresponding key
                print(f"{key}: {actions[key][0]}")
            # Ask for the user's choice
            choice = input(backgroundColor + f"Entrez votre choix ({', '.join(actions.keys())}) : " + defaultColor).lower()
            # Check if the choice is in the actions
            if choice in actions:
                # Execute the corresponding function
                actions[choice][1]()
                return choice
            else:
                print(errorColor + "Invalid choice" + backgroundColor)

    def Quit(self):
        '''
        Quit the application
        '''
        print(Style.CLEAR)
        print(Style.CLEAR + goodbyeColor + "Au revoir!" + defaultColor)
        exit()


    def mainMenu(self):
        '''
        Print the main menu
        '''
        print(Style.BOLD + appHeaderColor + "APPLICATION DE GESTION DE QCM" + Style.END)
        print(backgroundColor + "*****************************")
        print(Style.BOLD + headerColor + "MENU PRINCIPAL" + Style.END)
        print(backgroundColor + "*****************************")

        self.ActionForm({
            '1': ("Mode PROFESSEUR", lambda: self.checkAccount("PROF")),
            '2': ("Mode ELEVE", lambda: self.checkAccount("ELEVE")),
            'q': ("Quitter", lambda: self.Quit())
            })


    def checkAccount(self, user):
        '''
        Check if the user has an account or not
        Also check if the user is a teacher or a student and redirect to the corresponding mode
        '''
        answer = input(backgroundColor + "Do you have an account? (y/n) : " + defaultColor)
        while True:
            # Check if the user has an account
            if answer == "y":
                # If yes, check if the user is a teacher or a student
                if user == "PROF" and self.login() == "PROF":
                    self.teacherMode()
                elif user == "ELEVE" and self.login() == "ELEVE":
                    self.studentMode()
                else:
                    # If the user is not a teacher or a student, print an error message and redirect to the main menu
                    print(Style.CLEAR + Style.PURPLE + "You dont have permission to access this mode\n" + backgroundColor)
                    time.sleep(1)
                    print(Style.CLEAR, end="")
                    self.mainMenu()
                break
            elif answer == "n":
                # If no, register a new account
                self.register(user, user)
                break
            else:
                answer = input(errorColor + "Please enter a valid answer (y/n) : " + defaultColor)


    def register(self, whoRegister, whoCreatedAccount):
        '''
        Register a new account
        '''
        while True:
            # Ask for username and password
            username = input(backgroundColor + "Username: " + defaultColor).lower()
            password = input(backgroundColor + "Password: " + defaultColor).lower()
            confirmPassword = input(backgroundColor + "Confirm Password: " + defaultColor).lower()
            # Check if the username and password are at least 2 characters and if the passwords match
            if len(username) < 2 or len(password) < 2 or password != confirmPassword:
                print(errorColor + "Username and password should be at least 2 characters and the passwords should match" + backgroundColor)
            else:
                # Assign the username and password to the class variables
                self.username = username
                self.password = password
                break
        try:
            # Open the accounts file
            with open(file="Accounts\\accounts.txt", mode="r", encoding='utf-8') as file:
                # Read all the accounts
                accounts = file.readlines()
                for account in accounts:
                    # Split the account into role and username:password
                    account = account.strip().split("|")
                    # Split the username:password into username and password
                    existingUsername = account[1].split(":")[0]
                    # Check if the username already exists
                    if existingUsername == self.username:
                        print(errorColor + "Username already exists" + backgroundColor)
                        self.mainMenu()

            # If the username doesn't exist, save the new account
            with open(file="Accounts\\accounts.txt", mode="a", encoding='utf-8') as file:
                file.write(f"{whoRegister}|{username}:{password}\n")

            # Print a success message and clear the screen
            print(correctColor + "Register successful!" + backgroundColor)
            time.sleep(1.5)
            print(Style.CLEAR, end="")

            # If the account was created by a teacher, redirect to teacher mode
            if whoCreatedAccount == "PROF":
                self.teacherMode()
            # If the account was created by a student, redirect to student mode
            else:
                self.mainMenu()
        except FileNotFoundError:
            print("No accounts file found")


    def login(self):
        '''
        Login to an existing account
        '''
        # Ask for username and password
        username = input(backgroundColor + "Username: " + defaultColor).lower()
        password = input(backgroundColor + "Password: " + defaultColor).lower()
        # Assign the username and password to the class variables
        self.username = username
        self.password = password

        try:
            # Open the accounts file
            with open(file="Accounts\\accounts.txt", mode="r", encoding='utf-8') as file:
                # Read all the accounts
                accounts = file.readlines()
        except FileNotFoundError:
            print(backgroundColor + "No accounts file found")

        for account in accounts:
            # Split the account into role and username:password
            account = account.strip().split("|")
            # Set the role to the first element of the account
            role = account[0]
            # Split the username:password into username and password
            account = account[1].split(":")
            # Check if the username and password match
            if self.username == account[0] and self.password == account[1]:
                return role


    def teacherMode(self):
        '''
        Print the teacher mode menu
        '''
        print(correctColor + "Login successful" + backgroundColor)
        # time.sleep(1.5)
        # print(Style.CLEAR, end="")

        print(backgroundColor + "*****************************")
        print(Style.BOLD + headerColor + "MODE PROFESSEUR" + Style.END + backgroundColor)
        print("*****************************")
        # - - - - - ACTION FORM - - - - -
        self.ActionForm({
            '1': ('Créer un QCM', lambda: self.createQuiz()),
            '2': ('Créer un compte pour un élève', lambda: self.createStudentAccount()),
            '3': ('Consulter les résultats d\'un élève', lambda: None), # self.showStudentResults()
            '4': ('Main Menu', lambda: (print(Style.CLEAR, end=''), self.mainMenu())),
            'q': ('Quitter', lambda: self.Quit())
            })


    def createQuiz(self):
        '''
        Create a new quiz
        '''
        # Clear the screen
        print(Style.CLEAR, end='')
        # Ask for the quiz name, number of questions, number of answers and quiz duration
        quizQuestions = []
        quizName = input(backgroundColor + "Veuillez entrer le nom du QCM : " + defaultColor)
        quizQuestionsNumber = input(backgroundColor + "Veuillez entrer le nombre de questions du QCM : " + defaultColor)
        quizAnswersNumber = input(backgroundColor + "Veuillez entrer le nombre de réponses par question : " + defaultColor)
        quizDuration = input(backgroundColor + "Veuillez entrer la durée du QCM (en minutes) : " + defaultColor)

        for i in range(int(quizQuestionsNumber)):
            # Ask for the question and the answers
            question = input(backgroundColor + f"Veuillez entrer la question {i+1} : " + defaultColor)
            quizQuestions.append(f"q: {question}")
            for j in range(int(quizQuestionsNumber)):
                answer = input(backgroundColor + f"Veuillez entrer la réponse {j+1} : " + defaultColor)
                quizQuestions.append(f"{j + 1}) {answer}")
                # If it's the last answer, ask for the correct answer because thats how the format is
                if j == int(quizAnswersNumber) - 1:
                    quizCorrectAnswer = input(backgroundColor + "Veuillez entrer le numéro de la bonne réponse : " + defaultColor)
                    quizQuestions.append(f"Correct: {quizCorrectAnswer}\n")

        try:
            # Create the quiz file if it doesn't exist
            if not os.path.exists(f"QCM\\{quizName}.txt"):
                open(f"QCM\\{quizName}.txt", "w").close()
            # Open the quiz file and write the questions and answers that were entered before
            with open(file=f"QCM\\{quizName}.txt", mode="a", encoding='utf-8') as file:
                for i in range(len(quizQuestions)):
                    file.write(f"{quizQuestions[i]}\n")
            # Print a success message and clear the screen clear the screen and redirect to teacher mode
            print(correctColor + "Quiz created successfully!" + backgroundColor)
            time.sleep(1)
            print(Style.CLEAR, end="")
            self.teacherMode()
        except FileNotFoundError:
            print(errorColor + "No quizzes file found" + backgroundColor)


    def createStudentAccount(self):
        '''
        Create a new student account as a teacher
        '''
        print(Style.CLEAR, end='')
        self.register("ELEVE", "PROF")

    
    def studentMode(self):
        '''
        Print the student mode menu
        '''
        print(correctColor + "Login successful" + backgroundColor)
        # time.sleep(1)
        # print(Style.CLEAR, end="")

        print(backgroundColor + "*****************************")
        print(Style.BOLD + headerColor + "MODE ELEVE" + Style.END + backgroundColor)
        print("*****************************")
        self.ActionForm({
            '1': ('Passer un QCM', lambda: self.takeQuiz()),
            "2": ("Main Menu", lambda: (print(Style.CLEAR, end=''), self.mainMenu())),
            'q': ('Quitter', lambda: self.Quit())
            })


    def takeQuiz(self):
        '''
        Take a quiz
        '''
        # Clear the screen
        print(Style.CLEAR, end='')
        # Create empty lists for questions, answers and correct answers
        questions = []
        answers = []
        correct_answers = []
        # Create a dictionary for the quizzes that exist in a folder
        qcmFiles = {}
        # Grade of the student
        grade = 0

        # Create folder for student
        self.folderName = f"{self.username}_QCM"
        # Check if folder exists
        if not os.path.exists(self.folderName):
            os.mkdir(self.folderName)

        # Check if there are any quizzes
        print(backgroundColor + "Liste des QCM disponibles : " + defaultColor)
        # Check if the user has already done the quiz, if yes, remove it from their quizzes list
        count = 1
        for i, file in enumerate(os.listdir("QCM")):
            if f"{self.username}_{file}" not in os.listdir(self.folderName):
                print(f"{count}) {file}")
                qcmFiles[str(count)] = file.split(".")[0]
                count += 1

        while True:
            try:
                # Ask user to choose a quiz
                qcmNumber = int(input(backgroundColor + f"Veuillez entrer un numéro valide ({', '.join(qcmFiles.keys())}) : " + defaultColor))
                # Convert to string
                qcmNumber = str(qcmNumber)
                # Check if choice is valid
                if qcmNumber in qcmFiles.keys():
                    print("You selected", qcmFiles[qcmNumber])
                    # Set selected quiz
                    selectedQCM = qcmFiles[qcmNumber]
                    break
                else:
                    print(errorColor + "Invalid choice" + backgroundColor)
            except ValueError:
                print(errorColor + "Invalid choice" + backgroundColor)
                
        # Clear the screen
        time.sleep(1)
        print(Style.CLEAR, end='')

        # Open selected quiz
        with open(f'QCM\{selectedQCM}.txt', "r", encoding='utf-8') as file:
            # Read all lines
            lines = file.readlines()

        i = 0
        while i < len(lines):
            # Check if line starts with q:
            if lines[i].startswith("q:"):
                # Get question and add it to questions list
                question = lines[i].replace("q:", "").strip()
                questions.append(question)
                i += 1
                answer_choices = []
                # Get answers and add them to answers list if the line doesn't start with Correct:
                while not lines[i].startswith("Correct:"):
                    answer = lines[i].strip()
                    answer_choices.append(answer)
                    i += 1
                answers.append(answer_choices)
                # Extract correct answer without "Correct:" and add it to correct_answers list
                correct_answer = lines[i].replace("Correct:", "").strip()
                # Convert to int and add to correct_answers list
                correct_answers.append(int(correct_answer))
            i += 1

        for question in range(len(questions)):
            # Print question
            print(questionColor + f"Question: {questions[question]}" + questionColor)
            # Print answers
            print("\n".join(answers[question]))
            # Ask user the question answer
            userInput = int(input(backgroundColor + "Enter your answer: " + defaultColor))
            # Check if answer is correct
            if userInput == correct_answers[question]:
                # If correct, add 1 to grade
                print(correctColor + "Correct!\n" + backgroundColor)
                grade += 1
            else:
                # If incorrect, print correct answer
                print(errorColor + "Incorrect!\n" + backgroundColor)

            # If file doesn't exist, create it
            if not os.path.exists(f"{self.folderName}\\{self.username}_{selectedQCM}.txt"):
                open(f"{self.folderName}\\{self.username}_{selectedQCM}.txt", "w").close()

            # Open file and write the questions, answers, correct answer and user answer
            with open(f"{self.folderName}\\{self.username}_{selectedQCM}.txt", "a", encoding='utf-8') as file:
                file.write(f"Question: {questions[question]}\n")
                file.write("Answers:\n")
                file.write("\n".join(answers[question]) + "\n")
                file.write(f"Correct Answer: {correct_answers[question]}\n")
                file.write(f"User Answer: {userInput}\n")
                file.write("\n")

        # Seperate each quiz
        with open(f"{self.folderName}\\{self.username}_{selectedQCM}.txt", "a", encoding='utf-8') as file:
            file.write(f"Student grade: {grade}/{len(questions)}\n")
            file.write("--------------------------------------------------\n")
        
        # Clear the screen
        time.sleep(1)
        print(Style.CLEAR, end='')
        # Print results
        print(correctColor + "Quiz completed!" + Style.END)
        if grade == len(questions):
            print(correctColor + f"Congratulations! You aced the test! ({grade}/{len(questions)})")
        elif grade >= len(questions) / 2:
            print(correctColor + f"Good job! You got {grade}/{len(questions)}" + backgroundColor)
        else:
            print(errorColor + f"SOOO BAAAAAD HAHAHA. You got {grade}/{len(questions)}" + Style.END)
        time.sleep(2)
        self.studentMode()


def main():
    print(Style.CLEAR, end='') # Clear the screen
    user = GestionExamens()
    user.mainMenu()


if __name__ == "__main__":
    main()