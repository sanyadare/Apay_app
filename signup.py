import tkinter as tk
import customtkinter as ctk
from tkinter import messagebox
import pyodbc
from tkinter import *

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("dark-blue")

class LoginApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Payroll App")

        self.login_frame = ctk.CTkFrame(self.root, bg_color='#001220',fg_color='#001220')
        self.signup_frame = ctk.CTkFrame(self.root,bg_color='#200012',fg_color='#200012')
        self.main_frame = ctk.CTkFrame(self.root, bg_color='#122000',fg_color='#122000')

        self.create_login_frame()
        self.create_signup_frame()
        self.create_main_frame()

        self.show_login_frame()

    def create_login_frame(self):
        self.login_label = ctk.CTkLabel(self.login_frame, text="Login Page")
        self.login_label.pack(pady=10)

        self.username_label = ctk.CTkLabel(self.login_frame, text="Username:")
        self.username_entry = ctk.CTkEntry(self.login_frame)

        self.password_label = ctk.CTkLabel(self.login_frame, text="Password:")
        self.password_entry = ctk.CTkEntry(self.login_frame, show="*")

        self.login_button = ctk.CTkButton(self.login_frame, text="Login", command=self.login)
        self.signup_button = ctk.CTkButton(self.login_frame, text="Switch to Signup", command=self.show_signup_frame)

        self.username_label.pack(pady=5)
        self.username_entry.pack(pady=5)
        self.password_label.pack(pady=5)
        self.password_entry.pack(pady=5)
        self.login_button.pack(pady=10)
        self.signup_button.pack(pady=5)

    def create_signup_frame(self):
        self.signup_label = ctk.CTkLabel(self.signup_frame, text="Signup Page")
        self.signup_label.pack(pady=10)

        # Include signup form elements here (similar to login frame)

        self.signup_button = ctk.CTkButton(self.signup_frame, text="Signup", command=self.signup)
        self.login_button = ctk.CTkButton(self.signup_frame, text="Switch to Login", command=self.show_login_frame)

        # Pack signup form elements and buttons here

    def create_main_frame(self):
        self.main_label = ctk.CTkLabel(self.main_frame, text="Financial Main Page")
        self.main_label.pack(pady=10)

        # Include main page elements and functionality here

        self.logout_button = ctk.CTkButton(self.main_frame, text="Logout", command=self.show_login_frame)
        self.logout_button.pack(pady=10)

    def show_login_frame(self):
        self.signup_frame.pack_forget()
        self.main_frame.pack_forget()
        self.login_frame.pack()

    def show_signup_frame(self):
        self.login_frame.pack_forget()
        self.main_frame.pack_forget()
        self.signup_frame.pack()

    def show_main_frame(self):
        self.login_frame.pack_forget()
        self.signup_frame.pack_forget()
        self.main_frame.pack()

    def login(self):
        # Add login functionality (e.g., check credentials)
        # If successful, switch to main frame using self.show_main_frame()

        def signup(self):
        # Add signup functionality (e.g., create a new user)
        # If successful, switch to main frame using self.show_main_frame()
            
            if __name__ == "__main__":
                root = ctk.CTk()
                root.geometry("700x550")
                #root.resizable(width=False,height=True)
                root.title("AkyeritPay Test")
                app = LoginApp(root)
                root.mainloop()

#if __name__ == "__main__":
 #   root = tk.Tk()
  #  app = FinancialApp(root)
   # root.mainloop()