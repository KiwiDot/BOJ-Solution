# 백준 33515번 노트북 세 대를 가지고 왔다
import sys
put = sys.stdin.readline

T1, T2 = map(int, put().split())
print(min(T1, T2))