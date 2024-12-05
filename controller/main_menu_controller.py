# controller/main_menu_controller.py
from view.main_menu_view import MainMenuView
from controller.profile_controller import ProfileController
from controller.product_controller import ProductController
from controller.equipment_controller import EquipmentController
from controller.employee_controller import EmployeeController
import tkinter as tk

class MainMenuController:
    def __init__(self, master, username):
        self.view = MainMenuView(master)
        self.username = username
        self.view.account_button.config(command=self.open_profile) 
        self.view.prod_button.config(command=self.open_product)
        self.view.equip_button.config(command=self.open_equip)
        self.view.staff_button.config(command=self.open_employ)

    def open_profile(self):
        profile_root = tk.Toplevel(self.view.master)  
        profile_app = ProfileController(profile_root, self.username)  

    def open_product(self):
        product_root = tk.Toplevel(self.view.master)  
        ProductController(product_root) 

    def open_equip(self):
        equip_root = tk.Toplevel(self.view.master)
        EquipmentController(equip_root)

    def open_employ(self):
        empoy_root = tk.Toplevel(self.view.master)
        EmployeeController(empoy_root)

        

    def show(self):
        self.view.master.deiconify() 