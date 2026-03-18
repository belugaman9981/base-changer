what_kind = float(input("What kind do you want it to be (normal to ?, ? to normal or ? to ?)? "))

digits = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"


if what_kind == 1:
    
    number = int(input("What is the number you want to transform? "))
    base = int(input("What base do you want to convert to? "))

    result = ""

    while number > 0:
        remainder = number % base
        result = str(remainder) + result   # add to the front
        number = number // base

    print(result)
    
elif what_kind == 2:
    
    number = input("Enter the number: ")
    base = int(input("Enter the base of that number: "))

    decimal = 0
    power = 0

    for digit in reversed(number):
        decimal += int(digit) * (base ** power)
        power += 1

    print("Base 10 value:", decimal)
    
elif what_kind == 3:
    
    number = input("Enter the number: ").upper()
    base_from = int(input("Enter the base of that number: "))
    base_to = int(input("Enter the base you want to convert to: "))

    # Step 1: Convert to base 10
    decimal = 0
    power = 0

    for digit in reversed(number):
        value = digits.index(digit)
        decimal += value * (base_from ** power)
        power += 1

    # Step 2: Convert from base 10 to target base
    result = ""

    while decimal > 0:
        remainder = decimal % base_to
        result = digits[remainder] + result
        decimal = decimal // base_to

    print("Converted value:", result)


else:
    print("Invalid choice ❌")
    