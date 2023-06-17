# 백준 5597번 과제 안 내신 분..?
import sys
put = sys.stdin.readline

num = {i for i in range(1, 31)}

for i in range(28):
    num -= {int(put())}

for i in sorted(list(num)):
    print(i)
