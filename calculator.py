# Simple Calculator Program

def add(x, y):
    return x + y

def sub(x, y):
    return x - y

def mul(x, y):
    return x * y

def div(x, y):
    return x / y

def main():
    is_running = True

    while is_running:
        operator = input("Choose an operator: + - * / (q to quit): ")

        if operator == "q":
            break
        
        user_input1 = float(input("Enter the first number: "))
        user_input2 = float(input("Enter the second number: "))

        if operator == "+":
            result = add(user_input1, user_input2)
        elif operator == "-":
            result = sub(user_input1, user_input2)
        elif operator == "*":
            result = mul(user_input1, user_input2)
        elif operator == "/":
            result = div(user_input1, user_input2)
        else:
            print("Invalid operator")
            continue
        print(f"Answer is: {result:.2f}")

    print("Bye for now!")

if __name__ == "__main__":
    main()
    