from abc import ABC, abstractmethod


class Person(ABC):
    def __init__(self, name, person_id, phone):
        self.name = name
        self.person_id = person_id
        self.phone = phone


    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value:str):
        if value.strip() == "":
            raise ValueError("Name cannot be empty.")

        self.__name = value

    @property
    def person_id(self):
        return self.__person_id

    @person_id.setter
    def person_id(self, value:str):
        if value.strip() == "":
            raise ValueError("Person id cannot be empty.")

        if len(value) != 8:
            raise ValueError("Person id cannot be longer that 8 digit or shorter that 8 digits.")
        if  not value.isdigit():
            raise ValueError("The Person id number must contain only digits")
        self.__person_id = value

    @property
    def phone(self):
        return self.__phone

    @phone.setter
    def phone(self, value:str):
        if value.strip() == "":
            raise ValueError("Phone cannot be empty")
        if len(value) != 10:
            raise ValueError('Phone cannot be longer that 10 digits or shorter that 10 digits.')

        if  not value.isdigit():
            raise ValueError("The phone number must contain only digits")

        self.__phone = value


    @abstractmethod
    def person_information(self):
        pass


