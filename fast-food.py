# Fast Food Joint

menu = {
    "fries": 2.5,
    "popcorn": 6,
    "fries": 2.5,
    "pretzel": 3.5,
    "chips": 1,
    "soda": 3,
    "lemonade": 4.25,
}

cart = []
total = 0

print("---------- MENU ----------")
print()
for key, value in menu.items():
    print(f"{key:10}: ${value:.2f}")

print()
print("---------------------")

while True:
    food = input("Select an item (q to quit): ").lower()
    if food == "q":
        break
    elif food != None:
        cart.append(food)

for food in cart:
    total += menu.get(food)
    print(f"- {food}")

print(f"Your total is: ${total:.2f}")
