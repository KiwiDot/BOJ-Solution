# 백준 33772번 Wow
import sys
put = sys.stdin.readline

N = int(put())
text = [put().strip() for i in range(2)]

text[0] = text[0].replace('\\../\\../', 'w')
text[0] = text[0].replace('\\../', 'v')

print(''.join(text[0].split('.')))