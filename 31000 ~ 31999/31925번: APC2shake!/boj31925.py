# 백준 31925번 APC2shake!
import sys
put = sys.stdin.readline

N = int(put())
ranking = []

while N:
    N -= 1
    name, school, win, S, A = put().split()
    S, A = int(S), int(A)
    if school == "jaehak" and win == "notyet" and (S < 0 or S > 3):
        ranking.append((name, A))

ranking = sorted(ranking, key=lambda x: x[1])[:10]

print(len(ranking))
for i in sorted(ranking):
    print(i[0])