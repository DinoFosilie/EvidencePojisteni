class Insured:

    def __init__(self, name, surname, age, phone_number):
        """
        Initialization of the Insured class
        :param name: Name of the insured
        :param surname: Surname of the insured
        :param age: Age of the insured
        :param phone_number: Telephone number of the insured
        """
        self.name = name
        self.surname = surname
        self.age = age
        self.phone_number = phone_number

    def __str__(self):
        """
        :return: Returns the textual representation of the object
        """
        return f"Jméno: {self.name} {self.surname}, Věk: {self.age}, Telefon: {self.phone_number}"