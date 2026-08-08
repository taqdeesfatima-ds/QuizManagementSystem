import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from database.database import (
    add_question,
    get_all_questions,
    update_question,
    delete_question,
    search_questions
)
class QuestionWindow:

    def __init__(self):

        self.window = tk.Toplevel()

        self.window.title("Question Management")

        self.window.geometry("1100x800")

        self.window.configure(bg="white")

        self.window.resizable(False, False)

        self.create_widgets()

        self.selected_question_id = None

        self.load_questions()

    def create_widgets(self):

        title = tk.Label(
            self.window,
            text="Question Management",
            font=("Arial", 20, "bold"),
            bg="white"
        )

        title.pack(pady=20)

        search_frame = tk.Frame(
            self.window,
            bg="white"
        )

        search_frame.pack(pady=10)

        search_label = tk.Label(
            search_frame,
            text="Search Question:",
            font=("Arial", 12),
            bg="white"
        )

        search_label.pack(side="left", padx=5)

        self.search_entry = tk.Entry(
            search_frame,
            font=("Arial", 12),
            width=40
        )

        self.search_entry.pack(side="left", padx=5)

        search_btn = tk.Button(
            search_frame,
            text="Search",
            width=10,
            command=self.search_question
        )

        search_btn.pack(side="left", padx=5)

        show_all_btn = tk.Button(
            search_frame,
            text="Show All",
            width=10,
            command=self.load_questions
        )

        show_all_btn.pack(side="left", padx=5)

        question_label = tk.Label(
            self.window,
            text="Question",
            font=("Arial", 12),
            bg="white"
        )

        question_label.pack()

        self.question_entry = tk.Entry(
            self.window,
            font=("Arial",12),
            width=80
        )

        self.question_entry.pack(pady=5)

        option_a_label = tk.Label(
            self.window,
            text="Option A",
            font=("Arial",12),
            bg="white"
        )

        option_a_label.pack()

        self.option_a_entry = tk.Entry(
            self.window,
            font=("Arial",12),
            width=60
        )

        self.option_a_entry.pack(pady=5)

        option_b_label = tk.Label(
            self.window,
            text="Option B",
            font=("Arial",12),
            bg="white"
        )

        option_b_label.pack()

        self.option_b_entry = tk.Entry(
            self.window,
            font=("Arial",12),
            width=60
        )

        self.option_b_entry.pack(pady=5)

        option_c_label = tk.Label(
            self.window,
            text="Option C",
            font=("Arial",12),
            bg="white"
        )

        option_c_label.pack()

        self.option_c_entry = tk.Entry(
            self.window,
            font=("Arial",12),
            width=60
        )

        self.option_c_entry.pack(pady=5)

        option_d_label = tk.Label(
            self.window,
            text="Option D",
            font=("Arial",12),
            bg="white"
        )

        option_d_label.pack()

        self.option_d_entry = tk.Entry(
            self.window,
            font=("Arial",12),
            width=60
        )

        self.option_d_entry.pack(pady=5)

        correct_label = tk.Label(
            self.window,
            text="Correct Answer",
            font=("Arial",12),
            bg="white"
        )

        correct_label.pack()

        self.correct_entry = tk.Entry(
            self.window,
            font=("Arial",12),
            width=20
        )

        self.correct_entry.pack(pady=5)

        button_frame = tk.Frame(
            self.window,
            bg="white"
        )

        button_frame.pack(pady=20)

        save_btn = tk.Button(
            button_frame,
            text="Save",
            width=12,
            font=("Arial", 11),
            command=self.save_question
        )

        save_btn.grid(row=0, column=0, padx=5)

        update_btn = tk.Button(
            button_frame,
            text="Update",
            width=12,
            font=("Arial", 11),
            command=self.update_selected_question
        )

        update_btn.grid(row=0, column=1, padx=5)

        delete_btn = tk.Button(
           button_frame,
           text="Delete",
           width=12,
           font=("Arial", 11),
           command=self.delete_selected_question
        )

        delete_btn.grid(row=0, column=2, padx=5)

        table_frame = tk.Frame(
           self.window,
           bg="white"
        )

        table_frame.pack(pady=20)

        self.question_table = ttk.Treeview(
            table_frame,
            columns=(
               "ID",
               "Question",
               "Option A",
               "Option B",
               "Option C",
               "Option D",
               "Correct"
            ),
            show="headings",
            height=8
        )

        self.question_table.pack()

        self.question_table.bind(
            "<<TreeviewSelect>>",
            self.select_question
        )

        self.question_table.heading("ID", text="ID")

        self.question_table.heading("Question", text="Question")

        self.question_table.heading("Option A", text="Option A")

        self.question_table.heading("Option B", text="Option B")

        self.question_table.heading("Option C", text="Option C")

        self.question_table.heading("Option D", text="Option D")

        self.question_table.heading("Correct", text="Correct Answer")

        self.question_table.column("ID", width=50)

        self.question_table.column("Question", width=220)

        self.question_table.column("Option A", width=120)

        self.question_table.column("Option B", width=120)

        self.question_table.column("Option C", width=120)

        self.question_table.column("Option D", width=120)

        self.question_table.column("Correct", width=120)  

        clear_btn = tk.Button(
            button_frame,
            text="Clear",
            width=12,
            font=("Arial", 11)
        )

        clear_btn.grid(row=0, column=3, padx=5)

    def save_question(self):

        question = self.question_entry.get()

        option_a = self.option_a_entry.get()

        option_b = self.option_b_entry.get()

        option_c = self.option_c_entry.get()

        option_d = self.option_d_entry.get()

        correct_answer = self.correct_entry.get()

        if (
            question == "" or
            option_a == "" or
            option_b == "" or
            option_c == "" or
            option_d == "" or
            correct_answer == ""
        ):

            messagebox.showwarning(
               "Warning",
               "Please fill all fields."
            )

            return

        add_question(
            question,
            option_a,
            option_b,
            option_c,
            option_d,
            correct_answer
        )

        messagebox.showinfo(
           "Success",
           "Question Saved Successfully."
        )
    
        self.clear_fields()

        self.load_questions()

    def update_selected_question(self):

        if self.selected_question_id is None:

            messagebox.showwarning(
                "Warning",
                "Please select a question first."
            )

            return

        question = self.question_entry.get()

        option_a = self.option_a_entry.get()

        option_b = self.option_b_entry.get()

        option_c = self.option_c_entry.get()

        option_d = self.option_d_entry.get()

        correct_answer = self.correct_entry.get()

        update_question(
            self.selected_question_id,
            question,
            option_a,
            option_b,
            option_c,
            option_d,
            correct_answer
        )

        messagebox.showinfo(
            "Success",
            "Question Updated Successfully."
        )

        self.clear_fields()

        self.load_questions()

    def delete_selected_question(self):

        if self.selected_question_id is None:

            messagebox.showwarning(
                "Warning",
                "Please select a question first."
            )

            return

        confirm = messagebox.askyesno(
            "Confirm Delete",
            "Are you sure you want to delete this question?"
        )

        if not confirm:
           return

        delete_question(self.selected_question_id)

        messagebox.showinfo(
           "Success",
           "Question Deleted Successfully."
        )

        self.selected_question_id = None

        self.clear_fields()

        self.load_questions()

    def clear_fields(self):

        self.question_entry.delete(0, tk.END)

        self.option_a_entry.delete(0, tk.END)

        self.option_b_entry.delete(0, tk.END)

        self.option_c_entry.delete(0, tk.END)

        self.option_d_entry.delete(0, tk.END)

        self.correct_entry.delete(0, tk.END)

    def load_questions(self):

        for row in self.question_table.get_children():
             self.question_table.delete(row)

        questions = get_all_questions()

        for question in questions:
             self.question_table.insert("", tk.END, values=question)

    def search_question(self):

        keyword = self.search_entry.get()

        questions = search_questions(keyword)

        for row in self.question_table.get_children():
            self.question_table.delete(row)

        for question in questions:
            self.question_table.insert("", tk.END, values=question)

    def select_question(self, event):

        selected = self.question_table.focus()

        if not selected:
            return

        values = self.question_table.item(selected, "values")

        self.selected_question_id = values[0]

        self.clear_fields()

        self.question_entry.insert(0, values[1])

        self.option_a_entry.insert(0, values[2])

        self.option_b_entry.insert(0, values[3])

        self.option_c_entry.insert(0, values[4])

        self.option_d_entry.insert(0, values[5])

        self.correct_entry.insert(0, values[6])

    def run(self):

        self.window.mainloop()