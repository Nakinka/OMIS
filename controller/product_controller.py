import tkinter as tk
from tkinter import messagebox
from view.product_view import ProductView
from model.product_model import ProductModel

class ProductController:
    def __init__(self, master):
        self.model = ProductModel()
        self.view = ProductView(master, self)
        self.update_view()

    def update_view(self):
        products = self.model.get_all_products()
        self.view.update_product_list(products)

    def add_product(self):
        def save_product():
            name = name_entry.get()
            product_type = type_entry.get()
            date = date_entry.get()
            if not product_type or not name:
                messagebox.showwarning("Ошибка", "Все поля должны быть заполнены!")
                return
            self.model.add_product(name, product_type, date)
            self.update_view()
            add_window.destroy()

        add_window = tk.Toplevel(self.view.master)
        add_window.title("Добавить продукт")
        add_window.geometry("300x200")

        tk.Label(add_window, text="Название:").pack(pady=5)
        name_entry = tk.Entry(add_window)
        name_entry.pack(pady=5)

        tk.Label(add_window, text="Тип:").pack(pady=5)
        type_entry = tk.Entry(add_window)
        type_entry.pack(pady=5)

        tk.Label(add_window, text="Дата (ГГГГ-ММ-ДД):").pack(pady=5)
        date_entry = tk.Entry(add_window)
        date_entry.pack(pady=5)

        tk.Button(add_window, text="Сохранить", command=save_product).pack(pady=10)

    def go_back(self):
        self.view.master.destroy()