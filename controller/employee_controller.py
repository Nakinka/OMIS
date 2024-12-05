import tkinter as tk
from tkinter import messagebox
from view.employee_view import EmployeeView
from model.employee_model import EmployeeModel

class EmployeeController:
    def __init__(self, master):
        self.model = EmployeeModel()
        self.view = EmployeeView(master, self)
        self.update_view()

    def update_view(self):
        employees = self.model.get_all_employees()
        self.view.update_employee_list(employees)

    def add_employee(self, name, position, status):
        self.model.add_employee(name, position, status)
        self.update_view()

    def delete_employee(self):
        employee_id = self.view.get_selected_employee_id()
        if employee_id is not None:
            self.model.delete_employee(employee_id)
            self.update_view()
        else:
            messagebox.showwarning("Ошибка", "Выберите сотрудника для удаления")

    def go_back(self):
        self.master.destroy()  

