# 백준 28932번 Префиксы-суффиксы
import sys
put = sys.stdin.readline

n = int(put())
a = list(map(int, put().split()))

# 모든 단어의 접두사와 접미사에는 자기 자신이 있다.
# 따라서 첫 번째 단어의 접두사 중 하나와 접미사 중 하나는 반드시 일치한다.
print(1, 1)