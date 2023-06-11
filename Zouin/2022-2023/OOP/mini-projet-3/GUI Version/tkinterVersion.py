import tkinter as tk
from tkinter import messagebox


class GestionExamensGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Gestion Examens")
        self.root.configure(bg="cyan")

        self.create_widgets()

    def create_widgets(self):
        app_header = tk.Label(
            self.root,
            text="APPLICATION DE GESTION DE QCM",
            font=("Arial", 16, "bold"),
            fg="dark cyan",
            bg="cyan",
        )
        app_header.pack(pady=10)

        menu_header = tk.Label(
            self.root,
            text="MENU PRINCIPAL",
            font=("Arial", 14, "bold"),
            fg="red",
            bg="cyan",
        )
        menu_header.pack()

        button_teacher = tk.Button(
            self.root,
            text="Mode PROFESSEUR",
            font=("Arial", 12),
            bg="cyan",
            fg="blue",
            command=lambda: self.check_account("PROF"),
        )
        button_teacher.pack(pady=5)

        button_student = tk.Button(
            self.root,
            text="Mode ELEVE",
            font=("Arial", 12),
            bg="cyan",
            fg="blue",
            command=lambda: self.check_account("ELEVE"),
        )
        button_student.pack(pady=5)

        button_quit = tk.Button(
            self.root,
            text="Quitter",
            font=("Arial", 12),
            bg="cyan",
            fg="blue",
            command=self.quit_application,
        )
        button_quit.pack(pady=5)

    def check_account(self, user):
        answer = messagebox.askyesno(
            "Confirmation",
            "Do you have an account?",
        )
        if answer:
            if user == "PROF" and self.login() == "PROF":
                self.teacher_mode()
            elif user == "ELEVE" and self.login() == "ELEVE":
                self.student_mode()
            else:
                messagebox.showerror(
                    "Error",
                    "You don't have permission to access this mode",
                )
                self.create_widgets()
        else:
            self.register(user, user)

    def register(self, who_register, who_created_account):
        register_window = tk.Toplevel(self.root)
        register_window.title("Register")

        username_label = tk.Label(register_window, text="Username:")
        username_label.pack()
        username_entry = tk.Entry(register_window)
        username_entry.pack()

        password_label = tk.Label(register_window, text="Password:")
        password_label.pack()
        password_entry = tk.Entry(register_window)
        password_entry.pack()

        confirm_password_label = tk.Label(register_window, text="Confirm Password:")
        confirm_password_label.pack()
        confirm_password_entry = tk.Entry(register_window)
        confirm_password_entry.pack()

        register_button = tk.Button(
            register_window,
            text="Register",
            command=lambda: self.save_account(
                register_window,
                who_register,
                who_created_account,
                username_entry.get(),
                password_entry.get(),
                confirm_password_entry.get(),
            ),
        )
        register_button.pack()

    def save_account(self, register_window, who_register, who_created_account, username, password, confirm_password):
        if len(username) < 2 or len(password) < 2 or password != confirm_password:
            messagebox.showerror(
                "Error",
                "Username and password should be at least 2 characters and the passwords should match",
            )
            return

        try:
            with open("Accounts/accounts.txt", "r") as file:
                accounts = file.readlines()
                for account in accounts:
                    existing_username = account.strip().split("|")[1].split(":")[0]
                    if existing_username == username:
                        messagebox.showerror("Error", "Username already exists")
                        register_window.destroy()
                        self.create_widgets()
                        return

            with open("Accounts/accounts.txt", "a") as file:
                file.write(f"{who_register}|{username}:{password}\n")

            messagebox.showinfo("Success", "Register successful!")
            register_window.destroy()
            if who_created_account == "PROF":
                self.teacher_mode()
            else:
                self.create_widgets()

        except FileNotFoundError:
            messagebox.showerror("Error", "No accounts file found")

    def login(self):
        login_window = tk.Toplevel(self.root)
        login_window.title("Login")

        username_label = tk.Label(login_window, text="Username:")
        username_label.pack()
        username_entry = tk.Entry(login_window)
        username_entry.pack()

        password_label = tk.Label(login_window, text="Password:")
        password_label.pack()
        password_entry = tk.Entry(login_window)
        password_entry.pack()

        login_button = tk.Button(
            login_window,
            text="Login",
            command=lambda: self.check_login(
                login_window,
                username_entry.get(),
                password_entry.get(),
            ),
        )
        login_button.pack()

    def check_login(self, login_window, username, password):
        try:
            with open("Accounts/accounts.txt", "r") as file:
                accounts = file.readlines()

            for account in accounts:
                role, user_password = account.strip().split("|")
                account_username, account_password = user_password.split(":")

                if username == account_username and password == account_password:
                    login_window.destroy()
                    return role

            messagebox.showerror("Error", "Invalid username or password")
            login_window.destroy()

        except FileNotFoundError:
            messagebox.showerror("Error", "No accounts file found")

    def teacher_mode(self):
        messagebox.showinfo("Teacher Mode", "You are in Teacher Mode")

    def student_mode(self):
        messagebox.showinfo("Student Mode", "You are in Student Mode")

    def quit_application(self):
        self.root.destroy()


if __name__ == "__main__":
    root = tk.Tk()
    GestionExamensGUI(root)
    root.mainloop()