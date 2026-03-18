what_kind = float(input("What kind do you want it to be (normal to ?, ? to normal or ? to ?)? "))


if what_kind == 1:
    
    
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
    