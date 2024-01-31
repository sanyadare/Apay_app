import tkinter as tk
import customtkinter as ctk
from tkinter import messagebox
import pyodbc
from tkinter import *
from PIL import Image
import os 
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("dark-blue")

class LoginApplication: 
    
    def __init__(self, root):
        self.root = root
        self.root.title("Akyerit Pay")
        right_frame=ctk.CTkFrame(self.root,fg_color='#200012')
        right_frame.pack(side="left",fill="both",expand=True)
        
        
        left_frame=ctk.CTkFrame(self.root,fg_color='#001220')
        left_frame.pack(side="left",fill="both",expand=True)


        left_inner_top_frame=ctk.CTkFrame(master=left_frame,fg_color='#001220')
        # left_inner_top_frame.pack(side="top",fill="both",expand=True)


        self.login_frame = ctk.CTkFrame(master=left_frame, bg_color='#001220',fg_color='#001220')
        self.login_frame.pack(fill="both",expand=True)
        # self.login_frame.grid(row=1, column=0, columnspan=2)
        self.signup_frame = ctk.CTkFrame(master=left_frame,bg_color='#200012',fg_color='#200012')
        # self.signup_frame.pack(fill="both",expand=True)

        left_inner_buttom_frame=ctk.CTkFrame(master=left_frame,fg_color='#001220')
        left_inner_buttom_frame.pack(side="top",fill="both",expand=True)

        self.main_frame = ctk.CTkFrame(self.root, bg_color='#122000',fg_color='#122000',width=350, height=550)
    

        self.create_login_frame()
        self.create_signup_frame()
        self.create_main_frame()

        self.show_login_frame()


    def create_login_frame(self):
        self.login_label = ctk.CTkLabel(self.login_frame, text="Login Page")
        # self.login_label.pack(pady=10)
        self.login_label.grid(row=0, column=2, columnspan=10, pady=0, padx=50)

        self.username_label = ctk.CTkLabel(self.login_frame, text="Username:")
        self.username_entry = ctk.CTkEntry(self.login_frame,
                                           width=200,
                                           height=25,
                                           corner_radius=10)
        
        self.username_entry.grid(row=3, column=2, columnspan=10, pady=0, padx=50)
        # self.username_entry.grid(row=3, column=2, columnspan=10, pady=0, padx=50)
        # self.username_entry.place(relx=0.5, rely=0.5, anchor=tk.CENTER)
        # text = self.username_entry.get()

        # self.password_label = ctk.CTkLabel(self.login_frame, text="Password:")
        # self.password_entry = ctk.CTkEntry(self.login_frame, 
        #                                         show="*",
        #                                         width=120,
        #                                         height=25,
        #                                         corner_radius=10)
        # self.password_entry.place(relx=0.5, rely=0.5, anchor=tk.CENTER)
        # text = self.password_entry.get()

        # self.login_button = ctk.CTkButton(self.login_frame,text="Login", corner_radius=30,fg_color="#3465FD",hover_color="#FD3465", command=self.login)
        # self.login_button.place(relx=0.5, rely=0.5)
        
        # self.signup_button = ctk.CTkButton(self.login_frame, text="Switch to Signup",fg_color="#3465FD",hover_color="#FD3465", command=self.show_signup_frame)
        # self.signup_button.place(relx=0.5, rely=0.5)

        # self.username_label.pack(pady=5)
        # self.username_entry.pack(pady=5)
        # self.password_label.pack(pady=5)
        # self.password_entry.pack(pady=5)
        # self.login_button.pack(pady=10)
        # self.signup_button.pack(pady=5)
# creating signup
    def create_signup_frame(self):
        self.signup_label = ctk.CTkLabel(self.signup_frame, text="Signup Page")
        self.signup_label.pack(pady=10)

        # Include signup form elements here (similar to login frame)

        self.signup_button = ctk.CTkButton(self.signup_frame, text="Signup", command=self.signup)
        self.login_button = ctk.CTkButton(self.signup_frame, text="Switch to Login", command=self.show_login_frame)

        self.username_label = ctk.CTkLabel(self.signup_frame, text="Username:")
        self.username_entry = ctk.CTkEntry(self.signup_frame,
                                           width=120,
                                           height=25,
                                           corner_radius=10)
        self.username_entry.place(relx=0.5, rely=0.5)
        text = self.username_entry.get()

        self.password_label = ctk.CTkLabel(self.signup_frame, text="Password:")
        self.password_entry = ctk.CTkEntry(self.signup_frame, 
                                                show="*",
                                                width=120,
                                                height=25,
                                                corner_radius=10)
        self.password_entry.place(relx=0.5, rely=0.5)
        text = self.password_entry.get()

        self.signup_button = ctk.CTkButton(self.signup_frame,text="signup", corner_radius=30,fg_color="#3465FD",hover_color="#FD3465", command=self.signup)
        self.signup_button.place(relx=0.5, rely=0.5)
        
        self.login_button = ctk.CTkButton(self.signup_frame, text="login Instead",corner_radius=30, fg_color="#3465FD",hover_color="#FD3465", command=self.show_login_frame)
        self.login_button.place(relx=0.5, rely=0.5)

        self.username_label.pack(pady=5)
        self.username_entry.pack(pady=5)
        self.password_label.pack(pady=5)
        self.password_entry.pack(pady=5)
        self.login_button.pack(pady=10)
        self.signup_button.pack(pady=5)

# ################creating main frame @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
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


    def signup(self):
        # Add signup functionality (e.g., create a new user)
        # If successful, switch to main frame using self.show_main_frame()\  
        username = self.username_entry.get()
        password = self.password_entry.get()

    def login(self):
        username = self.username_entry.get()
        password = self.password_entry.get()

        # Replace these values with your MSSQL server information
        server = 'DESKTOP-O6L0LBE'
        database = 'HRM'
        username_db = 'sanya'
        password_db = ''

        try:
            connection = pyodbc.connect(
                f'DRIVER=ODBC Driver 11 for SQL Server;'
                f'SERVER={server};'
                f'DATABASE={database};'
                f'UID={username_db};'
                f'PWD={password_db}'
            )

            cursor = connection.cursor()
            query = f"SELECT * FROM registration where Email = '{username}' AND password = '{password}'"
            cursor.execute(query)

            if cursor.fetchone():
                messagebox.showinfo("Login Successful", "Welcome!")
                self.show_main_frame()
            else:
                messagebox.showerror("Login Failed", "Invalid username or password")

        except pyodbc.Error as e:
            messagebox.showerror("Database Error", f"Error: {str(e)}")

        finally:
            try:
                connection.close()
            except NameError:
                pass

   

if __name__ == "__main__":
    root = ctk.CTk()
    root.geometry("700x550")
    #root_tk.resizable(width=False,height=True)
    root.title("AkyeritPay Test")
    app = LoginApplication(root)
    root.mainloop()
    

    
    



#============================================================================
#import tkinter as tk
#from tkinter import messagebox
#import pyodbc

# Function to handle login button click
#def login():
 #   email = entry_username.get()
 #   password = entry_password.get()

    # Replace 'your_database_connection_string' with your actual connection string
  #  conn_str = 'DRIVER={SQL Server};SERVER=DESKTOP-O6L0LBE;DATABASE=HRM;UID=sanya;PWD='
    
  #  try:
        # Connect to the database
    #    connection = pyodbc.connect(conn_str)
    #    cursor = connection.cursor()

        # Execute a query to check the login credentials
     #   query = f"SELECT * FROM registration where Email = '{email}' AND password = '{password}'"
      #  cursor.execute(query)
   #     row = cursor.fetchone()
#
   #     if row:
   #         messagebox.showinfo("Login Successful", "Welcome, " + email)
   #     else:
   #         messagebox.showerror("Login Failed", "Invalid username or password")

  #  except pyodbc.Error as e:
  #      messagebox.showerror("Database Error", "Error connecting to the database")

  #  finally:
        # Close the database connection
 #       if connection:
  #          connection.close()

# Create the main window
#root.title("Akyerit PayrollHRMS")

# Create and place widgets
#label_username = tk.Label(root, text="Username:")
#label_username.pack(pady=10)
#entry_username = tk.Entry(root)
#entry_username.pack(pady=10)

#label_password = tk.Label(root, text="Password:")
#label_password.pack(pady=10)
#entry_password = tk.Entry(root, show="*")
#entry_password.pack(pady=10)

#button_login = tk.Button(root, text="Login", command=login)
#button_login.pack(pady=20)

# Run the main loop
#root.mainloop()''
