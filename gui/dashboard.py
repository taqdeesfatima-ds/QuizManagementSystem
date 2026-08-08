import tkinter as tk
from gui.questions import QuestionWindow
from gui.students import StudentWindow
from gui.quiz import QuizWindow
from gui.results import ResultsWindow

class Dashboard:

    def __init__(self):

        self.window = tk.Tk()

        self.window.title("Quiz Management System")

        self.window.geometry("800x800")

        self.window.configure(bg="white")

        self.window.resizable(False, False)

        self.create_widgets()

    def create_widgets(self):

        title = tk.Label(
           self.window,
           text="QUIZ MANAGEMENT SYSTEM",
           font=("Arial", 22, "bold"),
           bg="white"
        )

        title.pack(pady=20)

        welcome = tk.Label(
            self.window,
            text="Welcome, Admin",
            font=("Arial", 16),
            bg="white"
        )

        welcome.pack(pady=10)

        button_frame = tk.Frame(
           self.window,
           bg="white"
        )

        button_frame.pack(pady=20)

        questions_btn = tk.Button(
           button_frame,
           text="Manage Questions",
           font=("Arial", 12),
           width=25,
           height=2,
           command=self.open_questions
        )

        questions_btn.pack(pady=8)

        students_btn = tk.Button(
            button_frame,
            text="Manage Students",
            font=("Arial", 12),
            width=25,
            height=2,
            command=self.open_students
        )

        students_btn.pack(pady=8)

        quiz_btn = tk.Button(
            button_frame,
            text="Start Quiz",
            font=("Arial", 12),
            width=25,
            height=2,
            command=self.open_quiz
            
        )

        quiz_btn.pack(pady=8)

        results_btn = tk.Button(
            button_frame,
            text="View Results",
            font=("Arial", 12),
            width=25,
            height=2,
            command=self.open_results
        )

        results_btn.pack(pady=8)

        settings_btn = tk.Button(
            button_frame,
            text="Settings",
            font=("Arial", 12),
            width=25,
            height=2,
            command=self.open_settings
        )

        settings_btn.pack(pady=8)

        logout_btn = tk.Button(
            button_frame,
            text="Logout",
            font=("Arial", 12),
            width=25,
            height=2,
            command=self.logout
        )

        logout_btn.pack(pady=8)

    def open_questions(self):

        QuestionWindow()
    def open_students(self):

        StudentWindow()

    def open_quiz(self):

        QuizWindow()

    def open_results(self):

        ResultsWindow()

    def logout(self):

        self.window.destroy()

        from gui.login import LoginWindow

        LoginWindow().run()

    def open_settings(self):

        settings_window = tk.Toplevel(self.window)

        settings_window.title("Settings")

        settings_window.geometry("400x300")

        settings_window.configure(bg="white")

        title = tk.Label(
            settings_window,
            text="Admin Settings",
            font=("Arial", 20, "bold"),
            bg="white"
        )

        title.pack(pady=25)

        username_label = tk.Label(
            settings_window,
            text="Username: admin",
            font=("Arial", 12),
            bg="white"
        )

        username_label.pack(pady=10)

        info_label = tk.Label(
            settings_window,
            text="Quiz Management System",
            font=("Arial", 11),
            bg="white"
        )

        info_label.pack(pady=10)

        close_btn = tk.Button(
            settings_window,
            text="Close",
            width=15,
            command=settings_window.destroy
        )

        close_btn.pack(pady=20)

    def run(self):

        self.window.mainloop()