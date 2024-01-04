# 백준 31097번 Astrology
import sys
put = sys.stdin.readline

YYYY, MM, DD = put().split('-')
time = int(MM + DD)

check = [(321, 419, "Aries"),
         (420, 520, "Taurus"),
         (521, 620, "Gemini"),
         (621, 722, "Cancer"),
         (723, 822, "Leo"),
         (823, 922, "Virgo"),
         (923, 1022, "Libra"),
         (1023, 1122, "Scorpio"),
         (1123, 1221, "Sagittarius"),
         (1222, 119, "Capricorn"),
         (120, 218, "Aquarius"),
         (219, 320, "Pisces")]

for x, y, zodiac in check:
    if x <= time <= y:
        print(zodiac)
        break
else:
    print("Capricorn")