
def input_error(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except KeyError:
            return "Enter user name"
        except ValueError:
            return "Give me name and phone please"
        except IndexError:
            return "Contact not found"

    return wrapper



def hello():
    return "How can I help you?"



contacts = {}



@input_error
def add_contact(command):
    _, name, phone = command.split()
    contacts[name] = phone
    return f"Added contact: {name} - {phone}"



@input_error
def change_contact(command):
    _, name, phone = command.split()
    if name in contacts:
        contacts[name] = phone
        return f"Changed phone for {name} to {phone}"
    else:
        raise IndexError



@input_error
def phone(command):
    _, name = command.split()
    if name in contacts:
        return f"Phone for {name}: {contacts[name]}"
    else:
        raise IndexError



def show_all():
    if contacts:
        result = "All contacts:\n"
        for name, phone in contacts.items():
            result += f"{name} - {phone}\n"
        return result.strip()
    else:
        return "No contacts saved."


def good_bye():
    return "Good bye!"



def main():
    while True:
        command = input("Enter a command: ").lower()
        if command == "hello":
            print(hello())
        elif command.startswith("add"):
            print(add_contact(command))
        elif command.startswith("change"):
            print(change_contact(command))
        elif command.startswith("phone"):
            print(phone(command))
        elif command == "show all":
            print(show_all())
        elif command in ["good bye", "close", "exit"]:
            print(good_bye())
            break
        else:
            print("Unknown command. Please try again.")


if __name__ == "__main__":
    main()