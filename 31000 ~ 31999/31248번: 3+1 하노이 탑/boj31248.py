# 백준 31248번 3+1 하노이 탑
import sys
put = sys.stdin.readline
loc_1 = 'A'


def big_hanoi(n, T1, T2, T3, T4):
    global loc_1
    if n == 1:
        print(loc_1, T4)
        return

    def little_hanoi(m, t1, t2, t3):
        global loc_1
        if m == 1:
            print(t1, t3)
            loc_1 = t3
            return

        little_hanoi(m-1, t1, t3, t2)
        little_hanoi(1, t1, t2, t3)
        little_hanoi(m-1, t2, t1, t3)

    # (1) ~ (N-2)번째 원반까지 이동
    if n > 2:
        little_hanoi(n-2, T1, T2, T3)

    # (N-1), (N)번째 원반 이동
    print(T1, T2)
    print(T1, T4)
    print(T2, T4)

    if n > 2:
        big_hanoi(n-2, T3, T1, T2, T4)


N = n = int(put())
answer = 0

while n > 2:
    answer += 2 ** (n-2) - 1
    answer += 3
    n -= 2

answer += n * (n + 1) // 2
# answer = N + (2**N - 1) // 3

print(answer)
big_hanoi(N, 'A', 'B', 'C', 'D')