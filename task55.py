def work_with_phonebook():

    choice = show_menu()

    phone_book = read_csv('phonebook.csv')

    while (choice <= 6):
        if choice == 1:
            print_result(phone_book)
        elif choice == 2:
            last_name = input('Фамилия: ')
            print(find_by_lastname(phone_book, last_name))
        elif choice == 3:
            last_name = input('Фамилия: ')
            new_number = input('Новый номер: ')
            change_number(phone_book, last_name, new_number)
        elif choice == 4:
            lastname = input('Фамилия: ')
            delete_by_lastname(phone_book, lastname)
        elif choice == 5:
            number = input('Номер: ')
            print(find_by_number(phone_book, number))
        elif choice == 6:
            print('Новый контакт: ')
            add_user(phone_book)
            write_csv('phonebook.csv', phone_book)

        choice = show_menu()


def show_menu():
    print('1. Распечатать справочник ',
          '2. Найти телефон по фамилии ',
          '3. Изменить номер телефона ',
          '4. Удалить запись ',
          '5. Найти абонента по номеру телефона ',
          '6. Добавить абонента в справочник ',
          '7. Закончить работу', sep='\n')
    choice = int(input("Введите команду: "))
    return choice


def read_csv(filename):

    phone_book = []

    fields = ['Фамилия', 'Имя', 'Телефон', 'Описание']

    with open(filename, 'r', encoding='utf-8') as phb:
        for line in phb:
            record = dict(zip(fields, line.split(',')))
            phone_book.append(record)
    return phone_book


def write_csv(filename, phone_book):

    with open('phonebook.csv', 'w', encoding='utf-8') as phout:
        for i in range(len(phone_book)):
            s = ''
            for v in phone_book[i].values():
                s += v+','
            phout.write(f'{s[:-1]}\n')

#################################################################### сами функции:
def print_result(phone_book):
    for line in phone_book:
        print(line)


def find_by_lastname(phone_book, last_name):
    lastname = ""
    for line in phone_book:
        if line['Фамилия'] == last_name:
            lastname = line['Фамилия'] + " - " + line["Телефон"]
    return lastname    
    

def change_number(phone_book, last_name, new_number):
    for line in phone_book:
        if line['Фамилия'] == last_name:
            line.update(Телефон=new_number)
        write_csv("phonebook.csv", phone_book)
    return(print("Номер успешно изменен\n"))        


def delete_by_lastname(phone_book, last_name):
    for line in phone_book:
        if line['Фамилия'] == last_name:
            line.clear()
    write_csv("phonebook.csv", phone_book)
    return print("Запись удалена\n")


def find_by_number(phone_book, number):
    string = ''
    for line in phone_book:
        if line['Телефон'] == number:
            string = line['Фамилия'] + ' ' + line['Имя'] + ', описание: ' + line['Описание']
    return string


def add_user(phone_book):
    lastname = input("Фамилия: ")
    name = input("Имя: ")
    number = input('Номер телефона: ')
    description = input('Описание: ')
    newUser = {'Фамилия': lastname,'Имя': name, 'Телефон': number,'Описание': description}
    phone_book.append(newUser)
    print('Новый контакт успешно добавлен\n')

work_with_phonebook()
