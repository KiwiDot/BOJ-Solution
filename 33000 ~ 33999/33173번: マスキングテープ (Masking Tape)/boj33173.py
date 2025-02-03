# 백준 33173번 マスキングテープ (Masking Tape)
import sys
put = sys.stdin.readline

H, W, Q = map(int, put().split())
paper = [[0] * W for i in range(H)]
tape = [[0] * W for i in range(H)]

while Q:
    Q -= 1
    q = list(map(int, put().split()))

    if len(q) == 4:
        n, x, y, c = q
        for xi, yi in [(x, y), (x+1, y), (x, y+1), (x+1, y+1)]:
            if not tape[xi-1][yi-1]:
                paper[xi-1][yi-1] = c

    else:
        n, x, y = q
        for xi, yi in [(x, y), (x+1, y), (x, y+1), (x+1, y+1)]:
            tape[xi-1][yi-1] = 1

for i in paper:
    print(*i)