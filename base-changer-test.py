def convert_from_base10(number, base):
    if number == 0:
        return "0"
    
    digits = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    result = ""
    
    while number > 0:
        remainder = number % base
        result = digits[remainder] + result
        number //= base
    
    return result

# Example
print(convert_from_base10(255, 16))  # FF