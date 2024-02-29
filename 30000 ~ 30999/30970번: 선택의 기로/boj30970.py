# 백준 30970번 선택의 기로
import sys
put = sys.stdin.readline

N = int(put())
data = [list(map(int, put().split())) for i in range(N)]

# 첫 번째 방법
data.sort(key=lambda x: [-x[0], x[1]])
print(*data[0], *data[1])

# 두 번째 방법
data.sort(key=lambda x: [x[1], -x[1]])
print(*data[0], *data[1])