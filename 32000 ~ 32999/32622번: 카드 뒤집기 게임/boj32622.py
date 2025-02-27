# 백준 32622번 카드 뒤집기 게임
import sys
put = sys.stdin.readline

N = int(put())
A = put().split()
a = [A[0]]

for i in range(1, N):
    if A[i] == '0':
        if a[-1][-1] == '0':
            a[-1] += '0'
        else:
            a.append('0')

    else:
        if a[-1][-1] == '1':
            a[-1] += '1'
        else:
            a.append('1')

w, b = [''], ['']
for i in a:
    if i[-1][-1] == '0':
        w.append(i)
    else:
        w[-1] += i

    if i[-1][-1] == '1':
        b.append(i)
    else:
        b[-1] += i

answer = max(max([len(i) for i in w]), max([len(i) for i in b]))
print(answer)