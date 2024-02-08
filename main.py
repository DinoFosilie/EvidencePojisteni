from insured import Insured
from management import Management

def menu():
    '''
    Displays the user menu
    '''
    print("\nMenu:")
    print("1 - Přidat nového pojištěného")
    print("2 - Zobrazit seznam pojištěných")
    print("3 - Vyhledat pojištěného")
    print("4 - Konec")

def load_data(manage):
    try:
        manage.load_from_file("insured_data.txt")
        print("Data byla načtena ze souboru.")
    except FileNotFoundError:
        print("Soubor s daty nebyl nalezen")

def save_data(manage):
    """
    Saves data to a file
    :param manage: The management object to save data from.
    """
    manage.save_to_file("insured_data.txt")
    print("Data byla uložena do souboru")

manage = Management()
load_data(manage)

while True:
    menu()
    choice = input("")

    # Code for add insured
    if choice == "1":
        name = input("Zadejte jméno: ")
        surname = input("Zadejte příjmení: ")
        age = int(input("Zadejte věk: "))
        phone_number = input("Zadejte telefonní číslo: ")#

        if not name.strip():
            print("Jméno nesmí být prázdné")
            continue

        insured = Insured(name, surname, age, phone_number)
        manage.add_insured(insured)
        print("Pojištěný byl přidán.")

    # Code for display insurance
    elif choice == "2":
        print("\nSeznam pojištěných: ")
        manage.display_insured()

    # Code for finding the insured
    elif choice == "3":
        name = input("Zadejte jméno pojištěného: ")
        surname = input("Zadejte příjmení: ")
        found = manage.find_insured(name, surname)
        if found:
            print("\nHledaný pojištěný nalezen: ")
            print(found)
        else:
            print("\nHledaný pojištěný nenalezen.")

    elif choice == "4":
        save_data(manage)
        break

    else:
        print("Neplatná volba")