# 백준 28691번 정보보호학부 동아리 소개
import sys
put = sys.stdin.readline

answer = {'M': "MatKor", 'W': "WiCys", 'C': "CyKor", 'A': "AlKor", '$': "$clear"}

print(answer[put().strip()])