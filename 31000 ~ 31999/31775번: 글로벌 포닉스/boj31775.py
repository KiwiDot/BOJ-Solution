# 백준 31775번 글로벌 포닉스
import sys
put = sys.stdin.readline

S = {put().strip()[0] for i in range(3)}

print("GLOBAL" if S == {'l', 'k', 'p'} else "PONIX")