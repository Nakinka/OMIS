import tkinter as tk
from tkinter import ttk, messagebox

class EmployeeView:
    def __init__(self, master, controller):
        self.master = master
        self.controller = controller
        self.master.title("Сотрудники")
        self.master.geometry("934x536")
        self.master.configure(bg="#A49FB1")

        # Заголовок
        title_label = tk.Label(master, text="Сотрудники", bg="#A49FB1", fg="black", font=("Arial", 24, "bold"))
        title_label.pack(pady=10)

        # Дерево для отображения сотрудников
        self.tree = ttk.Treeview(master, columns=("ID", "Ф.И.О.", "Должность", "Статус"), show="headings")
        self.tree.heading("ID", text="ID")
        self.tree.heading("Ф.И.О.", text="Ф.И.О.")
        self.tree.heading("Должность", text="Должность")
        self.tree.heading("Статус", text="Статус")
        self.tree.column("ID", width=50, anchor="center")
        self.tree.column("Ф.И.О.", width=200, anchor="w")
        self.tree.column("Должность", width=150, anchor="w")
        self.tree.column("Статус", width=100, anchor="center")
        self.tree.pack(fill=tk.BOTH, expand=True, pady=10)

        # Панель кнопок
        button_frame = tk.Frame(master, bg="#A49FB1")
        button_frame.pack(fill=tk.X, pady=5)

        add_button = tk.Button(button_frame, text="Добавить", command=self.open_add_window, bg="#D6D5DF", font=("Arial", 12))
        add_button.pack(side=tk.RIGHT, padx=10)

        back_button = tk.Button(button_frame, text="← Назад", command=self.controller.go_back, bg="#D6D5DF", font=("Arial", 12))
        back_button.pack(side=tk.LEFT, padx=10)

    def update_employee_list(self, employees):
        """Обновить список сотрудников в дереве."""
        for row in self.tree.get_children():
            self.tree.delete(row)
        for employee in employees:
            self.tree.insert("", tk.END, values=(employee["id"], employee["name"], employee["position"], employee["status"]))

    def get_selected_employee_id(self):
        """Получить ID выбранного сотрудника."""
        selected_item = self.tree.selection()
        if selected_item:
            return int(self.tree.item(selected_item[0], "values")[0])
        return None

    def open_add_window(self):
        """Открыть окно для добавления нового сотрудника."""
        def save_employee():
            name = name_entry.get()
            position = position_entry.get()
            status = status_entry.get()
            self.controller.add_employee(name, position, status)
            add_window.destroy()

        add_window = tk.Toplevel(self.master)
        add_window.title("Добавить сотрудника")
        add_window.geometry("300x200")

        tk.Label(add_window, text="Ф.И.О.:").pack(pady=5)
        name_entry = tk.Entry(add_window)
        name_entry.pack(pady=5)

        tk.Label(add_window, text="Должность:").pack(pady=5)
        position_entry = tk.Entry(add_window)
        position_entry.pack(pady=5)

        tk.Label(add_window, text="Статус:").pack(pady=5)
        status_entry = tk.Entry(add_window)
        status_entry.pack(pady=5)

        tk.Button(add_window, text="Сохранить", command=save_employee).pack(pady=10)
