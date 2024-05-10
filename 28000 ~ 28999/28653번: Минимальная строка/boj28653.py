# 백준 28653번 Минимальная строка
import sys
put = sys.stdin.readline

a = list(put().strip())
b = list(put().strip())

answer = ''.join(sorted(a + b))[:len(a)]
print(answer)