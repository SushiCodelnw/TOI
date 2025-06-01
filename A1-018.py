a = int(input())

roman_numerals = {
    1: "I", 2: "II", 3: "III", 4: "IV", 5: "V",
    6: "VI", 7: "VII", 8: "VIII", 9: "IX"
}

if a <= 0:
    print("Error : Please input positive number")
elif a > 9:
    print("Error : Out of range")
else:
    print(roman_numerals[a])