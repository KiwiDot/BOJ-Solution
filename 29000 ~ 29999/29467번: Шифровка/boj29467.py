# 백준 29467번 Шифровка
import sys
put = sys.stdin.readline

s = put().strip()
answer = [s[i:] for i in range(len(s))]

print(max(answer))