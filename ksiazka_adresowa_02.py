
def main():
    address_book = {
    'first_name' : ['Jan', 'Anna', 'Krzysztof', 'Małgorzata', 'Piotr', 'Alicja', 'Wojciech', 'Zofia', 'Michał', 'Barbara'],
    'last_name' : ['Kowalski', 'Nowak', 'Wiśniewski', 'Wójcik', 'Kowalczyk', 'Kamińska', 'Lewandowski', 'Zielińska', 'Szymański', 'Woźniak'],
    'phone' : ['501234567', '512345678', '523456789', '534567890', '545678901', '556789012', '567890123', '578901234', '589012345', '590123456'],
    'department' : ['accounting', 'accounting', 'HR', 'HR', 'HR', 'HR', 'engineering','engineering', 'engineering', 'engineering'],
    'email' : ['Jan.Kowalski@firma.com', 'Anna.Nowak@firma.com', 'Krzysztof.Wiśniewski@firma.com', 'Małgorzata.Wójcik@firma.com', 'Piotr.Kowalczyk@firma.com', 'Alicja.Kamińska@firma.com', 'Wojciech.Lewandowski@firma.com', 'Zofia.Zielińska@firma.com', 'Michał.Szymański@firma.com', 'Barbara.Wozniak@firma.com']
    }
    print("Wybierz, co chcesz zrobić: \n P - by wyświetlić wszystkie dane, \n C - by utworzyć nowy wpis, \n D - by usunąć wpis, \n E - by zakończyć program  ")
    user_command = input("Wybierz P/C/D/E: ").capitalize()


    if user_command == 'P':
        print_all_data(address_book)
    elif user_command == 'C':
        add_entry_and_create_email_address(address_book)
    elif user_command == 'D':
        remove_data(address_book)
    elif user_command == 'E':
        end_program(address_book)


def add_entry_and_create_email_address(address_book):
    dept_list = ["accounting", "HR", "engineering"]
    new_name = input("Podaj imię: ").title()
    new_surname = input("Podaj nazwisko: ").title()
    new_phone = input("Podaj numer telefonu: ")
    while len(new_phone) != 9:
        print("Prosimy o podanie poprawnego numeru telefonu.")
        new_phone = input("Podaj numer telefonu: ")
    new_department = input("Podaj dział (accounting, HR, engineering): ")
    while new_department not in dept_list:
        print("Podaj poprawną nazwę działu.")
        new_department = input("Podaj dział (accounting, HR, engineering): ")
    generated_email = new_name +"."+ new_surname + "@"+"firma.com"
    address_book['first_name'].append(new_name)
    address_book['last_name'].append(new_surname)
    address_book['phone'].append(new_phone)
    address_book['department'].append(new_department)
    address_book['email'].append(generated_email)
    print(generated_email)



def print_all_data(address_book):
    for name in range(len(address_book['first_name'])):
        print("Imię i nzawisko: ", end="")
        print(address_book['first_name'][name], end=" ")
        print(address_book['last_name'][name], end=" ")
        print("Numer telefonu: ", end="")
        print(address_book['phone'][name], end=" ")
        print('Adres e-mail: ', end="")
        print(address_book['email'][name])

def remove_data(address_book):
    delete_surname = input('Podaj nazwisko osóby, której rekord chcesz usnąć: ')
    temp_surname_list = address_book['last_name']
    print(temp_surname_list)
    surname_index = temp_surname_list.index(delete_surname)
    print(surname_index)
    for key in address_book:
        address_book['first_name'].pop(surname_index)
        print(address_book)


def end_program():
    print("Zakończyłeś używanie programu")
    exit()


main()
