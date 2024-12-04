# 백준 32778번 가희와 부역명
import sys
put = sys.stdin.readline

text = put().strip()

if '(' in text:
    text = text.split(' (')
    print(text[0])
    print(text[1][:-1])
else:
    print(text)
    print('-')