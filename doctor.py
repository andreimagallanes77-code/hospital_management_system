from person import Person

class Doctor(Person):

    def __init__(self, full_name, age, specialization):
        super().__init__(full_name, age)
        self.__specialization = specialization

    def get_specialization(self):
        return self.__specialization

    def display_information(self):
        print("\n=== DOCTOR INFO ===")
        print("Name:", self.get_full_name())
        print("Age:", self.get_age())
        print("Specialization:", self.get_specialization())