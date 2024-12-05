class EmployeeModel:
    def __init__(self):
        self.employees = []  # Изначально список сотрудников пуст

    def get_all_employees(self):
        """Получить всех сотрудников"""
        return self.employees

    def add_employee(self, name, position, hire_date):
        """Добавить нового сотрудника"""
        new_id = len(self.employees) + 1
        self.employees.append({"id": new_id, "name": name, "position": position, "hire_date": hire_date})

    def delete_employee(self, employee_id):
        """Удалить сотрудника по ID"""
        self.employees = [e for e in self.employees if e["id"] != employee_id]
