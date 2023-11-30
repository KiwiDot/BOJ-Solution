# 백준 28642번 Электронный замок
import sys
put = sys.stdin.readline

n = int(put())

if n % 2:
    answer = '7' + '1' * ((n - 3) // 2)
else:
    answer = '1' * (n // 2)

print(answer)