from collections import UserDict


class Field:
    """Класс Field, который 
    будет родительским для всех полей, 
    в нем потом 
    реализуем логику общую для всех полей."""
    pass


class Name(Field):

    def __init__(self, name):
        self.value = name
        

class Phone(Field):
    """Класс Phone, 
    необязательное поле 
    с телефоном и таких одна запись (Record) может содержать несколько."""

    def __init__(self, phone):
        self.value = phone
        print(f"phone - {self.value}   {type(self.value)}")

    def __repr__(self):
        return self.value


class AddressBook(UserDict):     #  , Record

    # def __init__(self):
    #     super().

    def add_record(self, record):
        print(f"record111 - {record.name.value}   {type(record.name.value)}")
        self.data[record.name.value] = record


class Record:
    """Класс Record, который 
    отвечает за логику добавления/удаления/редактирования 
    необязательных полей 
    и хранения обязательного поля Name

    Record хранит объект Name в отдельном атрибуте.

    Record хранит список объектов Phone в отдельном атрибуте.

    Record реализует методы для добавления/удаления/редактирования объектов Phone."""

    def __init__(self, new_name, new_phone):
        self.name = new_name
        self.phones = []
        print(f"phone111 - {new_phone}   {type(phone.value)}")
        print(f"phone111 - {self.name.value}   {type(self.name.value)}")

    # def add_phone(self, new_phone):        
        self.phones.append(new_phone)

    def change_phone(self, old_phone, new_phone):        
        for phone in self.phones:
            if phone.value == old_phone:
                self.phones.add_phone(new_phone)
                self.phones.remove_phone(phone)
            else:
                print("Phone number doesn't exist")  

    def remove_phone(self, old_phone):        
        for phone in self.phones:
            if phone.value == old_phone:
                self.phones.remove(phone)
            else:
                print("Phone number does't exist")

        
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
