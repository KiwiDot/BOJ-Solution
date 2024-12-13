# 백준 32805번 A Stack of Gold
import sys
put = sys.stdin.readline

w, s = map(int, input().split())

si = s * (s + 1) // 2 * 29260
answer = (w - si) // 110

print(answer)
