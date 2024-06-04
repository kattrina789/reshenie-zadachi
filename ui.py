from logger import input_data, print_data

def interface():
    print("Добрый день: \n 1- запись данных \n 2 - вывод данных")
    command = int(input("Введите число: "))
    while command !=2 and command != 1:
        print("неправильный ввод")
        command = int(input("Введите число: "))
    if command == 1:
        input_data()
    elif command ==2:
        print_data()
        