
contact_book = {}


def add_contact(name, phone):
    if name in contact_book:
        print(f"Contact '{name}' already exists with phone number {contact_book[name]}.")
    else:
        contact_book[name] = phone
        print(f"Contact '{name}' added successfully.")


def search_contact(name):
    if name in contact_book:
        print(f"Phone number of '{name}' is {contact_book[name]}.")
    else:
        print(f"Contact '{name}' not found.")


def display_contacts():
    if contact_book:
        print("Contact List:")
        for name, phone in contact_book.items():
            print(f"{name}: {phone}")
    else:
        print("Contact book is empty.")


def main():
    while True:
        print("\nContact Book Menu:")
        print("1. Add Contact")
        print("2. Search Contact")
        print("3. Display All Contacts")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ")

        if choice == '1':
            name = input("Enter contact name: ")
            phone = input("Enter phone number: ")
            add_contact(name, phone)
        elif choice == '2':
            name = input("Enter contact name to search: ")
            search_contact(name)
        elif choice == '3':
            display_contacts()
        elif choice == '4':
            print("Exiting Contact Book. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 4.")

if __name__ == "__main__":
    main()
