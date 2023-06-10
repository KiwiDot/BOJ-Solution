# 백준 4999번 아!
import sys
put = sys.stdin.readline

user = len(put().strip())
doctor = len(put().strip())

print("go" if user >= doctor else "no")
