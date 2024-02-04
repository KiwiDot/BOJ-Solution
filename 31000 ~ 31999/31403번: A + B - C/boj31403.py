# 백준 31403번 A + B - C
import sys
put = sys.stdin.readline

A, B, C = [put().strip() for i in range(3)]

print(eval(f"{A} + {B} - {C}"))
print(int(A + B) - int(C))