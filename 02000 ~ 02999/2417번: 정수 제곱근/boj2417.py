# 백준 2417번 정수 제곱근
import sys
put = sys.stdin.readline

n = int(put())
answer = 2 ** 63
start = 0
end = n

while start <= end:
    mid = (start + end) // 2

    if mid ** 2 >= n:
        answer = min(answer, mid)
        end = mid - 1
    else:
        start = mid + 1

print(answer)