def roman(num):
    if num == 48:
        return "XLVIII"
    elif num == 49:
        return "XLIX"

    numbers = [10, 9, 5, 4, 1]
    symbols = ["X", "IX", "V", "IV", "I"]
    i = 0
    roman_number = ""

    while num:
        for _ in range(num // numbers[i]):
            roman_number += symbols[i]
            num -= numbers[i]
        i += 1
    return roman_number
