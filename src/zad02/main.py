def roman(num):
    numbers = [50, 40, 10, 9, 5, 4, 1]
    symbols = ["L", "XL", "X", "IX", "V", "IV", "I"]
    i = 0
    roman_number = ""

    while num:
        for _ in range(num // numbers[i]):
            roman_number += symbols[i]
            num -= numbers[i]
        i += 1
    return roman_number
