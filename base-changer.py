
Number   = int(input("What is the number you want to transform? "))
intoBase = int(input("What base do you want to convert to? "))

list = []
i = 0

while intoBase != 0:
    intoBase = Number // intoBase
    list.append(intoBase)
    
print(list)