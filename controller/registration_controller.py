from model.registration_model import RegistrationModel
from view.registration_view import RegistrationView
import tkinter as tk

class RegistrationController:
    def __init__(self, master, on_registered):
        self.model = RegistrationModel()
        self.view = RegistrationView(master)
        self.view.set_register_command(self.register)
        self.on_registered = on_registered  # Сохраняем ссылку на функцию для обработки события регистрации

    def register(self):
        data = self.view.get_registration_data()
        self.model.save_registration(
            data["fio"],
            data["birth_date"],
            data["phone_number"],
            data["position"],
            data["worker_type"],
            data["login"],
            data["password"]
        )
        print("Регистрация завершена. Данные сохранены.")
        self.view.master.destroy()  # Закрываем окно регистрации
        self.on_registered()  # Вызываем функцию, переданную при инициализации

    def clear_form(self):
        self.view.fio_entry.delete(0, tk.END)
        self.view.birth_date_entry.delete(0, tk.END)
        self.view.phone_number_entry.delete(0, tk.END)
        self.view.position_entry.delete(0, tk.END)
        self.view.worker_type_var.set('')
        self.view.login_entry.delete(0, tk.END)
        self.view.password_entry.delete(0, tk.END)