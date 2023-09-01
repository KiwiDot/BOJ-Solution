# 백준 1802번 종이 접기
import sys
put = sys.stdin.readline

T = int(put())

while T:
    T -= 1
    paper = put().strip()

    while len(paper) > 1:
        n = len(paper) // 2
        p1, p2 = paper[:n], paper[n+1:][::-1]

        for i in range(n):
            if p1[i] == p2[i]:
                print("NO")
                break
        else:
            paper = p1
            continue
        break

    else:
        print("YES")

