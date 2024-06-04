from data_create import name_data, surname_data, phone_data, address_data
def delete_data():
    file_to_update = input("Введите имя файла для удаления данных (sprav1.csv или sprav2.csv): ")
    field_to_delete = input("Введите поле для удаления (имя, фамилия, номер телефона, адрес): ")
    value_to_delete = input(f"Введите {field_to_delete} для удаления: ")
    with open(file_to_update, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    found = False
    with open(file_to_update, 'w', encoding='utf-8') as f:
        for line in lines:
            if value_to_delete in line:
                found = True
            else:
                f.write(line)
    if not found:
        print(f"{field_to_delete} не найден в файле.")
# delete_data()
def update_data():
    file_to_update = input("Введите имя файла для обновления данных (sprav1.csv или sprav2.csv): ")
    field_to_update = input("Введите поле для обновления (имя, фамилия, номер телефона, адрес): ")
    value_to_update = input(f"Введите {field_to_update} для обновления: ")
    new_lines = []
    with open(file_to_update, 'r', encoding='utf-8') as f:
        lines = f.readlines()
        for line in lines:
            if value_to_update in line:
                print("Введите новые данные:")
                new_value = input(f"Новый {field_to_update}: ")
                new_lines.append(line.replace(value_to_update, new_value))
            else:
                new_lines.append(line)
    with open(file_to_update, 'w', encoding='utf-8') as f:
        for line in new_lines:
            f.write(line)

update_data()
