import json
import os

# Функция для загрузки данных из файла
def load_data(file_name):
    if os.path.exists(file_name):
        with open(file_name, 'r') as file:
            data = json.load(file)
    else:
        data = {}
    return data

# Функция для сохранения данных в файл
def save_data(file_name, data):
    with open(file_name, 'w') as file:
        json.dump(data, file)

# Функция для добавления нового контакта
def add_contact(data):
    name = input("Введите имя: ")
    number = input("Введите номер телефона: ")
    # Получаем текущее значение ID и увеличиваем его на 1
    current_id = len(data) + 1
    data[current_id] = {"name": name, "phone": number}
    save_data("contacts.json", data)
    print("Контакт успешно добавлен.")

# Функция для просмотра всех контактов
def view_contacts(data):
    if data:
        print("Список контактов:")
        for contact_id, contact_info in data.items():
            print(f"ID: {contact_id}, Имя: {contact_info['name']}, Телефон: {contact_info['phone']}")
    else:
        print("Список контактов пуст.")

# Функция для поиска контакта по имени или ID
def search_contact(data):
    search_key = input("Введите имя или ID контакта для поиска: ")
    for contact_id, contact_info in data.items():
        if search_key.lower() == contact_info['name'].lower() or search_key == str(contact_id):
            print(f"ID: {contact_id}, Имя: {contact_info['name']}, Телефон: {contact_info['phone']}")
            return
    print("Контакт не найден.")

# Функция для удаления контакта
def delete_contact(data):
    search_key = input("Введите имя или ID контакта для удаления: ")
    found = False
    for contact_id, contact_info in list(data.items()):
        if search_key.lower() == contact_info['name'].lower() or search_key == str(contact_id):
            del data[contact_id]
            print("Контакт успешно удален.")
            found = True
            break
    if not found:
        print("Контакт не найден.")

    # Обновляем идентификаторы всех ниже стоящих контактов
    updated_data = {}
    for idx, (contact_id, contact_info) in enumerate(data.items(), start=1):
        updated_data[idx] = contact_info

    # Перезаписываем данные с обновленными идентификаторами
    save_data("contacts.json", updated_data)





# Функция для редактирования контакта
def edit_contact(data):
    search_key = input("Введите имя или ID контакта для редактирования: ")
    for contact_id, contact_info in data.items():
        if search_key.lower() == contact_info['name'].lower() or search_key == str(contact_id):
            new_name = input("Введите новое имя (или оставьте пустым для сохранения текущего): ")
            if new_name:
                contact_info['name'] = new_name
            new_number = input("Введите новый номер телефона (или оставьте пустым для сохранения текущего): ")
            if new_number:
                contact_info['phone'] = new_number
            save_data("contacts.json", data)
            print("Контакт успешно отредактирован.")
            return
    print("Контакт не найден.")

# Функция для импорта контактов из другого файла JSON
def import_contacts(data):
    file_name_to_import = input("Введите имя файла, откуда вы хотите импортировать контакты: ")
    imported_data = load_data(file_name_to_import)
    if imported_data:
        print("Доступные контакты для импорта:")
        for contact_id, contact_info in imported_data.items():
            print(f"ID: {contact_id}, Имя: {contact_info['name']}, Телефон: {contact_info['phone']}")
        file_name_to_export = input("Введите имя файла, куда вы хотите импортировать контакты: ")
        confirm = input(f"Вы уверены, что хотите импортировать контакты в файл '{file_name_to_export}'? (да/нет): ")
        if confirm.lower() == 'да':
            start_id = len(data) + 1  # Начальное значение ID для импортированных контактов
            for contact_id, contact_info in imported_data.items():
                # Проверяем, что такого контакта нет уже в текущем справочнике
                contact_exists = False
                for existing_id, existing_info in data.items():
                    if existing_info == contact_info:
                        contact_exists = True
                        break
                if not contact_exists:
                    current_id = start_id
                    while current_id in data:  # Проверяем, чтобы ID был уникальным
                        current_id += 1
                    data[current_id] = contact_info
                    start_id = current_id + 1  # Увеличиваем начальное значение ID для следующего импорта
            save_data(file_name_to_export, data)
            print("Контакты успешно импортированы.")
    else:
        print("Невозможно импортировать контакты из файла.")

# Основная функция для работы с телефонным справочником
def main():
    def data_choise():
        ch1 = input("Введите имя файла с которым хотите работать: ")
        data = load_data(f"{ch1}")
        return data

    data = data_choise()
    while True:
        print("\nМеню:")
        print("1. Добавить контакт")
        print("2. Просмотреть все контакты")
        print("3. Найти контакт по имени или ID")
        print("4. Удалить контакт")
        print("5. Редактировать контакт")
        print("6. Импортировать контакты")
        print("7. Выйти из программы")
        print("8. Сменить файл")

        choice = input("Выберите действие: ")
        
        if choice == '1':
            add_contact(data)
        elif choice == '2':
            view_contacts(data)
        elif choice == '3':
            search_contact(data)
        elif choice == '4':
            delete_contact(data)
        elif choice == '5':
            edit_contact(data)
        elif choice == '6':
            import_contacts(data)
        elif choice == '7':
            print("До свидания!")
            break
        elif choice == '8':
            data = data_choise()
        else:
            print("Неверный выбор. Пожалуйста, выберите действие из списка.")

if __name__ == "__main__":
    main()

