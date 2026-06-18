from abc import ABC, abstractmethod

class Person(ABC):

    def __init__(self, full_name, age):
        self.__full_name = full_name
        self.__age = age

    def get_full_name(self):
        return self.__full_name

    def get_age(self):
        return self.__age

    @abstractmethod
    def display_information(self):
        pass