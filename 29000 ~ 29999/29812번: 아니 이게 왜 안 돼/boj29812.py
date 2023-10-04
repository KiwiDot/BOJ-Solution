# 백준 29812번 아니 이게 왜 안 돼
import sys
put = sys.stdin.readline

N = int(put())
S = put().strip()
D, M = map(int, put().split())

s = ""
energy = 0
cnt = {'H': 0, 'Y': 0, 'U': 0}
for i in S:
    if i.isupper():
        cnt[i] += 1
        energy += min(len(s) * D, D + M)
        s = ""
    else:
        s += i
energy += min(len(s) * D, D + M)
minimum = min(cnt.values())

print(energy if energy else "Nalmeok")
print(minimum if minimum else "I love HanYang University")