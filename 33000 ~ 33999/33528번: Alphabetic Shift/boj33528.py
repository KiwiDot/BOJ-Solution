# 백준 33528번 Alphabetic Shift
import sys
put = sys.stdin.readline

text = put().strip()

for i in range(26):
    shift = 26 - i
    abc = {}

    for j in range(26):
        abc[chr(j + 65)] = chr((j + shift) % 26 + 65)

    print(''.join([abc[j] for j in text]))