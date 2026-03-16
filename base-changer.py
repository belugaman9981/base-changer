
Number   = int(input("What is the number you want to transform? "))
Base = int(input("What base do you want to convert to? "))

list = []
i = 0

while Base != 0:
    Remainder = Number % Base
    Number = Number // Base
    list.append(Remainder)
    
print(list)