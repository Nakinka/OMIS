from controller.login_controller import LoginController
import tkinter as tk

if __name__ == "__main__":
    root = tk.Tk()
    app = LoginController(root)
    root.mainloop()