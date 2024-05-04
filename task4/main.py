import os

def input_error(func):
    """
    Decorator. Errors handler
    """

    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError:
            return "Enter the argument for the command."
        except KeyError:
            return "Cannot add contact. Contact with the same name already exists."
        except IndexError:
            return "Contact does not exists."

    return inner

def parse_input(user_input):
    """
    This function parses usder input and return command and list of the arguments
    """
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args

@input_error
def add_contact(args, contacts:dict)->str:
    """
    This function adds contact to the contacts dictionary.
    Only unique contact name is available
    """
    if len(args) == 2: #function requires 2 arguments
        name, phone = args
        if not contacts.get(name): #trying to get contact from the dict
            contacts[name] = phone #adding new if not found
            save_phonebook(contacts)
            return "Contact added."
        else:
            raise KeyError
    else:
        raise ValueError

@input_error
def change_contact(args,contacts:dict)->str:
    """
    This function cnahges existing contact.
    Returns an error if contact does not exist
    """
    if len(args) == 2:
        name, phone = args
        if contacts.get(name):
            contacts[name] = phone
            save_phonebook(contacts)
            return "Contact updated."
        else:
            raise IndexError
    else:
        raise ValueError

@input_error
def delete_contact(args,contacts:dict)->str:
    """
    This function deletes existing contact.
    Returns an error if contact does not exist
    """
    if len(args) == 1:
        name=args[0]
        if contacts.get(name):
            del contacts[name]
            save_phonebook(contacts)
            return "Contact deleted."
        else:
            raise IndexError
    else:
        raise ValueError

def show_contacts(contacts:dict)->str:
    """
    This function returns contacts added to the dictionary
    """
    list_of_contacts=f"{'name':^10}{'phone':^10}\n"
    
    for name,phone in contacts.items():
        list_of_contacts+=f"{name:^10}{phone:^10}\n"
    
    return list_of_contacts

@input_error
def show_contact(args,contacts:dict)->str:
    if len(args) == 1:
        name = args[0]
        if contacts.get(name):
            return f"The phone number for the contact {name} is {contacts.get(name)}."
        else:
            raise IndexError
    else:
        raise ValueError

def load_phonebook()->dict:
    """
    This function loads contacts from the phonebook.txt
    If file does not exist it creates empty one
    """
    contacts={}
    with open(f"{os.path.dirname(os.path.abspath(__file__))}/phonebook.txt", 'a+',encoding="utf-8") as phonebook_file: #creating new file if it does not exist
        phonebook_file.seek(0)
        for line in phonebook_file:
            (key, val) = line.split(",")
            if val.strip() != "":
                contacts[key] = val.strip()

    return contacts

def save_phonebook(contacts:dict):
    """
    Function saves the contacts dictionary to the file
    """
    with open(f"{os.path.dirname(os.path.abspath(__file__))}/phonebook.txt", 'w',encoding="utf-8") as phonebook_file:
        for name in sorted(contacts.keys()):
            phonebook_file.write(f"{name},{contacts.get(name)}\n")


def main():
    contacts = load_phonebook()
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Good bye!")
            break
        elif command == "hello":
            print("How can I help you?")
        elif command == "add":
            print(add_contact(args, contacts))
        elif command == "change":
            print(change_contact(args, contacts))
        elif command in ["delete","del"]:
            print(delete_contact(args, contacts))
        elif command == "all":
            print(show_contacts(contacts))
        elif command == "phone":
            print(show_contact(args,contacts))
        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()