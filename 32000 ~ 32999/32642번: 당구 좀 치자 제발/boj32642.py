# 백준 32642번 당구 좀 치자 제발
import sys
put = sys.stdin.readline

N = int(put())
n = list(map(int, put().split()))
answer = anger = 0

for i in n:
    if i:
        anger += 1
    else:
        anger -= 1

    answer += anger

print(answer)