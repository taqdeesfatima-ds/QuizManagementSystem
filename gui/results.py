import tkinter as tk
from tkinter import ttk, messagebox

from database.database import (
    get_all_results,
    delete_result
)


class ResultsWindow:

    def __init__(self):

        self.window = tk.Toplevel()

        self.window.title("Quiz Results")

        self.window.geometry("850x550")

        self.window.configure(bg="white")

        self.window.resizable(False, False)

        self.create_widgets()

    def create_widgets(self):

        title = tk.Label(
            self.window,
            text="QUIZ RESULTS",
            font=("Arial", 22, "bold"),
            bg="white"
        )

        title.pack(pady=25)

        self.result_table = ttk.Treeview(
            self.window,
            columns=(
                "ID",
                "Student",
                "Roll Number",
                "Score",
                "Total",
                "Percentage",
                "Status"
            ),
            show="headings",
            height=15
        )

        # Headings

        self.result_table.heading(
            "ID",
            text="ID"
        )

        self.result_table.heading(
            "Student",
            text="Student"
        )

        self.result_table.heading(
            "Roll Number",
            text="Roll Number"
        )

        self.result_table.heading(
            "Score",
            text="Score"
        )

        self.result_table.heading(
            "Total",
            text="Total"
        )

        self.result_table.heading(
            "Percentage",
            text="Percentage"
        )

        self.result_table.heading(
            "Status",
            text="Status"
        )

        # Columns

        self.result_table.column(
            "ID",
            width=50,
            anchor="center"
        )

        self.result_table.column(
            "Student",
            width=160,
            anchor="center"
        )

        self.result_table.column(
            "Roll Number",
            width=120,
            anchor="center"
        )

        self.result_table.column(
            "Score",
            width=70,
            anchor="center"
        )

        self.result_table.column(
            "Total",
            width=100,
            anchor="center"
        )

        self.result_table.column(
            "Percentage",
            width=110,
            anchor="center"
        )

        self.result_table.column(
            "Status",
            width=90,
            anchor="center"
        )

        self.result_table.pack(
            padx=20,
            pady=20
        )

        delete_btn = tk.Button(
            self.window,
            text="Delete Result",
            width=15,
            font=("Arial", 11),
            command=self.delete_selected_result
        )

        delete_btn.pack(pady=10)

        self.load_results()

    def load_results(self):

        for row in self.result_table.get_children():

            self.result_table.delete(row)

        results = get_all_results()

        for result in results:

            result_id = result[0]

            student_name = result[1]

            roll_number = result[2]

            score = result[3]

            total = result[4]

            if total > 0:

                percentage = (
                    score / total
                ) * 100

            else:

                percentage = 0

            if percentage >= 50:

                status = "PASS"

            else:

                status = "FAIL"

            self.result_table.insert(
                "",
                tk.END,
                values=(
                    result_id,
                    student_name,
                    roll_number,
                    score,
                    total,
                    f"{percentage:.1f}%",
                    status
                )
            )

    def delete_selected_result(self):

        selected = self.result_table.selection()

        if not selected:

            messagebox.showwarning(
                "Warning",
                "Please select a result first."
            )

            return

        values = self.result_table.item(
            selected[0],
            "values"
        )

        result_id = values[0]

        delete_result(result_id)

        messagebox.showinfo(
            "Success",
            "Result Deleted Successfully."
        )

        self.load_results()