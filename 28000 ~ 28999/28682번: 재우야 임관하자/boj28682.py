# 백준 28682번 재우야 임관하자
import sys
put = sys.stdin.readline

n = int(put())
subject = {"swimming", "bowling", "soccer"}

check = ["swimming"] * n
print(*check, flush=True)

F = put().split()
answer = []

for i in range(n):
    answer.append(list(subject - {check[i], F[i]})[0])

print(*answer)