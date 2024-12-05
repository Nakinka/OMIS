import tkinter as tk
from tkinter import messagebox
from model.equipment_model import EquipmentModel
from view.equipment_view import EquipmentView


class EquipmentController:
    def __init__(self, master):
        self.model = EquipmentModel()
        self.view = EquipmentView(master, self)
        self.update_view()

    def update_view(self):
        equipment = self.model.get_all_equipment()
        self.view.update_equipment_list(equipment)

    def add_equipment(self):
        def save_equipment():
            equip_type = type_entry.get()
            number = number_entry.get()
            date = date_entry.get()
            if not equip_type or not number or not date:
                messagebox.showwarning("Ошибка", "Все поля должны быть заполнены!")
                return
            self.model.add_equipment(equip_type, number, date)
            self.update_view()
            add_window.destroy()

        add_window = tk.Toplevel(self.view.master)
        add_window.title("Добавить оборудование")
        add_window.geometry("300x200")

        tk.Label(add_window, text="Вид:").pack(pady=5)
        type_entry = tk.Entry(add_window)
        type_entry.pack(pady=5)

        tk.Label(add_window, text="Номер:").pack(pady=5)
        number_entry = tk.Entry(add_window)
        number_entry.pack(pady=5)

        tk.Label(add_window, text="Дата добавления (ГГГГ-ММ-ДД):").pack(pady=5)
        date_entry = tk.Entry(add_window)
        date_entry.pack(pady=5)

        tk.Button(add_window, text="Сохранить", command=save_equipment).pack(pady=10)

    def go_back(self):
        self.view.master.destroy()


if __name__ == "__main__":
    root = tk.Tk()
    app = EquipmentController(root)
    root.mainloop()
