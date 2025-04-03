# 백준 33709번 치매예방수칙 3.3.3
import sys
put = sys.stdin.readline

N = int(put())
text = put().strip()
t = ['.', '|', ':', '#']

for i in t:
    text = ' '.join(text.split(i))

text = list(map(int, text.split()))
print(sum(text))