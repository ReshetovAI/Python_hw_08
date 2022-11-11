from random import choice
from unittest import mock
import view
import model


def start():
    choice = 1
    while choice != 9:
        choice = view.show_menu()
        match(choice):
            case 0:
                phone_book = model.get_phone_book()
                view.show_phone_book(phone_book)
            case 1:
                path = view.input_path()
                model.open_file(path)
            case 2:
                path = view.input_path_record()
                model.record_file(path)
            case 3:
                contact = view.input_contact()
                model.new_contact(contact)
            case 4:
                contact = view.input_change()
                model.chage_contact(*contact)
            case 5:
                id = view.input_delete()
                model.delete_contact(id)
            case 6:
                my_search = view.input_search()
                model.search_contact(*my_search)
                search_phone_book = model.get_search_phone_book()
                view.show_search_phone_book(search_phone_book)
