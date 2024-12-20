# 백준 31279번 САМОЛЕТИ
import sys
put = sys.stdin.readline

N, d, ap1, ap2 = map(int, input().split())
v1, v2 = {0}, {0}
s1 = s2 = 0
answer = [0, 0, 1, 0]

while len(v1) < N or len(v2) < N:
    if len(v1) < N:
        m1 = 0
        while m1 <= ap1 or s1 in v1:
            m1 += 1
            s1 = (s1 + 1) % N
            answer[0] += d
            if m1 > ap1 and s1 not in v1:
                if s1 == s2:
                    answer[2] += 1
                v1.add(s1)
                break
            if s1 == s2:
                answer[3] += 1

    if len(v2) < N:
        m2 = 0
        while m2 <= ap2 or s2 in v2:
            m2 += 1
            s2 -= 1
            if s2 == -1:
                s2 = N - 1
            answer[1] += d
            if m2 > ap2 and s2 not in v2:
                if s1 == s2:
                    answer[2] += 1
                v2.add(s2)
                break
            if s1 == s2:
                answer[3] += 1

print(*answer)
