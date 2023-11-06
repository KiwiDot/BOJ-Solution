# 백준 30455번 이제는 더 이상 물러날 곳이 없다
import sys
put = sys.stdin.readline

N = int(put())
print("Goose" if N % 2 else "Duck")