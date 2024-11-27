# 백준 32767번 계산기가 필요해
import sys
put = sys.stdin.readline

a, op1, b, op2, c = put().split()

result = str(eval(a + op1 + b))
result = eval(result + op2 + c)
result = f"{result:.3f}"
blank = len("         44.123")

print("""=================
|SASA CALCULATOR|""")
print('|' + ' ' * (blank - len(result)) + result + '|')
print("""-----------------
|               |
| AC         /  |
| 7  8  9    *  |
| 4  5  6    -  |
| 1  2  3    +  |
|    0  .    =  |
=================""")