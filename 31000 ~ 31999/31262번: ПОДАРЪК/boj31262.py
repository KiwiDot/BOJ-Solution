# 백준 31262번 ПОДАРЪК
import sys
put = sys.stdin.readline

text = put().strip()
alphabet = sorted(i for i in text[:3])
number = sorted([i for i in text[3:]], reverse=True)

answer = ''.join([alphabet[i] + number[i] for i in range(3)])
print(answer)