
def create_phone_book():
    contacts = {}

    # Add contact
    def add_contact(name, number):
        name = name.strip()
        number = number.strip()

        if name == "":
            return "Name can't be empty!"

        if not number.isdigit():
            return "Please enter a valid phone number!"

        for stored_name in contacts:
            if stored_name.lower() == name.lower():
                return "This name already exists!"

        contacts[name] = number
        return "Contact added successfully!"

    # Delete contact
    def delete_contact(name):
        name = name.strip()

        for stored_name in contacts:
            if stored_name.lower() == name.lower():
                del contacts[stored_name]
                return "Contact deleted successfully!"

        return "Contact not found!"

    # Search contact
    def search_contact(name):
        name = name.strip()

        for stored_name, number in contacts.items():
            if stored_name.lower() == name.lower():
                return f"Name: {stored_name} | Number: {number}"

        return "Contact not found!"

    # Update contact
    def update_contact(old_name, new_name, new_number):
        old_name = old_name.strip()
        new_name = new_name.strip()
        new_number = new_number.strip()

        if new_name == "":
            return "Name can't be empty!"

        if not new_number.isdigit():
            return "Please enter a valid phone number!"

        # Find the existing contact
        actual_name = None

        for stored_name in contacts:
            if stored_name.lower() == old_name.lower():
                actual_name = stored_name
                break

        if actual_name is None:
            return "Contact not found!"

        # Prevent duplicate names, ignoring capitalization
        for stored_name in contacts:
            if (
                stored_name.lower() == new_name.lower()
                and stored_name != actual_name
            ):
                return "Another contact with this name already exists!"

        # Update the contact
        del contacts[actual_name]
        contacts[new_name] = new_number

        return "Contact updated successfully!"

    # Show all contacts
    def show_contacts():
        if not contacts:
            print("Phone book is empty!")
            return

        print("\n====== PHONE BOOK CONTACTS ======")

        for name, number in contacts.items():
            print(f"Name: {name} | Number: {number}")

        print("=================================")

    return {
        "add_contact": add_contact,
        "delete_contact": delete_contact,
        "search_contact": search_contact,
        "update_contact": update_contact,
        "show_contacts": show_contacts
    }


# Create phone book
account = create_phone_book()

# Main menu
while True:
    print("\n===== PHONE BOOK MENU =====")
    print("1. Add Contact")
    print("2. Delete Contact")
    print("3. Search Contact")
    print("4. Show All Contacts")
    print("5. Update Contact")
    print("6. Exit")

    choice = input("Enter your choice (1-6): ").strip()

    if choice == "1":
        name = input("Enter name: ")
        number = input("Enter phone number: ")

        print(account["add_contact"](name, number))

    elif choice == "2":
        name = input("Enter name to delete: ")

        print(account["delete_contact"](name))

    elif choice == "3":
        name = input("Enter name to search: ")

        print(account["search_contact"](name))

    elif choice == "4":
        account["show_contacts"]()

    elif choice == "5":
        old_name = input("Enter existing contact name: ")
        new_name = input("Enter new name: ")
        new_number = input("Enter new phone number: ")

        print(
            account["update_contact"](
                old_name, new_name, new_number
            )
        )

    elif choice == "6":
        print("Thank you for using our phone book!")
        break

    else:
        print("Invalid choice! Please enter 1 to 6.")
