contacts = {}

is_running = True

while is_running:
    print("\n--- Contact Book ---")
    print("1. Add contact")
    print("2. View all contacts")
    print("3. Quit")
    
    user_choice = input("Choose an option (1-3): ")
    
    if user_choice == "1":
        name = input("Enter name: ")
        phone = input("Enter phone number: ")
        email = input("Enter email: ")
        
        contacts[name] = {
            "phone": phone,
            "email": email
        }
        print(f"Contact for {name} added!")
    
    elif user_choice == "2":
        if contacts == {}:
            print("No contacts found.")
        else:
            for name, info in contacts.items():
                print(f"\nName: {name}")
                print(f"Phone: {info['phone']}")
                print(f"Email: {info['email']}")
    
    elif user_choice == "3":
        is_running = False
        print("Goodbye!")
    
    else:
        print("Invalid choice. Try again.")
