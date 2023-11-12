# 백준 30642번 아이그루스와 화장실
import sys
put = sys.stdin.readline
check = {"annyong": 1,
         "induck": 0}

N = int(put())
name = check[put().strip()]
K = int(put())

answer = K - (K % 2) + name
if answer == 0:
    answer += 2
elif answer > N:
    answer -= 2

print(answer)