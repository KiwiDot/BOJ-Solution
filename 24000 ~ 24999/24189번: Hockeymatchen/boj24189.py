# 백준 24189번 Hockeymatchen
import sys
put = sys.stdin.readline

s1, g1, sh1 = map(int, put().split())
s2, g2, sh2 = map(int, put().split())

# 슛을 못했음 = 골을 못 넣었음 = 상대팀 골키퍼가 막은 적이 없음
if sh1 == 0:
    g1 = s2 = 0
if sh2 == 0:
    g2 = s1 = 0

# 골키퍼의 막은 횟수
if s1 == -1 and -1 not in {sh2, g2}:
    s1 = sh2 - g2
if s2 == -1 and -1 not in {sh1, g1}:
    s2 = sh1 - g1

# 골을 넣은 횟수
if g1 == -1 and -1 not in {sh1, s2}:
    g1 = sh1 - s2
if g2 == -1 and -1 not in {sh2, s1}:
    g2 = sh2 - s1

# 슛을 시도한 횟수
if sh1 == -1 and -1 not in {g1, s2}:
    sh1 = g1 + s2
if sh2 == -1 and -1 not in {g2, s1}:
    sh2 = g2 + s1

print(s1, g1, sh1)
print(s2, g2, sh2)