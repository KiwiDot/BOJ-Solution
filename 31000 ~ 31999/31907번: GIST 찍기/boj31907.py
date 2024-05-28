# 백준 31907번 GIST 찍기
import sys
put = sys.stdin.readline

K = int(put())

for i in range(K):
    print('G' * K + '...' * K)

for i in range(K):
    print('.' * K + 'I' * K + '.' * K + 'T' * K)

for i in range(K):
    print('..' * K + 'S' * K + '.' * K)