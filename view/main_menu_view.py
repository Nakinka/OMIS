import tkinter as tk

class MainMenuView:
    def __init__(self, master):
        self.master = master
        self.master.title("Главное меню")
        self.master.geometry("934x536")
        self.master.configure(bg='#A49FB1')

        # Заголовок
        title_label = tk.Label(master, text="Главное меню", bg='#A49FB1', font=("Arial", 24, "bold"))
        title_label.pack(pady=20)

        # Фрейм для кнопок
        self.buttons_frame = tk.Frame(master, bg='white', bd=10, relief='ridge')
        self.buttons_frame.pack(pady=50, padx=50)

        # Кнопки разделов
        self.create_buttons()

        # Нижние кнопки
        self.bottom_frame = tk.Frame(master, bg='#A49FB1')
        self.bottom_frame.pack(side='bottom', fill='x', padx=20, pady=10)

        # Кнопки аккаунта
        self.create_account_buttons()

    def create_buttons(self):
        self.prod_button = tk.Button(self.buttons_frame, text="Продукция", command=lambda: self.open_section("Продукция"), width=20, height=2, bg='#D6D5DF')
        self.prod_button.grid(row=0, column=0, padx=30, pady=20)

        self.equip_button = tk.Button(self.buttons_frame, text="Оборудование", command=lambda: self.open_section("Оборудование"), width=20, height=2, bg='black', fg='white')
        self.equip_button.grid(row=0, column=1, padx=30, pady=20)

        self.staff_button = tk.Button(self.buttons_frame, text="Сотрудники", command=lambda: self.open_section("Сотрудники"), width=20, height=2, bg='#D6D5DF')
        self.staff_button.grid(row=0, column=2, padx=30, pady=20)

    def create_account_buttons(self):
        self.account_button = tk.Button(self.bottom_frame, text="👤 Мой аккаунт", command=self.my_account, bg='#A49FB1', borderwidth=0)
        self.account_button.pack(side='left')

        self.logout_button = tk.Button(self.bottom_frame, text="⮐ Выйти", command=self.logout, bg='#A49FB1', borderwidth=0)
        self.logout_button.pack(side='right')

    def open_section(self, section):
        print(f"Открыт раздел: {section}")

    def my_account(self):
        print("Мой аккаунт")

    def logout(self):
        print("Выход из системы")
        self.master.destroy()  # Закрываем главное окно приложения