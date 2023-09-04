# 백준 15723번 n단 논법
import sys
put = sys.stdin.readline

n = int(put())
logic = dict([(chr(i+97), [chr(i+97)]) for i in range(26)])

while n:
    n -= 1
    a, b = put().strip().split(' is ')
    logic[a].append(b)

m = int(put())

while m:
    m -= 1
    a, b = put().strip().split(' is ')

    visited = [0] * 26
    bfs = [a]
    visited[ord(a)-97] = 1

    while bfs:
        c = bfs.pop(0)
        if c == b:
            print('T')
            break

        for i in logic[c]:
            if not visited[ord(i)-97]:
                visited[ord(i)-97] = 1
                bfs.append(i)

    else:
        print('F')