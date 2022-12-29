from collections import UserList, UserDict




class Field:
    """Класс Field, который 
    будет родительским для всех полей, 
    в нем потом 
    реализуем логику общую для всех полей."""
    pass


class Name:

    def __init__(self, name):
        self.name = name
    pass


class Phone:
    """Класс Phone, 
    необязательное поле 
    с телефоном и таких одна запись (Record) может содержать несколько."""

    def __init__(self, phone):
        self.phone = phone
    pass


class Record(UserDict, Name, Phone):
    """Класс Record, который 
    отвечает за логику добавления/удаления/редактирования 
    необязательных полей 
    и хранения обязательного поля Name

    Record хранит объект Name в отдельном атрибуте.

    Record хранит список объектов Phone в отдельном атрибуте.

    Record реализует методы для добавления/удаления/редактирования объектов Phone."""
 
    pass


class AddressBook:
    """Записи Record в AddressBook хранятся как значения в словаре. 
    В качестве ключей используется 
    значение Record.name.value
    
    AddressBook реализует метод add_record, 
    который добавляет Record в self.data."""

    def add_record(self):
        pass

#-----------------------------------------------------

if __name__ == '__main__':
    name = Name('Bill')
    phone = Phone('1234567890')
    rec = Record(name, phone)
    ab = AddressBook()
    ab.add_record(rec)
    
    assert isinstance(ab['Bill'], Record)
    assert isinstance(ab['Bill'].name, Name)
    assert isinstance(ab['Bill'].phones, list)
    assert isinstance(ab['Bill'].phones[0], Phone)
    assert ab['Bill'].phones[0].value == '1234567890'
    
    print('All Ok)')