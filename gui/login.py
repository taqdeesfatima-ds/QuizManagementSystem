from database.database import verify_admin
import tkinter as tk
from tkinter import messagebox
from gui.dashboard import Dashboard
from gui.register import RegisterWindow

class LoginWindow:

    def __init__(self):

        self.window = tk.Tk()

        self.window.title("Quiz Management System")
        self.window.geometry("600x400")
        self.window.resizable(False, False)
        self.window.configure(bg="white")

        self.create_widgets()

    def create_widgets(self):

        # ================= Title =================
        title = tk.Label(
            self.window,
            text="Quiz Management System",
            font=("Arial", 22, "bold"),
            bg="white"
        )
        title.pack(pady=20)

        # ================= Subtitle =================
        subtitle = tk.Label(
            self.window,
            text="Admin Login",
            font=("Arial", 16),
            bg="white"
        )
        subtitle.pack(pady=10)

        # ================= Username =================
        username_label = tk.Label(
            self.window,
            text="Username",
            font=("Arial", 12),
            bg="white"
        )
        username_label.pack()

        self.username_entry = tk.Entry(
            self.window,
            font=("Arial", 12),
            width=30
        )
        self.username_entry.pack(pady=5)

        # ================= Password =================
        password_label = tk.Label(
            self.window,
            text="Password",
            font=("Arial", 12),
            bg="white"
        )
        password_label.pack()

        self.password_entry = tk.Entry(
            self.window,
            font=("Arial", 12),
            width=30,
            show="*"
        )
        self.password_entry.pack(pady=5)

        # ================= Show Password =================
        self.show_password = tk.BooleanVar()

        show = tk.Checkbutton(
            self.window,
            text="Show Password",
            variable=self.show_password,
            command=self.toggle_password,
            bg="white"
        )
        show.pack(pady=10)

        # ================= Buttons =================
        button_frame = tk.Frame(
            self.window,
            bg="white"
        )
        button_frame.pack(pady=20)

        login_btn = tk.Button(
            button_frame,
            text="Login",
            width=12,
            command=self.login
        )
        login_btn.grid(row=0, column=0, padx=10)

        register_btn = tk.Button(
            self.window,
            text="Register New Admin",
            font=("Arial", 11),
            width=20,
            command=self.open_register
        )

        register_btn.pack(pady=10)

        exit_btn = tk.Button(
            button_frame,
            text="Exit",
            width=12,
            command=self.window.destroy
        )
        exit_btn.grid(row=0, column=1, padx=10)

    def toggle_password(self):

        if self.show_password.get():
            self.password_entry.config(show="")
        else:
            self.password_entry.config(show="*")

    def login(self):

        username = self.username_entry.get().strip()

        password = self.password_entry.get()

        if username == "" or password == "":
            messagebox.showwarning(
               "Warning",
               "Please enter username and password."
            )
            return

        admin = verify_admin(username, password)

        if admin:

            self.window.destroy()

            dashboard = Dashboard()

            dashboard.run()

        else:
            messagebox.showerror(
               "Error",
               "Invalid Username or Password"
            )

    def open_register(self):

        RegisterWindow()
    def run(self):
        self.window.mainloop()