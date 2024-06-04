from data_create import name_data, surname_data, phone_data, address_data
def input_data():
    name = name_data()
    surname = surname_data()
    phone = phone_data()
    address = address_data()
    var = int (input(f" Вкаком формате записать данные " 
    f"1 Вариант:  "
    f"{name} \n {surname} \n {phone} \n {address}\n"
    f"2 Вариант: \n"
    f"{name};{surname};{phone};{address}\n\n"
    f"Выберите вариант: "))
    while var !=2 and var != 1:
        print("неправильный ввод")
        var = int(input("Введите число: "))
    if var == 1:
        with open('sprav1.csv', 'a', encoding='utf-8') as f:
            f.write(f" {name} \n {surname} \n {phone} \n {address}")
    elif var == 2:
        with open('sprav2.csv', 'a',encoding='utf-8') as f:
            f.write(f" {name};{surname};{phone};{address}\n\n")

def print_data():
    print('Вывожу данные из 1 файла : \n')
    with open('sprav1.csv', 'r', encoding='utf-8') as f:
        data_first =f.readlines()
        data_first_list=[]
        j=0
        for i in range(len(data_first)):
            if data_first[i]=="\n"or i == len(data_first)-1:
                data_first_list.append(''.join(data_first[j:i+1]))
                j=1+i
        print(''.join(data_first_list))
    print('Вывожу данные из 2 файла : \n')
    with open('sprav2.csv', 'r', encoding='utf-8') as f:
        data_second = f.readlines()
        print(*data_second)
# print_data()


 
