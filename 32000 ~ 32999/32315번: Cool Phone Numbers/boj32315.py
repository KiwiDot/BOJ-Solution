# 백준 32315번 Cool Phone Numbers
import sys
put = sys.stdin.readline

data = set(put().strip()) - {'-'}

print(len(data))