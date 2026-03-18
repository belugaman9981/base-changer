number = input("Enter the number: ")
base = int(input("Enter the base of the you want to tranform number into: "))
    
decimal = 0
power = 0

for digit in number:
    decimal += int(digit) * (base ** power)
    power += 1
        
print("Base", base, "value is:", decimal)