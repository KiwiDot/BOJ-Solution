# 백준 28720번 Ножницы
import sys
put = sys.stdin.readline

n, m = map(int, put().split())
answer = 0

ni = n - 1
mi = m - 2

nd = max(0, ni-mi-1)
answer += ni * (ni + 1) // 2 - nd * (nd + 1) // 2

md = max(0, mi-ni)
answer += mi * (mi + 1) // 2 - md * (md + 1) // 2

print(answer)