# 백준 27259번 Разноцветные диагонали
import sys
put = sys.stdin.readline

n = int(put())

for i in range(n):
    answer = ''
    for j in range(n):
        d = min(abs(i - j), abs(i + j - (n - 1)))
        apb = chr((d % 26) + 97)
        answer += apb
    print(answer)
