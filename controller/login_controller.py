from controller.main_menu_controller import MainMenuController
from controller.registration_controller import RegistrationController
from model.login_model import LoginModel
from view.login_view import LoginView
import tkinter as tk

class LoginController:
    def __init__(self, master):
        self.model = LoginModel()
        self.view = LoginView(master)
        self.view.set_login_command(self.login)
        self.view.set_register_command(self.show_registration)

    def login(self):
        username = self.view.get_username()
        password = self.view.get_password()
        
        
        self.model.authenticate(username, password)
        # Если авторизация успешна, открываем главное меню
        self.open_main_menu()

    def open_main_menu(self):
        self.view.master.withdraw()  # Скрываем окно авторизации
        main_menu_root = tk.Toplevel(self.view.master)
        main_menu_app = MainMenuController(main_menu_root, self.view.get_username())

    def show_registration(self):
        self.view.master.withdraw()  # Скрываем окно авторизации
        registration_root = tk.Toplevel(self.view.master)
        
        # Передаем метод open_login для обработки регистрации
        registration_app = RegistrationController(registration_root, self.open_login)

    def open_login(self):
        # Открываем окно авторизации
        login_root = tk.Toplevel()  # Создаем новое окно
        login_app = LoginController(login_root)


        