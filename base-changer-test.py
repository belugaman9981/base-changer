
number = int(input("What is the number you want to transform? "))
base = int(input("What base do you want to convert to? "))

result = ""

while number > 0:
    remainder = number % base
    result = str(remainder) + result
    number = number // base

print(result)


