import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
import sqlite3


class StudentWindow:

    def __init__(self):

        self.window = tk.Toplevel()

        self.window.title("Student Management")

        self.window.geometry("900x700")

        self.window.configure(bg="white")

        self.window.resizable(False, False)

        self.create_widgets()

    def create_widgets(self):

        title = tk.Label(
            self.window,
            text="Student Management",
            font=("Arial", 20, "bold"),
            bg="white"
        )

        title.pack(pady=20)

        name_label = tk.Label(
            self.window,
            text="Student Name",
            font=("Arial", 12),
            bg="white"
        )

        name_label.pack()

        self.name_entry = tk.Entry(
            self.window,
            font=("Arial", 12),
            width=50
        )

        self.name_entry.pack(pady=5)

        roll_label = tk.Label(
            self.window,
            text="Roll Number",
            font=("Arial", 12),
            bg="white"
        )

        roll_label.pack()

        self.roll_entry = tk.Entry(
            self.window,
            font=("Arial", 12),
            width=50
        )

        self.roll_entry.pack(pady=5)

        email_label = tk.Label(
            self.window,
            text="Email",
            font=("Arial", 12),
            bg="white"
        )

        email_label.pack()

        self.email_entry = tk.Entry(
            self.window,
            font=("Arial", 12),
            width=50
        )

        self.email_entry.pack(pady=5)

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
            command=self.save_student
        )
        save_btn.grid(row=0, column=0, padx=5)

        update_btn = tk.Button(
            button_frame,
            text="Update",
            width=12,
            font=("Arial", 11),
            command=self.update_student
        )

        update_btn.grid(row=0, column=1, padx=5)


        delete_btn = tk.Button(
            button_frame,
            text="Delete",
            width=12,
            font=("Arial", 11),
            command=self.delete_student
        )

        delete_btn.grid(row=0, column=2, padx=5)

        clear_btn = tk.Button(
            button_frame,
            text="Clear",
            width=12,
            font=("Arial", 11),
            command=self.clear_fields
        )

        clear_btn.grid(row=0, column=3, padx=5)

        search_frame = tk.Frame(
            self.window,
            bg="white"
        )

        search_frame.pack(pady=5)

        search_label = tk.Label(
            search_frame,
            text="Search Student",
            font=("Arial", 11),
            bg="white"
        )

        search_label.grid(row=0, column=0, padx=5)

        self.search_entry = tk.Entry(
            search_frame,
            font=("Arial", 11),
            width=30
        )

        self.search_entry.grid(row=0, column=1, padx=5)

        search_btn = tk.Button(
            search_frame,
            text="Search",
            width=10,
            command=self.search_student
        )

        search_btn.grid(row=0, column=2, padx=5)

        show_all_btn = tk.Button(
            search_frame,
            text="Show All",
            width=10,
            command=self.load_students
        )

        show_all_btn.grid(row=0, column=3, padx=5)

        self.student_table = ttk.Treeview(
            self.window,
            columns=("ID", "Name", "Roll Number", "Email"),
            show="headings",
            height=10
        )

        self.student_table.heading("ID", text="ID")
        self.student_table.heading("Name", text="Name")
        self.student_table.heading("Roll Number", text="Roll Number")
        self.student_table.heading("Email", text="Email")

        self.student_table.column("ID", width=60)
        self.student_table.column("Name", width=200)
        self.student_table.column("Roll Number", width=150)
        self.student_table.column("Email", width=250)

        self.student_table.pack(pady=20)

        self.load_students()

        self.student_table.bind(
            "<<TreeviewSelect>>",
            self.select_student
        )

    def save_student(self):

        name = self.name_entry.get()

        roll_number = self.roll_entry.get()

        email = self.email_entry.get()

        connection = sqlite3.connect("database/quiz.db")

        cursor = connection.cursor()

        try:

            cursor.execute(
                """
                INSERT INTO students(name, roll_number, email)
                VALUES(?, ?, ?)
                """,
                (name, roll_number, email)
            )

            connection.commit()

            messagebox.showinfo(
                "Success",
                "Student Saved Successfully."
            )

            self.clear_fields()
            self.load_students()
            

        except sqlite3.IntegrityError:

            messagebox.showerror(
                "Error",
                "Roll Number already exists."
            )

        connection.close()

    def load_students(self):

        for row in self.student_table.get_children():
            self.student_table.delete(row)

        connection = sqlite3.connect("database/quiz.db")

        cursor = connection.cursor()

        cursor.execute("""
            SELECT * FROM students
        """)

        students = cursor.fetchall()

        connection.close()

        for student in students:
            self.student_table.insert(
                "",
                tk.END,
                values=student
            )

    def search_student(self):

        keyword = self.search_entry.get()

        for row in self.student_table.get_children():
            self.student_table.delete(row)

        connection = sqlite3.connect("database/quiz.db")

        cursor = connection.cursor()

        cursor.execute(
            """
            SELECT * FROM students
            WHERE name LIKE ?
            OR roll_number LIKE ?
            OR email LIKE ?
            """,
            (
               "%" + keyword + "%",
               "%" + keyword + "%",
               "%" + keyword + "%"
            )
        )

        students = cursor.fetchall()

        connection.close()

        for student in students:

            self.student_table.insert(
               "",
               tk.END,
               values=student
            )

    def select_student(self, event):

        selected = self.student_table.selection()

        if not selected:
            return

        values = self.student_table.item(
            selected[0],
            "values"
        )

        self.selected_student_id = values[0]

        self.name_entry.delete(0, tk.END)
        self.name_entry.insert(0, values[1])

        self.roll_entry.delete(0, tk.END)
        self.roll_entry.insert(0, values[2])

        self.email_entry.delete(0, tk.END)
        self.email_entry.insert(0, values[3])

    def update_student(self):

        if not hasattr(self, "selected_student_id"):
            messagebox.showerror(
               "Error",
               "Please select a student first."
            )
            return

        name = self.name_entry.get()
        roll_number = self.roll_entry.get()
        email = self.email_entry.get()

        connection = sqlite3.connect("database/quiz.db")

        cursor = connection.cursor()

        try:

            cursor.execute(
               """
               UPDATE students
               SET name = ?, roll_number = ?, email = ?
               WHERE id = ?
               """,
               (
                    name,
                    roll_number,
                    email,
                    self.selected_student_id
                )
            )

            connection.commit()

            messagebox.showinfo(
                "Success",
                "Student Updated Successfully."
            )

            self.clear_fields()
            self.load_students()

        except sqlite3.IntegrityError:

            messagebox.showerror(
               "Error",
               "Roll Number already exists."
            )

        connection.close()

    def delete_student(self):

        if not hasattr(self, "selected_student_id"):
            messagebox.showerror(
               "Error",
               "Please select a student first."
            )
            return

        connection = sqlite3.connect("database/quiz.db")

        cursor = connection.cursor()

        cursor.execute(
            """
            DELETE FROM students
            WHERE id = ?
            """,
            (self.selected_student_id,)
        )

        connection.commit()

        connection.close()

        messagebox.showinfo(
           "Success",
           "Student Deleted Successfully."
        )

        self.clear_fields()
        self.load_students()

        del self.selected_student_id

    def clear_fields(self):

        self.name_entry.delete(0, tk.END)

        self.roll_entry.delete(0, tk.END)

        self.email_entry.delete(0, tk.END)

    def run(self):

        self.window.mainloop()