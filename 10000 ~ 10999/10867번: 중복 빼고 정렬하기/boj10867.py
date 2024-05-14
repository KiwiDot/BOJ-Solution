# 백준 10867번 중복 빼고 정렬하기
import sys
put = sys.stdin.readline

N = int(put())
n = sorted(list(set(map(int, put().split()))))

print(*n)