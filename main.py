from collections import UserDict
import re

class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)


class Name(Field):
		pass


class Phone(Field):
    def is_valid(self) -> bool:
        return bool(re.fullmatch(r"\d{10}", self.value))


class Record:
    def __init__(self, name: str):
        self.name = Name(name)
        self.phones = []

    def add_phone(self, phone: str) -> None:
        new_phone = Phone(phone)

        if new_phone.is_valid():
            self.phones.append(new_phone)

        else:
            print('Warning: incorrect phone number')

    def remove_phone(self, phone: str) -> None:
        phone_obj = self.find_phone(phone)

        if phone_obj:
            self.phones.remove(phone_obj)

    def edit_phone(self, old_phone: str, new_phone: str) -> None:
        phone_obj = self.find_phone(old_phone)

        if phone_obj:
            updated_phone = Phone(new_phone)

            if updated_phone.is_valid():
                phone_obj.value = new_phone

            else:
                print('Warning: incorrect phone number')

    def find_phone(self, phone: str) -> Phone:
        searched_phone = next((p for p in self.phones if p.value == phone), None)

        if not searched_phone:
            print('Warning: no such phone number in the list')

        return searched_phone

    def __str__(self):
        return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}"


class AddressBook(UserDict):
    def add_record(self, record: Record):
        self.data[record.name.value] = record
    
    def find(self, name):
        record = self.data.get(name)

        if not record:
            print(f"Warning: No record found for {name}")

        return record
    
    def delete(self, name):
        if self.find(name):
            del self.data[name]


book = AddressBook()

john_record = Record("John")
john_record.add_phone("1234567890")
john_record.add_phone("5555555555")
book.add_record(john_record)

jane_record = Record("Jane")
jane_record.add_phone("9876543210")
book.add_record(jane_record)

for name, record in book.data.items():
    print(record)

john = book.find("John")
john.edit_phone("1234567890", "1112223333")
print(john)  

found_phone = john.find_phone("5555555555")
print(f"{john.name}: {found_phone}")  

book.delete("Jane")
jane = book.find("Jane")