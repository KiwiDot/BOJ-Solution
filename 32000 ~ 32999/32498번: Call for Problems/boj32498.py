# 백준 32498번 Call for Problems
import sys
put = sys.stdin.readline

n = int(put())
d = [int(put()) for i in range(n)]

print(len([1 for i in d if i % 2]))