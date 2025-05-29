# 백준 33869번 일기 암호화하기
import sys
put = sys.stdin.readline

W = put().strip()
a = {chr(i+65) for i in range(26)} - set(W)
change = sorted(list(set(W)), key=lambda x: W.find(x)) + sorted(list(a))

answer = ''.join([change[ord(i)-65] for i in put().strip()])

print(answer)