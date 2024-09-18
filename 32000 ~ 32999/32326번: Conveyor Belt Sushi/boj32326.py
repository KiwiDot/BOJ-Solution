# 백준 32326번 Conveyor Belt Sushi
import sys
put = sys.stdin.readline

R, G, B = [int(put()) for i in range(3)]
answer = R * 3 + G * 4 + B * 5

print(answer)