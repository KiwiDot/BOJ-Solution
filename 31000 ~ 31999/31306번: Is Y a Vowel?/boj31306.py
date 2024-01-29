# 백준 31306번 Is Y a Vowel?
import sys
put = sys.stdin.readline

vowel = {'a': 0, 'e': 0, 'i': 0, 'o': 0, 'u': 0, 'y': 0}
text = put().strip().lower()

for i in text:
    if i in vowel:
        vowel[i] += 1

y_yes = sum(vowel.values())
y_no = y_yes - vowel['y']

print(y_no, y_yes)