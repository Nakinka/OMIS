from model.profile_model import ProfileModel
from view.profile_view import UserProfileView
import tkinter as tk

class ProfileController:
    def __init__(self, master, username):
        self.model = ProfileModel(username)
        print(f"Данные для View: {self.model.data}")
        self.view = UserProfileView(master, self.model.data, self.go_back)

    def go_back(self):
        self.view.master.destroy()  # Закрываем окно профиля