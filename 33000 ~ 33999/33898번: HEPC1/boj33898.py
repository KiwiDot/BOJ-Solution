# 백준 33898번 HEPC1
import sys
put = sys.stdin.readline

data = put().strip() + put().strip()[::-1]
answer = "NO"

for i in range(4):
    if data[i:] + data[:i] in {"HEPC", "CPEH"}:
        answer = "YES"
        break

print(answer)