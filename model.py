import controller

phone_book = []
search_phone_book = []
path = 'phone_book.txt'


def get_phone_book():
    global phone_book
    return phone_book


def open_file(path):
    global phone_book

    with open(path, 'r', encoding='UTF-8') as file:
        data = file.readlines()
        for item in data:
            contact = item.replace('\n', '').split(';')
            phone_book.append(contact)


def new_contact(contact):
    global phone_book
    phone_book.append(list(contact))


def chage_contact(id, choice, value):
    global phone_book
    phone_book[int(id)][int(choice)] = value


def delete_contact(id):
    global phone_book
    phone_book.pop(int(id))


def search_contact(id, value):
    global phone_book
    global search_phone_book
    for item in phone_book:
        if item[int(id)] == value:
            search_phone_book.append(item)


def get_search_phone_book():
    global search_phone_book
    return search_phone_book


def record_file(path):
    global phone_book

    with open(path, 'w', encoding='UTF-8') as file:
        file.write(str(phone_book))
