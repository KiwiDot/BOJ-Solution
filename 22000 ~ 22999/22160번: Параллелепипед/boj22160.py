# 백준 22160번 Параллелепипед
import sys
from collections import Counter
put = sys.stdin.readline

while True:
    data = dict(Counter(put().split()))
    if '0' in data and data['0'] == 12:
        break

    answer = sum([data[i] // 4 for i in data])
    print("yes" if answer == 3 else "no")