import tkinter as tk
from tkinter import messagebox, ttk

class UserProfileView:
    def __init__(self, master, user_data, go_back):
        self.master = master
        self.master.title("Мой профиль")
        self.master.geometry("934x536")
        self.master.configure(bg='#A49FB1')

        # Заголовок
        title_label = tk.Label(master, text="Мой профиль", bg='#A49FB1', font=("Arial", 24, "bold"))
        title_label.pack(pady=10)

        # Кнопка назад
        back_button = tk.Button(master, text="← Назад", command=go_back, bg='#A49FB1', borderwidth=0, font=("Arial", 12))
        back_button.place(x=10, y=10)

        # Фрейм для отображения информации
        self.info_frame = tk.Frame(master, bg='white', bd=8, relief='ridge')
        self.info_frame.pack(pady=20, padx=20, fill='both', expand=True)

        self.populate_user_info(user_data)

        # Кнопка "Смотреть историю действий"
        action_history_button = tk.Button(master, text="Смотреть историю действий", 
                                          command=self.show_action_history, 
                                          bg="black", fg="white", font=("Arial", 12))
        action_history_button.pack(pady=10)

    def populate_user_info(self, user_data):
        labels = [
            "ФИО", "Дата рождения", "Номер телефона", 
            "Логин", "Пароль", "Тип работника", 
            "Должность", "Статус"
        ]

        for i, label_text in enumerate(labels):
            label = tk.Label(self.info_frame, text=label_text, bg='white', font=("Arial", 12), anchor='w')
            label.grid(row=i, column=0, sticky='w', padx=10, pady=5)

            entry = tk.Entry(self.info_frame, font=("Arial", 12))
            entry.grid(row=i, column=1, padx=10, pady=5)

            # Заполнить поля данными из user_data
            entry.insert(0, user_data.get(label_text.lower(), ""))

            if label_text == "Статус":
                entry.destroy()  # Убрать Entry
                status_var = tk.StringVar()
                status_var.set(user_data.get("status", "Нет на смене"))
                status_menu = tk.OptionMenu(self.info_frame, status_var, 
                                            "На смене", "Нет на смене", "Обед", "Перерыв")
                status_menu.grid(row=i, column=1, padx=10, pady=5, sticky='w')

    def show_action_history(self):
        history_window = tk.Toplevel(self.master)
        history_window.title("История действий")
        history_window.geometry("800x400")
        history_window.configure(bg='#D3D3D3')

        # Заголовок окна
        title_label = tk.Label(history_window, text="История действий", bg='#D3D3D3', font=("Arial", 20, "bold"))
        title_label.pack(pady=10)

        # Таблица с историей действий
        columns = ("Действие", "Тип объекта", "Вид", "Номер", "Дата")
        tree = ttk.Treeview(history_window, columns=columns, show="headings")

        # Определение заголовков таблицы
        for col in columns:
            tree.heading(col, text=col)
            tree.column(col, anchor='center', width=150)


        # Прокрутка для таблицы
        scrollbar = ttk.Scrollbar(history_window, orient=tk.VERTICAL, command=tree.yview)
        tree.configure(yscroll=scrollbar.set)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        
        tree.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

