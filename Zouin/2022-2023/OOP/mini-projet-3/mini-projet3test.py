import os
import time


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
        while True:
            for key in actions:
                print(f"{key}: {actions[key][0]}")

            choice = input(backgroundColor + f"Entrez votre choix ({', '.join(actions.keys())}) : " + Style.WHITE).lower()
            if choice in actions:
                actions[choice][1]()
                return choice
            else:
                print(errorColor + "Invalid choice" + backgroundColor)

    def Quit(self):
        print(Style.CLEAR)
        print(Style.CLEAR + goodbyeColor + "Au revoir!" + Style.WHITE)
        exit()


    def mainMenu(self):
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
        answer = input(backgroundColor + "Do you have an account? (y/n) : " + Style.WHITE)
        while True:
            if answer == "y":
                if user == "PROF" and self.login() == "PROF":
                    self.teacherMode()
                elif user == "ELEVE" and self.login() == "ELEVE":
                    self.studentMode()
                else:
                    print(Style.CLEAR + Style.PURPLE + "You dont have permission to access this mode\n" + backgroundColor)
                    time.sleep(1.5)
                    print(Style.CLEAR, end="")
                    self.mainMenu()
                break
            elif answer == "n":
                self.register(user)
                break
            else:
                answer = input(errorColor + "Please enter a valid answer (y/n) : " + Style.WHITE)


    def register(self, whoRegister):
        username = input(backgroundColor + "Username: " + Style.WHITE).lower()
        password = input(backgroundColor + "Password: " + Style.WHITE).lower()
        confirm_password = input(backgroundColor + "Confirm password: " + Style.WHITE).lower()
        if password == confirm_password:
            self.username = username
            self.password = password
        else:
            print(Style.PURPLE + "Passwords do not match\n")
            time.sleep(1.5)
            print(Style.CLEAR, end="")
            self.mainMenu()

        try:
            with open(file="Accounts\\accounts.txt", mode="r", encoding='utf-8') as file:
                accounts = file.readlines()
                for account in accounts:
                    account = account.strip().split("|")
                    existingUsername = account[1].split(":")[0]
                    if existingUsername == self.username:
                        print(errorColor + "Username already exists" + backgroundColor)
                        self.mainMenu()

            with open(file="Accounts\\accounts.txt", mode="a", encoding='utf-8') as file:
                file.write(f"{whoRegister}|{username}:{password}\n")
            print(correctColor + "Register successful!" + backgroundColor)
            time.sleep(1.5)
            print(Style.CLEAR, end="")
            self.mainMenu()
        except FileNotFoundError:
            print("No accounts file found")


    def login(self):
        username = input(backgroundColor + "Username: " + Style.WHITE).lower()
        password = input(backgroundColor + "Password: " + Style.WHITE).lower()
        self.username = username
        self.password = password

        try:
            with open(file="Accounts\\accounts.txt", mode="r", encoding='utf-8') as file:
                accounts = file.readlines()
        except FileNotFoundError:
            print(backgroundColor + "No accounts file found")

        for account in accounts:
            account = account.strip().split("|")
            role = account[0]
            account = account[1].split(":")
            if self.username == account[0] and self.password == account[1]:
                print(correctColor + "Login successful" + backgroundColor)
                time.sleep(1.5)
                print(Style.CLEAR, end="")
                return role


    def teacherMode(self):
        print(backgroundColor + "*****************************")
        print(Style.BOLD + headerColor + "MODE PROFESSEUR" + Style.END + backgroundColor)
        print("*****************************")
        # - - - - - ACTION FORM - - - - -
        self.ActionForm({
            '1': ('Créer un QCM', lambda: None), # self.createQuiz()
            '2': ('Créer un compte pour un élève', lambda: None), # self.createStudentAccount()
            '3': ('Consulter les résultats d\'un élève', lambda: None), # self.showStudentResults()
            '4': ('Main Menu', lambda: (print(Style.CLEAR, end=''), self.mainMenu())),
            'q': ('Quitter', lambda: self.Quit())
            })

    
    def studentMode(self):
        print(backgroundColor + "*****************************")
        print(Style.BOLD + headerColor + "MODE ELEVE" + Style.END + backgroundColor)
        print("*****************************")
        self.ActionForm({
            '1': ('Passer un QCM', lambda: self.takeQuiz()),
            "2": ("Main Menu", lambda: (print(Style.CLEAR, end=''), self.mainMenu())),
            'q': ('Quitter', lambda: self.Quit())
            })

    
    def takeQuiz(self):
        print(Style.CLEAR, end='') # Clear screen
        qcmNumber = 0

        while True:
            try:
                qcmNumber = int(input(backgroundColor + "Veuillez entrer un numéro valide (1, 2, 3, 4, 5) : " + Style.WHITE))
                if qcmNumber in range(1, 6):
                    break
                else:
                    print(errorColor + "Invalid choice" + backgroundColor)
            except ValueError:
                print(errorColor + "Invalid choice" + backgroundColor)

        self.folderName = f"{self.username}_QCM"
        if not os.path.exists(self.folderName):
            os.mkdir(self.folderName)
        else:
            print(errorColor + "You have already taken this quiz.")
            time.sleep(2)
            self.studentMode()

        with open(f'QCM\qcm{qcmNumber}.txt', "r", encoding='utf-8') as file:
            lines = file.readlines()

        questions = []
        answers = []
        correct_answers = []

        i = 0
        mark = 0
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
            print(questionColor + f"Question: {questions[question]}" + questionColor)
            print("\n".join(answers[question]))
            print()

            userInput = int(input(backgroundColor + "Enter your answer: " + Style.WHITE))
            if userInput == correct_answers[question]:
                print(correctColor + "Correct!\n" + backgroundColor)
                mark += 1
            else:
                print(errorColor + "Incorrect!\n" + backgroundColor)

            if not os.path.exists(f"{self.folderName}\\{self.username}_QCM{qcmNumber}.txt"):
                open(f"{self.folderName}\\{self.username}_QCM{qcmNumber}.txt", "w").close()
            with open(f"{self.folderName}\\{self.username}_QCM{qcmNumber}.txt", "a", encoding='utf-8') as file:
                file.write(f"Question: {questions[question]}\n")
                file.write("Answers:\n")
                file.write("\n".join(answers[question]) + "\n")
                file.write(f"Correct Answer: {correct_answers[question]}\n")
                file.write(f"User Answer: {userInput}\n")
                file.write("\n")
        # Seperate each quiz
        with open(f"{self.folderName}\\{self.username}_QCM{qcmNumber}.txt", "a", encoding='utf-8') as file:
            file.write(f"Student mark: {mark}/{len(questions)}\n")
            file.write("--------------------------------------------------\n")
        
        print(correctColor + "Quiz completed!" + Style.END)
        if mark == len(questions):
            print(correctColor + f"Congratulations! You aced the test! ({mark}/{len(questions)})")
        elif mark >= len(questions) / 2:
            print(correctColor + f"Good job! You got {mark}/{len(questions)}" + backgroundColor)
        else:
            print( + f"SOOO BAAAAAD HAHAHA. You got {mark}/{len(questions)}" + Style.END)
        time.sleep(2)
        self.studentMode()


def main():
    print(Style.CLEAR, end='') # Clear the screen
    user = GestionExamens()
    user.mainMenu()


if __name__ == "__main__":
    main()