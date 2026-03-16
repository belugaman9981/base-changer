
Number   = int(input("What is the number you want to transform? "))
Base = int(input("What base do you want to convert to? "))

list = []
i = 0
StringNum = 0

while Number != 0:
    Remainder = Number % Base
    Number = Number // Base
    list.append(Remainder)
    StringNum =+ list.pop()
    
print(list)