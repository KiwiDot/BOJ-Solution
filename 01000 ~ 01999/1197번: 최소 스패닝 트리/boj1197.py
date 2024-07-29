# 백준 1197번 최소 스패닝 트리
import sys
put = sys.stdin.readline


def find(x):
    if parent[x] == x:
        return parent[x]

    parent[x] = find(parent[x])
    return parent[x]


def union(x, y):
    x = find(x)
    y = find(y)

    parent[x] = parent[y] = min(x, y)


V, E = map(int, put().split())
data = sorted([list(map(int, put().split())) for i in range(E)], key=lambda x: x[2])

parent = [i for i in range(V+1)]
answer = 0

for A, B, C in data:
    if find(A) != find(B):
        union(A, B)
        answer += C

print(answer)