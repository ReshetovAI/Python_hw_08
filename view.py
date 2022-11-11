from re import I
from secrets import choice


def show_menu():
    print('0. Показать все контакты')
    print('1. Открыть файл с контактами')
    print('2. Записать файл с контактами')
    print('3. Добавить контакт')
    print('4. Изменить контакт')
    print('5. Удалить контакт')
    print('6. Поиск по контактам')

    choice = int(input('Выберите пункт меню: '))
    return choice


def show_phone_book(phone_book):
    if len(phone_book) < 1:
        print('Телефонная книга пуста')
    else:
        for id, item in enumerate(phone_book):
            print(id, *item)


def input_path():
    path = input('Введите имя файла: ')
    return path


def input_contact():
    name_contact = input('Введите ФИО: ')
    phone_contact = input('Введите номер телефона: ')
    comment = input('Введите коментарий: ')


def input_change():
    id = input('Введите номер контакта: ')
    print('Что изменить?')
    choice = input(' 0- ФИО, 1 - Телефон, 2 - Комментарий, 3 - Отмена')
    value = input(' Введите изменение: ')
    return (id, choice, value)


def input_delete():
    id = input('Введите номер удаляемого контакта: ')
    return (id)


def input_search():
    print('Введите параметр для поиска:')
    id = input('0- ФИО, 1 - Телефон, 2 - Комментарий, 3 - Отмена')
    value = input(' Введите значение для поиска: ')
    return (id, value)


def show_search_phone_book(search_phone_book):
    if len(search_phone_book) < 1:
        print('Значение не найдено')
    else:
        for id, item in enumerate(search_phone_book):
            print(id, *item)


def input_path_record():
    path = input('Введите имя файла для записи: ')
    return path
