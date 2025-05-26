# Shopping Cart Program

# declare variables and lists
foods = [] 
prices = []
total = 0

# while loop to run program over and over
while True:
    # input
    food = input("Enter food to buy (q to quit): ")
    # break in program
    if food.lower() == "q":
        break
    # continuation
    else:
        price = float(input(f"Enter the price of a {food}: $"))
        # add user input to existing lists
        foods.append(food)
        prices.append(price)

print("----- YOUR CART -----")
# iterate over items in lists and print each item
for food in foods:
    print(f"- {food}")

# add up items in lists
for price in prices:
    total = total + price

# print results
print(f"Your total is: ${total}")
