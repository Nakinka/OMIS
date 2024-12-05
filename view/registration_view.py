import tkinter as tk
from tkinter import ttk

class RegistrationView:
    def __init__(self, master):
        self.master = master
        self.master.title("Регистрация")
        self.master.geometry("934x536")
        self.master.configure(bg='#A49FB1')

        # Заголовок
        title_label = tk.Label(master, text="Регистрация", bg='#A49FB1', font=("Arial", 24, "bold"))
        title_label.pack(pady=10)

        # Фрейм для формы
        self.form_frame = tk.Frame(master, bg='white')
        self.form_frame.pack(pady=20, padx=20, fill='both', expand=True)

        # Поля ввода и подписи
        self.create_widgets()

    def create_widgets(self):
        tk.Label(self.form_frame, text="ФИО", bg='white').grid(row=0, column=0, sticky='w', padx=10, pady=5)
        self.fio_entry = tk.Entry(self.form_frame)
        self.fio_entry.grid(row=0, column=1, padx=10, pady=5)

        tk.Label(self.form_frame, text="Дата рождения", bg='white').grid(row=1, column=0, sticky='w', padx=10, pady=5)
        self.birth_date_entry = tk.Entry(self.form_frame)
        self.birth_date_entry.grid(row=1, column=1, padx=10, pady=5)

        tk.Label(self.form_frame, text="Номер телефона", bg='white').grid(row=2, column=0, sticky='w', padx=10, pady=5)
        self.phone_number_entry = tk.Entry(self.form_frame)
        self.phone_number_entry.grid(row=2, column=1, padx=10, pady=5)

        tk.Label(self.form_frame, text="Должность", bg='white').grid(row=3, column=0, sticky='w', padx=10, pady=5)
        self.position_entry = tk.Entry(self.form_frame)
        self.position_entry.grid(row=3, column=1, padx=10, pady=5)

        tk.Label(self.form_frame, text="Тип работника", bg='white').grid(row=0, column=2, sticky='w', padx=10, pady=5)
        self.worker_type_var = tk.StringVar()
        self.worker_type_combo = ttk.Combobox(self.form_frame, textvariable=self.worker_type_var, values=["Технолог", "Менеджер"])
        self.worker_type_combo.grid(row=0, column=3, padx=10, pady=5)

        tk.Label(self.form_frame, text="Логин", bg='white').grid(row=1, column=2, sticky='w', padx=10, pady=5)
        self.login_entry = tk.Entry(self.form_frame)
        self.login_entry.grid(row=1, column=3, padx=10, pady=5)

        tk.Label(self.form_frame, text="Пароль", bg='white').grid(row=2, column=2, sticky='w', padx=10, pady=5)
        self.password_entry = tk.Entry(self.form_frame, show='*')
        self.password_entry.grid(row=2, column=3, padx=10, pady=5)

        self.register_button = tk.Button(self.master, text="Зарегистрироваться", bg='black', fg='white')
        self.register_button.pack(pady=20)

    def set_register_command(self, command):
        self.register_button.config(command=command)

    def get_registration_data(self):
        return {
            "fio": self.fio_entry.get(),
            "birth_date": self.birth_date_entry.get(),
            "phone_number": self.phone_number_entry.get(),
            "position": self.position_entry.get(),
            "worker_type": self.worker_type_var.get(),
            "login": self.login_entry.get(),
            "password": self.password_entry.get(),
        }