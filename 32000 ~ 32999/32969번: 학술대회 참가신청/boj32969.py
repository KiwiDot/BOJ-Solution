# 백준 32969번 학술대회 참가신청
import sys
put = sys.stdin.readline

a = "social, history, language, literacy".split(', ')
b = "bigdata, public, society".split(', ')

s = put().strip()
for i in a:
    if i in s:
        print("digital humanities")
        break

for i in b:
    if i in s:
        print("public bigdata")
        break
