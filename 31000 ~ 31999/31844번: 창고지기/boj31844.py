# 백준 31844번 창고지기
import sys
put = sys.stdin.readline

data = put().strip()
check = [i for i in data if i != '.']

if check == ['@', '#', '!'] or check == ['!', '#', '@']:
    print(abs(data.index('!') - data.index('@')) - 1)
else:
    print(-1)