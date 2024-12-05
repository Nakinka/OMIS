import tkinter as tk
from tkinter import ttk, messagebox

class ProductView:
    def __init__(self, master, controller):
        self.master = master
        self.controller = controller
        self.master.title("Продукция")
        self.master.geometry("934x536")
        self.master.configure(bg="#A49FB1")

        # Заголовок
        title_label = tk.Label(master, text="Продукция", bg="#A49FB1", fg="black", font=("Arial", 24, "bold"))
        title_label.pack(pady=10)

        # Дерево для отображения продукции
        self.tree = ttk.Treeview(master, columns=("ID", "Тип", "Номер", "Дата"), show="headings")
        self.tree.heading("ID", text="ID")
        self.tree.heading("Тип", text="Тип")
        self.tree.heading("Номер", text="Номер")
        self.tree.heading("Дата", text="Дата")
        self.tree.column("ID", width=50, anchor="center")
        self.tree.column("Тип", width=200, anchor="w")
        self.tree.column("Номер", width=150, anchor="center")
        self.tree.column("Дата", width=150, anchor="center")
        self.tree.pack(fill=tk.BOTH, expand=True, pady=10)

        # Панель кнопок
        button_frame = tk.Frame(master, bg="#A49FB1")
        button_frame.pack(fill=tk.X, pady=5)

        add_button = tk.Button(button_frame, text="Добавить", command=self.open_add_window, bg="#D6D5DF", font=("Arial", 12))
        add_button.pack(side=tk.RIGHT, padx=10)

        back_button = tk.Button(button_frame, text="← Назад", command=self.controller.go_back, bg="#D6D5DF", font=("Arial", 12))
        back_button.pack(side=tk.LEFT, padx=10)

    def update_product_list(self, products):
        """Обновить список продукции в дереве."""
        for row in self.tree.get_children():
            self.tree.delete(row)
        for product in products:
            self.tree.insert("", tk.END, values=(product["id"], product["kind"], product["number"], product["date"]))

    def get_selected_product_id(self):
        """Получить ID выбранного продукта."""
        selected_item = self.tree.selection()
        if selected_item:
            return int(self.tree.item(selected_item[0], "values")[0])
        return None

    def open_add_window(self):
        """Открыть окно для добавления нового продукта."""
        def save_product():
            kind = kind_entry.get()
            number = number_entry.get()
            date = date_entry.get()
            self.controller.add_product(kind, number, date)
            add_window.destroy()

        add_window = tk.Toplevel(self.master)
        add_window.title("Добавить продукт")
        add_window.geometry("300x200")

        tk.Label(add_window, text="Тип:").pack(pady=5)
        kind_entry = tk.Entry(add_window)
        kind_entry.pack(pady=5)

        tk.Label(add_window, text="Номер:").pack(pady=5)
        number_entry = tk.Entry(add_window)
        number_entry.pack(pady=5)

        tk.Label(add_window, text="Дата (ГГГГ-ММ-ДД):").pack(pady=5)
        date_entry = tk.Entry(add_window)
        date_entry.pack(pady=5)

        tk.Button(add_window, text="Сохранить", command=save_product).pack(pady=10)
