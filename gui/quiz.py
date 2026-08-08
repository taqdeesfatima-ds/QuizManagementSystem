import tkinter as tk
from tkinter import messagebox
from database.database import (
    get_all_questions,
    get_all_students,
    save_result
)

class QuizWindow:

    def __init__(self):

        self.window = tk.Toplevel()

        self.window.title("Start Quiz")

        self.window.geometry("700x500")

        self.window.configure(bg="white")

        self.window.resizable(False, False)

        self.questions = get_all_questions()

        self.students = get_all_students()

        self.selected_student_id = None
        self.selected_student_name = None

        self.create_start_screen()

    def create_start_screen(self):

        title = tk.Label(
            self.window,
            text="QUIZ START",
            font=("Arial", 24, "bold"),
            bg="white"
        )

        title.pack(pady=30)

        student_label = tk.Label(
            self.window,
            text="Select Student",
            font=("Arial", 14, "bold"),
            bg="white"
        )

        student_label.pack(pady=10)

        self.student_list = tk.Listbox(
            self.window,
            font=("Arial", 13),
            width=45,
            height=8
        )

        self.student_list.pack(pady=10)

        for student in self.students:

            student_id = student[0]
            name = student[1]
            roll_number = student[2]

            self.student_list.insert(
                tk.END,
                f"{student_id} - {name} ({roll_number})"
            )

        start_btn = tk.Button(
            self.window,
            text="Start Quiz",
            width=18,
            font=("Arial", 12, "bold"),
            command=self.start_quiz
        )

        start_btn.pack(pady=25)

    def start_quiz(self):

        selected = self.student_list.curselection()

        if not selected:

            messagebox.showwarning(
                "Warning",
                "Please select a student."
            )

            return

        index = selected[0]

        student = self.students[index]

        self.selected_student_id = student[0]

        self.selected_student_name = student[1]

        self.start_questions()

    def start_questions(self):

        if not self.questions:

            messagebox.showerror(
                "Error",
                "No questions available."
            )

            return

        self.current_question = 0

        self.score = 0

        self.time_left = 30
        self.timer_id = None

        self.create_quiz_widgets()

        self.show_question()

    def create_quiz_widgets(self):

        for widget in self.window.winfo_children():
            widget.destroy()

        title = tk.Label(
            self.window,
            text="QUIZ",
            font=("Arial", 24, "bold"),
            bg="white"
        )

        title.pack(pady=20)

        self.student_label = tk.Label(
            self.window,
            text=f"Student: {self.selected_student_name}",
            font=("Arial", 12),
            bg="white"
        )

        self.student_label.pack()

        self.question_number = tk.Label(
            self.window,
            text="",
            font=("Arial", 12),
            bg="white"
        )

        self.question_number.pack(pady=10)

        self.timer_label = tk.Label(
            self.window,
            text="Time: 30",
            font=("Arial", 13, "bold"),
            bg="white"
        )

        self.timer_label.pack(pady=5)

        self.question_label = tk.Label(
            self.window,
            text="",
            font=("Arial", 16, "bold"),
            bg="white",
            wraplength=650
        )

        self.question_label.pack(
            anchor="w",
            padx=50,
            pady=20
        )

        self.answer_var = tk.StringVar()

        self.option_a = tk.Radiobutton(
            self.window,
            text="",
            variable=self.answer_var,
            value="",
            font=("Arial", 13),
            bg="white",
            anchor="w"
        )

        self.option_a.pack(fill="x", padx=70, pady=6)

        self.option_b = tk.Radiobutton(
            self.window,
            text="",
            variable=self.answer_var,
            value="",
            font=("Arial", 13),
            bg="white",
            anchor="w"
        )

        self.option_b.pack(fill="x", padx=70, pady=6)

        self.option_c = tk.Radiobutton(
            self.window,
            text="",
            variable=self.answer_var,
            value="",
            font=("Arial", 13),
            bg="white",
            anchor="w"
        )

        self.option_c.pack(fill="x", padx=70, pady=6)

        self.option_d = tk.Radiobutton(
            self.window,
            text="",
            variable=self.answer_var,
            value="",
            font=("Arial", 13),
            bg="white",
            anchor="w"
        )

        self.option_d.pack(fill="x", padx=70, pady=6)

        self.next_btn = tk.Button(
            self.window,
            text="Next",
            width=15,
            font=("Arial", 12, "bold"),
            command=self.next_question
        )

        self.next_btn.pack(pady=20)

    def show_question(self):

        question = self.questions[self.current_question]

        self.question_number.config(
            text=f"Question {self.current_question + 1} of {len(self.questions)}"
        )

        self.question_label.config(
            text=question[1].strip()
        )

        self.option_a.config(
            text=question[2].strip(),
            value=question[2].strip()
        )

        self.option_b.config(
            text=question[3].strip(),
            value=question[3].strip()
        )

        self.option_c.config(
            text=question[4].strip(),
            value=question[4].strip()
        )

        self.option_d.config(
            text=question[5].strip(),
            value=question[5].strip()
        )

        self.answer_var.set("")
        self.time_left = 30

        self.start_timer()
    def next_question(self):

        if self.current_question >= len(self.questions):

            return

        if self.timer_id is not None:

            self.window.after_cancel(
               self.timer_id
            )

        self.timer_id = None

        selected_answer = self.answer_var.get().strip()

        if not selected_answer:

            selected_answer = ""   

        correct_answer = self.questions[
            self.current_question
        ][6].strip()

        if selected_answer == correct_answer:

            self.score += 1

        self.current_question += 1

        if self.current_question < len(self.questions):

            self.show_question()

        else:

            total_questions = len(self.questions)

            percentage = (
                self.score / total_questions
            ) * 100

            if percentage >= 50:
                status = "PASS"
            else:
                status = "FAIL"

            save_result(
                self.selected_student_id,
                self.score,
                total_questions
            )

            messagebox.showinfo(
                "Quiz Completed",
                f"Student: {self.selected_student_name}\n\n"
                f"Score: {self.score}/{total_questions}\n"
                f"Percentage: {percentage:.1f}%\n"
                f"Status: {status}"
            )

            self.window.destroy()

          

    def start_timer(self):

        if self.timer_id is not None:

            self.window.after_cancel(self.timer_id)

        self.timer_label.config(
            text=f"Time: {self.time_left}"
        )

        if self.time_left > 0:

            self.time_left -= 1

            self.timer_id = self.window.after(
                1000,
                self.start_timer
            )

        else:

            self.next_question()