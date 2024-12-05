class RegistrationModel:
    def save_registration(self, fio, birth_date, phone_number, position, worker_type, login, password):
        with open('registrations.txt', 'a') as file:
            file.write(f"ФИО: {fio}\n")
            file.write(f"Дата рождения: {birth_date}\n")
            file.write(f"Номер телефона: {phone_number}\n")
            file.write(f"Должность: {position}\n")
            file.write(f"Тип работника: {worker_type}\n")
            file.write(f"Логин: {login}\n")
            file.write(f"Пароль: {password}\n")
            file.write("-" * 40 + "\n")  # Разделитель между записями