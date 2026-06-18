from person import Person

class Patient(Person):

    def __init__(self, full_name, age, illness):
        super().__init__(full_name, age)
        self.__illness = illness

    def get_illness(self):
        return self.__illness

    def display_information(self):
        print("\n=== PATIENT INFO ===")
        print("Name:", self.get_full_name())
        print("Age:", self.get_age())
        print("Illness:", self.get_illness())