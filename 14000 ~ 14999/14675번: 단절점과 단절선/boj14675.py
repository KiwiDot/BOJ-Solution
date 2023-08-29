# 백준 14675번 단절점과 단절선
import sys
put = sys.stdin.readline

N = int(put())
tree = dict([(i+1, []) for i in range(N)])

for i in range(N-1):
    a, b = map(int, put().split())
    tree[a].append(b)
    tree[b].append(a)

q = int(put())
while q:
    q -= 1
    t, k = map(int, put().split())

    if t == 1:
        if len(tree[k]) > 1:
            print("yes")
        else:
            print("no")
    else:
        print("yes")