# 백준 32154번 SUAPC 2024 Winter
import sys
put = sys.stdin.readline

answer = [(0, []),
          (11, ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'J', 'L', 'M']),
          (9, ['A', 'C', 'E', 'F', 'G', 'H', 'I', 'L', 'M']),
          (9, ['A', 'C', 'E', 'F', 'G', 'H', 'I', 'L', 'M']),
          (9, ['A', 'B', 'C', 'E', 'F', 'G', 'H', 'L', 'M']),
          (8, ['A', 'C', 'E', 'F', 'G', 'H', 'L', 'M']),
          (8, ['A', 'C', 'E', 'F', 'G', 'H', 'L', 'M']),
          (8, ['A', 'C', 'E', 'F', 'G', 'H', 'L', 'M']),
          (8, ['A', 'C', 'E', 'F', 'G', 'H', 'L', 'M']),
          (8, ['A', 'C', 'E', 'F', 'G', 'H', 'L', 'M']),
          (8, ['A', 'B', 'C', 'F', 'G', 'H', 'L', 'M'])]

N = int(put())

print(answer[N][0])
print(*answer[N][1])