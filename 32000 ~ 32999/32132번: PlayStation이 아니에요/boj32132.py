# 백준 32132번 PlayStation이 아니에요
import sys
put = sys.stdin.readline

N = int(put())
text = put().strip()
answer = ""

for i in text:
    if answer[-2:] == "PS" and i in {'4','5'}:
        continue
    answer += i

print(answer)