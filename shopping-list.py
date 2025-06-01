# Grocery Shopping List

groceries = []
is_running = True

while is_running:
    user_input = input("Add items you need to get (q to quit, l to list all the items): ")
    if user_input == "q":
        break
    elif user_input == "l":
        print("Your items include: ")
        for items in groceries:
            print(f"- {items}")
    else:
        groceries.append(user_input)


