# 백준 30502번 미역은 식물 아닌데요
import sys
put = sys.stdin.readline

N, M = map(int, put().split())
data = dict([(str(i+1), {'P': -1, 'M': -1}) for i in range(N)])

while M:
    M -= 1
    a, b, c = put().split()
    data[a][b] = c

cnt1 = 0
cnt2 = 0

for i in data:
    if data[i]['P'] == '1' and data[i]['M'] == '0':
        cnt1 += 1
    elif data[i]['P'] != '0' and data[i]['M'] != '1':
        cnt2 += 1

print(cnt1, cnt1 + cnt2)