print("1 - addition")
print("2 - subtraction")
print("3 - multiplication")
print("4 - division")
print("choose an operation (1/2/3/4):")
option = input()
if option in ('1', '2', '3', '4'):
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    if option == '1':
        print(f"{num1} + {num2} = {num1 + num2}")

    elif option == '2':
        print(f"{num1} - {num2} = {num1 - num2}")

    elif option == '3':
        print(f"{num1} * {num2} = {num1 * num2}")

    elif option == '4':
        if num2 != 0:
            print(f"{num1} / {num2} = {num1 / num2}")
        else:
            print("Error: Division by zero is not allowed.")
