import os

class ProfileModel:
    def __init__(self, username):
        self.username = username
        self.data = self.load_user_data()

    def load_user_data(self):
        user_data = {}
        base_dir = os.path.dirname(os.path.abspath(__file__))  # Директория текущего файла
        file_path = os.path.join(base_dir, '..', 'registrations.txt')  # Поднимаемся на уровень выше

        if not os.path.exists(file_path):
            print(f"Файл {file_path} не найден!")
            return user_data

        # Читаем файл
        try:
            with open(file_path, 'r', encoding='utf-8') as file:
                lines = iter(file.readlines())
                for line in lines:
                    if f"Логин: {self.username}" in line:
                        user_data["login"] = self.username
                        user_data["fio"] = next(lines).strip().split(": ")[1]
                        user_data["birth_date"] = next(lines).strip().split(": ")[1]
                        user_data["phone_number"] = next(lines).strip().split(": ")[1]
                        user_data["position"] = next(lines).strip().split(": ")[1]
                        user_data["worker_type"] = next(lines).strip().split(": ")[1]
                        user_data["status"] = "На смене"
                        break
        except Exception as e:
            print(f"Ошибка при чтении файла: {e}")
        
        print(f"Загруженные данные: {user_data}")
        return user_data
