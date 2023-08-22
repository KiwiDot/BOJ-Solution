# 백준 29340번 Отряд
import sys
put = sys.stdin.readline

a = put().strip()
b = put().strip()

answer = ''.join([max(a[i], b[i]) for i in range(len(a))])
print(answer)