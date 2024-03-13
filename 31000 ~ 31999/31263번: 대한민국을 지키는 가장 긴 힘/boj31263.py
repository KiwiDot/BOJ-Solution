# 백준 31263번 대한민국을 지키는 가장 긴 힘
import sys
put = sys.stdin.readline

N = int(put())
S = put().strip()
r = 10 ** 6
dp = [[r, r, r], [1, r, r], [2, 1, r]]

for i in range(2, N):
    d = [0, 0, 0]

    for j in range(3):
        s = S[i-j:i+1]
        if s[0] != '0' and 1 <= int(s) <= 641:
            match j:
                case 0:
                    d[0] = min(dp[-1]) + 1
                case 1:
                    d[1] = dp[-1][0]
                case 2:
                    d[2] = dp[-1][1]
        else:
            d[j] = r

    dp.append(d)

print(min(dp[-1]))