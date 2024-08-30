# 백준 23544번 Kinder Surprise
import sys
put = sys.stdin.readline

n = int(put())
hippo = {put().strip() for i in range(n)}

print(n - len(hippo))