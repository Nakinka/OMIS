import tkinter as tk
from tkinter import messagebox 

class LoginView:
    def __init__(self, master):
        self.master = master
        self.master.title("Контроль качества производства")
        self.master.geometry("934x536")
        self.master.configure(bg='#A49FB1')

       
        title_label = tk.Label(master, text="Контроль качества производства", bg='#A49FB1', font=("Arial", 20, "bold"))
        title_label.pack(pady=20)

        self.form_frame = tk.Frame(master, padx=20, pady=20, bg='white')
        self.form_frame.place(relx=0.5, rely=0.5, anchor='center')

       
        self.create_widgets()

    def create_widgets(self):
        tk.Label(self.form_frame, text="Имя пользователя", bg='white').pack(anchor='w')
        self.username_entry = tk.Entry(self.form_frame, width=30)
        self.username_entry.pack(pady=5)

        tk.Label(self.form_frame, text="Пароль", bg='white').pack(anchor='w')
        self.password_entry = tk.Entry(self.form_frame, width=30, show='*')
        self.password_entry.pack(pady=5)

        self.login_button = tk.Button(self.form_frame, text="Войти", bg='black', fg='white')
        self.login_button.pack(fill='x', pady=10)

        self.register_label = tk.Label(self.form_frame, text="Нет аккаунта?", bg='white', fg='blue', cursor="hand2")
        self.register_label.pack(pady=5)

    def set_login_command(self, command):
        self.login_button.config(command=command)

    def set_register_command(self, command):
        self.register_label.bind("<Button-1>", lambda e: command())

    def get_username(self):
        return self.username_entry.get()

    def get_password(self):
        return self.password_entry.get()
    
    def show_error(self, message):
        messagebox.showerror("Ошибка", message)