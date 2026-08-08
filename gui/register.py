import tkinter as tk
from tkinter import messagebox
import re
from database.database import register_admin


class RegisterWindow:

    def __init__(self):

        self.window = tk.Toplevel()

        self.window.title("Admin Registration")

        self.window.geometry("450x550")

        self.window.configure(bg="white")

        self.window.resizable(False, False)

        self.create_widgets()

    def create_widgets(self):

        title = tk.Label(
            self.window,
            text="ADMIN REGISTRATION",
            font=("Arial", 20, "bold"),
            bg="white"
        )

        title.pack(pady=30)

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

        self.username_entry.pack(pady=8)

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

        self.password_entry.pack(pady=8)

        self.password_entry.bind(
            "<KeyRelease>",
            self.check_password_strength
        )

        self.strength_label = tk.Label(
            self.window,
            text="Password Strength: ",
            font=("Arial", 10, "bold"),
            bg="white"
        )

        self.strength_label.pack(pady=3)

        self.requirements_label = tk.Label(
            self.window,
            text="",
            font=("Arial", 9),
            bg="white",
            justify="left"
        )

        self.requirements_label.pack()

        self.show_password = tk.BooleanVar()

        show_password_check = tk.Checkbutton(
            self.window,
            text="Show Password",
            variable=self.show_password,
            command=self.toggle_password,
            bg="white"
        )

        show_password_check.pack()

        confirm_label = tk.Label(
            self.window,
            text="Confirm Password",
            font=("Arial", 12),
            bg="white"
        )

        confirm_label.pack()

        self.confirm_entry = tk.Entry(
            self.window,
            font=("Arial", 12),
            width=30,
            show="*"
        )

        self.confirm_entry.pack(pady=8)

        self.show_confirm_password = tk.BooleanVar()

        show_confirm_check = tk.Checkbutton(
            self.window,
            text="Show Confirm Password",
            variable=self.show_confirm_password,
            command=self.toggle_confirm_password,
            bg="white"
        )

        show_confirm_check.pack()

        register_btn = tk.Button(
            self.window,
            text="Register",
            font=("Arial", 11),
            width=15,
            command=self.register
        )

        register_btn.pack(pady=20)

    def register(self):

        username = self.username_entry.get().strip()

        password = self.password_entry.get()

        confirm_password = self.confirm_entry.get()

        if username == "":

            messagebox.showerror(
                "Error",
                "Please enter username.",
                parent=self.window
            )

            return

        if password == "":

            messagebox.showerror(
                "Error",
                "Please enter password.",
                parent=self.window
            )
            
            return

        if len(password) < 8:

            messagebox.showerror(
                "Weak Password",
                "Password must be at least 8 characters.",
                parent=self.window
            )

            return

        if not re.search(r"[A-Z]", password):

            messagebox.showerror(
                "Weak Password",
                "Password must contain at least one uppercase letter.",
                parent=self.window
            )

            return

        if not re.search(r"[a-z]", password):

            messagebox.showerror(
                "Weak Password",
                "Password must contain at least one lowercase letter.",
                parent=self.window
            )

            return

        if not re.search(r"[0-9]", password):

            messagebox.showerror(
                "Weak Password",
                "Password must contain at least one number.",
                parent=self.window
            )

            return

        if not re.search(r"[^A-Za-z0-9]", password):

            messagebox.showerror(
               "Weak Password",
                "Password must contain at least one special character.",
                parent=self.window
            )

            return


        if password != confirm_password:

            messagebox.showerror(
                "Error",
                "Passwords do not match.",
                parent=self.window
            )

            return

        success = register_admin(
            username,
            password
        )

        if success:

            messagebox.showinfo(
                "Success",
                "Admin registered successfully.",
                parent=self.window
            )

            self.window.destroy()

        else:

            messagebox.showerror(
                "Error",
                "Username already exists.",
                parent=self.window
            )

    def check_password_strength(self, event=None):

        password = self.password_entry.get()

        if password == "":

            self.strength_label.config(
                text="Password Strength: ",
                fg="black"
            )

            self.requirements_label.config(
                text=""
            )

            return

        requirements = []

        if len(password) >= 8:
            requirements.append("✓ 8 characters")
        else:
            requirements.append("✗ 8 characters")

        if re.search(r"[A-Z]", password):
            requirements.append("✓ Uppercase letter")
        else:
            requirements.append("✗ Uppercase letter")

        if re.search(r"[a-z]", password):
            requirements.append("✓ Lowercase letter")
        else:
            requirements.append("✗ Lowercase letter")

        if re.search(r"[0-9]", password):
            requirements.append("✓ Number")
        else:
            requirements.append("✗ Number")

        if re.search(r"[^A-Za-z0-9]", password):
            requirements.append("✓ Special character")
        else:
            requirements.append("✗ Special character")

        self.requirements_label.config(
            text="\n".join(requirements)
        )

        if (
           len(password) >= 8
           and re.search(r"[A-Z]", password)
           and re.search(r"[a-z]", password)
           and re.search(r"[0-9]", password)
           and re.search(r"[^A-Za-z0-9]", password)
        ):

            self.strength_label.config(
               text="Password Strength: STRONG",
               fg="green"
            )

        elif len(password) >= 6:

            self.strength_label.config(
               text="Password Strength: MEDIUM",
               fg="orange"
            )

        else:

            self.strength_label.config(
               text="Password Strength: WEAK",
               fg="red"
            )

    def toggle_password(self):

        if self.show_password.get():

            self.password_entry.config(show="")

        else:

            self.password_entry.config(show="*")

    def toggle_confirm_password(self):

        if self.show_confirm_password.get():

            self.confirm_entry.config(show="")

        else:

            self.confirm_entry.config(show="*")

    def run(self):

        self.window.mainloop()