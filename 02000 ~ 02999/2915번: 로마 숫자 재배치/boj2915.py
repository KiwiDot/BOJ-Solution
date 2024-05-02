# 백준 2915번 로마 숫자 재배치
import sys
put = sys.stdin.readline

n1 = {0: '', 1: 'X', 2: 'XX', 3: 'XXX', 4: 'XL',
      5: 'L', 6: 'LX', 7: 'LXX', 8: 'LXXX', 9: 'XC'}
n2 = {0: '', 1: 'I', 2: 'II', 3: 'III', 4: 'IV',
      5: 'V', 6: 'VI', 7: 'VII', 8: 'VIII', 9: 'IX'}

num = {}
change = {}

for i in range(1, 100):
    s1 = n1[i // 10]
    s2 = n2[i % 10]
    s = ''.join(sorted(list(s1) + list(s2)))
    change[i] = s1 + s2

    if s not in num:
        num[s] = i

B = ''.join(sorted(list(put().strip())))
print(change[num[B]])