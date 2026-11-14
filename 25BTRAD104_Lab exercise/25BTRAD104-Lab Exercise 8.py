# Contact Book using a dictionary (name -> details)
contacts = {}

def add_contact():
    name = input("Enter name: ").strip()
    if name in contacts:
        print("Contact already exists.")
        return
    phone = input("Enter phone: ").strip()
    email = input("Enter email: ").strip()
    contacts[name] = {"phone": phone, "email": email}
    print("Contact added.")

def search_contact():
    name = input("Enter name to search: ").strip()
    if name in contacts:
        print("Name:", name)
        print("Phone:", contacts[name]["phone"])
        print("Email:", contacts[name]["email"])
    else:
        print("Contact not found.")

def update_contact():
    name = input("Enter name to update: ").strip()
    if name in contacts:
        phone = input("Enter new phone: ").strip()
        email = input("Enter new email: ").strip()
        contacts[name] = {"phone": phone, "email": email}
        print("Contact updated.")
    else:
        print("Contact not found.")

def delete_contact():
    name = input("Enter name to delete: ").strip()
    if name in contacts:
        del contacts[name]
        print("Contact deleted.")
    else:
        print("Contact not found.")

def display_contacts():
    if not contacts:
        print("No contacts available.")
        return
    for name, details in contacts.items():
        print(name, "|", details["phone"], "|", details["email"])

while True:
    print("\n--- Contact Book ---")
    print("1. Add")
    print("2. Search")
    print("3. Update")
    print("4. Delete")
    print("5. Display All")
    print("6. Exit")
    choice = input("Enter choice: ")

    if choice == "1":
        add_contact()
    elif choice == "2":
        search_contact()
    elif choice == "3":
        update_contact()
    elif choice == "4":
        delete_contact()
    elif choice == "5":
        display_contacts()
    elif choice == "6":
        print("Goodbye!")
        break
    else:
        print("Invalid choice.")