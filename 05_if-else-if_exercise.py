print('if elif else - Exercise')
# Create a calculator which handles +,-,*,/ and outputs answer based on the mode/ operator used
# Hint: use 3 separate inputs
# Bonus: Extend functionality with extra mode so it also does celsius to fahrenheit conversion
# formula is: temp in C*9/5 + 32 = temp in f
mode = input("Enter math operation(+,-,*,/) or f for Celsius to Fahrenheit conversion: ")
num1 = float(input("Enter first number: "))
if mode.lower() == "f":
    print(f"Conversion to Fahrenheit: {(num1 * 9 / 5) + 32}")

else:
    num2 = float(input("Enter second number: "))
    if mode == "+":
        print(f"{num1 + num2}")
    elif mode == "-":
        print(f"{num1 - num2}")
    elif mode == "*":
        print(f"{num1 * num2}")
    elif mode == "/":
        print(f"{num1 / num2}")
    else:
        print("input error")