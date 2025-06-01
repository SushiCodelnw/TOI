d = int(input())
m = int(input())

def r():
    if m == 12 and d >= 22 or m == 1 and d <= 19: return "capricorn"
    if m == 1 and d >= 20 or m == 2 and d <= 18: return "aquarius"
    if m == 2 and d >= 19 or m == 3 and d <= 20: return "pisces"
    if m == 3 and d >= 21 or m == 4 and d <= 19: return "aries"
    if m == 4 and d >= 20 or m == 5 and d <= 20: return "taurus"
    if m == 5 and d >= 21 or m == 6 and d <= 21: return "gemini"
    if m == 6 and d >= 22 or m == 7 and d <= 22: return "cancer"
    if m == 7 and d >= 23 or m == 8 and d <= 22: return "leo"
    if m == 8 and d >= 23 or m == 9 and d <= 22: return "virgo"
    if m == 9 and d >= 23 or m == 10 and d <= 23: return "libra"
    if m == 10 and d >= 24 or m == 11 and d <= 21: return "scorpio"
    if m == 11 and d >= 22 or m == 12 and d <= 21: return "sagittarius"
print(r())