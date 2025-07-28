# 백준 34073번 DORO
import sys
put = sys.stdin.readline

N = int(put())
word = put().split()

print(*[i + "DORO" for i in word])