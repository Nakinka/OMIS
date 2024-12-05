import tkinter as tk
from tkinter import ttk, messagebox

class EquipmentView:
    def __init__(self, master, controller):
        self.master = master
        self.controller = controller
        self.master.title("Оборудование")
        self.master.geometry("934x536")
        self.master.configure(bg="#A49FB1")

       
        title_label = tk.Label(master, text="Оборудование", bg="#A49FB1", fg="black", font=("Arial", 24, "bold"))
        title_label.pack(pady=10)

       
        self.tree = ttk.Treeview(master, columns=("ID", "Вид", "Номер", "Дата добавления"), show="headings")
        self.tree.heading("ID", text="ID")
        self.tree.heading("Вид", text="Вид")
        self.tree.heading("Номер", text="Номер")
        self.tree.heading("Дата добавления", text="Дата добавления")
        self.tree.column("ID", width=50, anchor="center")
        self.tree.column("Вид", width=200, anchor="w")
        self.tree.column("Номер", width=150, anchor="center")
        self.tree.column("Дата добавления", width=150, anchor="center")
        self.tree.pack(fill=tk.BOTH, expand=True, pady=10)

        
        button_frame = tk.Frame(master, bg="#A49FB1")
        button_frame.pack(fill=tk.X, pady=5)

        add_button = tk.Button(button_frame, text="Добавить", command=self.controller.add_equipment, bg="#D6D5DF", font=("Arial", 12))
        add_button.pack(side=tk.RIGHT, padx=10)

        back_button = tk.Button(button_frame, text="← Назад", command=self.controller.go_back, bg="#D6D5DF", font=("Arial", 12))
        back_button.pack(side=tk.LEFT, padx=10)

    def update_equipment_list(self, equipment):
        for row in self.tree.get_children():
            self.tree.delete(row)
        for equip in equipment:
            self.tree.insert("", tk.END, values=(equip["id"], equip["type"], equip["number"], equip["date"]))

    def get_selected_equipment_id(self):
        selected_item = self.tree.selection()
        if selected_item:
            return int(self.tree.item(selected_item[0], "values")[0])
        return None
