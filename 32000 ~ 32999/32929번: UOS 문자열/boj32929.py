# 백준 32929번 UOS 문자열
import sys
put = sys.stdin.readline

answer = "UOS"
x = int(put())

print(answer[(x - 1) % 3])