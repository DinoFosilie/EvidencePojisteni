from insured import Insured

class Management:
    def __init__(self):
        """
        Initialization of the Management class
        Creates a list of insured persons
        """
        self.insurance = []

    def add_insured(self, insured):
        """
        Adds a new insured to the list
        :param insured: Object representing the insured
        """
        self.insurance.append(insured)

    def display_insured(self):
        """
        Displays a list of all insured persons
        """
        for insured in self.insurance:
            print(insured)

    def find_insured(self, name, surname):
        """
        Searches for the insured by name and surname
        :param name: Name of the sought insured
        :param surname: Surname of the sought insured
        """
        for insured in self.insurance:
            if insured.name == name and insured.surname == surname:
                return insured
        return None

    def save_to_file(self, file_name):
        """
        Save list of insured persons to a file
        :param file_name: File name to save
        """
        with open(file_name, "w") as file:
            for insured in self.insurance:
                file.write(f"{insured.name}, {insured.surname}, {insured.age}, {insured.phone_number}\n")

    def load_from_file(self, file_name):
        """
        Loads the list of insureds from a file
        :param file_name: File name to load
        """
        self.insured_list = []
        with open(file_name, "r") as file:
            for line in file:
                data = line.strip().split(",")
                self.add_insured(Insured(data[0], data[1], int(data[2]), data[3]))
