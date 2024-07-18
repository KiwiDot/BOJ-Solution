# 백준 32090번 シンプルなエディタ
import sys
put = sys.stdin.readline

while True:
    N = int(put())
    if not N:
        break

    answer = []
    idx = 0

    while N:
        N -= 1
        a, n = put().split()

        match a:
            case "INSERT":
                answer.insert(idx, n)
                idx += 1
            case "LEFT":
                idx = max(idx-1, 0)
            case "RIGHT":
                idx = min(idx+1, len(answer))

    print(''.join(answer))