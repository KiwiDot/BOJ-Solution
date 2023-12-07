# 백준 30794번 가희와 클럽 오디션 1
import sys
put = sys.stdin.readline
score = {"miss": 0, "bad": 200, "cool": 400, "great": 600, "perfect": 1000}

lv, result = put().split()
answer = int(lv) * score[result]

print(answer)