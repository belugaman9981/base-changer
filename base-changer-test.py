number = input("Enter the number: ").upper()
base = int(input("Enter the base of the number: "))

decimal = 0
power = 0

digits = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"

for digit in reversed(number):
    value = digits.index(digit)
    decimal += value * (base ** power)
    power += 1

print("Base 10 value is:", decimal)